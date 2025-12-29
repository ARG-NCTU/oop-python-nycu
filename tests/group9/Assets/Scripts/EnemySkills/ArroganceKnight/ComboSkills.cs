using UnityEngine;

/// <summary>
/// Simple Combo Skill for ArroganceKnight
/// Queues the sequence: Approach -> HorizontalSwing1 -> SmallRest -> HorizontalSwing2 -> BigRest
/// </summary>

[System.Serializable]
public class SimpleCombo : BossSkill
{
    [Header("Combo Settings")]
    [SerializeField] private GameObject hAttack1Prefab;
    [SerializeField] private GameObject hAttack2Prefab;
    
    private BossSkillManager skillManager;
    private bool comboQueued = false;
    
    public SimpleCombo() : base("SimpleCombo", 0.1f) // Very short duration - just queues skills
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    public SimpleCombo(GameObject attack1Prefab, GameObject attack2Prefab) : base("SimpleCombo", 0.1f)
    {
        hAttack1Prefab = attack1Prefab;
        hAttack2Prefab = attack2Prefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        // Get reference to skill manager
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        comboQueued = false;
        
        // Queue the combo immediately
        QueueComboSkills();
    }
    
    protected override void OnSkillUpdate()
    {
        // Complete immediately after queueing
        if (comboQueued)
        {
            CompleteSkill();
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
    }
    
    /// <summary>
    /// Queue all the skills in the combo sequence
    /// </summary>
    private void QueueComboSkills()
    {
        // Create skills for the combo sequence
        BossSkill[] comboSkills = {
            new Approach(3f, 2f, 3f),                    // Approach
            new HorizontalSwing_1(hAttack1Prefab),       // HorizontalSwing1
            new SmallRest(0.5f),                         // SmallRest
            new HorizontalSwing_2(hAttack2Prefab)       // HorizontalSwing2                             // BigRest
        };
        
        // Add all skills to the queue
        skillManager.AddSkillsToQueue(comboSkills);
        
        comboQueued = true;

        string skillNames = string.Join(" -> ", System.Array.ConvertAll(comboSkills, s => s.skillName));
    }
    
    public override BossSkill CreateCopy()
    {
        return new SimpleCombo(hAttack1Prefab, hAttack2Prefab);
    }
    
    // Configuration methods
    public void SetAttackPrefabs(GameObject attack1, GameObject attack2)
    {
        hAttack1Prefab = attack1;
        hAttack2Prefab = attack2;
    }
    
    // Status getters
    public bool ComboQueued => comboQueued;
}

/// <summary>
/// Fan Combo Skill for ArroganceKnight
/// Queues the sequence: Approach -> Cyclone -> SmallRest -> FanSwing
/// </summary>

[System.Serializable]
public class FanCombo : BossSkill
{
    [Header("Combo Settings")]
    [SerializeField] private GameObject cycloneAttackPrefab;
    [SerializeField] private GameObject fanSwingAttackPrefab;
    
    private BossSkillManager skillManager;
    private bool comboQueued = false;
    
    public FanCombo() : base("FanCombo", 0.1f) // Very short duration - just queues skills
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    public FanCombo(GameObject cyclonePrefab, GameObject fanSwingPrefab) : base("FanCombo", 0.1f)
    {
        cycloneAttackPrefab = cyclonePrefab;
        fanSwingAttackPrefab = fanSwingPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        // Get reference to skill manager
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        comboQueued = false;
        
        // Queue the combo immediately
        QueueComboSkills();
    }
    
