using UnityEngine;

/// <summary>
/// Universal Enemy Stats component for managing enemy's health, damage, and other statistics
/// This is the base stats component that every enemy should have
/// Works with specific EnemyAI scripts for different enemy behaviors
/// Features knockback system and integrates with EnemyAI for death handling
/// </summary>
public class EnemyStats : MonoBehaviour
{
    [Header("Health Settings")]
    [SerializeField] public float maxHealth = 50f;
    [SerializeField] public float currentHealth = 50f;
    [SerializeField] private bool canTakeDamage = true;
    
    [Header("Invulnerability Settings")]
    [SerializeField] private float invulnerableFrameDuration = 0.5f;
    private bool isInvulnerable = false;
    private float invulnerableTimer = 0f;
    
    private float attackDamage = 15f;
    private float defence = 2f;
    
    [Header("Knockback Settings")]
    [SerializeField] private float knockbackForce = 5f;
    [SerializeField] private float knockbackUpwardForce = 3f;
    [SerializeField] private float knockbackDuration = 0.2f;
    
    [Header("Movement Modifier")]
    [SerializeField] private float walkSpeedAdjustment = 1f; // Multiplier for base walk speed
    
    [Header("Component References")]
    private MonoBehaviour enemyAI; // Generic reference to any EnemyAI script
    [SerializeField] private Rigidbody2D rb2D; // Reference to Rigidbody2D for movement tracking
    
    [Header("Visual Settings")]
    [SerializeField] private bool isFacingRight = true; // Current facing direction
    [SerializeField] private bool enableAutoFlip = true; // Enable automatic flipping based on movement
    [SerializeField] private float flipThreshold = 0.1f; // Minimum velocity to trigger flip
    [SerializeField] private float flipCooldown = 0.5f; // Cooldown between flips to prevent rapid flipping
    
    // Events for stat changes
    public System.Action<float, float> OnHealthChanged; // currentHealth, maxHealth
    public System.Action OnEnemyDeath;
    public System.Action<float> OnDamageReceived; // damage amount
    public System.Action OnInvulnerabilityStart;
    public System.Action OnInvulnerabilityEnd;
    
    // Properties for external access
    public float MaxHealth
    {
        get => maxHealth;
        set
        {
            maxHealth = Mathf.Max(1f, value);
            currentHealth = Mathf.Min(currentHealth, maxHealth);
            OnHealthChanged?.Invoke(currentHealth, maxHealth);
        }
    }
    
    public float CurrentHealth
    {
        get => currentHealth;
        private set
        {
            float oldHealth = currentHealth;
            currentHealth = Mathf.Clamp(value, 0f, maxHealth);
            if (oldHealth != currentHealth)
            {
                OnHealthChanged?.Invoke(currentHealth, maxHealth);
            }
        }
    }
    
    public float HealthPercentage => maxHealth > 0 ? currentHealth / maxHealth : 0f;
    public bool IsAlive => currentHealth > 0f;
    public bool IsDead => currentHealth <= 0f;
    
    public float InvulnerableFrameDuration
    {
        get => invulnerableFrameDuration;
        set => invulnerableFrameDuration = Mathf.Max(0f, value);
    }
    
    public bool IsInvulnerable => isInvulnerable;
    public float InvulnerableTimeRemaining => invulnerableTimer;
    
    public float AttackDamage
    {
        get => attackDamage;
        set => attackDamage = Mathf.Max(0f, value);
    }
    
    public float Defence
    {
        get => defence;
        set => defence = Mathf.Max(0f, value);
    }
    
    public float KnockbackForce
    {
        get => knockbackForce;
        set => knockbackForce = Mathf.Max(0f, value);
    }
    
    public float KnockbackUpwardForce
    {
        get => knockbackUpwardForce;
        set => knockbackUpwardForce = Mathf.Max(0f, value);
    }
    
    public float KnockbackDuration
    {
        get => knockbackDuration;
        set => knockbackDuration = Mathf.Max(0f, value);
    }
    
    public float WalkSpeedAdjustment
    {
        get => walkSpeedAdjustment;
        set
        {
            walkSpeedAdjustment = Mathf.Max(0.1f, value); // Minimum 10% speed
            // Notify AI about speed change
            NotifyAIOfSpeedChange();
        }
    }
    
