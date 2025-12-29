using UnityEngine;

/// <summary>
/// Enemy Contact Hitbox component for dealing continuous damage to the player
/// Unlike EnemyAttackHitbox which is temporary, this provides persistent contact damage
/// Attach to a GameObject with a Collider2D set as a trigger for the boss's body
/// Continuously damages player while they remain in contact with the enemy
/// </summary>
public class EnemyHitbox : MonoBehaviour
{
    [Header("Contact Damage Settings")]
    [SerializeField] private float contactDamage = 15f;
    [SerializeField] private bool hasKnockback = true;
    [SerializeField] private bool ignoreDefence = false;
    
    [Header("Damage Timing")]
    [SerializeField] private float damageInterval = 1f; // Time between damage instances
    [SerializeField] private bool damageOnEnter = true; // Deal damage immediately on contact
    [SerializeField] private bool continuousDamage = true; // Continue damaging while in contact
    
    [Header("Detection Settings")]
    [SerializeField] private string playerTag = "Player";
    [SerializeField] private LayerMask playerLayerMask = (1 << 6); // Player layer (Layer 6)
    
    [Header("Visual Feedback")]
    [SerializeField] private GameObject hitEffect;
    [SerializeField] private bool showGizmos = true;
    [SerializeField] private Color gizmoColor = Color.yellow;
    
    [Header("Audio")]
    [SerializeField] private AudioClip contactSound;
    
    [Header("Debug")]
    [SerializeField] private bool showDebugInfo = true; // Enable debug by default
    
    // Private variables
    private Collider2D hitboxCollider;
    private PlayerStats currentPlayerInContact;
    private float lastDamageTime = 0f;
    private bool isActive = true;
    
    // Events
    public System.Action<PlayerStats> OnPlayerContact;
    public System.Action<PlayerStats> OnPlayerExit;
    public System.Action<float> OnContactDamageDealt; // damage amount
    
