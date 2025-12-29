using UnityEngine;

/// <summary>
/// Enemy Attack Hitbox component for dealing damage to the player
/// Attach to a GameObject with a Collider2D set as a trigger
/// Automatically detects player collision and applies damage with configurable settings
/// </summary>
public class EnemyAttackHitbox : MonoBehaviour
{
    [Header("Damage Settings")]
    [SerializeField] private float damage = 25f;
    [SerializeField] private bool hasKnockback = true;
    [SerializeField] private bool ignoreDefence = false;
    [SerializeField] private BuffType applyBuffsOnHit;
    [SerializeField] private BuffType removeBuffsOnHit;
    [SerializeField] private DamageType damageType = DamageType.Red;
    public enum BuffType
    {
        None,
        Enlight,
        Slow
    }

    public enum DamageType
    {
        Red,
        White,
        Black
    }


    [Header("Hitbox Behavior")]
    [SerializeField] private bool destroyOnHit = false;
    [SerializeField] private bool canHitMultipleTimes = true;
    [SerializeField] private float cooldownBetweenHits = 0f;
    [SerializeField] private float lifetime = 0.3f; // Auto-destroy after this time

    [Header("Detection Settings")]
    [SerializeField] private string playerTag = "Player";
    [SerializeField] private LayerMask playerLayerMask = -1; // All layers by default

    [Header("Visual Feedback")]
    [SerializeField] private GameObject hitEffect;
    [SerializeField] private bool showGizmos = true;
    [SerializeField] private Color gizmoColor = Color.red;

    [Header("Audio")]
    [SerializeField] private AudioClip hitSound;

    [Header("Debug")]
    [SerializeField] private bool showDebugInfo = false;

    // Private variables
    private Collider2D hitboxCollider;
    private bool hasHitPlayer = false;
    private float lastHitTime = 0f;

    // Events
    public System.Action<PlayerStats> OnPlayerHit;
    public System.Action<float> OnDamageDealt; // damage amount
    public System.Action OnHitboxTriggered;

    // Properties
    public float Damage
    {
        get => damage;
        set => damage = Mathf.Max(0f, value);
    }

    public bool HasKnockback
    {
        get => hasKnockback;
        set => hasKnockback = value;
    }

    public bool IgnoreDefence
    {
        get => ignoreDefence;
        set => ignoreDefence = value;
    }

    public bool DestroyOnHit
    {
        get => destroyOnHit;
        set => destroyOnHit = value;
    }

    public float Lifetime
    {
        get => lifetime;
        set => lifetime = Mathf.Max(0.1f, value);
    }

    public float CooldownBetweenHits
    {
        get => cooldownBetweenHits;
        set => cooldownBetweenHits = Mathf.Max(0f, value);
    }

    public bool HasHitPlayer => hasHitPlayer;
    public float TimeSinceLastHit => Time.time - lastHitTime;
    public bool CanHitAgain => canHitMultipleTimes && (Time.time - lastHitTime >= cooldownBetweenHits);

    private void Awake()
    {
        // Get collider component
        hitboxCollider = GetComponent<Collider2D>();

        if (hitboxCollider == null)
        {
            Debug.LogError($"EnemyAttackHitbox on {gameObject.name} requires a Collider2D component!");
            return;
        }

        // Ensure collider is set as trigger
        if (!hitboxCollider.isTrigger)
        {
            Debug.LogWarning($"EnemyAttackHitbox on {gameObject.name}: Collider2D should be set as trigger. Auto-fixing...");
            hitboxCollider.isTrigger = true;
        }
    }

    private void Start()
    {
        // Auto-destroy this hitbox after the specified lifetime
        Destroy(gameObject, lifetime);

        if (showDebugInfo)
            Debug.Log($"EnemyAttackHitbox: {gameObject.name} will auto-destroy in {lifetime} seconds");
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        // Check if the colliding object is on the player layer
        if (!IsInLayerMask(other.gameObject.layer, playerLayerMask))
            return;

        // Check if the colliding object has the player tag (if specified)
        if (!string.IsNullOrEmpty(playerTag) && !other.CompareTag(playerTag))
            return;

        // Try to get PlayerStats component
        PlayerStats playerStats = other.GetComponent<PlayerStats>();
        if (playerStats == null)
        {
            if (showDebugInfo)
                Debug.Log($"EnemyAttackHitbox: Object {other.name} doesn't have PlayerStats component");
            return;
        }

        // Check if we can hit the player
        if (!CanHitPlayer())
            return;

        // Deal damage to player according to damage type
        bool damageDealt = false;
        if (damageType == DamageType.Red)
        {
            damageDealt = DealDamageToPlayer(playerStats);
        }
        else if (damageType == DamageType.White)
        {
            damageDealt = DealSanityDamageToPlayer(playerStats);
        }
        else if (damageType == DamageType.Black)
        {
            damageDealt = DealBothDamageToPlayer(playerStats);
        }

        if (damageDealt)
        {
            // Update hit tracking
            hasHitPlayer = true;
            lastHitTime = Time.time;

            // Trigger events
            OnPlayerHit?.Invoke(playerStats);
            OnDamageDealt?.Invoke(damage);
            OnHitboxTriggered?.Invoke();

            // Play hit effects
            PlayHitEffects();

            // Destroy hitbox if configured
            if (destroyOnHit)
            {
                DestroyHitbox();
            }

            if (showDebugInfo)
            {
                Debug.Log($"EnemyAttackHitbox: Dealt {damage} damage to {other.name}" +
                         $" | Knockback: {hasKnockback}" +
                         $" | Ignore Defence: {ignoreDefence}" +
                         $" | Position: {transform.position}");
            }
        }
    }