    protected override void OnSkillUpdate()
    {
        // Complete immediately after queueing
        if (comboQueued)
        {
            CompleteSkill();
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
    }
    
    /// <summary>
    /// Queue all the skills in the combo sequence
    /// </summary>
    private void QueueComboSkills()
    {
        // Create skills for the combo sequence
        BossSkill[] comboSkills = {
            new Waiting(2f, 0.5f),                     // Waiting
            new Approach(3f, 2f, 3f),                    // Approach
            new Cyclone(cycloneAttackPrefab),            // Cyclone
            new SmallRest(0.5f),                         // SmallRest
            new FanSwing(fanSwingAttackPrefab),          // FanSwing
            new SmallRest(0.5f)
        };
        
        // Add all skills to the queue
        skillManager.AddSkillsToQueue(comboSkills);
        
        comboQueued = true;

        string skillNames = string.Join(" -> ", System.Array.ConvertAll(comboSkills, s => s.skillName));
    }
    
    public override BossSkill CreateCopy()
    {
        return new FanCombo(cycloneAttackPrefab, fanSwingAttackPrefab);
    }
    
    // Configuration methods
    public void SetAttackPrefabs(GameObject cyclone, GameObject fanSwing)
    {
        cycloneAttackPrefab = cyclone;
        fanSwingAttackPrefab = fanSwing;
    }
    
    // Status getters
    public bool ComboQueued => comboQueued;
}

/// <summary>
/// Dance Combo Skill for ArroganceKnight
/// Queues the sequence: JumpSlash -> BigRest -> FanSwing -> SmallRest
/// A graceful but deadly combination of aerial attack and ground control
/// </summary>

[System.Serializable]
public class DanceCombo : BossSkill
{
    [Header("Combo Settings")]
    [SerializeField] private GameObject jumpSlashAttackPrefab;
    [SerializeField] private GameObject fanSwingAttackPrefab;
    [SerializeField] private Transform attackSpawnPoint;
    
    private BossSkillManager skillManager;
    private bool comboQueued = false;
    
    public DanceCombo() : base("DanceCombo", 0.1f) // Very short duration - just queues skills
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    public DanceCombo(GameObject jumpSlashPrefab, GameObject fanSwingPrefab, Transform spawnPoint = null) : base("DanceCombo", 0.1f)
    {
        jumpSlashAttackPrefab = jumpSlashPrefab;
        fanSwingAttackPrefab = fanSwingPrefab;
        attackSpawnPoint = spawnPoint;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        // Get reference to skill manager
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        comboQueued = false;
        
        // Queue the combo immediately
        QueueComboSkills();
    }
    
    protected override void OnSkillUpdate()
    {
        // Complete immediately after queueing
        if (comboQueued)
        {
            CompleteSkill();
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
    }
    
    /// <summary>
    /// Queue all the skills in the dance combo sequence
    /// </summary>
    private void QueueComboSkills()
    {
        
        // Create skills for the dance combo sequence
        BossSkill[] comboSkills = {
            new JumpSlash(jumpSlashAttackPrefab, attackSpawnPoint), // JumpSlash
            new BigRest(3f),                                       // BigRest
            new FanSwing(fanSwingAttackPrefab),                    // FanSwing
            new SmallRest(0.5f)                                    // SmallRest
        };
        
        // Add all skills to the queue
        skillManager.AddSkillsToQueue(comboSkills);
        
        comboQueued = true;
        
        string skillNames = string.Join(" -> ", System.Array.ConvertAll(comboSkills, s => s.skillName));
    }
    
    public override BossSkill CreateCopy()
    {
        return new DanceCombo(jumpSlashAttackPrefab, fanSwingAttackPrefab, attackSpawnPoint);
    }
    
    // Configuration methods
    public void SetAttackPrefabs(GameObject jumpSlash, GameObject fanSwing, Transform spawnPoint = null)
    {
        jumpSlashAttackPrefab = jumpSlash;
        fanSwingAttackPrefab = fanSwing;
        attackSpawnPoint = spawnPoint;
    }
    
    // Status getters
    public bool ComboQueued => comboQueued;
}

/// <summary>
/// Start Combo Skill for ArroganceKnight
/// Special opening combo that only executes once at the very beginning of the fight
/// Sequence: GiantSwing -> Approach -> HorizontalSwing1 -> SmallRest -> HorizontalSwing2 -> Waiting
/// </summary>

[System.Serializable]
public class StartCombo : BossSkill
{
    [Header("Start Combo Settings")]
    [SerializeField] private GameObject giantSwingAttackPrefab;
    [SerializeField] private GameObject hAttack1Prefab;
    [SerializeField] private GameObject hAttack2Prefab;
    
    private BossSkillManager skillManager;
    private bool comboQueued = false;
    public static bool hasBeenUsed = false; // Static flag to ensure only one use per fight
    