    public MonoBehaviour EnemyAI
    {
        get => enemyAI;
        set => enemyAI = value;
    }
    
    public bool IsFacingRight
    {
        get => isFacingRight;
        set
        {
            if (isFacingRight != value)
            {
                isFacingRight = value;
                UpdateVisualFacing();
            }
        }
    }
    
    public bool EnableAutoFlip
    {
        get => enableAutoFlip;
        set => enableAutoFlip = value;
    }
    
    // Knockback system variables
    private Rigidbody2D rb;
    private bool isKnockedBack = false;
    private float knockbackTimer = 0f;
    private float lastFlipTime = 0f; // Track when the last flip occurred
    
    private void Awake()
    {
        // Get components
        rb = GetComponent<Rigidbody2D>();
        
        // Auto-assign rb2D if not set
        if (rb2D == null)
        {
            rb2D = rb; // Use the same reference for movement tracking
        }
        // Set cross-reference in AI if it supports it
        SetAICrossReference();
    }
    
    private void Start()
    {
        // Initialize stats
        CurrentHealth = currentHealth;
        
        // Update AI speed with our modifier
        NotifyAIOfSpeedChange();
    }
    
    private void Update()
    {
        // Handle invulnerability timer
        if (isInvulnerable)
        {
            invulnerableTimer -= Time.deltaTime;
            if (invulnerableTimer <= 0f)
            {
                EndInvulnerability();
            }
        }
        
        // Handle knockback timer
        if (isKnockedBack)
        {
            knockbackTimer -= Time.deltaTime;
            if (knockbackTimer <= 0f)
            {
                EndKnockback();
            }
        }
        
        // Handle automatic flipping based on movement
        if (enableAutoFlip && rb2D != null)
        {
            HandleAutoFlip();
        }
    }
    
    /// <summary>
    /// Apply damage to the enemy
    /// </summary>
    /// <param name="damage">Damage amount</param>
    /// <param name="hasKnockback">Whether to apply knockback</param>
    /// <param name="playerPosition">Position of attacking player for knockback direction</param>
    /// <param name="ignoreDefence">If true, ignores defence stat</param>
    /// <returns>True if damage was dealt, false if blocked</returns>
    public bool TakeDamage(float damage, bool hasKnockback = false, Vector3 playerPosition = default, bool ignoreDefence = false)
    {
        // Check if can take damage (always consider invulnerability)
        if (!canTakeDamage || isInvulnerable || IsDead)
        {
            return false;
        }
        
        // Calculate final damage
        float finalDamage = damage;
        if (!ignoreDefence)
        {
            finalDamage = Mathf.Max(1f, damage - defence); // Minimum 1 damage
        }
        
        // Apply damage
        CurrentHealth -= finalDamage;
        OnDamageReceived?.Invoke(finalDamage);
        
        // Apply knockback if enabled
        if (hasKnockback && rb != null)
        {
            ApplyKnockback(playerPosition);
        }
        
        // Start invulnerability frames
        if (invulnerableFrameDuration > 0f)
        {
            StartInvulnerability();
        }
        
        // Check for death
        if (IsDead)
        {
            HandleDeath();
        }
        return true;
    }
    
    /// <summary>
    /// Heal the enemy
    /// </summary>
    /// <param name="healAmount">Amount to heal</param>
    /// <returns>Actual amount healed</returns>
    public float Heal(float healAmount)
    {
        if (IsDead) return 0f;
        
        float oldHealth = currentHealth;
        CurrentHealth += healAmount;
        
        return currentHealth - oldHealth;
    }
    
    /// <summary>
    /// Start invulnerability frames
    /// </summary>
    public void StartInvulnerability()
    {
        if (invulnerableFrameDuration <= 0f) return;
        
        isInvulnerable = true;
        invulnerableTimer = invulnerableFrameDuration;
        OnInvulnerabilityStart?.Invoke();
        
    }
    
    /// <summary>
    /// End invulnerability frames
    /// </summary>
    public void EndInvulnerability()
    {
        isInvulnerable = false;
        invulnerableTimer = 0f;
        OnInvulnerabilityEnd?.Invoke();
    }
    
