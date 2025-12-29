using UnityEngine;

/// <summary>
/// Waiting Skill for ArroganceKnight
/// Lasts up to 4 seconds, switches to waiting animation
/// Ends early if player comes within range of 2 units after 1 second
/// </summary>

[System.Serializable]
public class Waiting : BossSkill
{
    [Header("Waiting Settings")]
    [SerializeField] private float playerDetectionRange = 2f;
    [SerializeField] private float minimumWaitTime = 1f; // Must wait at least 1 second
    [SerializeField] private bool useHorizontalDistanceOnly = true; // Only check X distance
    
    private float waitTimer = 0f;
    private bool canEndEarly = false;
    
    public Waiting() : base("Waiting", 4f)
    {
        canBeInterrupted = true; // Can be interrupted
    }
    
    public Waiting(float maxDuration, float detectionRange = 2f) : base("Waiting", maxDuration)
    {
        playerDetectionRange = detectionRange;
        canBeInterrupted = true;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting Waiting skill - will wait for {minimumWaitTime}s minimum, then check for player within {playerDetectionRange} units");
        
        // Switch to Waiting animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("Waiting");
        }
        
        // Reset timers
        waitTimer = 0f;
        canEndEarly = false;
    }
    
    protected override void OnSkillUpdate()
    {
        // Keep boss stationary during waiting
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        // Update wait timer
        waitTimer += Time.deltaTime;
        
        // Enable early ending after minimum wait time
        if (!canEndEarly && waitTimer >= minimumWaitTime)
        {
            canEndEarly = true;

            Debug.Log($"Waiting: Minimum wait time reached, now checking for player proximity");
        }
        
        // Check for early completion if allowed
        if (canEndEarly && IsPlayerInRange())
        {
            Debug.Log($"Waiting: Player detected within range {playerDetectionRange}, ending skill early");
            CompleteSkill();
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        float actualWaitTime = Mathf.Min(waitTimer, duration);

        string reason = canEndEarly && IsPlayerInRange() ? "player proximity" : "duration expired";
        Debug.Log($"ArroganceKnight: Waiting skill completed after {actualWaitTime:F1}s due to {reason}");
    }
    
    /// <summary>
    /// Check if player is within detection range
    /// </summary>
    /// <returns>True if player is close enough</returns>
    private bool IsPlayerInRange()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player == null) return false;
        
        Vector3 playerPosition = player.transform.position;
        Vector3 bossPosition = bossTransform.position;
        
        float distance;
        
        if (useHorizontalDistanceOnly)
        {
            // Only check horizontal distance (ignore Y difference)
            distance = Mathf.Abs(playerPosition.x - bossPosition.x);
        }
        else
        {
            // Check full 2D distance
            distance = Vector2.Distance(playerPosition, bossPosition);
        }
        
        return distance <= playerDetectionRange;
    }
    
    /// <summary>
    /// Get current distance to player (for debugging)
    /// </summary>
    /// <returns>Distance to player, or -1 if player not found</returns>
    public float GetDistanceToPlayer()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player == null) return -1f;
        
        Vector3 playerPosition = player.transform.position;
        Vector3 bossPosition = bossTransform.position;
        
        if (useHorizontalDistanceOnly)
        {
            return Mathf.Abs(playerPosition.x - bossPosition.x);
        }
        else
        {
            return Vector2.Distance(playerPosition, bossPosition);
        }
    }
    
    public override BossSkill CreateCopy()
    {
        return new Waiting(duration, playerDetectionRange);
    }
    
    // Configuration methods
    public void SetDetectionRange(float range)
    {
        playerDetectionRange = Mathf.Max(0.5f, range);
    }
    
    public void SetMinimumWaitTime(float time)
    {
        minimumWaitTime = Mathf.Max(0f, time);
    }
    
    public void SetUseHorizontalDistanceOnly(bool horizontal)
    {
        useHorizontalDistanceOnly = horizontal;
    }
    
    // Status getters
    public bool CanEndEarly => canEndEarly;
    public float WaitTimeElapsed => waitTimer;
    public float TimeUntilCanEndEarly => canEndEarly ? 0f : Mathf.Max(0f, minimumWaitTime - waitTimer);
    public float PlayerDetectionRange => playerDetectionRange;
}