    public StartCombo() : base("StartCombo", 0.1f) // Very short duration - just queues skills
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    public StartCombo(GameObject giantSwingPrefab, GameObject attack1Prefab, GameObject attack2Prefab) : base("StartCombo", 0.1f)
    {
        giantSwingAttackPrefab = giantSwingPrefab;
        hAttack1Prefab = attack1Prefab;
        hAttack2Prefab = attack2Prefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        // Get reference to skill manager
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        comboQueued = false;
        
        // Queue the combo immediately
        QueueComboSkills();
        
        // Mark as used
        hasBeenUsed = true;
    }
    
    protected override void OnSkillUpdate()
    {
        // Complete immediately after queueing
        if (comboQueued)
        {
            CompleteSkill();
        }
    }

    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
    }
    
    /// <summary>
    /// Queue all the skills in the start combo sequence
    /// </summary>
    private void QueueComboSkills()
    {
        
        // Create skills for the start combo sequence
        BossSkill[] comboSkills = {
            new GiantSwing(giantSwingAttackPrefab),  // GiantSwing
            new Approach(2f,1f,5f),                          // Approach
            new HorizontalSwing_1(hAttack1Prefab),  // HorizontalSwing1
            new SmallRest(1f),                      // SmallRest
            new HorizontalSwing_2(hAttack2Prefab),  // HorizontalSwing2
            new Waiting(2f)                         // Waiting
        };
        
        // Add all skills to the queue
        skillManager.AddSkillsToQueue(comboSkills);
        
        comboQueued = true;
        
        string skillNames = string.Join(" -> ", System.Array.ConvertAll(comboSkills, s => s.skillName));
    }
    
    public override BossSkill CreateCopy()
    {
        return new StartCombo(giantSwingAttackPrefab, hAttack1Prefab, hAttack2Prefab);
    }
    
    // Configuration methods
    public void SetAttackPrefabs(GameObject giantSwing, GameObject attack1, GameObject attack2)
    {
        giantSwingAttackPrefab = giantSwing;
        hAttack1Prefab = attack1;
        hAttack2Prefab = attack2;
    }
    
    // Status getters
    public bool ComboQueued => comboQueued;
    public static bool HasBeenUsed => hasBeenUsed;
    
    // Reset for new fight
    public static void ResetForNewFight()
    {
        hasBeenUsed = false;
    }
}

/// <summary>
/// Half Combo Skill for ArroganceKnight
/// Special combo that triggers once when boss health drops below 50%
/// Sequence: HugeBackUp -> FixDash -> GreatSlashHorizontal -> MidRest -> GiantSwing -> Waiting -> Counter
/// </summary>

[System.Serializable]
public class HalfCombo : BossSkill
{
    [Header("Half Combo Settings")]
    [SerializeField] private GameObject greatSlashHorizontalPrefab;
    [SerializeField] private GameObject giantSwingAttackPrefab;
    [SerializeField] private GameObject counterAttackPrefab;
    [SerializeField] private GameObject counterSwingAttackPrefab;
    
    private BossSkillManager skillManager;
    private bool comboQueued = false;
    public static bool hasBeenUsed = false; // Static flag to ensure only one use per fight
    
    public HalfCombo() : base("HalfCombo", 0.1f) // Very short duration - just queues skills
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    public HalfCombo(GameObject greatSlashPrefab, GameObject giantSwingPrefab, GameObject counterPrefab, GameObject counterSwingPrefab) : base("HalfCombo", 0.1f)
    {
        greatSlashHorizontalPrefab = greatSlashPrefab;
        giantSwingAttackPrefab = giantSwingPrefab;
        counterAttackPrefab = counterPrefab;
        counterSwingAttackPrefab = counterSwingPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        // Get reference to skill manager
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        comboQueued = false;
        
        // Queue the combo immediately
        QueueComboSkills();
        
        // Mark as used
        hasBeenUsed = true;
    }
    
    protected override void OnSkillUpdate()
    {
        // Complete immediately after queueing
        if (comboQueued)
        {
            CompleteSkill();
        }
    }

    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
    }
    
