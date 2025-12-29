using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Base class for all boss skills
/// A skill represents a specific action or behavior that a boss can perform
/// Skills have a duration and can contain complex logic
/// </summary>
public abstract class BossSkill
{
    [Header("Skill Settings")]
    public string skillName;
    public float duration;
    public bool isCompleted = false;
    public bool canBeInterrupted = false;
    
    // References passed from the boss
    protected MonoBehaviour bossAI;
    protected Transform bossTransform;
    protected Rigidbody2D bossRigidbody;
    protected EnemyStats bossStats;
    
    // Timing
    protected float startTime;
    protected float elapsedTime;
    
    /// <summary>
    /// Constructor for boss skills
    /// </summary>
    /// <param name="name">Display name of the skill</param>
    /// <param name="skillDuration">How long the skill should last</param>
    public BossSkill(string name, float skillDuration)
    {
        skillName = name;
        duration = skillDuration;
        isCompleted = false;
    }
    
    /// <summary>
    /// Initialize the skill with boss references
    /// Called when the skill is first activated
    /// </summary>
    /// <param name="boss">Reference to the boss AI</param>
    /// <param name="transform">Boss transform</param>
    /// <param name="rigidbody">Boss rigidbody</param>
    /// <param name="stats">Boss stats</param>
    public virtual void Initialize(MonoBehaviour boss, Transform transform, Rigidbody2D rigidbody, EnemyStats stats)
    {
        bossAI = boss;
        bossTransform = transform;
        bossRigidbody = rigidbody;
        bossStats = stats;
        startTime = Time.time;
        elapsedTime = 0f;
        isCompleted = false;
        
        OnSkillStart();
    }
    
    /// <summary>
    /// Update the skill logic - called every frame while skill is active
    /// </summary>
    public virtual void UpdateSkill()
    {
        if (isCompleted) return;
        
        elapsedTime = Time.time - startTime;
        
        // Check if skill duration has elapsed
        if (elapsedTime >= duration)
        {
            CompleteSkill();
            return;
        }
        
        // Call derived class update logic
        OnSkillUpdate();
    }
    
    /// <summary>
    /// Force complete the skill (used for interruptions)
    /// </summary>
    public virtual void CompleteSkill()
    {
        if (isCompleted) return;
        
        isCompleted = true;
        OnSkillEnd();
    }
    
    /// <summary>
    /// Called when the skill starts - override for specific skill logic
    /// </summary>
    protected virtual void OnSkillStart()
    {
        Debug.Log($"Boss Skill '{skillName}' started");
    }
    
    /// <summary>
    /// Called every frame while skill is active - override for specific skill logic
    /// </summary>
    protected virtual void OnSkillUpdate()
    {
        // Override in derived classes
    }
    
    /// <summary>
    /// Called when the skill ends - override for cleanup logic
    /// </summary>
    protected virtual void OnSkillEnd()
    {
        Debug.Log($"Boss Skill '{skillName}' completed");
    }
    
    /// <summary>
    /// Get the remaining time for this skill
    /// </summary>
    public float GetRemainingTime()
    {
        return Mathf.Max(0f, duration - elapsedTime);
    }
    
    /// <summary>
    /// Get the progress of this skill (0 to 1)
    /// </summary>
    public float GetProgress()
    {
        if (duration <= 0f) return 1f;
        return Mathf.Clamp01(elapsedTime / duration);
    }
    
    /// <summary>
    /// Create a copy of this skill for reuse
    /// </summary>
    public abstract BossSkill CreateCopy();
}

/// <summary>
/// Simple idle skill for testing the boss skill system
/// Boss stays idle for a specified duration
/// </summary>
public class IdleSkill : BossSkill
{
    public IdleSkill(float idleDuration) : base("Idle", idleDuration)
    {
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        // Stop any movement when starting idle
        if (bossRigidbody != null)
        {
            Vector2 velocity = bossRigidbody.velocity;
            velocity.x = 0f;
            bossRigidbody.velocity = velocity;
        }
    }
    
    protected override void OnSkillUpdate()
    {
        // Keep the boss stationary during idle
        if (bossRigidbody != null)
        {
            Vector2 velocity = bossRigidbody.velocity;
            velocity.x = 0f;
            bossRigidbody.velocity = velocity;
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        Debug.Log($"Boss finished idling for {duration} seconds");
    }
    
    public override BossSkill CreateCopy()
    {
        return new IdleSkill(duration);
    }
}
