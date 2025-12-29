using UnityEngine;
using System.Collections.Generic;
using System.Linq;

/// <summary>
/// Boss Skill Manager handles the skill queue and skill pool system for bosses
/// Manages skill execution, queueing, and random selection from available skills
/// </summary>
public class BossSkillManager
{
    [Header("Skill System")]
    private List<BossSkill> actionQueue = new List<BossSkill>();
    private List<BossSkill> skillPool = new List<BossSkill>();
    private List<BossSkill> originalSkillPool = new List<BossSkill>(); // Master copy for resetting
    private List<BossSkill> secondPhaseSkillPool = new List<BossSkill>(); // Second phase skills (below 50% health)
    private List<BossSkill> originalSecondPhasePool = new List<BossSkill>(); // Master copy for second phase
    private BossSkill currentSkill = null;
    
    // Phase management
    private bool isSecondPhase = false;
    private bool secondPhaseActivated = false;
    
    // Skill transition delay
    private float skillTransitionDelay = 0.5f; // Delay between skills
    private float transitionTimer = 0f;
    private bool inTransition = false;
    
    // Boss references
    private MonoBehaviour bossAI;
    private Transform bossTransform;
    private Rigidbody2D bossRigidbody;
    private EnemyStats bossStats;
    
    // Settings
    private bool autoQueueSkills = true;
    private int maxQueueSize = 3;
    private bool showDebugInfo = false;
    
    // Events
    public System.Action<BossSkill> OnSkillStarted;
    public System.Action<BossSkill> OnSkillCompleted;
    public System.Action OnSkillPoolReset;
    