    /// <summary>
    /// Queue all the skills in the half combo sequence
    /// </summary>
    private void QueueComboSkills()
    {
        
        // Create skills for the half combo sequence
        BossSkill[] comboSkills = {
            new HugeBackUpSkill(),                                // HugeBackUp
            new FixDashSkill(),                                   // FixDash
            new GreatSlashHorizontalSkill(greatSlashHorizontalPrefab), // GreatSlashHorizontal
            new MidRest(2f),                                      // MidRest
            new GiantSwing(giantSwingAttackPrefab),              // GiantSwing
            new Waiting(3f),                                     // Waiting
            new Counter(counterAttackPrefab, counterSwingAttackPrefab)  // Counter with both prefabs
        };
        
        // Add all skills to the queue
        skillManager.AddSkillsToQueue(comboSkills);
        
        comboQueued = true;
        
        string skillNames = string.Join(" -> ", System.Array.ConvertAll(comboSkills, s => s.skillName));
    }
    
    public override BossSkill CreateCopy()
    {
        return new HalfCombo(greatSlashHorizontalPrefab, giantSwingAttackPrefab, counterAttackPrefab, counterSwingAttackPrefab);
    }
    
    // Configuration methods
    public void SetAttackPrefabs(GameObject greatSlash, GameObject giantSwing, GameObject counter, GameObject counterSwing)
    {
        greatSlashHorizontalPrefab = greatSlash;
        giantSwingAttackPrefab = giantSwing;
        counterAttackPrefab = counter;
        counterSwingAttackPrefab = counterSwing;
    }
    
    // Status getters
    public bool ComboQueued => comboQueued;
    public static bool HasBeenUsed => hasBeenUsed;
    
    // Reset for new fight
    public static void ResetForNewFight()
    {
        hasBeenUsed = false;
    }
}

/// <summary>
/// Triple Slash Combo Skill for ArroganceKnight Phase 2
/// Relentless aerial assault with triple jump slashes
/// Sequence: SmallRest -> JumpSlash -> MidRest -> JumpSlash -> MidRest -> JumpSlash -> BigRest
/// </summary>

[System.Serializable]
public class TripleSlashCombo : BossSkill
{
    [Header("Triple Slash Combo Settings")]
    [SerializeField] private GameObject jumpSlashAttackPrefab;
    
    private BossSkillManager skillManager;
    private bool comboQueued = false;
    
    public TripleSlashCombo() : base("TripleSlashCombo", 0.1f) // Very short duration - just queues skills
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    public TripleSlashCombo(GameObject jumpSlashPrefab) : base("TripleSlashCombo", 0.1f)
    {
        jumpSlashAttackPrefab = jumpSlashPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        // Get reference to skill manager
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        comboQueued = false;
        
        // Queue the combo immediately
        QueueComboSkills();
    }
    
    protected override void OnSkillUpdate()
    {
        // Complete immediately after queueing
        if (comboQueued)
        {
            CompleteSkill();
        }
    }

    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
    }
    
    /// <summary>
    /// Queue all the skills in the triple slash combo sequence
    /// </summary>
    private void QueueComboSkills()
    {
        
        // Create skills for the triple slash combo sequence
        BossSkill[] comboSkills = {
            new SmallRest(0.5f),                        // SmallRest
            new JumpSlash(jumpSlashAttackPrefab, null), // JumpSlash 1
            new SmallRest(0.5f),                          // MidRest
            new JumpSlash(jumpSlashAttackPrefab, null), // JumpSlash 2
            new SmallRest(0.5f),                          // MidRest
            new JumpSlash(jumpSlashAttackPrefab, null), // JumpSlash 3
            new BigRest(2.5f)                           // BigRest
        };
        
        // Add all skills to the queue
        skillManager.AddSkillsToQueue(comboSkills);
        
        comboQueued = true;
        
        string skillNames = string.Join(" -> ", System.Array.ConvertAll(comboSkills, s => s.skillName));
    }
    
    public override BossSkill CreateCopy()
    {
        return new TripleSlashCombo(jumpSlashAttackPrefab);
    }
    
    // Configuration methods
    public void SetAttackPrefab(GameObject jumpSlash)
    {
        jumpSlashAttackPrefab = jumpSlash;
    }
    
    // Status getters
    public bool ComboQueued => comboQueued;
}

/// <summary>
/// Spinner Combo Skill for ArroganceKnight Phase 2
/// Aggressive close-range spinning combo with counterattack
/// Sequence: Approach -> Cyclone -> Counter -> FanSwing -> MidRest
/// </summary>

