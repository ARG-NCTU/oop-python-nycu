using UnityEngine;

/// <summary>
/// ArroganceKnight Boss AI - First boss implementation using the skill queue system
/// Uses the BossSkillManager to handle skill execution, queueing, and randomization
/// </summary>
public class ArroganceKnightAI : EnemyAI
{
    [Header("ArroganceKnight Settings")]
    [SerializeField] private bool startImmediately = true;
    
    [Header("Skill System")]
    [SerializeField] private bool autoStartSkills = true;
    [SerializeField] private int maxQueueSize = 3;
    [SerializeField] private float skillTransitionDelay = 1.0f; // Delay between skills
    
    [Header("Animation References")]
    [SerializeField] private GameObject idleAnimationSet;
    [SerializeField] private GameObject walkAnimationSet;
    [SerializeField] private GameObject waitingAnimationSet;
    [SerializeField] private GameObject counterPrepareAnimationSet;
    [SerializeField] private GameObject counterSwingAnimationSet;
    [SerializeField] private GameObject bigRestAnimationSet;
    [SerializeField] private GameObject horizontalSwing1AnimationSet;
    [SerializeField] private GameObject horizontalSwing2AnimationSet;
    [SerializeField] private GameObject fanSwingAnimationSet;
    [SerializeField] private GameObject cycloneAnimationSet;
    [SerializeField] private GameObject giantSwingAnimationSet;
    [SerializeField] private GameObject jumpSlashAnimationSet;
    [SerializeField] private GameObject backUpAnimationSet;
    [SerializeField] private GameObject dashAnimationSet;
    [SerializeField] private GameObject greatSlashAnimationSet;
    [SerializeField] private GameObject currentAnimationSet;
    
    [Header("Attack Prefab References")]
    [SerializeField] private GameObject hAttack1Prefab;
    [SerializeField] private GameObject hAttack2Prefab;
    [SerializeField] private GameObject counterSwingAttackPrefab;
    [SerializeField] private GameObject fanSwingAttackPrefab;
    [SerializeField] private GameObject cycloneAttackPrefab;
    [SerializeField] private GameObject giantSwingAttackPrefab;
    [SerializeField] private GameObject jumpSlashAttackPrefab;
    [SerializeField] private GameObject greatSlashHorizontalAttackPrefab; // For GreatSlashHorizontal skill
    
    [Header("Debug")]
    [SerializeField] private bool showSkillDebug = true;
    
    // Skill system
    private BossSkillManager skillManager;
    private UniversalAnimation currentAnimation;
    
    // Boss state
    private bool bossStarted = false;
    private bool halfComboTriggered = false; // Track if HalfCombo has been triggered
    private bool secondPhaseActivated = false; // Track if second phase skills have been activated
    
    protected override void Awake()
    {
        base.Awake();
        
        // Initialize skill manager
        skillManager = new BossSkillManager();
    }
    
    protected override void Start()
    {
        base.Start();
        
        // Make boss immune to knockback - bosses should not be stunned or knocked around
        if (EnemyStats != null)
        {
            EnemyStats.KnockbackForce = 0f;
            EnemyStats.KnockbackUpwardForce = 0f;
            EnemyStats.KnockbackDuration = 0f;
            
            Debug.Log("ArroganceKnight: Set to be immune to knockback - boss cannot be stunned");
        }
        
        // Initialize skill manager with boss references
        skillManager.Initialize(this, transform, GetComponent<Rigidbody2D>(), EnemyStats, showSkillDebug);
        
        // Configure skill manager settings
        skillManager.AutoQueueSkills = autoStartSkills;
        skillManager.MaxQueueSize = maxQueueSize;
        skillManager.SkillTransitionDelay = skillTransitionDelay;
        
        // Set up skill events
        skillManager.OnSkillStarted += OnSkillStarted;
        skillManager.OnSkillCompleted += OnSkillCompleted;
        skillManager.OnSkillPoolReset += OnSkillPoolReset;
        
        // Setup available skills
        SetupSkillPool();
        
        // Cache animation components
        CacheAnimationComponents();
        
        // Start with idle animation
        SwitchToAnimation(idleAnimationSet);
        
        // Start boss behavior if configured
        if (startImmediately)
        {
            StartBoss();
        }
        
        if (showSkillDebug)
        {
            Debug.Log($"ArroganceKnight: Initialized with {skillManager.SkillPoolCount} skills in pool");
        }
    }
    
