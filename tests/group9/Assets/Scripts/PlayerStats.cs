using UnityEngine;

/// <summary>
/// Player Stats component for managing player's health, mana, damage, and other statistics
/// Works alongside PlayerController to provide complete player functionality
/// Features knockback system that temporarily disables player control during damage
/// </summary>
public class PlayerStats : MonoBehaviour
{
    [Header("Health Settings")]
    [SerializeField] public float maxHealth = 100f;
    [SerializeField] public float currentHealth = 100f;
    [SerializeField] private bool canTakeDamage = true;
    [SerializeField] public float maxSanity = 100f;
    [SerializeField] public float currentSanity = 100f;
    [SerializeField] private bool canTakeSanityDamage = true;

    [Header("Invulnerability Settings")]
    [SerializeField] private float invulnerableFrameDuration = 1f;
    [SerializeField] private bool isInvulnerable = false;
    [SerializeField] private float sanityInvulnerableFrameDuration = 1f;
    [SerializeField] private bool isSanityInvulnerable = false;
    private float invulnerableTimer = 0f;

    [Header("Combat Settings")]
    [SerializeField] private float attackDamage = 5f;
    [SerializeField] private float defence = 5f;

    [Header("Knockback Settings")]
    [SerializeField] private float knockbackForce = 8f;
    [SerializeField] private float knockbackUpwardForce = 5f;
    [SerializeField] private float knockbackDuration = 0.3f;

    [Header("Movement Modifier")]
    [SerializeField] private float walkSpeedAdjustment = 1f; // Multiplier for base walk speed

    [Header("Heal Settings")]
    [SerializeField] private bool isHealing = false;
    public int maxHealCount = 3;
    public int currentHealCount = 3;

    [Header("Mana Settings")]
    [SerializeField] private float maxMana = 50f;
    [SerializeField] private float currentMana = 50f;
    [SerializeField] private float manaRegenRate = 5f; // Mana per second
    [SerializeField] private bool enableManaRegen = true;

    [Header("Buff Settings")]
    public bool Enlight = false;
    public bool Slow = false;

    [Header("Component References")]
    [SerializeField] private PlayerController playerController;
    [SerializeField] private DeathPanelController deathPanelController;


