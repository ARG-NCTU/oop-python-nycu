using UnityEngine;

/// <summary>
/// Movement Enemy Attack Hitbox - Enhanced Enemy Attack with movement capabilities
/// Supports two movement modes: JustGo (linear movement) and GoAndReturn (cosine-based movement)
/// </summary>
public class MovementEnemyAttackHitbox : EnemyAttackHitbox
{
    [System.Serializable]
    public enum MovementMode
    {
        JustGo,         // Move in direction until destroyed
        GoAndReturn     // Move out, then return with cosine movement
    }
    
    [Header("Movement Settings")]
    [SerializeField] private MovementMode movementOption = MovementMode.JustGo;
    [SerializeField] private Vector3 direction = Vector3.right; // Movement direction
    [SerializeField] private float moveSpeed = 5f; // Movement speed
    [SerializeField] private bool normalizeDirection = true; // Auto-normalize direction vector
    [SerializeField] private bool useWorldSpace = true; // Whether direction is in world space or local space
    
    [Header("GoAndReturn Settings")]
    [SerializeField] private float maxDistance = 3f; // Maximum distance to travel before returning
    [SerializeField] private AnimationCurve speedCurve = AnimationCurve.Linear(0f, 1f, 1f, 1f); // Speed modulation over time
    [SerializeField] private bool pauseAtPeak = false; // Whether to pause briefly at the furthest point
    [SerializeField] private float pauseDuration = 0.1f; // How long to pause at peak
    
    [Header("Movement Visual Settings")]
    [SerializeField] private bool showMovementPath = true;
    [SerializeField] private Color movementGizmoColor = Color.green;
    [SerializeField] private GameObject movementTrail; // Optional trail effect
    [SerializeField] private bool rotateToMovement = false; // Whether to rotate towards movement direction
    
    [Header("Movement Debug")]
    [SerializeField] private bool showMovementDebug = false;
    
    // Private movement variables
    private Vector3 startPosition;
    private Vector3 targetDirection;
    private float movementTimer = 0f;
    private bool isReturning = false;
    private bool isPaused = false;
    private float pauseTimer = 0f;
    private Vector3 peakPosition;
    private Rigidbody2D rb;
    
    // Movement phases for GoAndReturn
    private float outwardPhaseTime;
    private float returnPhaseTime;
    
    // Events
    public System.Action OnMovementStarted;
    public System.Action OnReachedPeak; // For GoAndReturn mode
    public System.Action OnReturnStarted; // For GoAndReturn mode
    public System.Action OnMovementCompleted; // When movement ends
    
    // Properties
    public MovementMode CurrentMovementMode => movementOption;
    public Vector3 Direction => direction;
    public float MoveSpeed => moveSpeed;
    public bool IsReturning => isReturning;
    public bool IsPaused => isPaused;
    public float MovementProgress => movementTimer / Lifetime;
    
    private void Awake()
    {
        // Get or add Rigidbody2D for movement
        rb = GetComponent<Rigidbody2D>();
        if (rb == null)
        {
            rb = gameObject.AddComponent<Rigidbody2D>();
            rb.gravityScale = 0f; // Disable gravity for hitbox
            rb.angularDrag = 0f;
            rb.drag = 0f;
        }
        
        // Ensure rigidbody is kinematic for controlled movement
        rb.isKinematic = true;
    }
    
    private void Start()
    {
        // Auto-destroy this hitbox after the specified lifetime
        Destroy(gameObject, Lifetime);
        
        // Initialize movement
        InitializeMovement();
        
        // Start movement trail if specified
        if (movementTrail != null)
        {
            GameObject trail = Instantiate(movementTrail, transform);
        }
        
        OnMovementStarted?.Invoke();
        
        if (showMovementDebug)
        {
            Debug.Log($"MovementEnemyAttackHitbox: Started {movementOption} movement. Direction: {targetDirection}, Speed: {moveSpeed}");
        }
    }
    
    private void Update()
    {
        // Handle movement based on mode
        HandleMovement();
        
        // Update rotation if enabled
        if (rotateToMovement && rb.velocity.magnitude > 0.1f)
        {
            float angle = Mathf.Atan2(rb.velocity.y, rb.velocity.x) * Mathf.Rad2Deg;
            transform.rotation = Quaternion.AngleAxis(angle, Vector3.forward);
        }
    }
    
    /// <summary>
    /// Initialize movement settings and direction
    /// </summary>
    private void InitializeMovement()
    {
        startPosition = transform.position;
        
        // Normalize direction if enabled
        if (normalizeDirection && direction.magnitude > 0f)
        {
            direction = direction.normalized;
        }
        
        // Convert direction to world space if needed
        if (useWorldSpace)
        {
            targetDirection = direction;
        }
        else
        {
            targetDirection = transform.TransformDirection(direction);
        }
        
        // Calculate movement phases for GoAndReturn mode
        if (movementOption == MovementMode.GoAndReturn)
        {
            outwardPhaseTime = (Lifetime - pauseDuration) * 0.5f;
            returnPhaseTime = (Lifetime - pauseDuration) * 0.5f;
            
            // Calculate peak position
            peakPosition = startPosition + targetDirection * maxDistance;
            
            if (showMovementDebug)
            {
                Debug.Log($"MovementEnemyAttackHitbox: GoAndReturn initialized. Peak: {peakPosition}, OutwardTime: {outwardPhaseTime}, ReturnTime: {returnPhaseTime}");
            }
        }
        
        movementTimer = 0f;
    }
    
