using UnityEngine;

/// <summary>
/// Horizontal Swing Attack Skills for ArroganceKnight
/// Two variants: HorizontalSwing_1 and HorizontalSwing_2
/// Both last 1 second, switch animations, and spawn attack hitboxes
/// </summary>

[System.Serializable]
public class HorizontalSwing_1 : BossSkill
{
    [Header("Attack Settings")]
    [SerializeField] private GameObject hAttack1Prefab;
    [SerializeField] private Vector3 attackOffset = new Vector3(1.2f, 0f, 0f);
    [SerializeField] private float attackDelay = 1f; // 1 second delay before spawning attack
    [SerializeField] private float moveSpeed = 2f; // Speed to move towards player
    
    private GameObject spawnedAttack;
    private GameObject playerTarget;
    private float attackTimer = 0f;
    private bool hasSpawned = false;
    
    public HorizontalSwing_1() : base("HorizontalSwing_1", 2f) // Extended to 2 seconds to account for delay
    {
        canBeInterrupted = false; // Cannot be interrupted during attack
    }
    
    public HorizontalSwing_1(GameObject attackPrefab) : base("HorizontalSwing_1", 2f)
    {
        hAttack1Prefab = attackPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting HorizontalSwing_1 attack - will spawn attack after {attackDelay} seconds delay");
        
        // Switch to HorizontalSwing1 animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("HorizontalSwing1");
        }
        
        // Find player target
        playerTarget = GameObject.FindGameObjectWithTag("Player");
        
        // Reset spawn tracking
        attackTimer = 0f;
        hasSpawned = false;
    }
    
    protected override void OnSkillUpdate()
    {
        attackTimer += Time.deltaTime;
        
        // Move towards player at low speed during attack, but only until attack spawns
        if (playerTarget != null && bossRigidbody != null && attackTimer < attackDelay && !hasSpawned)
        {
            Vector3 directionToPlayer = (playerTarget.transform.position - bossTransform.position).normalized;
            Vector2 moveVelocity = new Vector2(directionToPlayer.x * moveSpeed, bossRigidbody.velocity.y);
            bossRigidbody.velocity = moveVelocity;
        }
        else
        {
            // Keep boss stationary if no player found or after attack spawns
            if (bossRigidbody != null)
            {
                bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
            }
        }
        
        // Spawn attack after delay
        if (!hasSpawned && attackTimer >= attackDelay)
        {
            // Stop movement when spawning attack
            if (bossRigidbody != null)
            {
                bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
            }
            SpawnAttackHitbox();
            hasSpawned = true;
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        Debug.Log($"ArroganceKnight: HorizontalSwing_1 attack completed");
        
        // Clean up spawned attack if it still exists
        if (spawnedAttack != null)
        {
            Object.Destroy(spawnedAttack);
            spawnedAttack = null;
        }
    }
    
    private void SpawnAttackHitbox()
    {
        // Try to find the prefab if not set
        if (hAttack1Prefab == null)
        {
            // Look for HAttack1 prefab in Resources or try to find it
            hAttack1Prefab = Resources.Load<GameObject>("HAttack1");
            
            if (hAttack1Prefab == null)
            {
                Debug.LogError($"HorizontalSwing_1: HAttack1 prefab not found! Please assign it in the inspector or place it in Resources folder.");
                return;
            }
        }
        
        // Calculate spawn position considering boss facing direction
        Vector3 directionAdjustedOffset = attackOffset;
        
        // Get boss facing direction from EnemyStats
        if (bossAI != null && bossAI.TryGetComponent<EnemyStats>(out EnemyStats enemyStats))
        {
            // If boss is facing left, flip the X offset
            if (!enemyStats.IsFacingRight)
            {
                directionAdjustedOffset.x = -attackOffset.x;
            }
        }
        
        Vector3 spawnPosition = bossTransform.position + directionAdjustedOffset;
        
        // Spawn the attack hitbox
        spawnedAttack = Object.Instantiate(hAttack1Prefab, spawnPosition, bossTransform.rotation);
        Debug.Log($"HorizontalSwing_1: Spawned HAttack1 at {spawnPosition} (facing {(directionAdjustedOffset.x >= 0 ? "right" : "left")})");
    }
    
    public override BossSkill CreateCopy()
    {
        return new HorizontalSwing_1(hAttack1Prefab);
    }
    
    public void SetAttackPrefab(GameObject prefab)
    {
        hAttack1Prefab = prefab;
    }
}

