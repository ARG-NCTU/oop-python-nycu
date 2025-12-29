using UnityEngine;

/// <summary>
/// Counter Skill for ArroganceKnight
/// Lasts up to 3 seconds, switches to CounterPrepare animation
/// Ignores knockback and takes no damage from the next hit
/// Upon getting hit, adds HorizontalSwingSkill to the front of ActionQueue and ends
/// </summary>

[System.Serializable]
public class Counter : BossSkill
{
    [Header("Counter Settings")]
    [SerializeField] private GameObject horizontalSwingPrefab; // Which attack to use for counter (legacy - now used for SuccessCounter)
    [SerializeField] private GameObject counterSwingPrefab; // Specific prefab for SuccessCounter skill
    [SerializeField] private bool useHorizontalSwing1 = true; // True for swing 1, false for swing 2 (legacy)
    
    private bool hitReceived = false;
    private bool counterQueued = false;
    private EnemyStats enemyStats;
    private bool originalCanTakeDamage;
    private float originalKnockbackForce;
    private BossSkillManager skillManager;
    
    public Counter() : base("Counter", 3f)
    {
        canBeInterrupted = false; // Cannot be interrupted normally - only by hit
    }
    
    public Counter(GameObject attackPrefab, bool useSwing1 = true) : base("Counter", 3f)
    {
        horizontalSwingPrefab = attackPrefab;
        counterSwingPrefab = attackPrefab; // Use same prefab for both by default
        useHorizontalSwing1 = useSwing1;
        canBeInterrupted = false;
    }
    
    public Counter(GameObject attackPrefab, GameObject counterPrefab, bool useSwing1 = true) : base("Counter", 3f)
    {
        horizontalSwingPrefab = attackPrefab;
        counterSwingPrefab = counterPrefab;
        useHorizontalSwing1 = useSwing1;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting Counter skill - ignoring damage and knockback until hit");
        
        // Switch to CounterPrepare animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("CounterPrepare");
            
            // Get reference to skill manager for queueing
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        hitReceived = false;
        counterQueued = false;
        
        // Get reference to EnemyStats and modify damage/knockback settings
        enemyStats = bossStats;
        if (enemyStats != null)
        {
            // Store original settings
            originalCanTakeDamage = true; // We'll use events instead of disabling damage
            originalKnockbackForce = enemyStats.KnockbackForce;
            
            // Disable knockback during counter
            enemyStats.KnockbackForce = 0f;
            
            // Subscribe to damage events to detect hits
            enemyStats.OnDamageReceived += OnHitReceived;
            
            Debug.Log($"Counter: Disabled knockback and monitoring for hits on {enemyStats.gameObject.name}");
        }
        else
        {
            Debug.LogError("Counter: Could not find EnemyStats component to modify damage settings!");
        }
    }
    
    protected override void OnSkillUpdate()
    {
        // Keep boss stationary during counter preparation
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        // Check if we received a hit and should queue counter
        if (hitReceived && !counterQueued)
        {
            QueueCounterAttack();
            counterQueued = true;
            
            // End the skill immediately after queueing counter
            CompleteSkill();
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        // Restore original damage and knockback settings
        if (enemyStats != null)
        {
            enemyStats.KnockbackForce = originalKnockbackForce;
            enemyStats.OnDamageReceived -= OnHitReceived;
        }
        
        string reason = counterQueued ? "hit received - counter queued" : "duration expired - no hit taken";
        Debug.Log($"ArroganceKnight: Counter skill completed due to {reason}");
    }
    
    /// <summary>
    /// Called when the boss receives damage during counter state
    /// Note: We still take damage but ignore it for the first hit and don't get knocked back
    /// </summary>
    /// <param name="damage">Amount of damage received</param>
    private void OnHitReceived(float damage)
    {
        if (hitReceived) return; // Already triggered
        
        hitReceived = true;
        
        Debug.Log($"Counter: Hit received ({damage} damage) - will queue counter attack as next skill!");
    }
    
    /// <summary>
    /// Queue the counter attack skill to the front of the action queue
    /// </summary>
    private void QueueCounterAttack()
    {
        if (skillManager == null)
        {
            Debug.LogError("Counter: Could not access skill manager to queue counter attack!");
            return;
        }
        
        // Create the SuccessCounter skill instead of HorizontalSwing
        BossSkill counterSkill = new SuccessCounter(counterSwingPrefab ?? horizontalSwingPrefab);
        
        // Add to front of action queue (next skill to execute)
        AddSkillToFrontOfQueue(counterSkill);
        
        Debug.Log($"Counter: Queued SuccessCounter as next skill - boss will execute devastating counterattack!");
    }
    
    /// <summary>
    /// Add a skill to the front of the action queue
    /// </summary>
    private void AddSkillToFrontOfQueue(BossSkill skill)
    {
        if (skillManager == null) return;
        
        // Use reflection to access the private actionQueue
        var skillManagerType = skillManager.GetType();
        var actionQueueField = skillManagerType.GetField("actionQueue", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
        
        if (actionQueueField != null)
        {
            var actionQueue = actionQueueField.GetValue(skillManager) as System.Collections.Generic.List<BossSkill>;
            if (actionQueue != null)
            {
                // Insert at the beginning of the queue (index 0)
                actionQueue.Insert(0, skill);
                
                Debug.Log($"Counter: Successfully added {skill.skillName} to front of action queue");
            }
        }
        else
        {
            Debug.LogError("Counter: Could not access actionQueue field to insert counter skill!");
        }
    }
    
    public override BossSkill CreateCopy()
    {
        return new Counter(horizontalSwingPrefab, counterSwingPrefab, useHorizontalSwing1);
    }
    
    // Configuration methods
    public void SetCounterAttackPrefab(GameObject prefab)
    {
        horizontalSwingPrefab = prefab;
    }
    
    public void SetCounterSwingPrefab(GameObject prefab)
    {
        counterSwingPrefab = prefab;
    }
    
    public void SetUseHorizontalSwing1(bool useSwing1)
    {
        useHorizontalSwing1 = useSwing1;
    }
    
    // Status getters
    public bool HitReceived => hitReceived;
    public bool CounterQueued => counterQueued;
    public bool IsWaitingForHit => !hitReceived && !isCompleted;
}