    protected override void UpdateAI()
    {
        // Only update if boss has started and is alive
        if (!bossStarted || !ControlEnabled) return;
        
        // Check for HalfCombo trigger (50% health)
        CheckHalfComboTrigger();
        
        // Check for second phase activation (after HalfCombo completes)
        CheckSecondPhaseActivation();
        
        // Update skill manager (handles skill execution and queue management)
        skillManager.UpdateSkillManager();
        
        // Update animations based on current skill
        UpdateAnimations();
        
        // Debug output
        if (showSkillDebug && Time.frameCount % 60 == 0) // Every second
        {
            Debug.Log($"ArroganceKnight: {skillManager.GetDebugInfo()}");
        }
    }
    
    /// <summary>
    /// Check if boss health has dropped below 50% and trigger HalfCombo if needed
    /// </summary>
    private void CheckHalfComboTrigger()
    {
        if (halfComboTriggered || EnemyStats == null) return;
        
        float healthPercentage = EnemyStats.CurrentHealth / EnemyStats.MaxHealth;
        
        if (healthPercentage <= 0.5f && !HalfCombo.HasBeenUsed)
        {
            halfComboTriggered = true;
            
            // Create and queue the HalfCombo
            var halfCombo = new HalfCombo(greatSlashHorizontalAttackPrefab, giantSwingAttackPrefab, hAttack1Prefab, counterSwingAttackPrefab);
            skillManager.AddSkillsToQueue(halfCombo);
            
            if (showSkillDebug)
            {
                Debug.Log($"ArroganceKnight: Health dropped to {healthPercentage:P1}! Triggering HalfCombo desperation sequence!");
            }
        }
    }
    
    /// <summary>
    /// Check if second phase should be activated (after HalfCombo completion)
    /// </summary>
    private void CheckSecondPhaseActivation()
    {
        if (secondPhaseActivated || !halfComboTriggered || EnemyStats == null) return;
        
        // Check if HalfCombo has been used and health is still below 50%
        float healthPercentage = EnemyStats.CurrentHealth / EnemyStats.MaxHealth;
        bool halfComboCompleted = HalfCombo.HasBeenUsed;
        
        // Activate second phase if HalfCombo is completed and we're still below 50% health
        // Also check if there's no current skill or the current skill is not HalfCombo
        bool noActiveHalfCombo = skillManager.CurrentSkill == null || 
                                 skillManager.CurrentSkill.skillName != "HalfCombo";
        
        if (halfComboCompleted && healthPercentage <= 0.5f && noActiveHalfCombo)
        {
            secondPhaseActivated = true;
            skillManager.ActivateSecondPhase();
            
            // Queue some skills to start the second phase immediately
            skillManager.QueueRandomSkill();
            skillManager.QueueRandomSkill();
            
            if (showSkillDebug)
            {
                Debug.Log($"ArroganceKnight: SECOND PHASE ACTIVATED! Boss enters desperate final phase with new skill set!");
            }
        }
    }
    