    /// <summary>
    /// Handle movement based on the selected mode
    /// </summary>
    private void HandleMovement()
    {
        movementTimer += Time.deltaTime;
        
        switch (movementOption)
        {
            case MovementMode.JustGo:
                HandleJustGoMovement();
                break;
                
            case MovementMode.GoAndReturn:
                HandleGoAndReturnMovement();
                break;
        }
    }
    
    /// <summary>
    /// Handle linear movement in one direction
    /// </summary>
    private void HandleJustGoMovement()
    {
        // Simple linear movement
        float currentSpeed = moveSpeed * speedCurve.Evaluate(MovementProgress);
        Vector3 velocity = targetDirection * currentSpeed;
        
        rb.velocity = velocity;
        
        if (showMovementDebug && Time.frameCount % 30 == 0) // Log every 30 frames
        {
            Debug.Log($"MovementEnemyAttackHitbox: JustGo movement. Velocity: {velocity}, Progress: {MovementProgress:F2}");
        }
    }
    
    /// <summary>
    /// Handle cosine-based go and return movement
    /// </summary>
    private void HandleGoAndReturnMovement()
    {
        if (isPaused)
        {
            // Handle pause at peak
            pauseTimer += Time.deltaTime;
            rb.velocity = Vector3.zero;
            
            if (pauseTimer >= pauseDuration)
            {
                isPaused = false;
                isReturning = true;
                OnReturnStarted?.Invoke();
                
                if (showMovementDebug)
                {
                    Debug.Log($"MovementEnemyAttackHitbox: Started returning from peak");
                }
            }
            return;
        }
        
        Vector3 velocity = Vector3.zero;
        
        if (!isReturning)
        {
            // Outward movement phase
            if (movementTimer <= outwardPhaseTime)
            {
                // Use cosine for smooth acceleration/deceleration
                float progress = movementTimer / outwardPhaseTime;
                float cosineProgress = (1f - Mathf.Cos(progress * Mathf.PI)) * 0.5f; // 0 to 1 with cosine ease
                
                float currentSpeed = moveSpeed * speedCurve.Evaluate(progress);
                velocity = targetDirection * currentSpeed;
                
                // Apply cosine-based speed modulation (fast at start/end, slow in middle)
                float cosineSpeedMultiplier = Mathf.Sin(progress * Mathf.PI); // 0 to 1 to 0
                velocity *= cosineSpeedMultiplier;
            }
            else
            {
                // Reached peak - start pause or return
                if (pauseAtPeak && pauseDuration > 0f)
                {
                    isPaused = true;
                    pauseTimer = 0f;
                    OnReachedPeak?.Invoke();
                }
                else
                {
                    isReturning = true;
                    OnReachedPeak?.Invoke();
                    OnReturnStarted?.Invoke();
                }
            }
        }
        else
        {
            // Return movement phase
            float returnStartTime = outwardPhaseTime + (pauseAtPeak ? pauseDuration : 0f);
            float returnProgress = (movementTimer - returnStartTime) / returnPhaseTime;
            
            if (returnProgress <= 1f)
            {
                // Use cosine for smooth return movement
                float cosineProgress = (1f - Mathf.Cos(returnProgress * Mathf.PI)) * 0.5f;
                
                float currentSpeed = moveSpeed * speedCurve.Evaluate(returnProgress);
                velocity = -targetDirection * currentSpeed; // Move back towards start
                
                // Apply cosine-based speed modulation (fast at start, slow at end)
                float cosineSpeedMultiplier = Mathf.Sin(returnProgress * Mathf.PI);
                velocity *= cosineSpeedMultiplier;
            }
            else
            {
                // Movement completed
                velocity = Vector3.zero;
                OnMovementCompleted?.Invoke();
            }
        }
        
        rb.velocity = velocity;
        
        if (showMovementDebug && Time.frameCount % 30 == 0)
        {
            Debug.Log($"MovementEnemyAttackHitbox: GoAndReturn. Returning: {isReturning}, Paused: {isPaused}, Velocity: {velocity.magnitude:F2}");
        }
    }
    
    /// <summary>
    /// Manually stop movement
    /// </summary>
    public void StopMovement()
    {
        if (rb != null)
        {
            rb.velocity = Vector3.zero;
        }
        
        OnMovementCompleted?.Invoke();
        
        if (showMovementDebug)
        {
            Debug.Log($"MovementEnemyAttackHitbox: Movement stopped manually");
        }
    }
    