    /// <summary>
    /// Apply knockback force towards direction away from player
    /// </summary>
    /// <param name="playerPosition">Position of the attacking player</param>
    private void ApplyKnockback(Vector3 playerPosition)
    {
        if (rb == null || knockbackForce <= 0f) return;
        
        // Calculate direction away from player
        Vector2 knockbackDirection;
        if (playerPosition != default)
        {
            knockbackDirection = (transform.position - playerPosition).normalized;
        }
        else
        {
            // Fallback: use current facing direction or right
            knockbackDirection = Vector2.right;
        }
        
        // Apply knockback force
        Vector2 knockbackVelocity = new Vector2(
            knockbackDirection.x * knockbackForce,
            knockbackUpwardForce
        );
        
        rb.velocity = knockbackVelocity;
        
        // Start knockback state
        isKnockedBack = true;
        knockbackTimer = knockbackDuration;
        
        // Notify AI about knockback start
        NotifyAIOfKnockback(true);
    }
    
    /// <summary>
    /// End knockback state
    /// </summary>
    private void EndKnockback()
    {
        isKnockedBack = false;
        knockbackTimer = 0f;
        
        // Restore AI control
        NotifyAIOfKnockback(false);
    }
    
    /// <summary>
    /// Handle death sequence
    /// </summary>
    private void HandleDeath()
    {
        OnEnemyDeath?.Invoke();
        
        // Call death sequence in AI if available
        NotifyAIOfDeath();
    }
    
    /// <summary>
    /// Enable or disable damage taking
    /// </summary>
    /// <param name="canTake">True to enable damage, false to disable</param>
    public void SetCanTakeDamage(bool canTake)
    {
        canTakeDamage = canTake;
    }
    
    /// <summary>
    /// Check if enemy is currently in a disabled state (knockback, death, etc.)
    /// </summary>
    public bool IsDisabled => IsDead || isKnockedBack;
    
    /// <summary>
    /// Get debug information about current stats
    /// </summary>
    /// <returns>Debug string with current stats</returns>
    public string GetDebugInfo()
    {
        return $"EnemyStats - {gameObject.name}: " +
               $"Health: {currentHealth:F1}/{maxHealth:F1} | " +
               $"Defence: {defence:F1} | " +
               $"Attack: {attackDamage:F1} | " +
               $"Speed Adj: {walkSpeedAdjustment:F1} | " +
               $"Knockback: {isKnockedBack} | " +
               $"Invulnerable: {isInvulnerable} ({invulnerableTimer:F2}s) | " +
               $"Alive: {IsAlive}";
    }
    
    #region Visual Flipping Methods
    
    /// <summary>
    /// Handle automatic flipping based on Rigidbody2D movement
    /// </summary>
    private void HandleAutoFlip()
    {
        if (rb2D == null) return;
        
        // Check if enough time has passed since last flip
        if (Time.time - lastFlipTime < flipCooldown)
        {
            return; // Still in cooldown
        }
        
        // Check horizontal velocity
        float horizontalVelocity = rb2D.velocity.x;
        
        // Only flip if velocity is above threshold to avoid jittering
        if (Mathf.Abs(horizontalVelocity) > flipThreshold)
        {
            bool shouldFaceRight = horizontalVelocity > 0f;
            
            // Update facing direction if it changed
            if (shouldFaceRight != isFacingRight)
            {
                IsFacingRight = shouldFaceRight;
                lastFlipTime = Time.time; // Record the flip time
                
            }
        }
    }
    
    /// <summary>
    /// Update the visual facing of the enemy gameobject
    /// </summary>
    private void UpdateVisualFacing()
    {
        if (transform == null) return;
        
        // Get current scale
        Vector3 scale = transform.localScale;
        
        // Set x scale based on facing direction
        // Positive scale = facing right, negative scale = facing left
        float targetScaleX = isFacingRight ? Mathf.Abs(scale.x) : -Mathf.Abs(scale.x);
        
        // Apply the scale
        if (Mathf.Abs(scale.x - targetScaleX) > 0.001f) // Avoid unnecessary updates
        {
            scale.x = targetScaleX;
            transform.localScale = scale;
        }
    }
    
    /// <summary>
    /// Manually set the facing direction (useful for skills that need specific facing)
    /// </summary>
    /// <param name="faceRight">True to face right, false to face left</param>
    /// <param name="force">Force the update even if enableAutoFlip is false or cooldown is active</param>
    public void SetFacingDirection(bool faceRight, bool force = false)
    {
        if (!enableAutoFlip && !force) return;
        
        // Check cooldown unless forced
        if (!force && Time.time - lastFlipTime < flipCooldown) return;
        
        if (isFacingRight != faceRight)
        {
            IsFacingRight = faceRight;
            lastFlipTime = Time.time; // Record the flip time
        }
    }
    
