using UnityEngine;
using System.Collections;

/// <summary>
/// Player Controller script for 2D platformer movement
/// Supports keyboard input, custom keybinds, Xbox controller, and dialogue integration
/// Features: Variable jump height, dash system, facing direction tracking, and automatic movement blocking during dialogue
/// Works with PlayerStats component for speed adjustments and stat-based modifications
/// Includes a 0.5 second delay after dialogue ends to prevent accidental inputs
/// </summary>
public class PlayerController : MonoBehaviour
{
    public enum PlayerState
    {
        Idle,
        Moving,
        Jumping
    }

    [Header("Movement Settings")]
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] public bool enableMovement = true;
    
    [Header("Dialogue Integration")]
    [SerializeField] private DialogueManager dialogueManager;
    
    [Header("Component References")]
    [SerializeField] private PlayerStats playerStats;
    
    [Header("Jump Settings")]
    [SerializeField] private float jumpForce = 10f;
    [SerializeField] private bool enableJump = true;
    public Rigidbody2D rb2D;
    
    [Header("Ground and Wall Detection Settings")]
    [SerializeField] private float groundedVelocityThreshold = 0.01f;
    [SerializeField] private float groundedTimerDuration = 0.1f; // Time velocity must stay low to be considered grounded
    [SerializeField] private float wallCheckDistance = 0.1f; // Distance to check for walls ahead
    [SerializeField] private LayerMask collisionLayers; // Layers to check for collisions
    
    [Header("Advanced Jump Settings")]
    [SerializeField] private bool enableCoyoteTime = true;
    [SerializeField] private float coyoteTime = 0.15f;
    [SerializeField] private bool enableJumpBuffering = true;
    [SerializeField] private float jumpBufferTime = 0.1f;
    [SerializeField] private bool enableDoubleJump = true;
    [SerializeField] private float doubleJumpForce = 8f;
    [SerializeField] private bool enableVariableJumpHeight = true;
    [SerializeField] private float jumpCutMultiplier = 0.5f; // Multiplier when jump button is released early
    
    [Header("Dash Settings")]
    [SerializeField] private bool enableDash = true;
    [SerializeField] private float dashSpeed = 15f;
    [SerializeField] private float dashDuration = 0.5f;
    [SerializeField] private bool dashCancellableByJump = true;
    [SerializeField] private KeyCode dashKey = KeyCode.Space;
    
    [Header("Heal Settings")]
    [SerializeField] private bool enableHeal = true;
    [SerializeField] private float healDuration = 1f;
    [SerializeField] private float healAmount = 50f;
    [SerializeField] private float healCooldown = 5f;
    [SerializeField] private KeyCode healKey = KeyCode.Z;
    [SerializeField] private GameObject healParticlePrefab;
    [SerializeField] private AudioClip healCompleteSound;
    [SerializeField] private AudioSource audioSource;
    
    [Header("Keyboard Controls")]
    [SerializeField] private KeyCode moveLeftKey1 = KeyCode.A;
    [SerializeField] private KeyCode moveLeftKey2 = KeyCode.LeftArrow;
    [SerializeField] private KeyCode moveRightKey1 = KeyCode.D;
    [SerializeField] private KeyCode moveRightKey2 = KeyCode.RightArrow;
    [SerializeField] private KeyCode jumpKey1 = KeyCode.W;
    [SerializeField] private KeyCode jumpKey2 = KeyCode.UpArrow;
    [SerializeField] private KeyCode attackKey = KeyCode.X;
    [SerializeField] private KeyCode pauseMenuKey = KeyCode.Escape;
    
    [Header("Controller Settings")]
    [SerializeField] private bool enableController = true;
    [SerializeField] private string horizontalAxisName = "Horizontal";
    [SerializeField] private string jumpButtonName = "Fire1"; // Xbox A button
    [SerializeField] private string dashButtonName = "Fire2"; // Xbox RT/Right Trigger
    [SerializeField] private string attackButtonName = "Fire3"; // Xbox X button
    [SerializeField] private string healButtonName = "Fire4"; // Xbox B button
    [SerializeField] private string pauseMenuButtonName = "Cancel"; // Xbox Menu button
    [SerializeField] private float controllerDeadzone = 0.1f;
    
    [Header("UI References")]
    [SerializeField] private GameObject pausePanel;
    [SerializeField] private bool pausePanelStartsActive = false;
    
    [Header("State System")]
    [SerializeField] private PlayerState currentState = PlayerState.Idle;
    
    [Header("Animation System")]
    [SerializeField] private GameObject AllAnimationForFlipping;
    [SerializeField] public UniversalAnimator universalAnimator;
    [SerializeField] private bool autoSwitchAnimations = true;
    
    // Animation indices for the UniversalAnimator
    private const int IDLE_ANIM = 0;
    private const int MOVING_ANIM = 1;
    private const int JUMPING_ANIM = 2;
    private const int HORIZONTAL_ATTACK1_ANIM = 3;
    private const int HORIZONTAL_ATTACK2_ANIM = 4;
    private const int UP_ATTACK_ANIM = 5;
    private const int DOWN_ATTACK_ANIM = 6;
    private const int HURT_ANIM = 7;
    private const int DEATH_ANIM = 9;
    private const int HEALING_ANIM = 10;
    
    [Header("Attack System")]
    [SerializeField] private float attackCoolDown = 0.5f;
    [SerializeField] private float TimeSinceLastAttack = 0f;
    [SerializeField] private GameObject leftAttackPrefab;
    [SerializeField] private GameObject rightAttackPrefab;
    [SerializeField] private GameObject upAttackPrefab;
    [SerializeField] private GameObject downAttackPrefab;
    
    [Header("Particle System (Unity)")]
    [SerializeField] private ParticleSystem moveEffect;

    [Header("Particle System (UniversalAnimation)")]
    //[SerializeField] private UniversalAnimation moveEffect;
    //This part will be design in the future

    [Header("Debug")]
    [SerializeField] private bool showDebugInfo = false;
    
    // Private variables
    private float horizontalInput;
    private bool isMovingLeft;
    private bool isMovingRight;
    private bool isGrounded;
    private bool jumpPressed;
    private bool wasGrounded;
    
    // Advanced jump variables
    private float coyoteTimeCounter;
    private float jumpBufferCounter;
    private bool hasDoubleJumped;
    private int jumpCount;
    
    // Ground detection timer
    private float groundedTimer;
    
    // Dialogue delay variables
    private bool wasDialogueActive = false;
    private float dialogueEndTimer = 0f;
    private const float DIALOGUE_END_DELAY = 0.5f; // Delay in seconds after dialogue ends before re-enabling movement
    
    // Variable jump variables
    private bool jumpHeld = false;
    private bool jumpReleased = false;
    
    // Dash variables
    private bool dashPressed = false;
    public bool isDashing = false;
    public float dashTimer = 0f;
    private int dashDirection = 0; // 1 for right, -1 for left
    
    // Heal variables
    private bool healPressed = false;
    private bool isHealing = false;
    private float healTimer = 0f;
    private float healCooldownTimer = 0f;
    
    // Attack variables
    private bool attackPressed = false;
    private bool isAttacking = false;
    private float attackCooldownTimer = 0f;
    private float attackAnimationTimer = 0f;
    
    // Pause menu variables
    private bool pauseMenuPressed = false;
    private bool wasPausedLastFrame = false;
    
    // Hurt variables
    private bool isHurt = false;
    private float hurtAnimationTimer = 0f;
    private const float HURT_ANIMATION_DURATION = 0.3f;
    
    // Death variables
    private bool isDead = false;
    
    // Facing direction
    private bool facingRight = true; // true = facing right, false = facing left
    
    private PlayerState previousState;
    private bool isJumping = false;
    
    // Properties for external access
    public float MoveSpeed 
    { 
        get => moveSpeed; 
        set => moveSpeed = Mathf.Max(0f, value); 
    }
    
    public float JumpForce 
    { 
        get => jumpForce; 
        set => jumpForce = Mathf.Max(0f, value); 
    }
    
    public bool EnableMovement 
    { 
        get => enableMovement; 
        set => enableMovement = value; 
    }
    
    public bool EnableJump 
    { 
        get => enableJump; 
        set => enableJump = value; 
    }
    
    public bool EnableDoubleJump 
    { 
        get => enableDoubleJump; 
        set => enableDoubleJump = value; 
    }
    
    public bool EnableCoyoteTime 
    { 
        get => enableCoyoteTime; 
        set => enableCoyoteTime = value; 
    }
    
    public bool EnableJumpBuffering 
    { 
        get => enableJumpBuffering; 
        set => enableJumpBuffering = value; 
    }
    
    public bool EnableController 
    { 
        get => enableController; 
        set => enableController = value; 
    }
    
    public bool EnableVariableJumpHeight 
    { 
        get => enableVariableJumpHeight; 
        set => enableVariableJumpHeight = value; 
    }
    
    public bool EnableDash 
    { 
        get => enableDash; 
        set => enableDash = value; 
    }
    
    public bool DashCancellableByJump 
    { 
        get => dashCancellableByJump; 
        set => dashCancellableByJump = value; 
    }
    
    // Read-only property to check if movement is currently blocked
    public bool IsMovementBlocked => !enableMovement || 
                                   (dialogueManager != null && dialogueManager.IsDialogueActive) || 
                                   (dialogueEndTimer > 0f);
    
    public float HorizontalInput => horizontalInput;
    public bool IsMovingLeft => isMovingLeft;
    public bool IsMovingRight => isMovingRight;
    public bool IsMoving => Mathf.Abs(horizontalInput) > 0.01f;
    public bool IsGrounded => isGrounded;
    public bool JumpPressed => jumpPressed;
    public PlayerState CurrentState => currentState;
    public bool IsJumping => isJumping;
    public bool HasDoubleJumped => hasDoubleJumped;
    public int JumpCount => jumpCount;
    public float CoyoteTimeRemaining => coyoteTimeCounter;
    public float JumpBufferRemaining => jumpBufferCounter;
    public float GroundedTimer => groundedTimer;
    public float DialogueDelayRemaining => dialogueEndTimer;
    public bool IsInDialogueDelay => dialogueEndTimer > 0f;
    public bool IsDashing => isDashing;
    public float DashTimeRemaining => dashTimer;
    public bool JumpHeld => jumpHeld;
    public bool FacingRight => facingRight;
    public bool IsAttacking => isAttacking;
    public float AttackCooldownRemaining => attackCooldownTimer;
    public bool CanAttack => !isAttacking && attackCooldownTimer <= 0f && !isHealing;
    public bool IsHurt => isHurt;
    public float HurtAnimationRemaining => hurtAnimationTimer;
    public bool IsHealing => isHealing;
    public float HealTimeRemaining => healTimer;
    public float HealCooldownRemaining => healCooldownTimer;
    public bool CanHeal => enableHeal && playerStats != null && healCooldownTimer <= 0f && 
                          !isAttacking && !isHurt && !isHealing && playerStats.CurrentHealth < playerStats.MaxHealth;
    
    // Pause menu properties
    public GameObject PausePanel
    {
        get => pausePanel;
        set => pausePanel = value;
    }
    
    public bool IsPauseMenuOpen => pausePanel != null && pausePanel.activeInHierarchy;
    
    // Component References
    public PlayerStats PlayerStats
    {
        get => playerStats;
        set => playerStats = value;
    }
    
    // Animation System Properties
    public UniversalAnimator UniversalAnimator
    {
        get => universalAnimator;
        set => universalAnimator = value;
    }
    
    public bool AutoSwitchAnimations
    {
        get => autoSwitchAnimations;
        set => autoSwitchAnimations = value;
    }
    
    /// <summary>
    /// Set the DialogueManager reference. If not assigned in inspector, 
    /// this method can be used to set it at runtime.
    /// </summary>
    /// <param name="manager">The DialogueManager instance</param>
    public void SetDialogueManager(DialogueManager manager)
    {
        dialogueManager = manager;
    }
    
    /// <summary>
    /// Reset the death state - useful for scene restarts
    /// </summary>
    public void ResetDeathState()
    {
        isDead = false;
    }
    
    /// <summary>
    /// Manually set or clear the dialogue delay timer.
    /// Useful for testing or special scenarios.
    /// </summary>
    /// <param name="delayTime">Time in seconds to delay movement. Use 0 to clear delay.</param>
    public void SetDialogueDelay(float delayTime)
    {
        dialogueEndTimer = Mathf.Max(0f, delayTime);
    }
    
    /// <summary>
    /// Manually set the facing direction of the player.
    /// </summary>
    /// <param name="faceRight">True to face right, false to face left</param>
    public void SetFacing(bool faceRight)
    {
        facingRight = faceRight;
    }

    private void Awake()
    {
        // Get or add Rigidbody2D component
        /*
        rb2D = GetComponent<Rigidbody2D>();
        if (rb2D == null)
        {
            rb2D = gameObject.AddComponent<Rigidbody2D>();
            Debug.LogWarning("No Rigidbody2D found on " + gameObject.name + ". Added one automatically.");
        }*/
        
        // Set up Rigidbody2D for platformer movement
        rb2D.freezeRotation = true;
        //rb2D.gravityScale = 1f;
        
        // Check for UniversalAnimator component
        if (universalAnimator == null)
        {
            universalAnimator = GetComponent<UniversalAnimator>();
            if (universalAnimator == null && showDebugInfo)
            {
                Debug.LogWarning($"PlayerController '{gameObject.name}': No UniversalAnimator component found!");
            }
        }
    }

    private void Start()
    {
        // Auto-find DialogueManager if not assigned
        if (dialogueManager == null)
        {
            dialogueManager = FindObjectOfType<DialogueManager>();
        }
        
        // Auto-find PlayerStats if not assigned
        if (playerStats == null)
        {
            playerStats = GetComponent<PlayerStats>();
        }
        
        // Set cross-reference in PlayerStats
        if (playerStats != null && playerStats.PlayerController == null)
        {
            playerStats.PlayerController = this;
        }
        
        // Initialize pause panel state
        if (pausePanel != null)
        {
            pausePanel.SetActive(pausePanelStartsActive);
        }
        
        // Initialize animation states
        if (autoSwitchAnimations)
        {
            SwitchToAnimationSetWithPriority();
        }

        //Set 1 second of dummy time to prevent dash at start
        SetDummyState(1f);

    }

    private void Update()
    {
        // Check for death state first - if dead, lock to death animation and disable all controls
        if (playerStats != null && playerStats.IsDead)
        {
            if (!isDead)
            {
                isDead = true;
                universalAnimator.ForceEnableAnimation(DEATH_ANIM);
            }
            // Stop all processing when dead
            return;
        }
        
        // Handle dialogue delay timer
        bool isDialogueCurrentlyActive = (dialogueManager != null && dialogueManager.IsDialogueActive);
        bool isInDialogueDelay = false;
        
        // Check if dialogue just ended and start delay timer
        if (wasDialogueActive && !isDialogueCurrentlyActive)
        {
            dialogueEndTimer = DIALOGUE_END_DELAY;
        }
        
        // Update dialogue delay timer
        if (dialogueEndTimer > 0f)
        {
            dialogueEndTimer -= Time.deltaTime;
            isInDialogueDelay = true;
        }
        
        // Handle healing
        HandleHeal();
        
        // Update dialogue state tracking
        wasDialogueActive = isDialogueCurrentlyActive;
        
        // Handle pause menu input (always check, regardless of movement block)
        HandlePauseMenuInput();
        
        // Check if movement should be disabled (manually, during dialogue, or in dialogue delay)
        bool movementBlocked = !enableMovement || isDialogueCurrentlyActive || isInDialogueDelay;
        
        // Update TimeSinceLastAttack Timer
        if (TimeSinceLastAttack > 0f)
        {
            TimeSinceLastAttack -= Time.deltaTime;
        }

        if (movementBlocked)
        {
            horizontalInput = 0f;
            isMovingLeft = false;
            isMovingRight = false;
            jumpPressed = false;
            UpdatePlayerState();
            return;
        }
        
        CheckGrounded();
        HandleInput();
        HandleDash();
        HandleHeal();
        HandleHurt();
        HandleAttack();
        HandleVariableJump();
        HandleAdvancedJumpTimers();
        UpdatePlayerState();
    }

    private void FixedUpdate()
    {
        // Check if movement should be disabled (manually, during dialogue, in dialogue delay, or blocking)
        bool isDialogueCurrentlyActive = (dialogueManager != null && dialogueManager.IsDialogueActive);
        bool isInDialogueDelay = (dialogueEndTimer > 0f);
        bool movementBlocked = !enableMovement || isDialogueCurrentlyActive || isInDialogueDelay || isHealing;
        
        if (movementBlocked)
            return;
            
        ApplyMovement();
        ApplyJump();
    }

    private void OnValidate()
    {
        // Clamp values in inspector
        moveSpeed = Mathf.Max(0f, moveSpeed);
        jumpForce = Mathf.Max(0f, jumpForce);
        doubleJumpForce = Mathf.Max(0f, doubleJumpForce);
        controllerDeadzone = Mathf.Clamp01(controllerDeadzone);
        coyoteTime = Mathf.Max(0f, coyoteTime);
        jumpBufferTime = Mathf.Max(0f, jumpBufferTime);
        groundedVelocityThreshold = Mathf.Max(0.001f, groundedVelocityThreshold);
        groundedTimerDuration = Mathf.Max(0.01f, groundedTimerDuration);
        healCooldown = Mathf.Max(0f, healCooldown);
        healDuration = Mathf.Max(0f, healDuration);
        healAmount = Mathf.Max(0f, healAmount);
    }

    private void HandleInput()
    {
        horizontalInput = 0f;
        jumpPressed = false;
        dashPressed = false;
        attackPressed = false;
        healPressed = false;
        pauseMenuPressed = false;
        
        // Handle keyboard input
        HandleKeyboardInput();
        
        // Handle controller input
        if (enableController)
        {
            HandleControllerInput();
        }
        
        // If healing, ignore movement and attack inputs but allow heal input
        if (isHealing)
        {
            horizontalInput = 0f;
            jumpPressed = false;
            dashPressed = false;
            attackPressed = false;
            isMovingLeft = false;
            isMovingRight = false;
            return;
        }
        
        // Determine movement direction
        isMovingLeft = horizontalInput < -0.01f;
        isMovingRight = horizontalInput > 0.01f;
        
        // Update facing direction based on movement
        UpdateFacingDirection();
        
        // Clamp horizontal input
        horizontalInput = Mathf.Clamp(horizontalInput, -1f, 1f);
    }

    private void HandleKeyboardInput()
    {
        // Check left movement keys
        bool leftPressed = Input.GetKey(moveLeftKey1) || Input.GetKey(moveLeftKey2);
        bool rightPressed = Input.GetKey(moveRightKey1) || Input.GetKey(moveRightKey2);
        
        if (leftPressed)
        {
            horizontalInput -= 1f;
        }
        
        if (rightPressed)
        {
            horizontalInput += 1f;
        }
        
        // Check jump keys
        bool jumpKeyPressed = Input.GetKeyDown(jumpKey1) || Input.GetKeyDown(jumpKey2);
        if (enableJump && jumpKeyPressed)
        {
            jumpPressed = true;
            
            // Set jump buffer timer when jump is pressed
            if (enableJumpBuffering)
            {
                jumpBufferCounter = jumpBufferTime;
            }
        }
        
        // Track jump held state for variable jump height
        if (enableVariableJumpHeight)
        {
            jumpHeld = Input.GetKey(jumpKey1) || Input.GetKey(jumpKey2);
            jumpReleased = Input.GetKeyUp(jumpKey1) || Input.GetKeyUp(jumpKey2);
        }
        
        // Check dash key
        if (enableDash && Input.GetKeyDown(dashKey))
        {
            dashPressed = true;
        }
        
        // Check attack key
        if (Input.GetKeyDown(attackKey))
        {
            attackPressed = true;
        }
        
        // Check heal key
        if (Input.GetKeyDown(healKey))
        {
            healPressed = true;
        }
        
        // Check pause menu key
        if (Input.GetKeyDown(pauseMenuKey))
        {
            pauseMenuPressed = true;
        }
    }

    private void HandleControllerInput()
    {
        // Get controller input
        float controllerInput = Input.GetAxis(horizontalAxisName);
        
        // Apply deadzone
        if (Mathf.Abs(controllerInput) > controllerDeadzone)
        {
            horizontalInput += controllerInput;
        }
        
        // Check jump button (Xbox A button)
        if (enableJump && Input.GetButtonDown(jumpButtonName))
        {
            jumpPressed = true;
            
            // Set jump buffer timer when jump is pressed
            if (enableJumpBuffering)
            {
                jumpBufferCounter = jumpBufferTime;
            }
        }
        
        // Track jump held state for variable jump height
        if (enableVariableJumpHeight)
        {
            jumpHeld = Input.GetButton(jumpButtonName);
            jumpReleased = Input.GetButtonUp(jumpButtonName);
        }
        
        // Check dash button (Xbox RT/Right Trigger)
        if (enableDash && Input.GetButtonDown(dashButtonName))
        {
            dashPressed = true;
        }
        
        // Check attack button (Xbox X button)
        if (Input.GetButtonDown(attackButtonName))
        {
            attackPressed = true;
        }
        
        // Check heal button (Xbox B button)
        if (enableHeal && Input.GetButtonDown(healButtonName))
        {
            healPressed = true;
        }
        
        // Check pause menu button (Xbox Menu button)
        if (Input.GetButtonDown(pauseMenuButtonName))
        {
            pauseMenuPressed = true;
        }
    }

    private void HandleHurt()
    {
        // Update hurt animation timer
        if (hurtAnimationTimer > 0f)
        {
            hurtAnimationTimer -= Time.deltaTime;
            if (hurtAnimationTimer <= 0f)
            {
                isHurt = false;
                // Return to appropriate animation based on current state
                SwitchToAnimationSetWithPriority();
            }
        }
    }

    private void HandleAttack()
    {
        // Update attack cooldown timer
        if (attackCooldownTimer > 0f)
        {
            attackCooldownTimer -= Time.deltaTime;
        }
        
        // Update attack animation timer (but respect hurt priority)
        if (attackAnimationTimer > 0f && !isHurt)
        {
            attackAnimationTimer -= Time.deltaTime;
            if (attackAnimationTimer <= 0f)
            {
                isAttacking = false;
                // Return to appropriate animation based on current state
                SwitchToAnimationSetWithPriority();
            }
        }
        
        // Handle attack input (but only if not hurt)
        if (attackPressed && CanAttack && !isHurt)
        {
            PerformAttack();
        }
    }
    
    private void PerformAttack()
    {
        // Start attack state
        isAttacking = true;
        attackCooldownTimer = attackCoolDown;
        attackAnimationTimer = 0.3f; // Animation duration
        
        // Check for directional input
        bool upPressed = Input.GetKey(KeyCode.UpArrow) || Input.GetKey(KeyCode.W) || Input.GetAxis("Vertical") > 0.5f;
        bool downPressed = Input.GetKey(KeyCode.DownArrow) || Input.GetKey(KeyCode.S) || Input.GetAxis("Vertical") < -0.5f;
        
        GameObject attackPrefab = null;
        int attackAnimationIndex = -1;
        
        if (upPressed)
        {
            // Up attack
            attackPrefab = upAttackPrefab;
            attackAnimationIndex = UP_ATTACK_ANIM;
        }
        else if (downPressed && isJumping)
        {
            // Down attack (only when jumping)
            attackPrefab = downAttackPrefab;
            attackAnimationIndex = DOWN_ATTACK_ANIM;
        }
        else
        {
            // Horizontal attack based on facing direction
            if (facingRight)
            {
                attackPrefab = rightAttackPrefab;
            }
            else
            {
                attackPrefab = leftAttackPrefab;
            }
            if (TimeSinceLastAttack <= 0.1f)
            {
                attackAnimationIndex = HORIZONTAL_ATTACK1_ANIM;
                TimeSinceLastAttack = 0.8f;
            }
            else
                attackAnimationIndex = HORIZONTAL_ATTACK2_ANIM;

        }
        
        // Spawn attack prefab at player position
        if (attackPrefab != null)
        {
            Instantiate(attackPrefab, transform.position, transform.rotation);
        }
        
        // Switch to attack animation temporarily (unless hurt)
        if (attackAnimationIndex >= 0 && !isHurt && universalAnimator != null)
        {
            universalAnimator.ForceEnableAnimation(attackAnimationIndex);
        }
    }

    private void ApplyMovement()
    {
        // Calculate movement velocity
        Vector2 velocity = rb2D.velocity;
        float targetVelocityX = 0f;

      
        // If dashing, override horizontal movement
        if (isDashing)
        {
            targetVelocityX = dashDirection * dashSpeed;
        }
        else
        {
            // Apply movement with speed adjustment from PlayerStats
            float adjustedSpeed = moveSpeed;
            if (playerStats != null)
            {
                adjustedSpeed *= playerStats.WalkSpeedAdjustment;
            }
            targetVelocityX = horizontalInput * adjustedSpeed;
        }
        
        // Only check for walls if there's horizontal movement
        if (Mathf.Abs(targetVelocityX) > 0.01f)
        {
            // Calculate movement direction
            Vector2 moveDirection = targetVelocityX > 0 ? Vector2.right : Vector2.left;
            
            // Calculate the distance we want to move this frame
            float moveDistance = Mathf.Abs(targetVelocityX) * Time.fixedDeltaTime;
            
            // Perform a cast to check for obstacles (exclude triggers)
            RaycastHit2D[] hits = new RaycastHit2D[5];
            ContactFilter2D filter = new ContactFilter2D();
            filter.useTriggers = false; // Ignore triggers
            filter.SetLayerMask(collisionLayers);
            filter.useLayerMask = true;
            
            int hitCount = rb2D.Cast(moveDirection, filter, hits, moveDistance + wallCheckDistance);
            
            // If we hit something solid, stop at the collision point
            if (hitCount > 0 && hits[0].collider != null)
            {
                // Calculate safe distance (stop just before the wall)
                float safeDistance = Mathf.Max(0f, hits[0].distance - wallCheckDistance);
                
                // If we're too close to the wall, don't move
                if (safeDistance < 0.01f)
                {
                    velocity.x = 0f;
                }
                else
                {
                    // Move at reduced speed to avoid penetrating the wall
                    float safeVelocity = (safeDistance / Time.fixedDeltaTime);
                    velocity.x = Mathf.Sign(targetVelocityX) * Mathf.Min(Mathf.Abs(targetVelocityX), safeVelocity);
                }
            }
            else
            {
                // No obstacle detected, apply normal velocity
                velocity.x = targetVelocityX;
            }
        }
        else
        {
            // No horizontal input, set velocity to 0
            velocity.x = 0f;
        }
        
        // Apply velocity to rigidbody
        rb2D.velocity = velocity;
        
    }

    private void ApplyJump()
    {
        if (!enableJump) return;
        
        // Handle dash cancellation by jump
        if (isDashing && jumpPressed && dashCancellableByJump)
        {
            // Stop dash and clear horizontal velocity
            isDashing = false;
            dashTimer = 0f;
            Vector2 velocity = rb2D.velocity;
            velocity.x = 0f;
            rb2D.velocity = velocity;
        }
        
        // If dashing and dash is not cancellable by jump, don't allow jumping
        if (isDashing && !dashCancellableByJump)
        {
            return;
        }
        
        // Check if we can perform a ground jump or coyote time jump
        bool canGroundJump = (isGrounded || (enableCoyoteTime && coyoteTimeCounter > 0f)) && jumpCount < 1;
        
        // Check if we can perform a double jump
        bool canDoubleJump = enableDoubleJump && !isGrounded && jumpCount == 1 && !hasDoubleJumped;
        
        // Check if jump input is available (direct press or buffered)
        bool jumpInputAvailable = jumpPressed || (enableJumpBuffering && jumpBufferCounter > 0f);
        
        if (jumpInputAvailable && (canGroundJump || canDoubleJump))
        {
            Vector2 velocity = rb2D.velocity;
            
            if (canGroundJump)
            {
                // Ground jump or coyote time jump
                velocity.y = jumpForce;
                jumpCount = 1;
                
                // Set jumping state immediately when jump is pressed
                isJumping = true;
                
                // Play move effect when player jumps
                if (moveEffect != null)
                {
                    moveEffect.Play();
                }
                
                // Reset coyote time when jumping
                coyoteTimeCounter = 0f;
                
                if (showDebugInfo)
                {
                    string jumpType = isGrounded ? "Ground jump" : "Coyote time jump";
                    Debug.Log($"{jumpType} performed - state set to jumping");
                }
            }
            else if (canDoubleJump)
            {
                // Double jump
                velocity.y = doubleJumpForce;
                hasDoubleJumped = true;
                jumpCount = 2;
                
                // Set jumping state for double jump
                isJumping = true;
                
                // Play move effect when player double jumps
                if (moveEffect != null)
                {
                    moveEffect.Play();
                }
                
                if (showDebugInfo)
                {
                    Debug.Log("Double jump performed - state set to jumping");
                }
            }
            
            rb2D.velocity = velocity;
            
            // Reset jump buffer when jump is performed
            jumpBufferCounter = 0f;
        }
    }

    private void CheckGrounded()
    {
        wasGrounded = isGrounded;
        
        // Check if velocity is below threshold
        bool velocityBelowThreshold = Mathf.Abs(rb2D.velocity.y) < groundedVelocityThreshold;
        
        if (velocityBelowThreshold)
        {
            // Velocity is low - increment timer
            groundedTimer += Time.deltaTime;
            
            // Only consider grounded if timer has reached duration
            if (groundedTimer >= groundedTimerDuration)
            {
                isGrounded = true;
            }
        }
        else
        {
            // Velocity is high - reset timer and not grounded
            groundedTimer = 0f;
            isGrounded = false;
        }
        
        // Reset jumping state when landing (after timer confirms grounding)
        if (!wasGrounded && isGrounded && isJumping)
        {
            isJumping = false;
            hasDoubleJumped = false;
            jumpCount = 0;
            
            if (showDebugInfo)
            {
                Debug.Log("Player landed - jumping state reset");
            }
        }
        
        // Handle coyote time
        if (enableCoyoteTime)
        {
            if (isGrounded)
            {
                coyoteTimeCounter = coyoteTime;
            }
            else if (coyoteTimeCounter > 0f)
            {
                coyoteTimeCounter -= Time.deltaTime;
            }
        }
    }

    private void HandleDash()
    {
        if (!enableDash) return;

        // Handle dash input
        if (dashPressed && !isDashing)
        {
            // Determine dash direction - prioritize current input, then use facing direction
            if (isMovingLeft)
            {
                dashDirection = -1;
                facingRight = false; // Update facing when dashing left
            }
            else if (isMovingRight)
            {
                dashDirection = 1;
                facingRight = true; // Update facing when dashing right
            }
            else
            {
                // Use current facing direction when no input
                dashDirection = facingRight ? 1 : -1;
            }

            // Start dash
            isDashing = true;
            dashTimer = dashDuration;
            //stop all verticle movement
            rb2D.velocity = new Vector2(rb2D.velocity.x, 0f);

            // Give player invulnerability during dash
            if (playerStats != null)
            {
                playerStats.StartInvulnerability(0.25f);
            }
        }

        // Update dash timer
        if (isDashing)
        {
            
            //disable gravity until dash finish
            rb2D.gravityScale = 0f;
            dashTimer -= Time.deltaTime;
            if (dashTimer <= 0f)
            {
                isDashing = false;
                dashTimer = 0f;
                rb2D.gravityScale = 1.5f;
            }
        }
    }

    private void HandlePauseMenuInput()
    {
        // Handle pause menu input (check both keyboard and controller)
        bool pauseKeyPressed = Input.GetKeyDown(pauseMenuKey);
        bool pauseButtonPressed = enableController && Input.GetButtonDown(pauseMenuButtonName);
        
        if (pauseKeyPressed || pauseButtonPressed)
        {
            TogglePauseMenu();
        }
    }
    
    /// <summary>
    /// Toggle the pause menu and game pause state
    /// </summary>
    public void TogglePauseMenu()
    {
        if (GameManager.Instance == null)
        {
            Debug.LogWarning("PlayerController: GameManager not found! Cannot toggle pause.");
            return;
        }
        
        bool shouldPause = !GameManager.Instance.IsPaused;
        
        // Toggle game pause state
        GameManager.Instance.SetPauseState(shouldPause);
        
        // Toggle pause panel visibility
        if (pausePanel != null)
        {
            pausePanel.SetActive(shouldPause);
        }
        
        if (showDebugInfo)
        {
            Debug.Log($"PlayerController: Pause menu {(shouldPause ? "opened" : "closed")}");
        }
    }
    
    /// <summary>
    /// Open the pause menu
    /// </summary>
    public void OpenPauseMenu()
    {
        if (GameManager.Instance != null && !GameManager.Instance.IsPaused)
        {
            TogglePauseMenu();
        }
    }
    
    /// <summary>
    /// Close the pause menu
    /// </summary>
    public void ClosePauseMenu()
    {
        if (GameManager.Instance != null && GameManager.Instance.IsPaused)
        {
            TogglePauseMenu();
        }
    }

    private void HandleHeal()
    {
        // Handle heal input (only if can heal and not already healing)
        if (healPressed && CanHeal)
        {
            StartHeal();
        }
        
        // Update heal timer
        if (isHealing)
        {
            healTimer -= Time.deltaTime;
            
            if (healTimer <= 0f)
            {
                CompleteHeal();
            }
        }
        
        // Update heal cooldown timer
        if (healCooldownTimer > 0f)
        {
            healCooldownTimer -= Time.deltaTime;
        }
        
        // Reset heal pressed flag
        healPressed = false;
    }
    
    private void StartHeal()
    {
        if (playerStats.currentHealCount <= 0)
        {
            Debug.Log("Cannot heal: No heals remaining.");
            return;
        }
        isHealing = true;
        healTimer = healDuration;
        healCooldownTimer = healCooldown;
        
        // Stop movement while healing
        StopMovement();
        
        // Update PlayerStats healing state
        if (playerStats != null)
        {
            playerStats.IsHealing = true;
        }
        
        // Switch to healing animation
        if (universalAnimator != null)
        {
            universalAnimator.ForceEnableAnimation(HEALING_ANIM);
        }
        
        if (showDebugInfo)
        {
            Debug.Log($"Started healing for {healDuration} seconds, will heal {healAmount} HP");
        }
    }
    
    private void CompleteHeal()
    {
        isHealing = false;
        healTimer = 0f;
        
        // Apply healing to player stats
        if (playerStats != null)
        {
            playerStats.Heal(healAmount);
            playerStats.IsHealing = false;
        }
        
        // Spawn heal particle effect
        if (healParticlePrefab != null)
        {
            Instantiate(healParticlePrefab, transform.position, Quaternion.identity);
        }
        
        // Play heal completion sound
        if (healCompleteSound != null && audioSource != null)
        {
            audioSource.PlayOneShot(healCompleteSound);
        }
        
        // Return to appropriate animation
        SwitchToAnimationSetWithPriority();
        
        if (showDebugInfo)
        {
            Debug.Log($"Completed healing, restored {healAmount} HP");
        }
    }

    private void StopMovement()
    {
        // Stop all horizontal movement immediately
        Vector2 velocity = rb2D.velocity;
        velocity.x = 0f;
        rb2D.velocity = velocity;
    }
    private void HandleVariableJump()
    {
        if (!enableVariableJumpHeight) return;

        // If player releases jump button while moving upward and hasn't reached peak
        if (jumpReleased && rb2D.velocity.y > 0f)
        {
            Vector2 velocity = rb2D.velocity;
            velocity.y *= jumpCutMultiplier;
            rb2D.velocity = velocity;
        }

        // Reset jumpReleased after checking it
        jumpReleased = false;
    }

    private void UpdateFacingDirection()
    {
        // Update facing direction based on movement input
        // flip AllAnimation if facing left
        if (isMovingLeft)
        {
            facingRight = false;
            AllAnimationForFlipping.transform.localScale = new Vector3(-1f, 1f, 1f);
        }
        else if (isMovingRight)
        {
            facingRight = true;
            AllAnimationForFlipping.transform.localScale = new Vector3(1f, 1f, 1f);
        }
        


    }

    private void HandleAdvancedJumpTimers()
    {
        // Handle jump buffer timer
        if (enableJumpBuffering && jumpBufferCounter > 0f)
        {
            jumpBufferCounter -= Time.deltaTime;
        }
    }

    private void UpdatePlayerState()
    {
        previousState = currentState;
        
        // Simple state logic with timer-based grounding:
        // 1. When jump is pressed, set state to jumping
        // 2. If vertical velocity stays minimal for the timer duration, player is grounded
        // 3. If player has vertical movement, set state to jumping
        
        if (Mathf.Abs(rb2D.velocity.y) > groundedVelocityThreshold)
        {
            // Player has vertical movement - set to jumping
            currentState = PlayerState.Jumping;
            if (!isJumping)
            {
                isJumping = true; // Sync jumping flag with state
            }
        }
        else if (isGrounded)
        {
            // Player is grounded (velocity has been low for timer duration) - ground states
            isJumping = false; // Clear jumping flag when grounded
            
            if (IsMoving)
            {
                currentState = PlayerState.Moving;
                
                // Play move effect when player starts moving on ground
                if (moveEffect != null)
                {
                    moveEffect.Play();
                }
            }
            else
            {
                currentState = PlayerState.Idle;
            }
        }
        
        // Switch animation sets if state changed and auto-switch is enabled
        if (autoSwitchAnimations && previousState != currentState)
        {
            SwitchToAnimationSetWithPriority();
        }
        
        // Log state changes if debug is enabled
        if (showDebugInfo && (previousState != currentState || Time.frameCount % 60 == 0))
        {
            Debug.Log($"State: {currentState} | Velocity.y: {rb2D.velocity.y:F3} | Grounded: {isGrounded} | Timer: {groundedTimer:F2}s");
        }
    }

    private void DisplayDebugInfo()
    {
        Debug.Log($"State: {currentState} | " +
                 $"Horizontal Input: {horizontalInput:F2} | " +
                 $"Moving Left: {isMovingLeft} | " +
                 $"Moving Right: {isMovingRight} | " +
                 $"Grounded: {isGrounded} | " +
                 $"Jumping: {isJumping} | " +
                 $"Jump Count: {jumpCount} | " +
                 $"Double Jumped: {hasDoubleJumped} | " +
                 $"Coyote Time: {coyoteTimeCounter:F2} | " +
                 $"Jump Buffer: {jumpBufferCounter:F2} | " +
                 $"Jump Pressed: {jumpPressed} | " +
                 $"Grounded Timer: {groundedTimer:F2} | " +
                 $"Movement Blocked: {IsMovementBlocked} | " +
                 $"Dialogue Active: {(dialogueManager != null ? dialogueManager.IsDialogueActive.ToString() : "No Manager")} | " +
                 $"Dialogue Delay: {dialogueEndTimer:F2}s | " +
                 $"Dashing: {isDashing} | " +
                 $"Dash Timer: {dashTimer:F2}s | " +
                 $"Dash Direction: {dashDirection} | " +
                 $"Jump Held: {jumpHeld} | " +
                 $"Facing Right: {facingRight} | " +
                 $"Keyboard Input: L({(Input.GetKey(moveLeftKey1) || Input.GetKey(moveLeftKey2))}) R({(Input.GetKey(moveRightKey1) || Input.GetKey(moveRightKey2))}) | " +
                 $"Velocity: ({rb2D.velocity.x:F2}, {rb2D.velocity.y:F2})");
    }

    private void SwitchToAnimationSetWithPriority()
    {
        // Don't switch animations if dead
        if (isDead)
            return;
            
        // Priority: Hurt > Heal > Attack > Movement
        // Note: The UniversalAnimator already handles priority checking, but we still need
        // to respect the current state logic for attacks and heals
        
        if (isHurt)
        {
            // Highest priority: Hurt animation - already handled by TriggerHurtAnimation
            return;
        }
        else if (isHealing)
        {
            // Second highest priority: Heal animation - keep current heal animation active
            // Don't change animations while healing
            return;
        }
        else if (isAttacking && attackAnimationTimer > 0f)
        {
            // Third priority: Attack animations - keep current attack animation active
            // Don't change animations while attacking
            return;
        }
        else
        {
            // Lowest priority: Movement animations
            SwitchToAnimationSet(currentState);
        }
    }
    
    public void TriggerHurtAnimation()
    {
        // Called by PlayerStats when taking damage
        isHurt = true;
        hurtAnimationTimer = HURT_ANIMATION_DURATION;
        
        // If currently attacking, interrupt the attack
        if (isAttacking)
        {
            isAttacking = false;
            attackAnimationTimer = 0f;
        }
        
        // If currently healing, interrupt the healing
        if (isHealing)
        {
            isHealing = false;
            healTimer = 0f;
            if (playerStats != null)
            {
                playerStats.IsHealing = false;
            }
        }
        
        // Switch to hurt animation immediately (highest priority)
        if (universalAnimator != null)
        {
            universalAnimator.ForceEnableAnimation(HURT_ANIM);
        }
    }

    /// <summary>
    /// Manually trigger healing (for external systems)
    /// </summary>
    public void TriggerHeal()
    {
        if (CanHeal)
        {
            StartHeal();
        }
    }

    private void SwitchToAnimationSet(PlayerState state)
    {
        // Use UniversalAnimator to enable the appropriate animation based on state
        if (universalAnimator != null)
        {
            switch (state)
            {
                case PlayerState.Idle:
                    universalAnimator.ForceEnableAnimation(IDLE_ANIM);
                    break;
                case PlayerState.Moving:
                    universalAnimator.ForceEnableAnimation(MOVING_ANIM);
                    break;
                case PlayerState.Jumping:
                    universalAnimator.ForceEnableAnimation(JUMPING_ANIM);
                    break;
            }
        }
    }

    #region Unity Editor Gizmos
    private void OnDrawGizmosSelected()
    {
        // Simple visualization for velocity-based ground detection
        Gizmos.color = isGrounded ? Color.green : Color.red;
        Vector3 playerPos = transform.position;
        
        // Draw a simple circle around the player
        Gizmos.DrawWireSphere(playerPos, 0.5f);
        
        // Draw velocity indicator
        Gizmos.color = Color.blue;
        Vector3 velocityIndicator = playerPos + Vector3.up * (rb2D != null ? rb2D.velocity.y : 0f) * 0.1f;
        Gizmos.DrawLine(playerPos, velocityIndicator);
    }
    #endregion

    #region Public Methods
    /// <summary>
    /// Forces ground state for testing
    /// </summary>
    /// <param name="grounded">Force grounded state</param>
    public void ForceGroundedState(bool grounded)
    {
        isGrounded = grounded;
        if (grounded)
        {
            isJumping = false;
            hasDoubleJumped = false;
            jumpCount = 0;
            groundedTimer = groundedTimerDuration; // Set timer as if already grounded
        }
        else
        {
            groundedTimer = 0f;
        }
    }

    public void SetDummyState(float duration)
    {
        StartCoroutine(DummyStateCoroutine(duration));
    }

    private IEnumerator DummyStateCoroutine(float duration)
    {
        // Disable player movement
        bool previousMovementState = enableMovement;
        enableMovement = false;

        // Wait for the specified duration
        yield return new WaitForSeconds(duration);

        // Revert to the previous state
        //enableMovement = previousMovementState;
        if (playerStats.currentHealth > 0)
        {
            enableMovement = true;
            Debug.Log("Dummy state ended, movement re-enabled");
        }
        else if (playerStats.currentHealth <= 0 && playerStats.currentHealth != -114514){
            Debug.Log(playerStats.currentHealth);
            enableMovement = false;
            SetDummyState(5f);
            playerStats.currentHealth = -114514;
        }
            
    }

    public void Pogo(){
        //when player downswing an enemy, give player a small upward boost
        rb2D.velocity = new Vector2(rb2D.velocity.x, 0f);
        rb2D.AddForce(Vector2.up * 5f, ForceMode2D.Impulse);
    }
    #endregion
}