[System.Serializable]
public class HorizontalSwing_2 : BossSkill
{
    [Header("Attack Settings")]
    [SerializeField] private GameObject hAttack2Prefab;
    [SerializeField] private Vector3 attackOffset = new Vector3(1.2f, 0f, 0f);
    [SerializeField] private float attackDelay = 1f; // 1 second delay before spawning attack
    [SerializeField] private float moveSpeed = 2f; // Speed to move towards player
    
    private GameObject spawnedAttack;
    private GameObject playerTarget;
    private float attackTimer = 0f;
    private bool hasSpawned = false;
    
    public HorizontalSwing_2() : base("HorizontalSwing_2", 2f) // Extended to 2 seconds to account for delay
    {
        canBeInterrupted = false; // Cannot be interrupted during attack
    }
    
    public HorizontalSwing_2(GameObject attackPrefab) : base("HorizontalSwing_2", 2f)
    {
        hAttack2Prefab = attackPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting HorizontalSwing_2 attack - will spawn attack after {attackDelay} seconds delay");
        
        // Switch to HorizontalSwing2 animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("HorizontalSwing2");
        }
        
        // Find player target
        playerTarget = GameObject.FindGameObjectWithTag("Player");
        
        // Reset spawn tracking
        attackTimer = 0f;
        hasSpawned = false;
    }
    
    protected override void OnSkillUpdate()
    {
        attackTimer += Time.deltaTime;
        
        // Move towards player at low speed during attack
        if (playerTarget != null && bossRigidbody != null && attackTimer < attackDelay)
        {
            Vector3 directionToPlayer = (playerTarget.transform.position - bossTransform.position).normalized;
            Vector2 moveVelocity = new Vector2(directionToPlayer.x * moveSpeed, bossRigidbody.velocity.y);
            bossRigidbody.velocity = moveVelocity;
        }
        else
        {
            // Keep boss stationary if no player found
            if (bossRigidbody != null)
            {
                bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
            }
        }
        
        // Spawn attack after delay
        if (!hasSpawned && attackTimer >= attackDelay)
        {
            bossRigidbody.velocity = Vector2.zero; // Stop movement
            SpawnAttackHitbox();
            hasSpawned = true;
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        Debug.Log($"ArroganceKnight: HorizontalSwing_2 attack completed");
        
        // Clean up spawned attack if it still exists
        if (spawnedAttack != null)
        {
            Object.Destroy(spawnedAttack);
            spawnedAttack = null;
        }
    }
    
    private void SpawnAttackHitbox()
    {
        // Try to find the prefab if not set
        if (hAttack2Prefab == null)
        {
            // Look for HAttack2 prefab in Resources or try to find it
            hAttack2Prefab = Resources.Load<GameObject>("HAttack2");
            
            if (hAttack2Prefab == null)
            {
                Debug.LogError($"HorizontalSwing_2: HAttack2 prefab not found! Please assign it in the inspector or place it in Resources folder.");
                return;
            }
        }
        
        // Calculate spawn position considering boss facing direction
        Vector3 directionAdjustedOffset = attackOffset;
        
        // Get boss facing direction from EnemyStats
        if (bossAI != null && bossAI.TryGetComponent<EnemyStats>(out EnemyStats enemyStats))
        {
            // If boss is facing left, flip the X offset
            if (!enemyStats.IsFacingRight)
            {
                directionAdjustedOffset.x = -attackOffset.x;
            }
        }
        
        Vector3 spawnPosition = bossTransform.position + directionAdjustedOffset;
        
        // Spawn the attack hitbox
        spawnedAttack = Object.Instantiate(hAttack2Prefab, spawnPosition, bossTransform.rotation);
        
        Debug.Log($"HorizontalSwing_2: Spawned HAttack2 at {spawnPosition} (facing {(directionAdjustedOffset.x >= 0 ? "right" : "left")})");
    }
    
    public override BossSkill CreateCopy()
    {
        return new HorizontalSwing_2(hAttack2Prefab);
    }
    
    public void SetAttackPrefab(GameObject prefab)
    {
        hAttack2Prefab = prefab;
    }
}
