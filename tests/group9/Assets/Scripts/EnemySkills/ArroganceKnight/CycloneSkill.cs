using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Cyclone Attack Skill for ArroganceKnight
/// Lasts 3 seconds, switches to Cyclone animation, and spawns CycloneAttack hitboxes every 0.25 seconds
/// </summary>

[System.Serializable]
public class Cyclone : BossSkill
{
    [Header("Attack Settings")]
    [SerializeField] private GameObject cycloneAttackPrefab;
    [SerializeField] private Vector3 attackOffset = Vector3.zero;
    [SerializeField] private float spawnInterval = 0.25f; // Spawn every 0.25 seconds
    [SerializeField] private float attackDelay = 1f; // 1 second delay before first attack
    [SerializeField] private float moveSpeed = 2f; // Speed to move towards player
    [SerializeField] private bool randomizePosition = true;
    [SerializeField] private float randomRadius = 1.5f; // Random spawn radius around boss
    
    private List<GameObject> spawnedAttacks = new List<GameObject>();
    private float nextSpawnTime = 0f;
    private float attackTimer = 0f;
    private bool hasStartedAttacking = false;
    private int attackCount = 0;
    private GameObject playerTarget;
    
    public Cyclone() : base("Cyclone", 4f) // Extended to 4 seconds to account for delay
    {
        canBeInterrupted = false; // Cannot be interrupted during cyclone
    }
    
    public Cyclone(GameObject attackPrefab) : base("Cyclone", 4f)
    {
        cycloneAttackPrefab = attackPrefab;
        canBeInterrupted = false;
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        Debug.Log($"ArroganceKnight: Starting Cyclone attack - will spawn attacks after {attackDelay} seconds delay, then every {spawnInterval} seconds");
        
        // Switch to Cyclone animation
        if (bossAI != null && bossAI.TryGetComponent<ArroganceKnightAI>(out ArroganceKnightAI knightAI))
        {
            knightAI.SwitchToAnimationSet("Cyclone");
        }
        
        // Find player target
        playerTarget = GameObject.FindGameObjectWithTag("Player");
        
        // Reset spawn tracking
        attackTimer = 0f;
        nextSpawnTime = attackDelay; // First spawn after delay
        hasStartedAttacking = false;
        attackCount = 0;
        spawnedAttacks.Clear();
    }
    
    protected override void OnSkillUpdate()
    {
        attackTimer += Time.deltaTime;
        
        // Move towards player at low speed during cyclone
        if (playerTarget != null && bossRigidbody != null)
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
        
        // Handle attack spawning after delay
        if (!hasStartedAttacking && attackTimer >= attackDelay)
        {
            hasStartedAttacking = true;
            nextSpawnTime = attackTimer + spawnInterval; // Schedule next spawn
            SpawnAttackHitbox(); // Spawn first attack
        }
        
        // Handle periodic spawning after initial delay
        if (hasStartedAttacking && attackTimer >= nextSpawnTime)
        {
            SpawnAttackHitbox();
            nextSpawnTime = attackTimer + spawnInterval; // Schedule next spawn
        }
        
        // Clean up destroyed attacks from the list
        CleanupDestroyedAttacks();
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        Debug.Log($"ArroganceKnight: Cyclone attack completed - spawned {attackCount} attacks total");
        
        // Clean up all remaining attacks
        CleanupAllAttacks();
    }
    
    private void SpawnAttackHitbox()
    {
        // Try to find the prefab if not set
        if (cycloneAttackPrefab == null)
        {
            // Look for CycloneAttack prefab in Resources or try to find it
            cycloneAttackPrefab = Resources.Load<GameObject>("CycloneAttack");
            
            if (cycloneAttackPrefab == null)
            {
                Debug.LogError($"Cyclone: CycloneAttack prefab not found! Please assign it in the inspector or place it in Resources folder.");
                return;
            }
        }

        // Spawn at boss position without randomize
        Vector3 spawnPosition = bossTransform.position + attackOffset;

        // Spawn the attack hitbox
        GameObject newAttack = Object.Instantiate(cycloneAttackPrefab, spawnPosition, bossTransform.rotation);
        spawnedAttacks.Add(newAttack);
        attackCount++;
        
        Debug.Log($"Cyclone: Spawned CycloneAttack #{attackCount} at {spawnPosition}");
    }
     
    private void CleanupDestroyedAttacks()
    {
        // Remove null references (destroyed objects) from the list
        for (int i = spawnedAttacks.Count - 1; i >= 0; i--)
        {
            if (spawnedAttacks[i] == null)
            {
                spawnedAttacks.RemoveAt(i);
            }
        }
    }
    
    private void CleanupAllAttacks()
    {
        // Destroy all remaining attacks
        foreach (GameObject attack in spawnedAttacks)
        {
            if (attack != null)
            {
                Object.Destroy(attack);
            }
        }
        
        spawnedAttacks.Clear();
    }
    
    public override BossSkill CreateCopy()
    {
        return new Cyclone(cycloneAttackPrefab);
    }
    
    public void SetAttackPrefab(GameObject prefab)
    {
        cycloneAttackPrefab = prefab;
    }
    
    public void SetSpawnInterval(float interval)
    {
        spawnInterval = Mathf.Max(0.1f, interval);
    }
    
    public void SetRandomRadius(float radius)
    {
        randomRadius = Mathf.Max(0.5f, radius);
    }
    
    public void SetRandomizePosition(bool randomize)
    {
        randomizePosition = randomize;
    }
    
    // Getter for current attack count (useful for debugging)
    public int GetAttackCount()
    {
        return attackCount;
    }
    
    public int GetActiveAttackCount()
    {
        CleanupDestroyedAttacks();
        return spawnedAttacks.Count;
    }
}
