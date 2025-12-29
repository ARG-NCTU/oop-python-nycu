using UnityEngine;

/// <summary>
/// Approach Skill for ArroganceKnight
/// Lasts up to 3 seconds, switches to walk animation and moves toward player
/// Ends early if player is within horizontal range of 2 units
/// </summary>

[System.Serializable]
public class Approach : BossSkill
{
    [Header("Approach Settings")]
    [SerializeField] private float horizontalDetectionRange = 2f;
    [SerializeField] private float moveSpeed = 3f;
    [SerializeField] private bool maintainGroundMovement = true; // Don't affect Y velocity
    
    private Vector2 targetDirection = Vector2.zero;
    private bool hasReachedPlayer = false;
    
    public Approach() : base("Approach", 3f)
    {
        canBeInterrupted = true; // Can be interrupted
    }
    
    public Approach(float maxDuration, float detectionRange = 2f, float speed = 3f) : base("Approach", maxDuration)
    {
        horizontalDetectionRange = detectionRange;
        moveSpeed = speed;
        canBeInterrupted = true;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting Approach skill - moving toward player at {moveSpeed} units/s, will stop when within {horizontalDetectionRange} units");
        
        // Switch to Walk animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("Walk");
        }
        
        // Reset state
        hasReachedPlayer = false;
        UpdateTargetDirection();
    }
    
    protected override void OnSkillUpdate()
    {
        // Update target direction each frame
        UpdateTargetDirection();
        
        // Check if we've reached the player
        if (IsPlayerInHorizontalRange())
        {
            if (!hasReachedPlayer)
            {
                hasReachedPlayer = true;
                
                Debug.Log($"Approach: Reached player (within {horizontalDetectionRange} units), ending skill");
                
                CompleteSkill();
            }
            return;
        }
        
        // Move toward player
        MoveTowardPlayer();
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        // Stop movement
        if (bossRigidbody != null && maintainGroundMovement)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        else if (bossRigidbody != null)
        {
            bossRigidbody.velocity = Vector2.zero;
        }

        string reason = hasReachedPlayer ? "reached player" : "duration expired";
        Debug.Log($"ArroganceKnight: Approach skill completed due to {reason}");
    }

    /// <summary>
    /// Update the direction toward the player
    /// </summary>
    private void UpdateTargetDirection()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player == null)
        {
            targetDirection = Vector2.zero;
            return;
        }
        
        Vector3 playerPosition = player.transform.position;
        Vector3 bossPosition = bossTransform.position;
        
        // Calculate direction (only horizontal movement)
        float horizontalDirection = playerPosition.x - bossPosition.x;
        targetDirection = new Vector2(Mathf.Sign(horizontalDirection), 0f);
    }
    
    /// <summary>
    /// Move the boss toward the player
    /// </summary>
    private void MoveTowardPlayer()
    {
        if (bossRigidbody == null || targetDirection == Vector2.zero) return;
        
        Vector2 currentVelocity = bossRigidbody.velocity;
        Vector2 newVelocity;
        
        if (maintainGroundMovement)
        {
            // Only change horizontal velocity, maintain Y velocity (for gravity, jumping, etc.)
            newVelocity = new Vector2(targetDirection.x * moveSpeed, currentVelocity.y);
        }
        else
        {
            // Full 2D movement
            newVelocity = targetDirection * moveSpeed;
        }
        
        bossRigidbody.velocity = newVelocity;
    }
    
    /// <summary>
    /// Check if player is within horizontal detection range
    /// </summary>
    /// <returns>True if player is close enough horizontally</returns>
    private bool IsPlayerInHorizontalRange()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player == null) return false;
        
        Vector3 playerPosition = player.transform.position;
        Vector3 bossPosition = bossTransform.position;
        
        float horizontalDistance = Mathf.Abs(playerPosition.x - bossPosition.x);
        return horizontalDistance <= horizontalDetectionRange;
    }
    
    /// <summary>
    /// Get current horizontal distance to player (for debugging)
    /// </summary>
    /// <returns>Horizontal distance to player, or -1 if player not found</returns>
    public float GetHorizontalDistanceToPlayer()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player == null) return -1f;
        
        Vector3 playerPosition = player.transform.position;
        Vector3 bossPosition = bossTransform.position;
        
        return Mathf.Abs(playerPosition.x - bossPosition.x);
    }
    
    public override BossSkill CreateCopy()
    {
        return new Approach(duration, horizontalDetectionRange, moveSpeed);
    }
    
    // Configuration methods
    public void SetHorizontalDetectionRange(float range)
    {
        horizontalDetectionRange = Mathf.Max(0.5f, range);
    }
    
    public void SetMoveSpeed(float speed)
    {
        moveSpeed = Mathf.Max(0.1f, speed);
    }
    
    public void SetMaintainGroundMovement(bool maintain)
    {
        maintainGroundMovement = maintain;
    }
    
    
    // Status getters
    public bool HasReachedPlayer => hasReachedPlayer;
    public Vector2 TargetDirection => targetDirection;
    public float HorizontalDetectionRange => horizontalDetectionRange;
    public float MoveSpeed => moveSpeed;
}
