using UnityEngine;

/// <summary>
/// JumpSlash Skill for ArroganceKnight
/// Complex skill that performs a jump, forward dash, and slash attack with special animation
/// </summary>

[System.Serializable]
public class JumpSlash : BossSkill
{
    [Header("Jump Settings")]
    [SerializeField] private float jumpForce = 10f;
    [SerializeField] private float dashForce = 20f;
    [SerializeField] private float dashDuration = 0.5f;
    
    [Header("Attack Settings")]
    [SerializeField] private GameObject slashAttackPrefab;
    [SerializeField] private Transform attackSpawnPoint;
    
    public enum JumpSlashPhase
    {
        Jumping,
        Dashing,
        Attacking,
        Landing
    }
    
    private JumpSlashPhase currentPhase;
    private float phaseTimer;
    private bool hasJumped = false;
    private bool hasDashed = false;
    private bool hasAttacked = false;
    private Vector2 dashDirection;
    private GameObject playerTarget;
    private CameraController cameraController;
    
    public JumpSlash() : base("JumpSlash", 4f) // Total duration for all phases
    {
        canBeInterrupted = false; // Cannot be interrupted during complex maneuver
    }
    
    public JumpSlash(GameObject attackPrefab, Transform spawnPoint = null) : base("JumpSlash", 3f)
    {
        slashAttackPrefab = attackPrefab;
        attackSpawnPoint = spawnPoint;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();

        // Get reference to CameraController
        cameraController = Camera.main.GetComponent<CameraController>();

        Debug.Log($"ArroganceKnight: Starting JumpSlash - initiating complex jump/dash/attack sequence");
        
        // Switch to JumpSlash animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("JumpSlash");
        }
        
        // Find player target for direction calculation
        playerTarget = GameObject.FindGameObjectWithTag("Player");
        
        // Reset all states
        currentPhase = JumpSlashPhase.Jumping;
        phaseTimer = 0f;
        hasJumped = false;
        hasDashed = false;
        hasAttacked = false;
        
        /*
        // Calculate dash direction toward player
        if (playerTarget != null && bossAI != null)
        {
            Vector3 directionToPlayer = (playerTarget.transform.position - bossAI.transform.position).normalized;
            dashDirection = new Vector2(directionToPlayer.x, 0f);
        }
        else
        {
            // Default to forward direction if no player found
            dashDirection = Vector2.right;
        }
        */
        