    /// <summary>
    /// Setup the skill pool with available skills for ArroganceKnight
    /// Includes both combo skills and new individual movement/attack skills
    /// Also sets up the second phase skill pool for post-50% health combat
    /// </summary>
    private void SetupSkillPool()
    {
        // FIRST PHASE SKILLS (0-50% health)
        // Add existing combo skills - provides complex behavior patterns
        skillManager.AddSkillToPool(new SimpleCombo(hAttack1Prefab, hAttack2Prefab));
        skillManager.AddSkillToPool(new FanCombo(cycloneAttackPrefab, fanSwingAttackPrefab));
        skillManager.AddSkillToPool(new DanceCombo(jumpSlashAttackPrefab, fanSwingAttackPrefab, null)); // Using jumpSlashAttackPrefab for JumpSlash

        // Add new individual movement skills for positioning and mobility
        //skillManager.AddSkillToPool(new BackUpSkill()); // 1-second backup away from player
        //skillManager.AddSkillToPool(new HugeBackUpSkill()); // 3-second movement to right wall
        //skillManager.AddSkillToPool(new FixDashSkill()); // 2-second dash towards x=0
        
        // Add new powerful attack skill
        //skillManager.AddSkillToPool(new GreatSlashHorizontalSkill(greatSlashHorizontalAttackPrefab)); // 1-second great slash attack

        // SECOND PHASE SKILLS (below 50% health - more aggressive and desperate)
        // More aggressive combos and faster individual skills
        skillManager.AddSkillToSecondPhasePool(new FanCombo(cycloneAttackPrefab, fanSwingAttackPrefab)); // Keep this combo - it's aggressive
        skillManager.AddSkillToSecondPhasePool(new DanceCombo(jumpSlashAttackPrefab, fanSwingAttackPrefab, null)); // Keep dance combo for complexity
        
        // Add new phase 2 combo skills for enhanced second phase combat
        skillManager.AddSkillToSecondPhasePool(new TripleSlashCombo(jumpSlashAttackPrefab)); // Relentless aerial assault
        skillManager.AddSkillToSecondPhasePool(new SpinnerCombo(cycloneAttackPrefab, fanSwingAttackPrefab, hAttack1Prefab, counterSwingAttackPrefab)); // Aggressive spinning combo with counter
        skillManager.AddSkillToSecondPhasePool(new CleanUpCombo(giantSwingAttackPrefab, hAttack1Prefab, counterSwingAttackPrefab)); // Defensive reset with massive counterattack
        skillManager.AddSkillToSecondPhasePool(new BurstCombo(greatSlashHorizontalAttackPrefab, jumpSlashAttackPrefab)); // Ultimate aggressive combo
        
        // Add more movement-focused skills for second phase (boss becomes more mobile)
        //skillManager.AddSkillToSecondPhasePool(new BackUpSkill()); // Quick repositioning
        //skillManager.AddSkillToSecondPhasePool(new FixDashSkill()); // Aggressive dashing
        //skillManager.AddSkillToSecondPhasePool(new FixDashSkill()); // Add twice for higher probability
        
        // Add more powerful attacks for second phase
        //skillManager.AddSkillToSecondPhasePool(new GreatSlashHorizontalSkill(greatSlashHorizontalAttackPrefab)); // Keep great slash
        //skillManager.AddSkillToSecondPhasePool(new GreatSlashHorizontalSkill(greatSlashHorizontalAttackPrefab)); // Add twice for aggression
        
        // Add individual attack skills for faster paced combat
        skillManager.AddSkillToSecondPhasePool(new HorizontalSwing_1(hAttack1Prefab)); // Quick individual attacks
        skillManager.AddSkillToSecondPhasePool(new HorizontalSwing_2(hAttack2Prefab)); // Quick individual attacks
        skillManager.AddSkillToSecondPhasePool(new Cyclone(cycloneAttackPrefab)); // Aggressive spinning attack

        Debug.Log($"ArroganceKnight: Setup enhanced two-phase skill system");
        Debug.Log($"Phase 1 skills ({skillManager.SkillPoolCount}): SimpleCombo, FanCombo, DanceCombo, BackUp, HugeBackUp, FixDash, GreatSlashHorizontal");
        Debug.Log($"Phase 2 skills: FanCombo, DanceCombo, TripleSlashCombo, SpinnerCombo, CleanUpCombo, BurstCombo, BackUp, FixDash(x2), GreatSlashHorizontal(x2), HorizontalSwing1, HorizontalSwing2, Cyclone");
    }
    