    // Properties
    public float ContactDamage
    {
        get => contactDamage;
        set => contactDamage = Mathf.Max(0f, value);
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
    
    public float DamageInterval
    {
        get => damageInterval;
        set => damageInterval = Mathf.Max(0.1f, value);
    }
    
    public bool IsActive
    {
        get => isActive;
        set => isActive = value;
    }
    
    public bool HasPlayerInContact => currentPlayerInContact != null;
    public float TimeSinceLastDamage => Time.time - lastDamageTime;
    public bool CanDealDamageNow => isActive && (Time.time - lastDamageTime >= damageInterval);
    
    private void Awake()
    {
        // Get collider component
        hitboxCollider = GetComponent<Collider2D>();
        
        if (hitboxCollider == null)
        {
            Debug.LogError($"EnemyHitbox on {gameObject.name} requires a Collider2D component!");
            return;
        }
        
        // Ensure collider is set as trigger
        if (!hitboxCollider.isTrigger)
        {
            Debug.LogWarning($"EnemyHitbox on {gameObject.name}: Collider2D should be set as trigger. Auto-fixing...");
            hitboxCollider.isTrigger = true;
        }
    }
    
    private void Start()
    {
        if (showDebugInfo)
        {
            Debug.Log($"EnemyHitbox: {gameObject.name} initialized - Contact damage: {contactDamage}, Interval: {damageInterval}s");
            Debug.Log($"EnemyHitbox: Player Tag: '{playerTag}', Player Layer Mask: {playerLayerMask}");
            Debug.Log($"EnemyHitbox: Damage on Enter: {damageOnEnter}, Continuous Damage: {continuousDamage}");
            Debug.Log($"EnemyHitbox: Is Active: {isActive}, Has Collider: {hitboxCollider != null}");
        }
    }
    
    private void Update()
    {
        // Handle continuous damage while player is in contact
        if (continuousDamage && currentPlayerInContact != null && CanDealDamageNow)
        {
            DealContactDamage(currentPlayerInContact);
        }
    }
    
    private void OnTriggerEnter2D(Collider2D other)
    {
        if (showDebugInfo)
            Debug.Log($"EnemyHitbox: OnTriggerEnter2D called with {other.name}");
        
        if (!isActive)
        {
            if (showDebugInfo)
                Debug.Log($"EnemyHitbox: Hitbox {gameObject.name} is not active");
            return;
        }
        
        // Check if the colliding object is on the player layer
        if (!IsInLayerMask(other.gameObject.layer, playerLayerMask))
        {
            if (showDebugInfo)
                Debug.Log($"EnemyHitbox: Object {other.name} is on layer {other.gameObject.layer}, not in player layer mask {playerLayerMask}");
            return;
        }
        
        // Check if the colliding object has the player tag (if specified)
        if (!string.IsNullOrEmpty(playerTag) && !other.CompareTag(playerTag))
        {
            if (showDebugInfo)
                Debug.Log($"EnemyHitbox: Object {other.name} doesn't have player tag '{playerTag}', has tag '{other.tag}'");
            return;
        }
        
        // Try to get PlayerStats component
        PlayerStats playerStats = other.GetComponent<PlayerStats>();
        if (playerStats == null)
        {
            if (showDebugInfo)
                Debug.Log($"EnemyHitbox: Object {other.name} doesn't have PlayerStats component");
            return;
        }
        
        // Store reference to player
        currentPlayerInContact = playerStats;
        
        // Trigger contact event
        OnPlayerContact?.Invoke(playerStats);
        
        // Deal immediate damage if enabled
        if (damageOnEnter)
        {
            if (showDebugInfo)
                Debug.Log($"EnemyHitbox: Attempting to deal damage on enter...");
            DealContactDamage(playerStats);
        }
        
        if (showDebugInfo)
        {
            Debug.Log($"EnemyHitbox: Player {other.name} entered contact with {gameObject.name}");
        }
    }
    
    private void OnTriggerExit2D(Collider2D other)
    {
        // Check if this is the player we're tracking
        if (currentPlayerInContact == null) return;
        
        PlayerStats playerStats = other.GetComponent<PlayerStats>();
        if (playerStats == currentPlayerInContact)
        {
            // Player left contact
            OnPlayerExit?.Invoke(playerStats);
            currentPlayerInContact = null;
            
            if (showDebugInfo)
            {
                Debug.Log($"EnemyHitbox: Player {other.name} exited contact with {gameObject.name}");
            }
        }
    }
    
    private bool DealContactDamage(PlayerStats playerStats)
    {
        if (playerStats == null || !isActive) return false;
        
        // Use the enemy's position (this transform) for knockback calculation
        Vector3 enemyPosition = transform.position;
        
        // Deal damage with all configured parameters
        bool damageDealt = playerStats.TakeDamage(contactDamage, hasKnockback, enemyPosition, ignoreDefence);
        
        if (damageDealt)
        {
            // Update damage timing
            lastDamageTime = Time.time;
            
            // Trigger events
            OnContactDamageDealt?.Invoke(contactDamage);
            
            // Play contact effects
            PlayContactEffects();
            
            if (showDebugInfo)
            {
                Debug.Log($"EnemyHitbox: Dealt {contactDamage} contact damage to {playerStats.name}" +
                         $" | Knockback: {hasKnockback}" +
                         $" | Ignore Defence: {ignoreDefence}" +
                         $" | Next damage in: {damageInterval}s");
            }
        }
        
        return damageDealt;
    }
    
    private void PlayContactEffects()
    {
        // Spawn hit effect
        if (hitEffect != null)
        {
            GameObject effect = Instantiate(hitEffect, transform.position, transform.rotation);
            
            // Auto-destroy effect after 3 seconds if it doesn't destroy itself
            Destroy(effect, 3f);
        }
        
        // Play contact sound
        if (contactSound != null && AudioManager.Instance != null)
        {
            AudioManager.Instance.PlaySFX(contactSound);
        }
        else if (contactSound != null)
        {
            // Fallback if no AudioManager
            AudioSource.PlayClipAtPoint(contactSound, transform.position);
        }
    }
    
    private bool IsInLayerMask(int layer, LayerMask layerMask)
    {
        return (layerMask.value & (1 << layer)) != 0;
    }
    
    /// <summary>
    /// Enable or disable the contact hitbox
    /// </summary>
    /// <param name="active">True to enable, false to disable</param>
    public void SetActive(bool active)
    {
        isActive = active;
        
        if (hitboxCollider != null)
        {
            hitboxCollider.enabled = active;
        }
        
        // Clear player reference if disabling
        if (!active)
        {
            currentPlayerInContact = null;
        }
        
        if (showDebugInfo)
        {
            Debug.Log($"EnemyHitbox: {(active ? "Enabled" : "Disabled")} contact hitbox {gameObject.name}");
        }
    }
    
    /// <summary>
    /// Force deal damage to current player in contact (if any)
    /// </summary>
    /// <returns>True if damage was dealt</returns>
    public bool ForceDamage()
    {
        if (currentPlayerInContact == null) return false;
        
        return DealContactDamage(currentPlayerInContact);
    }
    
    /// <summary>
    /// Reset damage timing (allows immediate damage on next contact)
    /// </summary>
    public void ResetDamageTimer()
    {
        lastDamageTime = 0f;
        
        if (showDebugInfo)
        {
            Debug.Log($"EnemyHitbox: Reset damage timer for {gameObject.name}");
        }
    }
    
    /// <summary>
    /// Check if a specific player is currently in contact
    /// </summary>
    /// <param name="playerStats">Player to check</param>
    /// <returns>True if the specified player is in contact</returns>
    public bool IsPlayerInContact(PlayerStats playerStats)
    {
        return currentPlayerInContact == playerStats;
    }
    
    private void OnDrawGizmos()
    {
        if (!showGizmos) return;
        
        Collider2D col = GetComponent<Collider2D>();
        if (col == null) return;
        
        // Set gizmo color based on active state and contact status
        Color drawColor = gizmoColor;
        if (!isActive)
        {
            drawColor = Color.gray; // Gray if inactive
        }
        else if (currentPlayerInContact != null)
        {
            drawColor = Color.red; // Red if player is in contact
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
            Gizmos.DrawWireSphere(transform.position, 0.8f);
        }
        
        // Draw contact damage text
        if (showDebugInfo && isActive)
        {
            Vector3 textPos = transform.position + Vector3.up * 1.5f;
            #if UNITY_EDITOR
            string statusText = currentPlayerInContact != null ? "IN CONTACT" : "READY";
            UnityEditor.Handles.Label(textPos, $"Contact DMG: {contactDamage}\nInterval: {damageInterval}s\n{statusText}");
            #endif
        }
    }
    
    private void OnValidate()
    {
        // Clamp values in editor
        contactDamage = Mathf.Max(0f, contactDamage);
        damageInterval = Mathf.Max(0.1f, damageInterval);
        
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
                Debug.LogWarning($"EnemyHitbox: Player tag '{playerTag}' does not exist in project tags.");
            }
            #endif
        }
    }
}
