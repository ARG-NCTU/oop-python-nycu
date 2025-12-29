using UnityEngine;

/// <summary>
/// Chain Attack Hitbox - Enhanced Enemy Attack that can spawn copies of itself
/// After waiting for a specified time, spawns a copy at an offset position with reduced spawn count
/// Continues chaining until spawn count reaches 0
/// </summary>
public class ChainEnemyAttackHitbox : EnemyAttackHitbox
{
    [Header("Chain Attack Settings")]
    [SerializeField] private int spawnCount = 3; // Number of times to spawn copies
    [SerializeField] private float waitTime = 0.5f; // Time to wait before spawning next copy
    [SerializeField] private Vector3 spawnOffset = Vector3.right; // Offset for spawning next copy
    [SerializeField] private bool useWorldSpace = true; // Whether offset is in world space or local space
    [SerializeField] private GameObject chainPrefab; // Prefab to spawn (should have this script)
    
    [Header("Chain Visual Settings")]
    [SerializeField] private bool showChainIndicator = true;
    [SerializeField] private Color chainGizmoColor = Color.cyan;
    [SerializeField] private GameObject spawnEffect; // Effect when spawning new chain
    
    [Header("Chain Debug")]
    [SerializeField] private bool showChainDebug = false;
    
    // Private variables for chain management
    private bool hasSpawned = false;
    private float spawnTimer = 0f;
    private bool isOriginalChain = true; // True if this is the first in the chain

    private Vector3 originalPosition;

    // Events
    public System.Action<ChainEnemyAttackHitbox> OnChainSpawned;
    public System.Action OnChainCompleted; // When this chain link completes (no more spawns)
    
    // Properties
    public int SpawnCount
    {
        get => spawnCount;
        set => spawnCount = Mathf.Max(0, value);
    }
    
    public float WaitTime
    {
        get => waitTime;
        set => waitTime = Mathf.Max(0f, value);
    }
    
    public Vector3 SpawnOffset
    {
        get => spawnOffset;
        set => spawnOffset = value;
    }
    
    public bool HasSpawned => hasSpawned;
    public bool IsOriginalChain => isOriginalChain;
    public int RemainingSpawns => spawnCount;
    private GameObject playerTarget;

    private void Start()
    {
        // Auto-destroy this hitbox after the specified lifetime
        Destroy(gameObject, Lifetime);

        // Validate wait time doesn't exceed lifetime
        if (waitTime >= Lifetime)
        {
            Debug.LogWarning($"ChainEnemyAttackHitbox: WaitTime ({waitTime}) should be less than Lifetime ({Lifetime}). Adjusting waitTime to {Lifetime * 0.8f}");
            waitTime = Lifetime * 0.8f;
        }

        // Start spawn timer
        spawnTimer = 0f;

        if (showChainDebug)
        {
            Debug.Log($"ChainEnemyAttackHitbox: Started with {spawnCount} spawns remaining. WaitTime: {waitTime}, Lifetime: {Lifetime}");
        }
        originalPosition = transform.position;

        if (isOriginalChain)
        {
            // Find player target for orientation
            playerTarget = GameObject.FindGameObjectWithTag("Player");
            //Check if player is on the left side, if not, invert the spawn offset
            if (playerTarget != null && playerTarget.transform.position.x > transform.position.x)
            {
                spawnOffset = new Vector3(-spawnOffset.x, spawnOffset.y, spawnOffset.z);
            }
            else
            {
                spawnOffset = new Vector3(spawnOffset.x, spawnOffset.y, spawnOffset.z);
            }
        }
    }
    
    private void Update()
    {
        // Handle chain spawning
        if (!hasSpawned && spawnCount > 0 && spawnTimer < waitTime)
        {
            spawnTimer += Time.deltaTime;
            
            // Check if it's time to spawn
            if (spawnTimer >= waitTime)
            {
                SpawnNextInChain();
            }
        }
    }
    