    /// <summary>
    /// Start the boss behavior (begin skill execution)
    /// </summary>
    public void StartBoss()
    {
        if (bossStarted)
        {
            if (showSkillDebug)
            {
                Debug.Log("ArroganceKnight: Boss already started");
            }
            return;
        }
        
        bossStarted = true;
        halfComboTriggered = false;
        secondPhaseActivated = false;
        
        // Reset static flags for new fight
        StartCombo.ResetForNewFight();
        HalfCombo.ResetForNewFight();
        
        // Start with the special opening combo
        var startCombo = new StartCombo(giantSwingAttackPrefab, hAttack1Prefab, hAttack2Prefab);
        skillManager.AddSkillsToQueue(startCombo);
        
        // Queue one additional random skill after the opening
        skillManager.QueueRandomSkill();
        
        if (showSkillDebug)
        {
            Debug.Log("ArroganceKnight: Boss started! Beginning with StartCombo opening sequence.");
        }
    }
    
    /// <summary>
    /// Stop the boss behavior
    /// </summary>
    public void StopBoss()
    {
        if (!bossStarted) return;
        
        bossStarted = false;
        skillManager.StopCurrentSkill();
        skillManager.ClearActionQueue();
        
        // Return to idle animation
        SwitchToAnimation(idleAnimationSet);
        
        if (showSkillDebug)
        {
            Debug.Log("ArroganceKnight: Boss stopped");
        }
    }
    
    /// <summary>
    /// Cache animation components
    /// </summary>
    private void CacheAnimationComponents()
    {
        if (idleAnimationSet != null)
        {
            currentAnimation = idleAnimationSet.GetComponent<UniversalAnimation>();
        }
    }
    
    /// <summary>
    /// Switch to a specific animation set by name (called by skills)
    /// </summary>
    public void SwitchToAnimationSet(string animationSetName)
    {
        GameObject targetAnimationSet = null;
        
        switch (animationSetName.ToLower())
        {
            case "idle":
                targetAnimationSet = idleAnimationSet;
                break;
            case "walk":
                targetAnimationSet = walkAnimationSet;
                break;
            case "waiting":
                targetAnimationSet = waitingAnimationSet;
                break;
            case "counterprepare":
                targetAnimationSet = counterPrepareAnimationSet;
                break;
            case "counterswing":
                targetAnimationSet = counterSwingAnimationSet;
                break;
            case "bigrest":
                targetAnimationSet = bigRestAnimationSet;
                break;
            case "horizontalswing1":
                targetAnimationSet = horizontalSwing1AnimationSet;
                break;
            case "horizontalswing2":
                targetAnimationSet = horizontalSwing2AnimationSet;
                break;
            case "fanswing":
                targetAnimationSet = fanSwingAnimationSet;
                break;
            case "cyclone":
                targetAnimationSet = cycloneAnimationSet;
                break;
            case "giantswing":
                targetAnimationSet = giantSwingAnimationSet;
                break;
            case "jumpslash":
                targetAnimationSet = jumpSlashAnimationSet;
                break;
            case "backup":
                targetAnimationSet = backUpAnimationSet;
                break;
            case "dash":
                targetAnimationSet = dashAnimationSet;
                break;
            case "greatslash":
                targetAnimationSet = greatSlashAnimationSet;
                break;
            default:
                Debug.LogWarning($"ArroganceKnight: Unknown animation set '{animationSetName}', falling back to idle");
                targetAnimationSet = idleAnimationSet;
                break;
        }
        
        if (targetAnimationSet != null)
        {
            SwitchToAnimation(targetAnimationSet);
        }
    }
    