        // Start jumping phase
        PerformJump();
    }
    
    protected override void OnSkillUpdate()
    {
        phaseTimer += Time.deltaTime;
        
        switch (currentPhase)
        {
            case JumpSlashPhase.Jumping:
                UpdateJumpingPhase();
                break;
                
            case JumpSlashPhase.Dashing:
                UpdateDashingPhase();
                break;
                
            case JumpSlashPhase.Attacking:
                UpdateAttackingPhase();
                break;
                
            case JumpSlashPhase.Landing:
                UpdateLandingPhase();
                break;
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        // Stop any remaining movement
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        Debug.Log($"ArroganceKnight: JumpSlash completed - complex maneuver finished");
    }
    
    private void PerformJump()
    {
        if (bossRigidbody != null && !hasJumped)
        {
            // Apply upward jump force
            bossRigidbody.velocity = new Vector2(bossRigidbody.velocity.x, jumpForce);
            hasJumped = true;
            
            Debug.Log($"JumpSlash: Performed jump with force {jumpForce}");
        }
    }
    
    private void UpdateJumpingPhase()
    {
        // Wait for boss to start falling or reach peak of jump
        if (bossRigidbody != null && bossRigidbody.velocity.y <= 0f)
        {
            // Transition to dashing phase
            currentPhase = JumpSlashPhase.Dashing;
            phaseTimer = 0f;
            PerformDash();
            
            Debug.Log($"JumpSlash: Transitioning to dashing phase");
        }
    }
    
    private void PerformDash()
    {
        if (bossRigidbody != null && !hasDashed)
        {
            //Calculate dash direction now, if already calculated, continue dashing
            if (playerTarget != null && bossAI != null)
            {
                Vector3 directionToPlayer = (playerTarget.transform.position - bossAI.transform.position).normalized;
                dashDirection = new Vector2(directionToPlayer.x, directionToPlayer.y);
            }
            else
            {
                // Default to forward direction if no player found
                dashDirection = Vector2.right;
            }
            // Apply horizontal dash force
            bossRigidbody.velocity = new Vector2(dashDirection.x * dashForce, dashDirection.y * dashForce);
            hasDashed = true;
            
            Debug.Log($"JumpSlash: Performed dash with force {dashForce} in direction {dashDirection}");
        }
    }
    
    private void UpdateDashingPhase()
    {
        // Check if boss has collided with ground (grounded check)
        bool isGrounded = false;
        if (bossAI != null)
        {
            // Check if velocity is very low or stopped (indicating ground collision)
            if (bossRigidbody != null && Mathf.Abs(bossRigidbody.velocity.y) < 0.1f && bossRigidbody.velocity.y >= -0.1f)
            {
                isGrounded = true;
            }
        }
        
        // Spawn attack immediately upon ground collision OR after dash duration as fallback
        if (isGrounded || phaseTimer >= dashDuration)
        {
            // Transition to attacking phase
            currentPhase = JumpSlashPhase.Attacking;
            phaseTimer = 0f;
            PerformSlashAttack();
            
            Debug.Log($"JumpSlash: Transitioning to attacking phase - Ground collision detected: {isGrounded}");
        }
    }
    
    private void PerformSlashAttack()
    {
        if (slashAttackPrefab != null && !hasAttacked)
        {
            /*
            // Determine spawn position
            Vector3 spawnPosition;
            if (attackSpawnPoint != null)
            {
                spawnPosition = attackSpawnPoint.position;
            }
            else if (bossAI != null)
            {
                // Spawn attack slightly in front of boss
                spawnPosition = bossAI.transform.position + new Vector3(dashDirection.x * 2f, 0f, 0f);
            }
            else
            {
                spawnPosition = Vector3.zero;
            }
            */
            //Always spawn at Boss position
            Vector3 spawnPosition;
            spawnPosition = bossAI.transform.position;

            // Spawn the slash attack
            GameObject attack = Object.Instantiate(slashAttackPrefab, spawnPosition, Quaternion.identity);
            hasAttacked = true;

            // Apply screen shake
            if (cameraController != null)
            {
                cameraController.ScreenShake(0.3f);
                Debug.Log($"JumpSlash: Applied screen shake");
            }
            //stop all movement
            if (bossRigidbody != null)
            {
                bossRigidbody.velocity = Vector2.zero;
            }

            Debug.Log($"JumpSlash: Spawned slash attack at position {spawnPosition}");
        }
    }
    
    private void UpdateAttackingPhase()
    {
        // Attack phase lasts briefly
        if (phaseTimer >= 0.5f)
        {
            // Transition to landing phase
            currentPhase = JumpSlashPhase.Landing;
            phaseTimer = 0f;
            
            Debug.Log($"JumpSlash: Transitioning to landing phase");
        }
    }
    
    private void UpdateLandingPhase()
    {
        // Gradually reduce horizontal movement
        if (bossRigidbody != null)
        {
            float currentVelocityX = bossRigidbody.velocity.x;
            float reducedVelocityX = Mathf.Lerp(currentVelocityX, 0f, Time.deltaTime * 3f);
            bossRigidbody.velocity = new Vector2(reducedVelocityX, bossRigidbody.velocity.y);
        }
        
        // Landing phase completes when we've reduced movement or time runs out
        if (phaseTimer >= 1f || (bossRigidbody != null && Mathf.Abs(bossRigidbody.velocity.x) < 0.1f))
        {
            CompleteSkill();
        }
    }
    
    public override BossSkill CreateCopy()
    {
        return new JumpSlash(slashAttackPrefab, attackSpawnPoint);
    }
    
    // Configuration methods
    public void SetJumpForce(float force)
    {
        jumpForce = Mathf.Max(0f, force);
    }
    
    public void SetDashSettings(float force, float duration)
    {
        dashForce = Mathf.Max(0f, force);
        dashDuration = Mathf.Max(0.1f, duration);
    }
    
    public void SetAttackPrefab(GameObject prefab, Transform spawnPoint = null)
    {
        slashAttackPrefab = prefab;
        attackSpawnPoint = spawnPoint;
    }
    
    // Status getters
    public JumpSlashPhase CurrentPhase => currentPhase;
    public bool HasJumped => hasJumped;
    public bool HasDashed => hasDashed;
    public bool HasAttacked => hasAttacked;
}
