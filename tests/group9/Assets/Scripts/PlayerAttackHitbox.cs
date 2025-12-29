using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Player Attack Hitbox component for dealing damage to enemies
/// Attach to a GameObject with a Collider2D set as a trigger
/// Automatically detects enemy collision and applies damage with configurable settings
/// </summary>
public class PlayerAttackHitbox : MonoBehaviour
{
    public enum AttackType
    {
        Physical,
        Magical
        // More types can be added in the future
    }
    
    [Header("Attack Settings")]
    [SerializeField] private float damage = 25f;
    [SerializeField] private AttackType attackType = AttackType.Physical;
    [SerializeField] private bool hasKnockback = true;
    [SerializeField] private bool ignoreDefence = false;
    [SerializeField] private bool isDownSwing = false;
    
    [Header("Hitbox Behavior")]
    [SerializeField] private bool destroyOnHit = false;
    [SerializeField] private bool canHitMultipleEnemies = true;
    [SerializeField] private float cooldownBetweenHits = 0f;
    [SerializeField] private float lifetime = 0.5f; // Auto-destroy after this time
    
    [Header("Detection Settings")]
    [SerializeField] private string enemyTag = "Enemy";
    [SerializeField] private LayerMask enemyLayerMask = -1; // All layers by default
    
    [Header("Visual Feedback")]
    [SerializeField] private GameObject hitEffect;
    [SerializeField] private bool showGizmos = true;
    [SerializeField] private Color gizmoColor = Color.blue;
    
    [Header("Audio")]
    [SerializeField] private AudioClip hitSound;
    
    [Header("Debug")]
    [SerializeField] private bool showDebugInfo = false;
    
    // Private variables
    private Collider2D hitboxCollider;
    private HashSet<GameObject> hitEnemies = new HashSet<GameObject>();
    private float lastHitTime = 0f;
    private int totalEnemiesHit = 0;
    private PlayerStats playerStats;
    
    // Events
    public System.Action<GameObject> OnEnemyHit; // Hit enemy GameObject
    public System.Action<float> OnDamageDealt; // damage amount
    public System.Action OnHitboxTriggered;
    public System.Action<int, AttackType> OnAttackComplete; // total enemies hit, attack type
    
    // Properties
    public float Damage
    {
        get => damage;
        set => damage = Mathf.Max(0f, value);
    }
    
    public AttackType Type
    {
        get => attackType;
        set => attackType = value;
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
    
    public bool CanHitMultipleEnemies
    {
        get => canHitMultipleEnemies;
        set => canHitMultipleEnemies = value;
    }
    
    public float CooldownBetweenHits
    {
        get => cooldownBetweenHits;
        set => cooldownBetweenHits = Mathf.Max(0f, value);
    }
    
    public float Lifetime
    {
        get => lifetime;
        set => lifetime = Mathf.Max(0.1f, value);
    }
    
    public int TotalEnemiesHit => totalEnemiesHit;
    public float TimeSinceLastHit => Time.time - lastHitTime;
    public bool CanHitAgain => canHitMultipleEnemies && (Time.time - lastHitTime >= cooldownBetweenHits);
    
    private void Awake()
    {
        // Get collider component
        hitboxCollider = GetComponent<Collider2D>();
        
        if (hitboxCollider == null)
        {
            Debug.LogError($"PlayerAttackHitbox on {gameObject.name} requires a Collider2D component!");
            return;
        }
        
        // Ensure collider is set as trigger
        if (!hitboxCollider.isTrigger)
        {
            Debug.LogWarning($"PlayerAttackHitbox on {gameObject.name}: Collider2D should be set as trigger. Auto-fixing...");
            hitboxCollider.isTrigger = true;
        }
        
        // Find PlayerStats in scene (for SuccessfulHit callback)
        FindPlayerStats();
    }
    
    private void Start()
    {
        // Auto-destroy this hitbox after the specified lifetime
        Destroy(gameObject, lifetime);
        
        if (showDebugInfo)
            Debug.Log($"PlayerAttackHitbox: {gameObject.name} will auto-destroy in {lifetime} seconds");
    }
    
    private void OnDestroy()
    {
        // When hitbox is destroyed, notify PlayerStats of total hits
        if (playerStats != null && totalEnemiesHit > 0)
        {
            playerStats.SuccessfulHit(totalEnemiesHit, attackType, isDownSwing);
            OnAttackComplete?.Invoke(totalEnemiesHit, attackType);
        }
    }
    
    private void OnTriggerEnter2D(Collider2D other)
    {
        // Check if the colliding object is on the enemy layer
        if (!IsInLayerMask(other.gameObject.layer, enemyLayerMask))
            return;
        
        // Check if the colliding object has the enemy tag (if specified)
        if (!string.IsNullOrEmpty(enemyTag) && !other.CompareTag(enemyTag))
            return;
        
        // Check if we can hit this enemy
        if (!CanHitEnemy(other.gameObject))
            return;
        
        // Deal damage to enemy (placeholder - will need enemy health system)
        bool damageDealt = DealDamageToEnemy(other.gameObject);
        
        if (damageDealt)
        {
            // Track this enemy as hit
            hitEnemies.Add(other.gameObject);
            totalEnemiesHit++;
            lastHitTime = Time.time;
            
            // Trigger events
            OnEnemyHit?.Invoke(other.gameObject);
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
                Debug.Log($"PlayerAttackHitbox: Dealt {damage} {attackType} damage to {other.name}" +
                         $" | Knockback: {hasKnockback}" +
                         $" | Ignore Defence: {ignoreDefence}" +
                         $" | Total Enemies Hit: {totalEnemiesHit}");
            }
        }
    }
    
