using UnityEngine;

/// <summary>
/// Giant Swing Attack Skill for ArroganceKnight
/// Lasts 3 seconds, switches to GiantSwing animation, spawns GiantSwingAttack at start, then stays idle
/// </summary>

[System.Serializable]
public class GiantSwing : BossSkill
{
    [Header("Attack Settings")]
    [SerializeField] private GameObject giantSwingAttackPrefab;
    [SerializeField] private float spawnDelay = 2f; // 2 second delay before spawning the attack for better reaction time
    [SerializeField] private bool maintainPosition = true; // Keep boss stationary during skill
    
    private GameObject spawnedAttack;
    private float spawnTimer = 0f;
    private bool hasSpawned = false;

    private CameraController cameraController;
    
    public GiantSwing() : base("GiantSwing", 5f) // Extended to 5 seconds for better reaction time
    {
        canBeInterrupted = false; // Cannot be interrupted during giant swing
    }
    
    public GiantSwing(GameObject attackPrefab) : base("GiantSwing", 5f)
    {
        giantSwingAttackPrefab = attackPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();

        // Get reference to CameraController
        cameraController = Camera.main.GetComponent<CameraController>();

        Debug.Log($"ArroganceKnight: Starting GiantSwing attack - will spawn attack after {spawnDelay} seconds");
        
        // Switch to GiantSwing animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("GiantSwing");
        }
        
        // Reset spawn tracking
        spawnTimer = 0f;
        hasSpawned = false;
    }
    
    protected override void OnSkillUpdate()
    {
        // Keep boss stationary if configured
        if (maintainPosition && bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
        
        // Handle delayed spawn (only once at the start)
        if (!hasSpawned)
        {
            spawnTimer += Time.deltaTime;
            
            if (spawnTimer >= spawnDelay)
            {
                SpawnAttackHitbox();
                hasSpawned = true;
                
                Debug.Log($"GiantSwing: Attack spawned, now staying idle for remaining duration");
            }
        }
        
        // After spawning, the boss just stays idle for the rest of the duration
        // This is handled automatically by the base class duration system
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        Debug.Log($"ArroganceKnight: GiantSwing attack completed");
        
        // Note: We don't destroy the spawned attack here because it should persist
        // based on its own lifetime settings in the EnemyAttackHitbox component
        // But we can clean up our reference
        spawnedAttack = null;
    }
    
    private void SpawnAttackHitbox()
    {
        // Try to find the prefab if not set
        if (giantSwingAttackPrefab == null)
        {
            // Look for GiantSwingAttack prefab in Resources or try to find it
            giantSwingAttackPrefab = Resources.Load<GameObject>("GiantSwingAttack");

            if (giantSwingAttackPrefab == null)
            {
                Debug.LogError($"GiantSwing: GiantSwingAttack prefab not found! Please assign it in the inspector or place it in Resources folder.");
                return;
            }
            //Apply screen shake
            cameraController.ScreenShake(0.3f);

        }
        
        // Calculate spawn position
        Vector3 spawnPosition = CalculateSpawnPosition();
        
        // Calculate rotation (face the player if desired)
        Quaternion spawnRotation = CalculateSpawnRotation();
        
        // Spawn the attack hitbox
        spawnedAttack = Object.Instantiate(giantSwingAttackPrefab, spawnPosition, spawnRotation);
        
        // Get facing direction for debug log
        bool isFacingRight = true;
        if (bossAI != null && bossAI.TryGetComponent<EnemyStats>(out EnemyStats enemyStats))
        {
            isFacingRight = enemyStats.IsFacingRight;
        }
        
        Debug.Log($"GiantSwing: Spawned GiantSwingAttack at {spawnPosition} (facing {(isFacingRight ? "right" : "left")})");
    }
    
    private Vector3 CalculateSpawnPosition()
    {
        // Base offset (configured for right-facing)
        Vector3 baseOffset = new Vector3(-1f, -5f, 0f); // Example offset below the boss
        Vector3 directionAdjustedOffset = baseOffset;
        
        // Get boss facing direction from EnemyStats
        if (bossAI != null && bossAI.TryGetComponent<EnemyStats>(out EnemyStats enemyStats))
        {
            // If boss is facing left, flip the X offset
            if (!enemyStats.IsFacingRight)
            {
                directionAdjustedOffset.x = -baseOffset.x;
            }
        }
        
        Vector3 basePosition = bossTransform.position + directionAdjustedOffset;
        
        return basePosition;
    }
    
    private Quaternion CalculateSpawnRotation()
    {
        // Use boss rotation directly
        return bossTransform.rotation;
    }
    
    public override BossSkill CreateCopy()
    {
        return new GiantSwing(giantSwingAttackPrefab);
    }
    
    public void SetAttackPrefab(GameObject prefab)
    {
        giantSwingAttackPrefab = prefab;
    }
    
    public void SetSpawnDelay(float delay)
    {
        spawnDelay = Mathf.Max(0f, delay);
    }
    
    public void SetMaintainPosition(bool maintain)
    {
        maintainPosition = maintain;
    }
    
    // Getters for status checking
    public bool HasSpawnedAttack()
    {
        return hasSpawned;
    }
    
    public float GetTimeUntilSpawn()
    {
        return hasSpawned ? 0f : Mathf.Max(0f, spawnDelay - spawnTimer);
    }
    
    public GameObject GetSpawnedAttack()
    {
        return spawnedAttack;
    }
}