    private bool CanHitPlayer()
    {
        // If already hit and can't hit multiple times
        if (hasHitPlayer && !canHitMultipleTimes)
            return false;

        // If can hit multiple times, check cooldown
        if (hasHitPlayer && canHitMultipleTimes)
            return CanHitAgain;

        return true;
    }

    private bool DealDamageToPlayer(PlayerStats playerStats)
    {
        // Use the enemy's position (this transform) for knockback calculation
        Vector3 enemyPosition = transform.position;

        // Deal damage with all configured parameters
        if (applyBuffsOnHit != null)
        {
            switch (applyBuffsOnHit)
            {
                case BuffType.Enlight:
                    playerStats.ApplyBuff("Enlight");
                    break;
                case BuffType.Slow:
                    playerStats.ApplyBuff("Slow");
                    playerStats.WalkSpeedAdjustment = 0.8f;
                    print(playerStats.WalkSpeedAdjustment);
                    break;
                    // Add more buff types as needed
            }
        }
        if (removeBuffsOnHit != null)
        {
            switch (removeBuffsOnHit)
            {
                case BuffType.Enlight:
                    playerStats.RemoveBuff("Enlight");
                    break;
                case BuffType.Slow:
                    playerStats.RemoveBuff("Slow");
                    break;
                    // Add more buff types as needed
            }
        }
        return playerStats.TakeDamage(damage, hasKnockback, enemyPosition, ignoreDefence);
    }
    private bool DealSanityDamageToPlayer(PlayerStats playerStats)
    {
        // Use the enemy's position (this transform) for knockback calculation
        Vector3 enemyPosition = transform.position;

        // Deal damage with all configured parameters
        if (applyBuffsOnHit != null)
        {
            switch (applyBuffsOnHit)
            {
                case BuffType.Enlight:
                    playerStats.ApplyBuff("Enlight");
                    break;
                case BuffType.Slow:
                    playerStats.ApplyBuff("Slow");
                    break;
                    // Add more buff types as needed
            }
        }
        if (removeBuffsOnHit != null)
        {
            switch (removeBuffsOnHit)
            {
                case BuffType.Enlight:
                    playerStats.RemoveBuff("Enlight");
                    break;
                case BuffType.Slow:
                    playerStats.RemoveBuff("Slow");
                    break;
                    // Add more buff types as needed
            }
        }
        return playerStats.TakeSanityDamage(damage, hasKnockback, enemyPosition, ignoreDefence);
    }

    public bool DealBothDamageToPlayer(PlayerStats playerStats)
    {
        // Use the enemy's position (this transform) for knockback calculation
        Vector3 enemyPosition = transform.position;

        // Deal damage with all configured parameters
        if (applyBuffsOnHit != null)
        {
            switch (applyBuffsOnHit)
            {
                case BuffType.Enlight:
                    playerStats.ApplyBuff("Enlight");
                    break;
                case BuffType.Slow:
                    playerStats.ApplyBuff("Slow");
                    break;
                    // Add more buff types as needed
            }
        }
        if (removeBuffsOnHit != null)
        {
            switch (removeBuffsOnHit)
            {
                case BuffType.Enlight:
                    playerStats.RemoveBuff("Enlight");
                    break;
                case BuffType.Slow:
                    playerStats.RemoveBuff("Slow");
                    break;
                    // Add more buff types as needed
            }
        }
        bool redDamageDealt = playerStats.TakeBothDamage(damage, hasKnockback, enemyPosition, ignoreDefence);
        return redDamageDealt;
    }

