using UnityEngine;

/// <summary>
/// Fan Swing Attack Skill for ArroganceKnight
/// Lasts 1 second, switches to FanSwing animation, and spawns FanSwingAttack hitbox
/// </summary>

[System.Serializable]
public class FanSwing : BossSkill
{
    [Header("Attack Settings")]
    [SerializeField] private GameObject fanSwingAttackPrefab;
    [SerializeField] private Vector3 attackOffset = Vector3.zero;
    [SerializeField] private float spawnDelay = 1f; // 1 second delay before spawning attack
    
    private GameObject spawnedAttack;
    private float spawnTimer = 0f;
    private bool hasSpawned = false;
    
    public FanSwing() : base("FanSwing", 2f) // Extended to 2 seconds to account for delay
    {
        canBeInterrupted = false; // Cannot be interrupted during attack
    }
    
    public FanSwing(GameObject attackPrefab) : base("FanSwing", 2f)
    {
        fanSwingAttackPrefab = attackPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting FanSwing attack");
        
        // Switch to FanSwing animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("FanSwing");
        }
        
        // Reset spawn tracking
        spawnTimer = 0f;
        hasSpawned = false;
    }
    
    protected override void OnSkillUpdate()
    {
        // Keep boss stationary during attack
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        // Handle delayed spawn
        if (!hasSpawned)
        {
            spawnTimer += Time.deltaTime;
            
            if (spawnTimer >= spawnDelay)
            {
                SpawnAttackHitbox();
                hasSpawned = true;
            }
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        Debug.Log($"ArroganceKnight: FanSwing attack completed");
        
        // Clean up spawned attack if it still exists
        if (spawnedAttack != null)
        {
            Object.Destroy(spawnedAttack);
            spawnedAttack = null;
        }
    }
    
    private void SpawnAttackHitbox()
    {
        // Try to find the prefab if not set
        if (fanSwingAttackPrefab == null)
        {
            // Look for FanSwingAttack prefab in Resources or try to find it
            fanSwingAttackPrefab = Resources.Load<GameObject>("FanSwingAttack");
            
            if (fanSwingAttackPrefab == null)
            {
                Debug.LogError($"FanSwing: FanSwingAttack prefab not found! Please assign it in the inspector or place it in Resources folder.");
                return;
            }
        }
        
        // Calculate spawn position
        // Calculate spawn position using the offset directly
        Vector3 spawnPosition = bossTransform.position + attackOffset;
        
        // Spawn the attack hitbox
        spawnedAttack = Object.Instantiate(fanSwingAttackPrefab, spawnPosition, bossTransform.rotation);
        
        Debug.Log($"FanSwing: Spawned FanSwingAttack at {spawnPosition}");
    }
    
    public override BossSkill CreateCopy()
    {
        return new FanSwing(fanSwingAttackPrefab);
    }
    
    public void SetAttackPrefab(GameObject prefab)
    {
        fanSwingAttackPrefab = prefab;
    }
    
    public void SetSpawnDelay(float delay)
    {
        spawnDelay = Mathf.Max(0f, delay);
    }
}
