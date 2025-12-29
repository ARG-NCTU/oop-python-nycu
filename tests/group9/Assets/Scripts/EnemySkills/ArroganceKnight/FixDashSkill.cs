using UnityEngine;

/// <summary>
/// Fix Dash Skill for ArroganceKnight
/// Dashes towards x=0 position with distance and time limits
/// </summary>

[System.Serializable]
public class FixDashSkill : BossSkill
{
    [Header("Dash Settings")]
    [SerializeField] private float dashSpeed = 8f; // Speed to move towards x=0
    [SerializeField] private float maxDistance = 6f; // Maximum travel distance
    [SerializeField] private Vector3 targetPosition = Vector3.zero; // x=0 target
    
    private Vector3 startPosition;
    private Vector3 dashDirection;
    private float traveledDistance = 0f;
    private bool dashStarted = false;
    
    public FixDashSkill() : base("FixDash", 2f) // Lasts at most 2 seconds
    {
        canBeInterrupted = true;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log("ArroganceKnight: Starting FixDash skill - moving towards x=0");
        
        // Switch to Dash animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("Dash");
        }
        
        // Store starting position and calculate direction
        startPosition = bossTransform.position;
        
        // Target position is x=0, keeping current y position
        targetPosition = new Vector3(0f, bossTransform.position.y, bossTransform.position.z);
        
        // Calculate direction towards x=0
        dashDirection = (targetPosition - startPosition).normalized;
        dashDirection.y = 0f; // Only horizontal movement
        dashDirection = dashDirection.normalized;
        
        // Reset tracking variables
        traveledDistance = 0f;
        dashStarted = true;
        
        Debug.Log($"ArroganceKnight: FixDash direction set to {dashDirection}, target: {targetPosition}");
    }
    
    protected override void OnSkillUpdate()
    {
        if (!dashStarted || bossRigidbody == null) return;
        
        // Calculate distance traveled this frame
        Vector3 currentPosition = bossTransform.position;
        float distanceThisFrame = Vector3.Distance(currentPosition, startPosition);
        
        // Check if we've reached the target x position or max distance
        bool reachedTarget = Mathf.Abs(currentPosition.x - targetPosition.x) < 0.1f;
        bool reachedMaxDistance = distanceThisFrame >= maxDistance;
        
        if (reachedTarget)
        {
            Debug.Log("ArroganceKnight: FixDash reached target x=0, stopping skill");
            CompleteSkill();
            return;
        }
        
        if (reachedMaxDistance)
        {
            Debug.Log($"ArroganceKnight: FixDash reached max distance of {maxDistance}, stopping skill");
            CompleteSkill();
            return;
        }
        
        // Continue dashing towards x=0
        Vector2 dashVelocity = new Vector2(dashDirection.x * dashSpeed, bossRigidbody.velocity.y);
        bossRigidbody.velocity = dashVelocity;
    }
    
    protected override void OnSkillEnd()
    {
        // Stop movement
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        // Switch back to idle animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("idle");
        }
        
        float finalDistance = Vector3.Distance(bossTransform.position, startPosition);
        Debug.Log($"ArroganceKnight: FixDash skill completed, traveled {finalDistance:F2} units");
        
        base.OnSkillEnd();
    }
    
    public override BossSkill CreateCopy()
    {
        return new FixDashSkill();
    }
}