    private void PlayHitEffects()
    {
        // Spawn hit effect
        if (hitEffect != null)
        {
            GameObject effect = Instantiate(hitEffect, transform.position, transform.rotation);

            // Auto-destroy effect after 5 seconds if it doesn't destroy itself
            Destroy(effect, 5f);
        }

        // Play hit sound
        if (hitSound != null && AudioManager.Instance != null)
        {
            AudioManager.Instance.PlaySFX(hitSound);
        }
        else if (hitSound != null)
        {
            // Fallback if no AudioManager
            AudioSource.PlayClipAtPoint(hitSound, transform.position);
        }
    }

    private void DestroyHitbox()
    {
        if (showDebugInfo)
            Debug.Log($"EnemyAttackHitbox: Destroying hitbox {gameObject.name}");

        Destroy(gameObject);
    }

    private bool IsInLayerMask(int layer, LayerMask layerMask)
    {
        return (layerMask.value & (1 << layer)) != 0;
    }

    /// <summary>
    /// Reset the hitbox so it can hit the player again
    /// </summary>
    public void ResetHitbox()
    {
        hasHitPlayer = false;
        lastHitTime = 0f;

        if (showDebugInfo)
            Debug.Log($"EnemyAttackHitbox: Reset hitbox {gameObject.name}");
    }

    /// <summary>
    /// Enable or disable the hitbox
    /// </summary>
    /// <param name="enabled">True to enable, false to disable</param>
    public void SetHitboxEnabled(bool enabled)
    {
        if (hitboxCollider != null)
        {
            hitboxCollider.enabled = enabled;
        }

        if (showDebugInfo)
            Debug.Log($"EnemyAttackHitbox: {(enabled ? "Enabled" : "Disabled")} hitbox {gameObject.name}");
    }

    /// <summary>
    /// Manually trigger the hitbox (useful for testing)
    /// </summary>
    /// <param name="targetPlayerStats">Target player to damage</param>
    public bool ManualTrigger(PlayerStats targetPlayerStats)
    {
        if (targetPlayerStats == null) return false;

        if (!CanHitPlayer()) return false;

        bool damageDealt = DealDamageToPlayer(targetPlayerStats);

        if (damageDealt)
        {
            hasHitPlayer = true;
            lastHitTime = Time.time;
            PlayHitEffects();

            if (destroyOnHit)
                DestroyHitbox();
        }

        return damageDealt;
    }

    private void OnDrawGizmos()
    {
        if (!showGizmos) return;

        Collider2D col = GetComponent<Collider2D>();
        if (col == null) return;

        // Set gizmo color based on hit state
        Color drawColor = gizmoColor;
        if (hasHitPlayer && !canHitMultipleTimes)
        {
            drawColor = Color.gray; // Gray if already hit and can't hit again
        }
        else if (hasHitPlayer && !CanHitAgain)
        {
            drawColor = Color.yellow; // Yellow if in cooldown
        }

        Gizmos.color = drawColor;

        // Draw different shapes based on collider type
        if (col is BoxCollider2D boxCol)
        {
            Vector3 size = new Vector3(boxCol.size.x, boxCol.size.y, 0.1f);
            Vector3 center = transform.position + (Vector3)boxCol.offset;
            Gizmos.matrix = Matrix4x4.TRS(center, transform.rotation, transform.lossyScale);
            Gizmos.DrawWireCube(Vector3.zero, size);
        }
        else if (col is CircleCollider2D circleCol)
        {
            Vector3 center = transform.position + (Vector3)circleCol.offset;
            float radius = circleCol.radius * Mathf.Max(transform.lossyScale.x, transform.lossyScale.y);
            Gizmos.DrawWireSphere(center, radius);
        }
        else
        {
            // For other collider types, draw a simple sphere
            Gizmos.DrawWireSphere(transform.position, 0.5f);
        }

        // Draw damage text
        if (showDebugInfo)
        {
            Vector3 textPos = transform.position + Vector3.up * 1f;
#if UNITY_EDITOR
            UnityEditor.Handles.Label(textPos, $"DMG: {damage}\nKB: {hasKnockback}");
#endif
        }
    }

    private void OnValidate()
    {
        // Clamp values in editor
        damage = Mathf.Max(0f, damage);
        cooldownBetweenHits = Mathf.Max(0f, cooldownBetweenHits);
        lifetime = Mathf.Max(0.1f, lifetime);

        // Ensure player tag is valid if specified
        if (!string.IsNullOrEmpty(playerTag))
        {
#if UNITY_EDITOR
            string[] allTags = UnityEditorInternal.InternalEditorUtility.tags;
            bool tagExists = false;
            foreach (string tag in allTags)
            {
                if (tag == playerTag)
                {
                    tagExists = true;
                    break;
                }
            }
            if (!tagExists)
            {
                Debug.LogWarning($"EnemyAttackHitbox: Player tag '{playerTag}' does not exist in project tags.");
            }
#endif
        }
    }
}
