using UnityEngine;

/// <summary>
/// Great Slash Horizontal Attack Skill for ArroganceKnight
/// Powerful horizontal attack with GreatSlashHorizontalAttack hitbox
/// </summary>

[System.Serializable]
public class GreatSlashHorizontalSkill : BossSkill
{
    [Header("Attack Settings")]
    [SerializeField] private GameObject greatSlashHorizontalPrefab; // GreatSlashHorizontalAttack prefab
    [SerializeField] private Vector3 attackOffset = Vector3.zero;
    
    private GameObject spawnedAttack;
    private GameObject playerTarget;
    private bool hasSpawned = false;
    private CameraController cameraController;
    
    public GreatSlashHorizontalSkill() : base("GreatSlashHorizontal", 1f) // Lasts 1 second
    {
        canBeInterrupted = false; // Cannot be interrupted during attack
    }
    
    public GreatSlashHorizontalSkill(GameObject attackPrefab) : base("GreatSlashHorizontal", 1f)
    {
        greatSlashHorizontalPrefab = attackPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        cameraController = Camera.main.GetComponent<CameraController>();

        
        Debug.Log("ArroganceKnight: Starting GreatSlashHorizontal attack");
        
        // Switch to GreatSlash animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("GreatSlash");
        }
        
        // Find player target for direction reference
        playerTarget = GameObject.FindGameObjectWithTag("Player");
        
        // Reset spawn tracking
        hasSpawned = false;
        
        // Spawn attack immediately upon activation
        SpawnAttackHitbox();
    }
    
    protected override void OnSkillUpdate()
    {
        // Keep boss stationary during attack
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = new Vector2(0f, bossRigidbody.velocity.y);
        }
    }
    
    private void SpawnAttackHitbox()
    {
        if (hasSpawned || greatSlashHorizontalPrefab == null)
        {
            Debug.LogWarning("ArroganceKnight: GreatSlashHorizontal attack already spawned or prefab is null");
            return;
        }
        
        // Calculate spawn position and rotation
        Vector3 spawnPosition = bossTransform.position + attackOffset;
        Quaternion spawnRotation = bossTransform.rotation;
        
        // Spawn the attack hitbox using boss rotation
        spawnedAttack = GameObject.Instantiate(greatSlashHorizontalPrefab, spawnPosition, spawnRotation);
        hasSpawned = true;
        if (cameraController != null)
        {
            cameraController.ScreenShake(0.6f);
            Debug.Log($"JumpSlash: Applied screen shake");
        }
        
        Debug.Log($"ArroganceKnight: GreatSlashHorizontal attack spawned at {spawnPosition}");
    }
    
    protected override void OnSkillEnd()
    {
        Debug.Log("ArroganceKnight: GreatSlashHorizontal skill completed");
        base.OnSkillEnd();
    }
    
    public override BossSkill CreateCopy()
    {
        return new GreatSlashHorizontalSkill(greatSlashHorizontalPrefab);
    }
    
    /// <summary>
    /// Set the attack prefab for this skill
    /// </summary>
    public void SetAttackPrefab(GameObject prefab)
    {
        greatSlashHorizontalPrefab = prefab;
    }
}