[System.Serializable]
public class SpinnerCombo : BossSkill
{
    [Header("Spinner Combo Settings")]
    [SerializeField] private GameObject cycloneAttackPrefab;
    [SerializeField] private GameObject fanSwingAttackPrefab;
    [SerializeField] private GameObject counterAttackPrefab;
    [SerializeField] private GameObject counterSwingAttackPrefab;
    
    private BossSkillManager skillManager;
    private bool comboQueued = false;
    
    public SpinnerCombo() : base("SpinnerCombo", 0.1f) // Very short duration - just queues skills
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    public SpinnerCombo(GameObject cyclonePrefab, GameObject fanSwingPrefab, GameObject counterPrefab, GameObject counterSwingPrefab) : base("SpinnerCombo", 0.1f)
    {
        cycloneAttackPrefab = cyclonePrefab;
        fanSwingAttackPrefab = fanSwingPrefab;
        counterAttackPrefab = counterPrefab;
        counterSwingAttackPrefab = counterSwingPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        // Get reference to skill manager
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        comboQueued = false;
        
        // Queue the combo immediately
        QueueComboSkills();
    }
    
    protected override void OnSkillUpdate()
    {
        // Complete immediately after queueing
        if (comboQueued)
        {
            CompleteSkill();
        }
    }

    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
    }
    
    /// <summary>
    /// Queue all the skills in the spinner combo sequence
    /// </summary>
    private void QueueComboSkills()
    {
        
        // Create skills for the spinner combo sequence
        BossSkill[] comboSkills = {
            new Approach(),                         // Approach
            new Cyclone(cycloneAttackPrefab),      // Cyclone
            new Counter(counterAttackPrefab, counterSwingAttackPrefab), // Counter with both prefabs
            new FanSwing(fanSwingAttackPrefab),    // FanSwing
            new MidRest(1.5f)                      // MidRest
        };
        
        // Add all skills to the queue
        skillManager.AddSkillsToQueue(comboSkills);
        
        comboQueued = true;
        
        string skillNames = string.Join(" -> ", System.Array.ConvertAll(comboSkills, s => s.skillName));
    }
    
    public override BossSkill CreateCopy()
    {
        return new SpinnerCombo(cycloneAttackPrefab, fanSwingAttackPrefab, counterAttackPrefab, counterSwingAttackPrefab);
    }
    
    // Configuration methods
    public void SetAttackPrefabs(GameObject cyclone, GameObject fanSwing, GameObject counter, GameObject counterSwing)
    {
        cycloneAttackPrefab = cyclone;
        fanSwingAttackPrefab = fanSwing;
        counterAttackPrefab = counter;
        counterSwingAttackPrefab = counterSwing;
    }
    
    // Status getters
    public bool ComboQueued => comboQueued;
}

/// <summary>
/// CleanUp Combo Skill for ArroganceKnight Phase 2
/// Defensive repositioning followed by massive counterattack
/// Sequence: HugeBackUp -> GiantSwing -> Waiting -> Counter
/// </summary>

[System.Serializable]
public class CleanUpCombo : BossSkill
{
    [Header("CleanUp Combo Settings")]
    [SerializeField] private GameObject giantSwingAttackPrefab;
    [SerializeField] private GameObject counterAttackPrefab;
    [SerializeField] private GameObject counterSwingAttackPrefab;
    
    private BossSkillManager skillManager;
    private bool comboQueued = false;
    
    public CleanUpCombo() : base("CleanUpCombo", 0.1f) // Very short duration - just queues skills
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    public CleanUpCombo(GameObject giantSwingPrefab, GameObject counterPrefab, GameObject counterSwingPrefab) : base("CleanUpCombo", 0.1f)
    {
        giantSwingAttackPrefab = giantSwingPrefab;
        counterAttackPrefab = counterPrefab;
        counterSwingAttackPrefab = counterSwingPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        // Get reference to skill manager
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        comboQueued = false;
        
        // Queue the combo immediately
        QueueComboSkills();
    }
    