    /// <summary>
    /// Change movement direction during runtime
    /// </summary>
    /// <param name="newDirection">New direction to move</param>
    /// <param name="worldSpace">Whether the direction is in world space</param>
    public void ChangeDirection(Vector3 newDirection, bool worldSpace = true)
    {
        direction = newDirection;
        
        if (normalizeDirection && newDirection.magnitude > 0f)
        {
            direction = direction.normalized;
        }
        
        if (worldSpace)
        {
            targetDirection = direction;
        }
        else
        {
            targetDirection = transform.TransformDirection(direction);
        }
        
        if (showMovementDebug)
        {
            Debug.Log($"MovementEnemyAttackHitbox: Direction changed to {targetDirection}");
        }
    }
    
    /// <summary>
    /// Force the return phase in GoAndReturn mode
    /// </summary>
    public void ForceReturn()
    {
        if (movementOption == MovementMode.GoAndReturn && !isReturning)
        {
            isReturning = true;
            isPaused = false;
            OnReachedPeak?.Invoke();
            OnReturnStarted?.Invoke();
            
            if (showMovementDebug)
            {
                Debug.Log($"MovementEnemyAttackHitbox: Forced return phase");
            }
        }
    }
    
    private void OnDrawGizmos()
    {
        if (!showMovementPath) return;
        
        Gizmos.color = movementGizmoColor;
        
        Vector3 startPos = Application.isPlaying ? startPosition : transform.position;
        Vector3 currentDirection = Application.isPlaying ? targetDirection : (useWorldSpace ? direction : transform.TransformDirection(direction));
        
        if (normalizeDirection && currentDirection.magnitude > 0f)
        {
            currentDirection = currentDirection.normalized;
        }
        
        switch (movementOption)
        {
            case MovementMode.JustGo:
                // Draw direction arrow
                Vector3 endPos = startPos + currentDirection * 2f; // 2 units for visualization
                Gizmos.DrawLine(startPos, endPos);
                Gizmos.DrawWireSphere(endPos, 0.1f);
                break;
                
            case MovementMode.GoAndReturn:
                // Draw outward path
                Vector3 peakPos = startPos + currentDirection * maxDistance;
                Gizmos.DrawLine(startPos, peakPos);
                
                // Draw return path with different color
                Gizmos.color = Color.Lerp(movementGizmoColor, Color.red, 0.5f);
                Gizmos.DrawLine(peakPos, startPos);
                
                // Draw peak indicator
                Gizmos.DrawWireSphere(peakPos, 0.2f);
                
                // Draw pause indicator if enabled
                if (pauseAtPeak)
                {
                    Gizmos.color = Color.yellow;
                    Gizmos.DrawWireCube(peakPos, Vector3.one * 0.1f);
                }
                break;
        }
        
        // Draw speed indicator
        #if UNITY_EDITOR
        if (showMovementDebug)
        {
            Vector3 textPos = transform.position + Vector3.up * 1.5f;
            string modeText = movementOption.ToString();
            string speedText = $"Speed: {moveSpeed:F1}";
            if (Application.isPlaying)
            {
                speedText += $"\nProgress: {MovementProgress:F2}";
                if (movementOption == MovementMode.GoAndReturn)
                {
                    speedText += $"\nReturning: {isReturning}";
                }
            }
            UnityEditor.Handles.Label(textPos, $"{modeText}\n{speedText}");
        }
        #endif
    }
    
    private void OnValidate()
    {
        // Clamp movement values
        moveSpeed = Mathf.Max(0f, moveSpeed);
        maxDistance = Mathf.Max(0.1f, maxDistance);
        pauseDuration = Mathf.Max(0f, pauseDuration);
        
        // Ensure pause duration doesn't exceed lifetime
        if (pauseDuration >= Lifetime && Lifetime > 0f)
        {
            Debug.LogWarning($"MovementEnemyAttackHitbox: PauseDuration ({pauseDuration}) should be less than Lifetime ({Lifetime})");
        }
        
        // Initialize speed curve if null
        if (speedCurve == null || speedCurve.keys.Length == 0)
        {
            speedCurve = AnimationCurve.Linear(0f, 1f, 1f, 1f);
        }
    }
    
    /// <summary>
    /// Get debug information about the movement state
    /// </summary>
    /// <returns>Debug string with movement information</returns>
    public string GetMovementDebugInfo()
    {
        return $"MovementEnemyAttackHitbox - {gameObject.name}: " +
               $"Mode: {movementOption} | " +
               $"Speed: {moveSpeed:F1} | " +
               $"Direction: {targetDirection} | " +
               $"Progress: {MovementProgress:F2} | " +
               $"Returning: {isReturning} | " +
               $"Paused: {isPaused} | " +
               $"Velocity: {(rb != null ? rb.velocity.magnitude.ToString("F2") : "N/A")}";
    }
}