    /// <summary>
    /// Initialize the skill manager with boss references
    /// </summary>
    public void Initialize(MonoBehaviour boss, Transform transform, Rigidbody2D rigidbody, EnemyStats stats, bool debug = false)
    {
        bossAI = boss;
        bossTransform = transform;
        bossRigidbody = rigidbody;
        bossStats = stats;
        showDebugInfo = debug;
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Initialized for {boss.name}");
        }
    }
    
    /// <summary>
    /// Add a skill to the skill pool (master list of available skills)
    /// </summary>
    public void AddSkillToPool(BossSkill skill)
    {
        if (skill == null)
        {
            Debug.LogError("BossSkillManager: Cannot add null skill to pool");
            return;
        }
        
        originalSkillPool.Add(skill);
        skillPool.Add(skill.CreateCopy());
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Added skill '{skill.skillName}' to pool. Pool size: {skillPool.Count}");
        }
    }
    
    /// <summary>
    /// Add a skill to the second phase skill pool (used after 50% health)
    /// </summary>
    public void AddSkillToSecondPhasePool(BossSkill skill)
    {
        if (skill == null)
        {
            Debug.LogError("BossSkillManager: Cannot add null skill to second phase pool");
            return;
        }
        
        originalSecondPhasePool.Add(skill);
        secondPhaseSkillPool.Add(skill.CreateCopy());
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Added skill '{skill.skillName}' to second phase pool. Pool size: {secondPhaseSkillPool.Count}");
        }
    }
    
    /// <summary>
    /// Switch to second phase skill pool (called after HalfCombo completes)
    /// </summary>
    public void ActivateSecondPhase()
    {
        if (secondPhaseActivated)
        {
            if (showDebugInfo)
            {
                Debug.Log("BossSkillManager: Second phase already activated");
            }
            return;
        }
        
        secondPhaseActivated = true;
        isSecondPhase = true;
        
        // Clear current skill pool and replace with second phase pool
        skillPool.Clear();
        foreach (var skill in originalSecondPhasePool)
        {
            skillPool.Add(skill.CreateCopy());
        }
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Second phase activated! Switched to second phase skill pool with {skillPool.Count} skills");
            string skillNames = string.Join(", ", skillPool.Select(s => s.skillName));
            Debug.Log($"BossSkillManager: Second phase skills: {skillNames}");
        }
    }
    
    /// <summary>
    /// Check if second phase is currently active
    /// </summary>
    public bool IsSecondPhaseActive => isSecondPhase;
    
    /// <summary>
    /// Check if second phase has been activated (even if temporarily switched back)
    /// </summary>
    public bool SecondPhaseActivated => secondPhaseActivated;
    
    /// <summary>
    /// Remove a skill type from the skill pool
    /// </summary>
    public void RemoveSkillFromPool(string skillName)
    {
        originalSkillPool.RemoveAll(skill => skill.skillName == skillName);
        skillPool.RemoveAll(skill => skill.skillName == skillName);
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Removed skill '{skillName}' from pool. Pool size: {skillPool.Count}");
        }
    }
    
    /// <summary>
    /// Reset the skill pool to its original state
    /// </summary>
    public void ResetSkillPool()
    {
        skillPool.Clear();
        
        // Create fresh copies of all original skills
        foreach (var skill in originalSkillPool)
        {
            skillPool.Add(skill.CreateCopy());
        }
        
        OnSkillPoolReset?.Invoke();
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Reset skill pool. Pool size: {skillPool.Count}");
        }
    }
    
    /// <summary>
    /// Queue a random skill from the skill pool
    /// If pool is empty, reset it first
    /// </summary>
    public void QueueRandomSkill()
    {
        // Reset pool if empty
        if (skillPool.Count == 0)
        {
            ResetSkillPool();
        }
        
        // If still empty after reset, nothing to queue
        if (skillPool.Count == 0)
        {
            if (showDebugInfo)
            {
                Debug.LogWarning("BossSkillManager: No skills available in pool to queue");
            }
            return;
        }
        
        // Don't exceed max queue size
        if (actionQueue.Count >= maxQueueSize)
        {
            if (showDebugInfo)
            {
                Debug.LogWarning($"BossSkillManager: Action queue is full ({maxQueueSize} skills)");
            }
            return;
        }
        
        // Select random skill from pool
        int randomIndex = Random.Range(0, skillPool.Count);
        BossSkill selectedSkill = skillPool[randomIndex];
        
        // Remove from pool and add to queue
        skillPool.RemoveAt(randomIndex);
        actionQueue.Add(selectedSkill);
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Queued skill '{selectedSkill.skillName}'. Queue size: {actionQueue.Count}, Pool size: {skillPool.Count}");
        }
    }
    
    /// <summary>
    /// Queue a specific skill by name (if available in pool)
    /// </summary>
    public bool QueueSpecificSkill(string skillName)
    {
        BossSkill targetSkill = skillPool.FirstOrDefault(skill => skill.skillName == skillName);
        
        if (targetSkill == null)
        {
            if (showDebugInfo)
            {
                Debug.LogWarning($"BossSkillManager: Skill '{skillName}' not found in pool");
            }
            return false;
        }
        
        // Don't exceed max queue size
        if (actionQueue.Count >= maxQueueSize)
        {
            if (showDebugInfo)
            {
                Debug.LogWarning($"BossSkillManager: Action queue is full ({maxQueueSize} skills)");
            }
            return false;
        }
        
        // Remove from pool and add to queue
        skillPool.Remove(targetSkill);
        actionQueue.Add(targetSkill);
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Queued specific skill '{skillName}'. Queue size: {actionQueue.Count}");
        }
        
        return true;
    }
    
    /// <summary>
    /// Add a skill to the front of the action queue (will be the next skill executed)
    /// </summary>
    public void AddSkillToFront(BossSkill skill)
    {
        if (skill == null)
        {
            Debug.LogError("BossSkillManager: Cannot add null skill to front of queue");
            return;
        }
        
        actionQueue.Insert(0, skill);
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Added skill '{skill.skillName}' to front of queue. Queue size: {actionQueue.Count}");
        }
    }
    
    /// <summary>
    /// Add multiple skills to the action queue in order
    /// </summary>
    public void AddSkillsToQueue(params BossSkill[] skills)
    {
        foreach (BossSkill skill in skills)
        {
            if (skill != null)
            {
                actionQueue.Add(skill);
            }
        }
        
        if (showDebugInfo)
        {
            string skillNames = string.Join(", ", skills.Where(s => s != null).Select(s => s.skillName));
            Debug.Log($"BossSkillManager: Added skills to queue: [{skillNames}]. Queue size: {actionQueue.Count}");
        }
    }
    
    /// <summary>
    /// Create a new skill instance by name (for combo skills)
    /// </summary>
    public BossSkill CreateSkillByName(string skillName)
    {
        // Find the skill in the original pool and create a copy
        BossSkill originalSkill = originalSkillPool.FirstOrDefault(s => s.skillName == skillName);
        
        if (originalSkill != null)
        {
            return originalSkill.CreateCopy();
        }
        
        if (showDebugInfo)
        {
            Debug.LogWarning($"BossSkillManager: Could not find skill '{skillName}' in original pool to create copy");
        }
        
        return null;
    }
    
    /// <summary>
    /// Update the skill manager - handles current skill and queue management
    /// Call this from the boss AI's Update method
    /// </summary>
    public void UpdateSkillManager()
    {
        // Handle transition delay
        if (inTransition)
        {
            transitionTimer -= Time.deltaTime;
            if (transitionTimer <= 0f)
            {
                inTransition = false;
                StartNextSkill();
            }
            return;
        }
        
        // Update current skill
        if (currentSkill != null)
        {
            currentSkill.UpdateSkill();
            
            // Check if current skill is completed
            if (currentSkill.isCompleted)
            {
                OnSkillCompleted?.Invoke(currentSkill);
                currentSkill = null;
                
                // Start transition delay before next skill
                if (skillTransitionDelay > 0f && actionQueue.Count > 0)
                {
                    inTransition = true;
                    transitionTimer = skillTransitionDelay;
                    
                    if (showDebugInfo)
                    {
                        Debug.Log($"BossSkillManager: Starting transition delay ({skillTransitionDelay}s) before next skill");
                    }
                }
                else
                {
                    // Immediately start next skill if no delay
                    StartNextSkill();
                }
            }
        }
        else if (!inTransition)
        {
            // No current skill and not in transition, start next one
            StartNextSkill();
        }
        
        // Auto-queue skills if enabled and queue is getting low
        if (autoQueueSkills && actionQueue.Count < 2)
        {
            QueueRandomSkill();
        }
    }
    
    /// <summary>
    /// Start the next skill in the action queue
    /// </summary>
    private void StartNextSkill()
    {
        if (actionQueue.Count == 0)
        {
            if (showDebugInfo)
            {
                Debug.Log("BossSkillManager: No skills in queue to start");
            }
            return;
        }
        
        // Get and remove the first skill from queue
        currentSkill = actionQueue[0];
        actionQueue.RemoveAt(0);
        
        // Initialize and start the skill
        currentSkill.Initialize(bossAI, bossTransform, bossRigidbody, bossStats);
        OnSkillStarted?.Invoke(currentSkill);
        
        if (showDebugInfo)
        {
            Debug.Log($"BossSkillManager: Started skill '{currentSkill.skillName}'. Queue size: {actionQueue.Count}");
        }
    }
    
    /// <summary>
    /// Interrupt the current skill and start the next one
    /// </summary>
    public void InterruptCurrentSkill()
    {
        if (currentSkill != null && currentSkill.canBeInterrupted)
        {
            if (showDebugInfo)
            {
                Debug.Log($"BossSkillManager: Interrupting skill '{currentSkill.skillName}'");
            }
            
            currentSkill.CompleteSkill();
            OnSkillCompleted?.Invoke(currentSkill);
            currentSkill = null;
            StartNextSkill();
        }
        else if (showDebugInfo)
        {
            Debug.Log("BossSkillManager: Current skill cannot be interrupted or no skill active");
        }
    }
    
    /// <summary>
    /// Clear the action queue
    /// </summary>
    public void ClearActionQueue()
    {
        actionQueue.Clear();
        
        if (showDebugInfo)
        {
            Debug.Log("BossSkillManager: Cleared action queue");
        }
    }
    
    /// <summary>
    /// Force stop current skill without starting next
    /// </summary>
    public void StopCurrentSkill()
    {
        if (currentSkill != null)
        {
            currentSkill.CompleteSkill();
            OnSkillCompleted?.Invoke(currentSkill);
            currentSkill = null;
        }
    }
    
    // Properties for external access
    public BossSkill CurrentSkill => currentSkill;
    public int ActionQueueCount => actionQueue.Count;
    public int SkillPoolCount => skillPool.Count;
    public bool HasCurrentSkill => currentSkill != null;
    public bool IsSkillPoolEmpty => skillPool.Count == 0;
    public bool IsActionQueueEmpty => actionQueue.Count == 0;
    
    public bool AutoQueueSkills 
    { 
        get => autoQueueSkills; 
        set => autoQueueSkills = value; 
    }
    
    public int MaxQueueSize 
    { 
        get => maxQueueSize; 
        set => maxQueueSize = Mathf.Max(1, value); 
    }
    
    public float SkillTransitionDelay
    {
        get => skillTransitionDelay;
        set => skillTransitionDelay = Mathf.Max(0f, value);
    }
    
    public bool InTransition => inTransition;
    public float TransitionTimeRemaining => inTransition ? transitionTimer : 0f;
    
    /// <summary>
    /// Get debug information about current state
    /// </summary>
    public string GetDebugInfo()
    {
        string current = currentSkill != null ? $"'{currentSkill.skillName}' ({currentSkill.GetRemainingTime():F1}s left)" : "None";
        string transition = inTransition ? $" [Transition: {transitionTimer:F1}s]" : "";
        string queue = actionQueue.Count > 0 ? string.Join(", ", actionQueue.Select(s => s.skillName)) : "Empty";
        string pool = skillPool.Count > 0 ? $"{skillPool.Count} skills available" : "Empty";
        
        return $"Current: {current}{transition} | Queue: [{queue}] | Pool: {pool}";
    }
}
