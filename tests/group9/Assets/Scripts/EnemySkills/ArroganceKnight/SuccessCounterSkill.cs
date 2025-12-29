using UnityEngine;

/// <summary>
/// SuccessCounter Skill for ArroganceKnight
/// Activates after a successful counter (when Counter skill detects a hit)
/// Duration: 1 second total (0.5s wait + spawn attack + 0.5s end)
/// Switches to CounterSwing animation, waits 0.5s, spawns CounterSwing attack, waits 0.5s more
/// </summary>

[System.Serializable]
public class SuccessCounter : BossSkill
{
    [Header("SuccessCounter Settings")]
    [SerializeField] private GameObject counterSwingPrefab; // CounterSwing attack prefab to spawn
    [SerializeField] private Transform attackSpawnPoint; // Where to spawn the attack (optional)
    
    private float waitBeforeAttack = 0.5f; // Time to wait before spawning attack
    private float waitAfterAttack = 0.5f;  // Time to wait after spawning attack
    private bool attackSpawned = false;
    private float elapsedTime = 0f;
    
    public SuccessCounter() : base("SuccessCounter", 1f) // 1 second total duration
    {
        canBeInterrupted = false; // Cannot be interrupted - this is the boss's reward for a successful counter
    }
    
    public SuccessCounter(GameObject attackPrefab, Transform spawnPoint = null) : base("SuccessCounter", 1f)
    {
        counterSwingPrefab = attackPrefab;
        attackSpawnPoint = spawnPoint;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting SuccessCounter - counter attack successful! Preparing devastating counterattack...");
        
        // Switch to CounterSwing animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("CounterSwing");
            Debug.Log($"SuccessCounter: Switched to CounterSwing animation");
        }
        
        // Reset state
        attackSpawned = false;
        elapsedTime = 0f;
        
        // Keep boss stationary during counter attack
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
    }
    
    protected override void OnSkillUpdate()
    {
        elapsedTime += Time.deltaTime;
        
        // Keep boss stationary during counter attack
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        // Spawn attack after waiting period
        if (!attackSpawned && elapsedTime >= waitBeforeAttack)
        {
            SpawnCounterSwingAttack();
            attackSpawned = true;
        }
        
        // Complete skill after total duration
        if (elapsedTime >= (waitBeforeAttack + waitAfterAttack))
        {
            CompleteSkill();
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        Debug.Log($"ArroganceKnight: SuccessCounter completed - devastating counterattack executed!");
    }
    
    /// <summary>
    /// Spawn the CounterSwing attack
    /// </summary>
    private void SpawnCounterSwingAttack()
    {
        if (counterSwingPrefab == null)
        {
            Debug.LogError("SuccessCounter: No CounterSwing prefab assigned! Cannot spawn counter attack.");
            // Try to load from Resources as fallback
            counterSwingPrefab = Resources.Load<GameObject>("CounterSwing");
            if (counterSwingPrefab == null)
            {
                Debug.LogError("SuccessCounter: Could not load CounterSwing prefab from Resources either!");
                return;
            }
        }
        
        // Determine spawn position
        Vector3 spawnPosition;
        if (attackSpawnPoint != null)
        {
            spawnPosition = attackSpawnPoint.position;
        }
        else if (bossAI != null)
        {
            spawnPosition = bossAI.transform.position;
        }
        else
        {
            Debug.LogError("SuccessCounter: No valid spawn position found!");
            return;
        }
        
        // Spawn the counter swing attack
        GameObject attackInstance = Object.Instantiate(counterSwingPrefab, spawnPosition, Quaternion.identity);
        
        // Configure the attack if it's an EnemyAttackHitbox
        if (attackInstance.TryGetComponent<EnemyAttackHitbox>(out EnemyAttackHitbox attackHitbox))
        {
            // Set up attack properties if needed
            attackHitbox.transform.position = spawnPosition;
            
            Debug.Log($"SuccessCounter: Spawned CounterSwing attack at {spawnPosition}");
        }
        else
        {
            Debug.LogWarning($"SuccessCounter: Spawned object does not have EnemyAttackHitbox component!");
        }
        
        Debug.Log($"SuccessCounter: Counter attack launched! Player will feel the boss's wrath!");
    }
    
    public override BossSkill CreateCopy()
    {
        return new SuccessCounter(counterSwingPrefab, attackSpawnPoint);
    }
    
    // Configuration methods
    public void SetCounterSwingPrefab(GameObject prefab)
    {
        counterSwingPrefab = prefab;
    }
    
    public void SetAttackSpawnPoint(Transform spawnPoint)
    {
        attackSpawnPoint = spawnPoint;
    }
    
    public void SetTimings(float waitBefore, float waitAfter)
    {
        waitBeforeAttack = waitBefore;
        waitAfterAttack = waitAfter;
        duration = waitBeforeAttack + waitAfterAttack;
    }
    
    // Status getters
    public bool AttackSpawned => attackSpawned;
    public float ElapsedTime => elapsedTime;
    public float WaitBeforeAttack => waitBeforeAttack;
    public float WaitAfterAttack => waitAfterAttack;
}
