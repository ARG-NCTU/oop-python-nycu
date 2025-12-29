using UnityEngine;

/// <summary>
/// Example script demonstrating how to use PlayerAttackHitbox
/// This script shows different attack patterns and configurations
/// In a real game, attacks would be triggered by player input or abilities
/// </summary>
public class PlayerAttackHitboxExample : MonoBehaviour
{
    [Header("Attack Prefabs")]
    [SerializeField] private GameObject attackHitboxPrefab;
    
    [Header("Spawn Settings")]
    [SerializeField] private Transform spawnPoint;
    
    [Header("Attack Templates")]
    [SerializeField] private PlayerAttackHitbox physicalAttackTemplate;
    [SerializeField] private PlayerAttackHitbox magicalAttackTemplate;
    
    private void Start()
    {
        // Example: Subscribe to attack events
        if (physicalAttackTemplate != null)
        {
            physicalAttackTemplate.OnEnemyHit += OnEnemyHit;
            physicalAttackTemplate.OnAttackComplete += OnAttackComplete;
        }
    }
    
    private void Update()
    {
        // Example controls for testing
        if (Input.GetKeyDown(KeyCode.Q))
        {
            CreatePhysicalAttack();
        }
        
        if (Input.GetKeyDown(KeyCode.E))
        {
            CreateMagicalAttack();
        }
        
        if (Input.GetKeyDown(KeyCode.R))
        {
            CreateAreaAttack();
        }
    }
    
    /// <summary>
    /// Example: Create a basic physical attack
    /// </summary>
    private void CreatePhysicalAttack()
    {
        if (attackHitboxPrefab == null || spawnPoint == null) return;
        
        GameObject hitbox = Instantiate(attackHitboxPrefab, spawnPoint.position, spawnPoint.rotation);
        PlayerAttackHitbox attackHitbox = hitbox.GetComponent<PlayerAttackHitbox>();
        
        if (attackHitbox != null)
        {
            // Configure physical attack
            attackHitbox.Damage = 20f;
            attackHitbox.Type = PlayerAttackHitbox.AttackType.Physical;
            attackHitbox.HasKnockback = true;
            attackHitbox.IgnoreDefence = false;
            attackHitbox.DestroyOnHit = true;
            attackHitbox.CanHitMultipleEnemies = false;
            attackHitbox.Lifetime = 0.3f; // Quick melee attack
        }
        
        // Note: No need for manual Destroy() call - hitbox will auto-destroy based on lifetime
    }
    
    /// <summary>
    /// Example: Create a magical projectile attack
    /// </summary>
    private void CreateMagicalAttack()
    {
        if (attackHitboxPrefab == null || spawnPoint == null) return;
        
        GameObject hitbox = Instantiate(attackHitboxPrefab, spawnPoint.position, spawnPoint.rotation);
        PlayerAttackHitbox attackHitbox = hitbox.GetComponent<PlayerAttackHitbox>();
        
        if (attackHitbox != null)
        {
            // Configure magical attack
            attackHitbox.Damage = 30f;
            attackHitbox.Type = PlayerAttackHitbox.AttackType.Magical;
            attackHitbox.HasKnockback = false;
            attackHitbox.IgnoreDefence = true;
            attackHitbox.DestroyOnHit = true;
            attackHitbox.CanHitMultipleEnemies = false;
            attackHitbox.Lifetime = 2f; // Projectile that travels for 2 seconds
            
            // Subscribe to events for this specific attack
            attackHitbox.OnEnemyHit += OnMagicalAttackHit;
        }
    }
    
    /// <summary>
    /// Example: Create an area-of-effect attack that hits multiple enemies
    /// </summary>
    private void CreateAreaAttack()
    {
        if (attackHitboxPrefab == null || spawnPoint == null) return;
        
        GameObject hitbox = Instantiate(attackHitboxPrefab, spawnPoint.position, spawnPoint.rotation);
        PlayerAttackHitbox attackHitbox = hitbox.GetComponent<PlayerAttackHitbox>();
        
        if (attackHitbox != null)
        {
            // Configure area attack
            attackHitbox.Damage = 15f;
            attackHitbox.Type = PlayerAttackHitbox.AttackType.Physical;
            attackHitbox.HasKnockback = true;
            attackHitbox.IgnoreDefence = false;
            attackHitbox.DestroyOnHit = false; // Don't destroy on first hit
            attackHitbox.CanHitMultipleEnemies = true;
            attackHitbox.CooldownBetweenHits = 0.1f;
            attackHitbox.Lifetime = 1f; // Area persists for 1 second
        }
    }
    
    // Event handlers
    private void OnEnemyHit(GameObject enemy)
    {
        Debug.Log($"Hit enemy: {enemy.name}!");
    }
    
    private void OnMagicalAttackHit(GameObject enemy)
    {
        Debug.Log($"Magical attack hit enemy: {enemy.name}!");
        // Could add special magical effects here
    }
    
    private void OnAttackComplete(int enemiesHit, PlayerAttackHitbox.AttackType attackType)
    {
        Debug.Log($"Attack complete! Hit {enemiesHit} enemies with {attackType} attack");
    }
    
    /// <summary>
    /// Example: Manually create and configure a custom attack
    /// </summary>
    /// <param name="damage">Attack damage</param>
    /// <param name="type">Attack type</param>
    /// <param name="lifetime">How long the hitbox lasts</param>
    /// <param name="multiHit">Whether it can hit multiple enemies</param>
    public void CreateCustomAttack(float damage, PlayerAttackHitbox.AttackType type, float lifetime, bool multiHit)
    {
        if (attackHitboxPrefab == null || spawnPoint == null) return;
        
        GameObject hitbox = Instantiate(attackHitboxPrefab, spawnPoint.position, spawnPoint.rotation);
        PlayerAttackHitbox attackHitbox = hitbox.GetComponent<PlayerAttackHitbox>();
        
        if (attackHitbox != null)
        {
            attackHitbox.Damage = damage;
            attackHitbox.Type = type;
            attackHitbox.Lifetime = lifetime;
            attackHitbox.CanHitMultipleEnemies = multiHit;
            
            // Configure other settings based on attack type
            if (type == PlayerAttackHitbox.AttackType.Physical)
            {
                attackHitbox.HasKnockback = true;
                attackHitbox.IgnoreDefence = false;
            }
            else if (type == PlayerAttackHitbox.AttackType.Magical)
            {
                attackHitbox.HasKnockback = false;
                attackHitbox.IgnoreDefence = true;
            }
        }
    }
    
    private void OnDestroy()
    {
        // Clean up event subscriptions
        if (physicalAttackTemplate != null)
        {
            physicalAttackTemplate.OnEnemyHit -= OnEnemyHit;
            physicalAttackTemplate.OnAttackComplete -= OnAttackComplete;
        }
    }
}