    private bool CanHitEnemy(GameObject enemy)
    {
        // If we can't hit multiple enemies and already hit this one
        if (!canHitMultipleEnemies && hitEnemies.Contains(enemy))
            return false;
        
        // If we can hit multiple enemies, check cooldown
        if (canHitMultipleEnemies && hitEnemies.Contains(enemy))
            return CanHitAgain;
        
        return true;
    }
    
    private bool DealDamageToEnemy(GameObject enemy)
    {
        // Try to get EnemyStats component (new unified system)
        EnemyStats enemyStats = enemy.GetComponent<EnemyStats>();
        if (enemyStats != null)
        {
            // Use the player's position (this transform) for knockback calculation
            Vector3 playerPosition = transform.position;
            
            // Deal damage with all configured parameters
            bool damageDealt = enemyStats.TakeDamage(damage, hasKnockback, playerPosition, ignoreDefence);
            
            if (showDebugInfo && damageDealt)
            {
                Debug.Log($"PlayerAttackHitbox: Dealt {damage} {attackType} damage to {enemy.name}");
            }
            
            return damageDealt;
        }
        
        // Fallback for enemies without EnemyStats (placeholder behavior)
        if (showDebugInfo)
        {
            Debug.Log($"PlayerAttackHitbox: Hit enemy {enemy.name} for {damage} {attackType} damage (no EnemyStats found)");
        }
        
        return true; // Assume successful hit for enemies without stats component
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
            Debug.Log($"PlayerAttackHitbox: Destroying hitbox {gameObject.name} after hitting {totalEnemiesHit} enemies");
            
        Destroy(gameObject);
    }
    
    private void FindPlayerStats()
    {
        // Try to find PlayerStats in the scene
        PlayerStats[] allPlayerStats = FindObjectsOfType<PlayerStats>();
        
        if (allPlayerStats.Length > 0)
        {
            playerStats = allPlayerStats[0];
            
            if (allPlayerStats.Length > 1 && showDebugInfo)
            {
                Debug.LogWarning($"PlayerAttackHitbox: Multiple PlayerStats found in scene. Using first one: {playerStats.gameObject.name}");
            }
        }
        else if (showDebugInfo)
        {
            Debug.LogWarning("PlayerAttackHitbox: No PlayerStats found in scene. SuccessfulHit callback will not work.");
        }
    }
    
    private bool IsInLayerMask(int layer, LayerMask layerMask)
    {
        return (layerMask.value & (1 << layer)) != 0;
    }
    
    /// <summary>
    /// Reset the hitbox so it can hit enemies again
    /// </summary>
    public void ResetHitbox()
    {
        hitEnemies.Clear();
        totalEnemiesHit = 0;
        lastHitTime = 0f;
        
        if (showDebugInfo)
            Debug.Log($"PlayerAttackHitbox: Reset hitbox {gameObject.name}");
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
            Debug.Log($"PlayerAttackHitbox: {(enabled ? "Enabled" : "Disabled")} hitbox {gameObject.name}");
    }
    
    /// <summary>
    /// Manually trigger the hitbox against a specific enemy (useful for testing)
    /// </summary>
    /// <param name="targetEnemy">Target enemy to hit</param>
    public bool ManualTrigger(GameObject targetEnemy)
    {
        if (targetEnemy == null) return false;
        
        if (!CanHitEnemy(targetEnemy)) return false;
        
        bool damageDealt = DealDamageToEnemy(targetEnemy);
        
        if (damageDealt)
        {
            hitEnemies.Add(targetEnemy);
            totalEnemiesHit++;
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
        
        // Set gizmo color based on attack type and hit state
        Color drawColor = gizmoColor;
        if (attackType == AttackType.Magical)
        {
            drawColor = Color.cyan; // Different color for magical attacks
        }
        
        if (totalEnemiesHit > 0 && !canHitMultipleEnemies)
        {
            drawColor = Color.gray; // Gray if already hit and can't hit again
        }
        else if (totalEnemiesHit > 0 && !CanHitAgain)
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
        
        // Draw attack type and damage info
        if (showDebugInfo)
        {
            Vector3 textPos = transform.position + Vector3.up * 1f;
            #if UNITY_EDITOR
            UnityEditor.Handles.Label(textPos, $"{attackType}\nDMG: {damage}\nHits: {totalEnemiesHit}");
            #endif
        }
    }
    
    private void OnValidate()
    {
        // Clamp values in editor
        damage = Mathf.Max(0f, damage);
        cooldownBetweenHits = Mathf.Max(0f, cooldownBetweenHits);
        lifetime = Mathf.Max(0.1f, lifetime);
        
        // Ensure enemy tag is valid if specified
        if (!string.IsNullOrEmpty(enemyTag))
        {
            #if UNITY_EDITOR
            string[] allTags = UnityEditorInternal.InternalEditorUtility.tags;
            bool tagExists = false;
            foreach (string tag in allTags)
            {
                if (tag == enemyTag)
                {
                    tagExists = true;
                    break;
                }
            }
            if (!tagExists)
            {
                Debug.LogWarning($"PlayerAttackHitbox: Enemy tag '{enemyTag}' does not exist in project tags.");
            }
            #endif
        }
    }
}