    /// <summary>
    /// Switch to a specific animation set
    /// </summary>
    private void SwitchToAnimation(GameObject animationSet)
    {
        if (animationSet == null) return;
        
        // Disable ALL animations first to prevent overlap
        DisableAllAnimations();
        
        // Enable new animation
        UniversalAnimation newAnimation = animationSet.GetComponent<UniversalAnimation>();
        if (newAnimation != null)
        {
            newAnimation.Enabled = true;
            currentAnimation = newAnimation;
            currentAnimationSet = animationSet;
            
            if (showSkillDebug)
            {
                Debug.Log($"ArroganceKnight: Switched to animation '{animationSet.name}'");
            }
        }
        else
        {
            Debug.LogWarning($"ArroganceKnight: Animation set '{animationSet.name}' does not have UniversalAnimation component");
        }
    }
    
    /// <summary>
    /// Disable all animation sets to prevent overlapping
    /// </summary>
    private void DisableAllAnimations()
    {
        GameObject[] allAnimationSets = {
            idleAnimationSet,
            walkAnimationSet,
            waitingAnimationSet,
            counterPrepareAnimationSet,
            counterSwingAnimationSet,
            bigRestAnimationSet,
            horizontalSwing1AnimationSet,
            horizontalSwing2AnimationSet,
            fanSwingAnimationSet,
            cycloneAnimationSet,
            giantSwingAnimationSet,
            jumpSlashAnimationSet,
            backUpAnimationSet,
            dashAnimationSet,
            greatSlashAnimationSet
        };
        
        foreach (GameObject animSet in allAnimationSets)
        {
            if (animSet != null)
            {
                UniversalAnimation anim = animSet.GetComponent<UniversalAnimation>();
                if (anim != null)
                {
                    anim.Enabled = false;
                }
            }
        }
    }
    
    /// <summary>
    /// Update animations based on current boss state
    /// </summary>
    private void UpdateAnimations()
    {
        // Handle transition state - return to idle during skill transitions
        if (skillManager.InTransition)
        {
            if (currentAnimationSet != idleAnimationSet)
            {
                SwitchToAnimation(idleAnimationSet);
            }
            return;
        }
        
        // Skills handle their own animation switching when active
        if (skillManager.HasCurrentSkill)
        {
            // Skills handle their own animations via SwitchToAnimationSet()
            // No need to override here unless there's special fallback logic
        }
        else
        {
            // No current skill - use idle animation
            if (currentAnimationSet != idleAnimationSet)
            {
                SwitchToAnimation(idleAnimationSet);
            }
        }
    }
    
    #region Skill Event Handlers
    
    /// <summary>
    /// Called when a skill starts
    /// </summary>
    private void OnSkillStarted(BossSkill skill)
    {
        if (showSkillDebug)
        {
            Debug.Log($"ArroganceKnight: Skill '{skill.skillName}' started (Duration: {skill.duration}s)");
        }
        
        // Handle specific skill start logic if needed
        switch (skill.skillName)
        {
            case "Waiting":
            case "Approach":
            case "Counter":
                // Logic skills handle their own animations
                break;
            case "SmallRest":
                // SmallRest doesn't change animation
                break;
            case "BigRest":
                // BigRest handles its own animation
                break;
            case "SimpleCombo":
            case "FanCombo":
                // Combo skills queue other skills
                break;
            case "HorizontalSwing_1":
            case "HorizontalSwing_2":
            case "FanSwing":
            case "Cyclone":
            case "GiantSwing":
                // Attack skills handle their own animations and spawning
                break;
        }
    }
    
    /// <summary>
    /// Called when a skill completes
    /// </summary>
    private void OnSkillCompleted(BossSkill skill)
    {
        if (showSkillDebug)
        {
            Debug.Log($"ArroganceKnight: Skill '{skill.skillName}' completed");
        }
        
        // Handle specific skill completion logic if needed
        switch (skill.skillName)
        {
            case "Waiting":
            case "Approach":
            case "Counter":
            case "SuccessCounter":
                // Return to idle animation after logic skills
                SwitchToAnimationSet("idle");
                break;
            case "SmallRest":
                // SmallRest doesn't change animation, so no need to switch back
                break;
            case "BigRest":
                // Return to idle animation after BigRest
                SwitchToAnimationSet("idle");
                break;
            case "SimpleCombo":
            case "FanCombo":
                // Combo skills just queue other skills, return to idle
                SwitchToAnimationSet("idle");
                break;
            case "HorizontalSwing_1":
            case "HorizontalSwing_2":
            case "FanSwing":
            case "Cyclone":
            case "GiantSwing":
                // Return to idle animation after attack skills
                SwitchToAnimationSet("idle");
                break;
        }
    }
    