    protected override void OnSkillUpdate()
    {
        // Complete immediately after queueing
        if (comboQueued)
        {
            CompleteSkill();
        }
    }

    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
    }
    
    /// <summary>
    /// Queue all the skills in the cleanup combo sequence
    /// </summary>
    private void QueueComboSkills()
    {
        
        // Create skills for the cleanup combo sequence
        BossSkill[] comboSkills = {
            new GiantSwing(giantSwingAttackPrefab), // GiantSwing
            new Waiting(2.5f),                      // Waiting
            new Counter(counterAttackPrefab, counterSwingAttackPrefab) // Counter with both prefabs
        };
        
        // Add all skills to the queue
        skillManager.AddSkillsToQueue(comboSkills);
        
        comboQueued = true;
        
        string skillNames = string.Join(" -> ", System.Array.ConvertAll(comboSkills, s => s.skillName));
    }
    
    public override BossSkill CreateCopy()
    {
        return new CleanUpCombo(giantSwingAttackPrefab, counterAttackPrefab, counterSwingAttackPrefab);
    }
    
    // Configuration methods
    public void SetAttackPrefabs(GameObject giantSwing, GameObject counter, GameObject counterSwing)
    {
        giantSwingAttackPrefab = giantSwing;
        counterAttackPrefab = counter;
        counterSwingAttackPrefab = counterSwing;
    }
    
    // Status getters
    public bool ComboQueued => comboQueued;
}

/// <summary>
/// Burst Combo Skill for ArroganceKnight Phase 2
/// Ultimate aggressive combo combining movement, dash, and powerful attacks
/// Sequence: HugeBackUp -> FixDash -> GreatSlashHorizontal -> MidRest -> JumpSlash -> BigRest
/// </summary>

[System.Serializable]
public class BurstCombo : BossSkill
{
    [Header("Burst Combo Settings")]
    [SerializeField] private GameObject greatSlashHorizontalPrefab;
    [SerializeField] private GameObject jumpSlashAttackPrefab;
    
    private BossSkillManager skillManager;
    private bool comboQueued = false;
    
    public BurstCombo() : base("BurstCombo", 0.1f) // Very short duration - just queues skills
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    public BurstCombo(GameObject greatSlashPrefab, GameObject jumpSlashPrefab) : base("BurstCombo", 0.1f)
    {
        greatSlashHorizontalPrefab = greatSlashPrefab;
        jumpSlashAttackPrefab = jumpSlashPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        // Get reference to skill manager
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            var skillManagerField = knightAI.GetType().GetField("skillManager", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
            if (skillManagerField != null)
            {
                skillManager = skillManagerField.GetValue(knightAI) as BossSkillManager;
            }
        }
        
        // Reset state
        comboQueued = false;
        
        // Queue the combo immediately
        QueueComboSkills();
    }
    
    protected override void OnSkillUpdate()
    {
        // Complete immediately after queueing
        if (comboQueued)
        {
            CompleteSkill();
        }
    }

    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
    }
    
    /// <summary>
    /// Queue all the skills in the burst combo sequence
    /// </summary>
    private void QueueComboSkills()
    {
        // Create skills for the burst combo sequence
        BossSkill[] comboSkills = {
            new HugeBackUpSkill(),                                     // HugeBackUp
            new FixDashSkill(),                                        // FixDash
            new GreatSlashHorizontalSkill(greatSlashHorizontalPrefab), // GreatSlashHorizontal
            new MidRest(1.5f),                                         // MidRest
            new JumpSlash(jumpSlashAttackPrefab, null),               // JumpSlash
            new BigRest(2.5f)                                          // BigRest
        };
        
        // Add all skills to the queue
        skillManager.AddSkillsToQueue(comboSkills);
        
        comboQueued = true;
        
        string skillNames = string.Join(" -> ", System.Array.ConvertAll(comboSkills, s => s.skillName));
    }
    
    public override BossSkill CreateCopy()
    {
        return new BurstCombo(greatSlashHorizontalPrefab, jumpSlashAttackPrefab);
    }
    
    // Configuration methods
    public void SetAttackPrefabs(GameObject greatSlash, GameObject jumpSlash)
    {
        greatSlashHorizontalPrefab = greatSlash;
        jumpSlashAttackPrefab = jumpSlash;
    }
    
    // Status getters
    public bool ComboQueued => comboQueued;
}