    /// <summary>
    /// Make enemy face towards a specific position
    /// </summary>
    /// <param name="targetPosition">Position to face towards</param>
    /// <param name="force">Force the update even if enableAutoFlip is false or cooldown is active</param>
    public void FaceTowards(Vector3 targetPosition, bool force = false)
    {
        if (!enableAutoFlip && !force) return;
        
        // Check cooldown unless forced
        if (!force && Time.time - lastFlipTime < flipCooldown) return;
        
        bool shouldFaceRight = targetPosition.x > transform.position.x;
        if (isFacingRight != shouldFaceRight)
        {
            IsFacingRight = shouldFaceRight;
            lastFlipTime = Time.time; // Record the flip time
        }
    }
    
    #endregion
    
    #region AI Communication Methods
    
    /// <summary>
    /// Set cross-reference in AI component if it supports it
    /// </summary>
    private void SetAICrossReference()
    {
        if (enemyAI == null) return;
        
        // Try to set EnemyStats reference using reflection
        var aiType = enemyAI.GetType();
        var statsProperty = aiType.GetProperty("EnemyStats");
        var statsField = aiType.GetField("enemyStats");
        
        if (statsProperty != null && statsProperty.CanWrite)
        {
            statsProperty.SetValue(enemyAI, this);
        }
        else if (statsField != null)
        {
            statsField.SetValue(enemyAI, this);
        }
    }
    
    /// <summary>
    /// Notify AI about speed changes
    /// </summary>
    private void NotifyAIOfSpeedChange()
    {
        if (enemyAI == null) return;
        
        // Try to call UpdateMovementSpeed method if it exists
        var aiType = enemyAI.GetType();
        var updateMethod = aiType.GetMethod("UpdateMovementSpeed");
        
        if (updateMethod != null)
        {
            updateMethod.Invoke(enemyAI, null);
        }
    }
    
    /// <summary>
    /// Notify AI about knockback state changes
    /// </summary>
    /// <param name="isKnockedBack">True if starting knockback, false if ending</param>
    private void NotifyAIOfKnockback(bool isKnockedBack)
    {
        if (enemyAI == null) return;
        
        // Try to call SetControlEnabled method if it exists
        var aiType = enemyAI.GetType();
        var controlMethod = aiType.GetMethod("SetControlEnabled");
        
        if (controlMethod != null)
        {
            controlMethod.Invoke(enemyAI, new object[] { !isKnockedBack });
        }
    }
    
    /// <summary>
    /// Notify AI about death
    /// </summary>
    private void NotifyAIOfDeath()
    {
        if (enemyAI == null) return;
        
        // Try to call DeathSequence method if it exists
        var aiType = enemyAI.GetType();
        var deathMethod = aiType.GetMethod("DeathSequence");
        
        if (deathMethod != null)
        {
            deathMethod.Invoke(enemyAI, null);

        }
    }
    
    #endregion
    
    private void OnValidate()
    {
        // Clamp values in editor
        maxHealth = Mathf.Max(1f, maxHealth);
        currentHealth = Mathf.Clamp(currentHealth, 0f, maxHealth);
        invulnerableFrameDuration = Mathf.Max(0f, invulnerableFrameDuration);
        attackDamage = Mathf.Max(0f, attackDamage);
        defence = Mathf.Max(0f, defence);
        knockbackForce = Mathf.Max(0f, knockbackForce);
        knockbackUpwardForce = Mathf.Max(0f, knockbackUpwardForce);
        knockbackDuration = Mathf.Max(0f, knockbackDuration);
        walkSpeedAdjustment = Mathf.Max(0.1f, walkSpeedAdjustment);
        flipThreshold = Mathf.Max(0.01f, flipThreshold);
    }
}

/// <summary>
/// Interface for EnemyAI components to ensure proper communication with EnemyStats
/// Implement this interface in your specific AI scripts for automatic detection
/// </summary>
public interface IEnemyAI
{
    EnemyStats EnemyStats { get; set; }
    void UpdateMovementSpeed();
    void SetControlEnabled(bool enabled);
    void DeathSequence();
}