    /// <summary>
    /// Called when the skill pool is reset
    /// </summary>
    private void OnSkillPoolReset()
    {
        if (showSkillDebug)
        {
            Debug.Log($"ArroganceKnight: Skill pool reset - {skillManager.SkillPoolCount} skills available");
        }
    }
    
    #endregion
    
    #region Boss AI Overrides
    
    public override void DeathSequence()
    {
        // Stop boss behavior before death
        StopBoss();
        
        // Call base death sequence
        base.DeathSequence();
    }
    
    public override void SetControlEnabled(bool enabled)
    {
        // For ArroganceKnight boss, we ignore control disabling from knockback
        // Bosses should not be stunned or have their skills interrupted by player attacks
        // Only death should disable the boss completely
        
        bool wasControlEnabled = ControlEnabled;
        
        // Only allow disabling control if the boss is dead
        if (!enabled && EnemyStats != null && EnemyStats.CurrentHealth <= 0)
        {
            // Boss is dead, allow control to be disabled
            base.SetControlEnabled(enabled);
            
            if (bossStarted)
            {
                skillManager.StopCurrentSkill();
            }
            
            Debug.Log("ArroganceKnight: Control disabled due to death");
        }
        else if (enabled)
        {
            // Always allow re-enabling control
            base.SetControlEnabled(enabled);
            
            Debug.Log("ArroganceKnight: Control re-enabled");
        }
        else
        {
            // Ignore knockback/stun attempts - boss is too powerful to be stunned
            Debug.Log("ArroganceKnight: Ignoring control disable attempt - boss cannot be stunned by player attacks");
        }
    }
    
    #endregion
    
    #region Public Methods for External Control
    
    /// <summary>
    /// Force queue a specific skill by name
    /// </summary>
    public bool QueueSkill(string skillName)
    {
        return skillManager.QueueSpecificSkill(skillName);
    }
    
    /// <summary>
    /// Queue a random skill
    /// </summary>
    public void QueueRandomSkill()
    {
        skillManager.QueueRandomSkill();
    }
    
    /// <summary>
    /// Interrupt current skill if possible
    /// </summary>
    public void InterruptCurrentSkill()
    {
        skillManager.InterruptCurrentSkill();
    }
    
    /// <summary>
    /// Get information about current boss state
    /// </summary>
    public string GetBossDebugInfo()
    {
        string bossState = bossStarted ? "Active" : "Inactive";
        string controlState = ControlEnabled ? "Enabled" : "Disabled";
        
        return $"ArroganceKnight - State: {bossState} | Control: {controlState} | {skillManager.GetDebugInfo()}";
    }
    
    #endregion
    
    #region Gizmos and Debug Visualization
    
    private void OnDrawGizmosSelected()
    {
        // Draw boss detection/interaction ranges if needed in the future
        Gizmos.color = Color.red;
        Gizmos.DrawWireSphere(transform.position, 2f); // Basic boss presence indicator
        
        #if UNITY_EDITOR
        // Display current skill info
        if (skillManager != null && skillManager.HasCurrentSkill)
        {
            Vector3 textPos = transform.position + Vector3.up * 3f;
            string skillInfo = $"Current: {skillManager.CurrentSkill.skillName}\n" +
                             $"Time Left: {skillManager.CurrentSkill.GetRemainingTime():F1}s\n" +
                             $"Queue: {skillManager.ActionQueueCount} skills";
            UnityEditor.Handles.Label(textPos, skillInfo);
        }
        #endif
    }
    
    #endregion
}
