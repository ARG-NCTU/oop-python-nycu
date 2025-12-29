using UnityEngine;

/// <summary>
/// Small Rest Skill for ArroganceKnight
/// Does nothing for 0.5 seconds with no animation change
/// Simple passive skill for brief pauses
/// </summary>

[System.Serializable]
public class SmallRest : BossSkill
{
    public SmallRest() : base("SmallRest", 0.5f)
    {
        canBeInterrupted = true; // Can be interrupted
    }
    
    public SmallRest(float duration) : base("SmallRest", duration)
    {
        canBeInterrupted = true;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting SmallRest - doing nothing for {duration} seconds");
        
        // No animation change - keep current animation
    }
    
    protected override void OnSkillUpdate()
    {
        // Keep boss stationary during rest
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        // Just wait - no other logic needed
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();

        Debug.Log($"ArroganceKnight: SmallRest completed after {duration} seconds");
    }
    
    public override BossSkill CreateCopy()
    {
        return new SmallRest(duration);
    }
    
    // Configuration method
    public void SetDuration(float newDuration)
    {
        duration = Mathf.Max(0.1f, newDuration);
    }
}

/// <summary>
/// Big Rest Skill for ArroganceKnight
/// Switches to BigRest animation and does nothing for 3 seconds
/// Longer passive skill for extended pauses
/// </summary>

[System.Serializable]
public class BigRest : BossSkill
{
    public BigRest() : base("BigRest", 3f)
    {
        canBeInterrupted = true; // Can be interrupted
    }
    
    public BigRest(float duration) : base("BigRest", duration)
    {
        canBeInterrupted = true;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();

        Debug.Log($"ArroganceKnight: Starting BigRest - switching to BigRest animation for {duration} seconds");

        // Switch to BigRest animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("BigRest");
        }
    }
    
    protected override void OnSkillUpdate()
    {
        // Keep boss stationary during rest
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        // Just wait - no other logic needed
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();

        Debug.Log($"ArroganceKnight: BigRest completed after {duration} seconds");
    }
    
    public override BossSkill CreateCopy()
    {
        return new BigRest(duration);
    }
    
    // Configuration method
    public void SetDuration(float newDuration)
    {
        duration = Mathf.Max(0.1f, newDuration);
    }
}

/// <summary>
/// MidRest Skill for ArroganceKnight
/// Medium duration rest - 1.5 seconds of stillness
/// </summary>

[System.Serializable]
public class MidRest : BossSkill
{
    [Header("Rest Settings")]
    [SerializeField] private float restDuration = 1.5f;
    
    private bool isResting = false;
    
    public MidRest() : base("MidRest", 1.5f)
    {
        canBeInterrupted = true; // Can be interrupted during rest
    }
    
    public MidRest(float duration) : base("MidRest", duration)
    {
        restDuration = duration;
        canBeInterrupted = true;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting MidRest for {restDuration} seconds - brief pause");
        
        isResting = true;
        
        // No animation change needed for mid rest - maintain current state
    }
    
    protected override void OnSkillUpdate()
    {
        // Keep boss stationary during rest
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        // Just wait for the duration to complete
        // No special logic needed during mid rest
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        isResting = false;
        
        Debug.Log($"ArroganceKnight: MidRest completed - ready for next action");
    }
    
    public override BossSkill CreateCopy()
    {
        return new MidRest(restDuration);
    }
    
    // Configuration methods
    public void SetRestDuration(float duration)
    {
        restDuration = duration;
        this.duration = duration;
    }
    
    // Status getters
    public bool IsResting => isResting;
}
