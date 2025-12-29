using UnityEngine;

/// <summary>
/// Back Up Movement Skills for ArroganceKnight
/// Two variants: BackUp and HugeBackUp
/// Movement-based skills for positioning and evasion
/// </summary>

[System.Serializable]
public class BackUpSkill : BossSkill
{
    [Header("Movement Settings")]
    [SerializeField] private float moveSpeed = 6f;
    [SerializeField] private bool useOppositePlayerDirection = true;
    
    private GameObject playerTarget;
    private Vector3 movementDirection;
    private bool movementSet = false;
    private LayerMask wallLayerMask = 1 << 8; // Assuming walls are on layer 8
    
    public BackUpSkill() : base("BackUp", 1f) // Lasts at most 1 second
    {
        canBeInterrupted = true;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log("ArroganceKnight: Starting BackUp skill - moving away from player");
        
        // Switch to BackUp animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("BackUp");
        }
        
        // Find player target and calculate movement direction
        playerTarget = GameObject.FindGameObjectWithTag("Player");
        
        if (playerTarget != null)
        {
            // Calculate direction opposite to player
            Vector3 directionToPlayer = (playerTarget.transform.position - bossTransform.position).normalized;
            movementDirection = -directionToPlayer; // Move opposite direction
            movementDirection.y = 0f; // Only horizontal movement
            movementDirection = movementDirection.normalized;
            movementSet = true;
            
            Debug.Log($"ArroganceKnight: BackUp direction set to {movementDirection}");
        }
        else
        {
            // Fallback: move left if no player found
            movementDirection = Vector3.left;
            movementSet = true;
        }
    }
    
    protected override void OnSkillUpdate()
    {
        if (!movementSet || bossRigidbody == null) return;
        
        // Check for wall collision ahead
        Vector3 raycastOrigin = bossTransform.position;
        Vector3 raycastDirection = movementDirection;
        float raycastDistance = 0.5f; // Check slightly ahead
        
        RaycastHit2D wallHit = Physics2D.Raycast(raycastOrigin, raycastDirection, raycastDistance, wallLayerMask);
        
        if (wallHit.collider != null)
        {
            // Hit a wall, stop the skill early
            Debug.Log("ArroganceKnight: BackUp hit wall, stopping skill early");
            CompleteSkill();
            return;
        }
        
        // Continue moving in the set direction
        Vector2 moveVelocity = new Vector2(movementDirection.x * moveSpeed, bossRigidbody.velocity.y);
        bossRigidbody.velocity = moveVelocity;
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
        
        Debug.Log("ArroganceKnight: BackUp skill completed");
        base.OnSkillEnd();
    }
    
    public override BossSkill CreateCopy()
    {
        return new BackUpSkill();
    }
}

[System.Serializable]
public class HugeBackUpSkill : BossSkill
{
    [Header("Movement Settings")]
    [SerializeField] private float moveSpeed = 8f;
    [SerializeField] private Vector3 targetDirection = Vector3.right; // Always move right
    
    private LayerMask wallLayerMask = 1 << 8; // Assuming walls are on layer 8

    public HugeBackUpSkill() : base("HugeBackUp", 2f) // Lasts at most 2 seconds
    {
        canBeInterrupted = true;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log("ArroganceKnight: Starting HugeBackUp skill - moving right until wall collision");
        
        // Switch to BackUp animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("BackUp");
        }
    }
    
    protected override void OnSkillUpdate()
    {
        if (bossRigidbody == null) return;
        
        // Check for wall collision ahead
        Vector3 raycastOrigin = bossTransform.position;
        Vector3 raycastDirection = targetDirection;
        float raycastDistance = 0.5f; // Check slightly ahead
        
        RaycastHit2D wallHit = Physics2D.Raycast(raycastOrigin, raycastDirection, raycastDistance, wallLayerMask);
        
        if (wallHit.collider != null)
        {
            // Hit a wall, stop the skill early
            Debug.Log("ArroganceKnight: HugeBackUp hit wall, stopping skill early");
            CompleteSkill();
            return;
        }
        
        // Continue moving right
        Vector2 moveVelocity = new Vector2(targetDirection.x * moveSpeed, bossRigidbody.velocity.y);
        bossRigidbody.velocity = moveVelocity;
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
        
        Debug.Log("ArroganceKnight: HugeBackUp skill completed");
        base.OnSkillEnd();
    }
    
    public override BossSkill CreateCopy()
    {
        return new HugeBackUpSkill();
    }
}