    // Events for stat changes
    public System.Action<float, float> OnHealthChanged; // currentHealth, maxHealth
    public System.Action<float, float> OnManaChanged;   // currentMana, maxMana
    public System.Action OnPlayerDeath;
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
            // Update PlayerController's speed if reference exists
            if (playerController != null)
            {
                UpdatePlayerControllerSpeed();
            }
        }
    }

    public float MaxMana
    {
        get => maxMana;
        set
        {
            maxMana = Mathf.Max(0f, value);
            currentMana = Mathf.Min(currentMana, maxMana);
            OnManaChanged?.Invoke(currentMana, maxMana);
        }
    }

    public float CurrentMana
    {
        get => currentMana;
        private set
        {
            float oldMana = currentMana;
            currentMana = Mathf.Clamp(value, 0f, maxMana);
            if (oldMana != currentMana)
            {
                OnManaChanged?.Invoke(currentMana, maxMana);
            }
        }
    }

    public float ManaPercentage => maxMana > 0 ? currentMana / maxMana : 0f;
    public bool HasMana => currentMana > 0f;

    public PlayerController PlayerController
    {
        get => playerController;
        set => playerController = value;
    }

    public bool IsHealing
    {
        get => isHealing;
        set => isHealing = value;
    }

    private void Awake()
    {
        // Auto-find PlayerController if not assigned
        if (playerController == null)
        {
            playerController = GetComponent<PlayerController>();
        }

        // Set PlayerStats reference in PlayerController
        if (playerController != null)
        {
            playerController.PlayerStats = this;
        }
    }

    private void Start()
    {
        // Initialize stats
        CurrentHealth = currentHealth;
        CurrentMana = currentMana;

        // Update PlayerController speed with our modifier
        UpdatePlayerControllerSpeed();
    }

    private void Update()
    {
        //Auto Assign DeathPanelController
        if (deathPanelController == null)
        {
            //use tag DeathPanel to find the DeathPanelController
            GameObject deathPanelObj = GameObject.FindGameObjectWithTag("DeathPanel");
            if (deathPanelObj != null)
            {
                //deathPanelObj's child has DeathPanelController
                deathPanelController = deathPanelObj.GetComponentInChildren<DeathPanelController>();
                deathPanelObj.SetActive(false);
            }
        }
        // Handle invulnerability timer
        if (isInvulnerable)
        {
            invulnerableTimer -= Time.deltaTime;
            if (invulnerableTimer <= 0f)
            {
                EndInvulnerability();
            }
        }

        // Handle mana regeneration
        if (enableManaRegen && currentMana < maxMana)
        {
            RegenerateMana(manaRegenRate * Time.deltaTime);
        }

    }

    /// <summary>
    /// Deal damage to the player
    /// </summary>
    /// <param name="damage">Amount of damage to deal</param>
    /// <param name="hasKnockback">If true, applies knockback effect</param>
    /// <param name="enemyPosition">Position of the enemy causing damage (for knockback direction)</param>
    /// <param name="ignoreDefence">If true, ignores defence stat</param>
    /// <returns>True if damage was dealt, false if blocked</returns>
    public bool TakeDamage(float damage, bool hasKnockback = false, Vector3 enemyPosition = default, bool ignoreDefence = false)
    {
        if (damage <= 0f) return false;
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

        //Cancle dash state
        if (playerController.isDashing)
        {
            playerController.isDashing = false;
            playerController.dashTimer = 0f;
            playerController.rb2D.gravityScale = 1.5f;
        }
        // Apply knockback if enabled
        if (hasKnockback && playerController != null)
        {
            ApplyKnockback(enemyPosition);
        }
        if (IsDead)
        {
            HandleDeath();
            return true;
        }

        // Trigger hurt animation in PlayerController
        if (playerController != null)
        {
            playerController.TriggerHurtAnimation();
        }

        // Start invulnerability frames
        if (invulnerableFrameDuration > 0f)
        {
            StartInvulnerability();
        }


        return true;
    }

    public bool TakeSanityDamage(float damage, bool hasKnockback = false, Vector3 enemyPosition = default, bool ignoreDefence = false)
    {
        if (damage <= 0f) return false;
        // Check if can take damage (always consider invulnerability)
        if (!canTakeSanityDamage || isSanityInvulnerable || IsDead)
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
        currentSanity -= finalDamage;
        OnDamageReceived?.Invoke(finalDamage);

        //Cancle dash state
        if (playerController.isDashing)
        {
            playerController.isDashing = false;
            playerController.dashTimer = 0f;
            playerController.rb2D.gravityScale = 1.5f;
        }
        // Apply knockback if enabled
        if (hasKnockback && playerController != null)
        {
            ApplyKnockback(enemyPosition);
        }

        if (IsDead)
        {
            HandleDeath();
            return true;
        }

        // Trigger hurt animation in PlayerController
        if (playerController != null)
        {
            playerController.TriggerHurtAnimation();
        }

        // Start invulnerability frames
        if (invulnerableFrameDuration > 0f)
        {
            StartInvulnerability();
        }

        return true;
    }
    public bool TakeBothDamage(float damage, bool hasKnockback = false, Vector3 enemyPosition = default, bool ignoreDefence = false)
    {
        if (damage <= 0f) return false;
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
        currentSanity -= finalDamage;
        currentHealth -= finalDamage;
        OnDamageReceived?.Invoke(finalDamage);

        //Cancle dash state
        if (playerController.isDashing)
        {
            playerController.isDashing = false;
            playerController.dashTimer = 0f;
            playerController.rb2D.gravityScale = 1.5f;
        }
        // Apply knockback if enabled
        if (hasKnockback && playerController != null)
        {
            ApplyKnockback(enemyPosition);
        }

        if (IsDead)
        {
            HandleDeath();
            return true;
        }

        // Trigger hurt animation in PlayerController
        if (playerController != null)
        {
            playerController.TriggerHurtAnimation();
        }


        // Start invulnerability frames
        if (invulnerableFrameDuration > 0f)
        {
            StartInvulnerability();
        }

        return true;
    }

    /// <summary>
    /// Apply knockback effect to the player
    /// </summary>
    /// <param name="enemyPosition">Position of the enemy causing the knockback</param>
    private void ApplyKnockback(Vector3 enemyPosition)
    {
        // Get player's Rigidbody2D
        Rigidbody2D playerRigidbody = playerController.GetComponent<Rigidbody2D>();
        if (playerRigidbody == null) return;

        // Determine knockback direction based on enemy position
        Vector3 playerPosition = transform.position;
        float horizontalDirection = playerPosition.x > enemyPosition.x ? 1f : -1f; // Right if player is to the right of enemy

        // Apply knockback force (up-left or up-right)
        Vector2 knockbackDirection = new Vector2(horizontalDirection * knockbackForce, knockbackUpwardForce);
        playerRigidbody.velocity = knockbackDirection;

        // Disable player control during knockback
        playerController.SetDummyState(knockbackDuration);
    }

    /// <summary>
    /// Heal the player
    /// </summary>
    /// <param name="healAmount">Amount to heal</param>
    /// <returns>Actual amount healed</returns>
    public float Heal(float healAmount)
    {
        if (IsDead || currentHealCount <= 0) return 0f;

        float oldHealth = currentHealth;
        CurrentHealth += healAmount;
        currentHealCount--;
        return currentHealth - oldHealth;
    }

    /// <summary>
    /// Restore the player to full health
    /// </summary>
    public void FullHeal()
    {
        CurrentHealth = maxHealth;
    }

    /// <summary>
    /// Use mana
    /// </summary>
    /// <param name="manaAmount">Amount of mana to use</param>
    /// <returns>True if mana was available and used, false otherwise</returns>
    public bool UseMana(float manaAmount)
    {
        if (currentMana >= manaAmount)
        {
            CurrentMana -= manaAmount;
            return true;
        }
        return false;
    }

    /// <summary>
    /// Restore mana
    /// </summary>
    /// <param name="manaAmount">Amount of mana to restore</param>
    /// <returns>Actual amount restored</returns>
    public float RestoreMana(float manaAmount)
    {
        float oldMana = currentMana;
        CurrentMana += manaAmount;
        return currentMana - oldMana;
    }

    /// <summary>
    /// Regenerate mana over time
    /// </summary>
    /// <param name="regenAmount">Amount to regenerate this frame</param>
    private void RegenerateMana(float regenAmount)
    {
        if (currentMana < maxMana)
        {
            CurrentMana += regenAmount;
        }
    }

    /// <summary>
    /// Start invulnerability frames
    /// </summary>
    /// <param name="customDuration">Optional custom duration. If not provided, uses default invulnerableFrameDuration</param>
    public void StartInvulnerability(float customDuration = -1f)
    {
        float duration = customDuration > 0f ? customDuration : invulnerableFrameDuration;

        if (!isInvulnerable)
        {
            isInvulnerable = true;
            invulnerableTimer = duration;
            OnInvulnerabilityStart?.Invoke();
        }
        else
        {
            // If already invulnerable, extend the timer if new duration is longer
            if (duration > invulnerableTimer)
            {
                invulnerableTimer = duration;
            }
        }
    }

    /// <summary>
    /// End invulnerability frames
    /// </summary>
    public void EndInvulnerability()
    {
        if (isInvulnerable)
        {
            isInvulnerable = false;
            invulnerableTimer = 0f;
            OnInvulnerabilityEnd?.Invoke();
        }
    }

    /// <summary>
    /// Revive the player with specified health
    /// </summary>
    /// <param name="reviveHealth">Health amount to revive with (default: max health)</param>
    public void Revive(float reviveHealth = -1f)
    {
        if (reviveHealth < 0f)
            reviveHealth = maxHealth;

        CurrentHealth = reviveHealth;
        EndInvulnerability();
    }

    /// <summary>
    /// Reset all stats to their starting values
    /// </summary>
    public void ResetStats()
    {
        CurrentHealth = maxHealth;
        CurrentMana = maxMana;
        EndInvulnerability();
    }

    private void HandleDeath()
    {
        OnPlayerDeath?.Invoke();
        deathPanelController.ShowDeathPanel();
        playerController.universalAnimator.ForceEnableAnimation(9);
        playerController.SetDummyState(5f); // Disable control for 5 seconds on death
    }

    private void UpdatePlayerControllerSpeed()
    {
        if (playerController != null)
        {
            // Apply speed adjustment to PlayerController
            float baseSpeed = playerController.MoveSpeed / GetPreviousSpeedAdjustment();
            playerController.MoveSpeed = baseSpeed * walkSpeedAdjustment;
        }
    }

    private float GetPreviousSpeedAdjustment()
    {
        // This is a simplified approach - in a real implementation,
        // you might want to store the base speed separately
        return 1f;
    }

    /// <summary>
    /// Called when player successfully hits enemies with an attack
    /// Used for combat feedback, statistics, and future combat mechanics
    /// </summary>
    /// <param name="enemyHitCount">Number of enemies hit by this attack</param>
    /// <param name="attackType">Type of attack used (Physical/Magical)</param>
    public void SuccessfulHit(int enemyHitCount, PlayerAttackHitbox.AttackType attackType, bool isDownSwing = false)
    {
        if (enemyHitCount <= 0) return;
        if (isDownSwing)
        {
            //give player a small upward boost
            playerController.Pogo();
        }

        // For now, just debug log - this can be expanded in the future
        Debug.Log($"PlayerStats: Successful {attackType} attack hit {enemyHitCount} enemy(ies)!");

        // Future implementations might include:
        // - Mana regeneration on successful hits
        // - Combo system tracking
        // - Experience/skill points
        // - Special effects based on attack type
        // - Achievement/statistics tracking

        // Example future expansions:
        // if (attackType == PlayerAttackHitbox.AttackType.Physical)
        // {
        //     // Physical attacks might restore small amount of health
        //     Heal(enemyHitCount * 2f);
        // }
        // else if (attackType == PlayerAttackHitbox.AttackType.Magical)
        // {
        //     // Magical attacks might restore mana
        //     RestoreMana(enemyHitCount * 5f);
        // }
    }

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
        maxMana = Mathf.Max(0f, maxMana);
        currentMana = Mathf.Clamp(currentMana, 0f, maxMana);
        manaRegenRate = Mathf.Max(0f, manaRegenRate);
    }

    public void ApplyBuff(string buffName)
    {
        switch (buffName)
        {
            case "Enlight":
                Enlight = true;
                Debug.Log("PlayerStats: Enlight buff applied.");
                break;
            case "Slow":
                Slow = true;
                Debug.Log("PlayerStats: Slow buff applied.");
                break;
            // Add more buffs as needed
            default:
                Debug.LogWarning($"PlayerStats: Unknown buff '{buffName}'");
                break;
        }
    }

    public void RemoveBuff(string buffName)
    {
        switch (buffName)
        {
            case "Enlight":
                Enlight = false;
                Debug.Log("PlayerStats: Enlight buff removed.");
                break;
            case "Slow":
                Slow = false;
                Debug.Log("PlayerStats: Enlight buff removed.");
                break;
            // Add more buffs as needed
            default:
                Debug.LogWarning($"PlayerStats: Unknown buff '{buffName}'");
                break;
        }
    }
}