    /// <summary>
    /// Spawn the next hitbox in the chain
    /// </summary>
    private void SpawnNextInChain()
    {
        if (hasSpawned || spawnCount <= 0) return;
        
        // Determine what to spawn
        GameObject prefabToSpawn = chainPrefab != null ? chainPrefab : gameObject;
        
        // Calculate spawn position
        Vector3 nextPosition;
        if (useWorldSpace)
        {
            nextPosition = originalPosition + spawnOffset;
        }
        else
        {
            nextPosition = originalPosition + transform.TransformDirection(spawnOffset);
        }
        
        // Spawn the next chain link
        GameObject nextChain = Instantiate(prefabToSpawn, nextPosition, transform.rotation);
        
        // Configure the next chain link
        ChainEnemyAttackHitbox nextChainScript = nextChain.GetComponent<ChainEnemyAttackHitbox>();
        if (nextChainScript != null)
        {
            // Reduce spawn count for next link
            nextChainScript.SpawnCount = spawnCount - 1;
            nextChainScript.WaitTime = waitTime;
            nextChainScript.SpawnOffset = spawnOffset;
            nextChainScript.isOriginalChain = false;
            
            // Copy other settings
            nextChainScript.Damage = Damage;
            nextChainScript.HasKnockback = HasKnockback;
            nextChainScript.IgnoreDefence = IgnoreDefence;
            nextChainScript.DestroyOnHit = DestroyOnHit;
            nextChainScript.Lifetime = Lifetime;
            nextChainScript.CooldownBetweenHits = CooldownBetweenHits;
            
            if (showChainDebug)
            {
                Debug.Log($"ChainEnemyAttackHitbox: Spawned next chain at {nextPosition} with {nextChainScript.SpawnCount} spawns remaining");
            }
            
            // Trigger events
            OnChainSpawned?.Invoke(nextChainScript);
        }
        else
        {
            Debug.LogWarning($"ChainEnemyAttackHitbox: Spawned object doesn't have ChainEnemyAttackHitbox component!");
        }
        
        // Play spawn effect
        if (spawnEffect != null)
        {
            GameObject effect = Instantiate(spawnEffect, nextPosition, transform.rotation);
            Destroy(effect, 3f); // Auto-destroy effect
        }
        
        // Mark as spawned
        hasSpawned = true;
        
        // Trigger completion event if this was the last spawn
        if (spawnCount <= 1)
        {
            OnChainCompleted?.Invoke();
            
            if (showChainDebug)
            {
                Debug.Log($"ChainEnemyAttackHitbox: Chain completed - no more spawns");
            }
        }
    }
    
    /// <summary>
    /// Manually trigger the next spawn (useful for testing or special effects)
    /// </summary>
    public void ForceSpawnNext()
    {
        if (!hasSpawned && spawnCount > 0)
        {
            spawnTimer = waitTime; // Set timer to trigger spawn
            SpawnNextInChain();
        }
    }
    
    /// <summary>
    /// Stop the chain from spawning more copies
    /// </summary>
    public void StopChain()
    {
        spawnCount = 0;
        hasSpawned = true;
        
        if (showChainDebug)
        {
            Debug.Log($"ChainEnemyAttackHitbox: Chain stopped manually");
        }
    }
    
    /// <summary>
    /// Initialize this as a spawned chain link (not the original)
    /// </summary>
    /// <param name="remainingSpawns">How many more spawns this link should make</param>
    /// <param name="waitTime">Time to wait before spawning</param>
    /// <param name="offset">Offset for next spawn</param>
    public void InitializeAsSpawnedLink(int remainingSpawns, float waitTime, Vector3 offset)
    {
        this.spawnCount = remainingSpawns;
        this.waitTime = waitTime;
        this.spawnOffset = offset;
        this.isOriginalChain = false;
        this.hasSpawned = false;
        this.spawnTimer = 0f;
        
        if (showChainDebug)
        {
            Debug.Log($"ChainEnemyAttackHitbox: Initialized as spawned link with {remainingSpawns} spawns");
        }
    }
    
    private void OnDrawGizmos()
    {
        if (!showChainIndicator) return;
        
        // Draw chain indicator
        Gizmos.color = chainGizmoColor;
        
        // Draw spawn position indicator
        if (spawnCount > 0)
        {
            Vector3 nextPosition;
            if (useWorldSpace)
            {
                nextPosition = transform.position + spawnOffset;
            }
            else
            {
                nextPosition = transform.position + transform.TransformDirection(spawnOffset);
            }
            
            // Draw line to next spawn position
            Gizmos.DrawLine(transform.position, nextPosition);
            
            // Draw spawn position marker
            Gizmos.DrawWireSphere(nextPosition, 0.2f);
            
            // Draw spawn count text
            #if UNITY_EDITOR
            if (showChainDebug)
            {
                Vector3 textPos = nextPosition + Vector3.up * 0.5f;
                UnityEditor.Handles.Label(textPos, $"Chain: {spawnCount}");
            }
            #endif
        }
        
        // Draw different color if this is part of a chain
        if (!isOriginalChain)
        {
            Gizmos.color = Color.Lerp(chainGizmoColor, Color.white, 0.5f);
            Gizmos.DrawWireCube(transform.position, Vector3.one * 0.1f);
        }
    }
    
    private void OnValidate()
    {
        // Clamp chain values
        spawnCount = Mathf.Max(0, spawnCount);
        waitTime = Mathf.Max(0f, waitTime);
        
        // Warn if wait time is too long
        if (waitTime >= Lifetime && Lifetime > 0f)
        {
            Debug.LogWarning($"ChainEnemyAttackHitbox: WaitTime ({waitTime}) should be less than Lifetime ({Lifetime})");
        }
    }
    
    /// <summary>
    /// Get debug information about the chain state
    /// </summary>
    /// <returns>Debug string with chain information</returns>
    public string GetChainDebugInfo()
    {
        return $"ChainEnemyAttackHitbox - {gameObject.name}: " +
               $"SpawnCount: {spawnCount} | " +
               $"WaitTime: {waitTime:F2}s | " +
               $"HasSpawned: {hasSpawned} | " +
               $"IsOriginal: {isOriginalChain} | " +
               $"Timer: {spawnTimer:F2}s | " +
               $"NextPosition: {(useWorldSpace ? transform.position + spawnOffset : transform.position + transform.TransformDirection(spawnOffset))}";
    }
}
