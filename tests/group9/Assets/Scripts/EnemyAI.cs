using UnityEngine;

public abstract class EnemyAI : MonoBehaviour, IEnemyAI
{
    [Header("Base AI Settings")]
    [SerializeField] private float baseMovementSpeed = 3f;
    [SerializeField] private bool controlEnabled = true;
    
    [Header("Component References")]
    [SerializeField] private EnemyStats enemyStats;
    [SerializeField] private Rigidbody2D rb;
    
    // Protected members for derived classes
    protected float currentMovementSpeed;
    protected bool isDead = false;
    
    // Properties
    public EnemyStats EnemyStats 
    { 
        get => enemyStats; 
        set => enemyStats = value; 
    }
    
    public float BaseMovementSpeed 
    { 
        get => baseMovementSpeed; 
        set => baseMovementSpeed = Mathf.Max(0f, value); 
    }
    
    public bool ControlEnabled => controlEnabled && !isDead;
    public bool IsDead => isDead;
    public float CurrentMovementSpeed => currentMovementSpeed;
    
    protected virtual void Awake()
    {
        if (enemyStats != null && enemyStats.EnemyAI == null)
        {
            enemyStats.EnemyAI = this;
        }
    }
    
    protected virtual void Start()
    {
        // Initialize movement speed
        currentMovementSpeed = baseMovementSpeed;
        currentMovementSpeed *= enemyStats.WalkSpeedAdjustment;
    }
    
    
    protected virtual void Update()
    {
        // Only process AI if control is enabled and alive
        if (!ControlEnabled) return;
        
        // Call derived class update logic
        UpdateAI();
    }
    
    /// <summary>
    /// Abstract method for derived classes to implement their specific AI logic
    /// </summary>
    protected abstract void UpdateAI();
    

    public virtual void SetControlEnabled(bool enabled)
    {
        controlEnabled = enabled;
    }
    
    public virtual void DeathSequence()
    {
        isDead = true;
        controlEnabled = false;
        
        // Stop any movement
        if (rb != null)
        {
            rb.velocity = Vector2.zero;
        }
        
        // Call specific death implementation
        OnDeath();
        
        // Default behavior: destroy after a short delay
        Destroy(gameObject, 2f);
    }
    
    protected virtual void OnDeath()
    {
        // Override in derived classes for specific death behavior
        
    }
    
    protected GameObject FindPlayer()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        
        return player;
    }
    
    protected float GetDistanceToPlayer()
    {
        GameObject player = FindPlayer();
        return player != null ? Vector2.Distance(transform.position, player.transform.position) : float.MaxValue;
    }
    
    protected Vector2 GetDirectionToPlayer()
    {
        GameObject player = FindPlayer();
        return player != null ? (player.transform.position - transform.position).normalized : Vector2.zero;
    }

    protected void Move(float direction)
    {
        if (rb == null || !ControlEnabled) return;
        
        Vector2 velocity = rb.velocity;
        velocity.x = direction * currentMovementSpeed;
        rb.velocity = velocity;
    }
    
    protected void StopMovement()
    {
        if (rb == null) return;
        
        Vector2 velocity = rb.velocity;
        velocity.x = 0f;
        rb.velocity = velocity;
    }
    
    private void OnValidate()
    {
        // Clamp values in editor
        baseMovementSpeed = Mathf.Max(0f, baseMovementSpeed);
    }

    //interface member of update movement speed
    public void UpdateMovementSpeed()
    {
        currentMovementSpeed = baseMovementSpeed * enemyStats.WalkSpeedAdjustment;
    }
}
