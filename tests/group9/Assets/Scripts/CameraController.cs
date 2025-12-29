using UnityEngine;

/// <summary>
/// Camera Controller script for 2D games
/// Supports focus mode (follow object) and set mode (fixed position)
/// Includes boundary constraints for camera movement
/// </summary>
public class CameraController : MonoBehaviour
{

    public enum CameraMode
    {
        Focus,          // Follow a target object
        Set,            // Fixed position mode
        DirectControl   // Player controls camera with WASD
    }

    [Header("Camera Mode")]
    [SerializeField] private CameraMode currentMode = CameraMode.Focus;

    [Header("Focus Mode Settings")]
    [SerializeField] private Transform target;
    [SerializeField] private Vector3 offset = new Vector3(0, 0, -10);
    [SerializeField] private float followSmoothness = 0.125f; // Lower = smoother (0.01-0.5)
    [SerializeField] private bool smoothFollow = true;

    [Header("Set Mode Settings")]
    [SerializeField] private Vector3 setPosition = new Vector3(0, 0, -10);
    [SerializeField] private float moveSmoothness = 0.125f; // Lower = smoother (0.01-0.5)
    [SerializeField] private bool smoothMove = true;

    [Header("Direct Control Settings")]
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] private bool useAcceleration = true;
    [SerializeField] private float acceleration = 10f;
    [SerializeField] private float deceleration = 15f;
    [SerializeField] private float maxMoveSpeed = 10f;

    [Header("Camera Boundaries")]
    [SerializeField] private bool useBoundaries = true;
    [SerializeField] private float minX = -10f;
    [SerializeField] private float maxX = 10f;
    [SerializeField] private float minY = -5f;
    [SerializeField] private float maxY = 5f;
    [SerializeField] private float minZ = -20f;
    [SerializeField] private float maxZ = -5f;

    [Header("Debug")]
    [SerializeField] private bool showDebugInfo = false;
    [SerializeField] private bool showBoundariesGizmos = true;

    // Private variables
    private Camera cameraComponent;
    private Vector3 targetPosition;
    private Vector3 velocity = Vector3.zero;
    private Vector3 currentVelocity = Vector3.zero; // For direct control movement
    private Vector3 shakeOffset = Vector3.zero;
    private float shakeDuration = 0f;

    // FullView toggle for DirectControl mode
    public bool FullView = false;
    public float FullViewSize = 8f;
    private Vector3 savedCameraPosition;
    
    // Cutscene camera movement
    private bool isCutsceneActive = false;
    private CameraMode savedMode;
    private Transform savedTarget;
    private Vector3 savedOffset;

    // Properties for external access
    public CameraMode CurrentMode
    {
        get => currentMode;
        set => currentMode = value;
    }

    public Transform Target
    {
        get => target;
        set => target = value;
    }

    public Vector3 Offset
    {
        get => offset;
        set => offset = value;
    }

    public float FollowSmoothness
    {
        get => followSmoothness;
        set => followSmoothness = Mathf.Clamp(value, 0.001f, 1f);
    }

    public bool SmoothFollow
    {
        get => smoothFollow;
        set => smoothFollow = value;
    }

    public Vector3 SetPosition
    {
        get => setPosition;
        set => setPosition = value;
    }

    public float MoveSmoothness
    {
        get => moveSmoothness;
        set => moveSmoothness = Mathf.Clamp(value, 0.001f, 1f);
    }

    public bool SmoothMove
    {
        get => smoothMove;
        set => smoothMove = value;
    }

    public bool UseBoundaries
    {
        get => useBoundaries;
        set => useBoundaries = value;
    }

    public float MinX
    {
        get => minX;
        set => minX = value;
    }

    public float MaxX
    {
        get => maxX;
        set => maxX = value;
    }

    public float MinY
    {
        get => minY;
        set => minY = value;
    }

    public float MaxY
    {
        get => maxY;
        set => maxY = value;
    }

    public float MinZ
    {
        get => minZ;
        set => minZ = value;
    }

    public float MaxZ
    {
        get => maxZ;
        set => maxZ = value;
    }

    public float MoveSpeed
    {
        get => moveSpeed;
        set => moveSpeed = Mathf.Max(0f, value);
    }

    public bool UseAcceleration
    {
        get => useAcceleration;
        set => useAcceleration = value;
    }

    public float Acceleration
    {
        get => acceleration;
        set => acceleration = Mathf.Max(0f, value);
    }

    public float Deceleration
    {
        get => deceleration;
        set => deceleration = Mathf.Max(0f, value);
    }

    public float MaxMoveSpeed
    {
        get => maxMoveSpeed;
        set => maxMoveSpeed = Mathf.Max(0f, value);
    }

    private void Awake()
    {
        // Get camera component
        cameraComponent = GetComponent<Camera>();
        if (cameraComponent == null)
        {
            Debug.LogError("CameraController requires a Camera component!");
        }

        // Initialize target position
        targetPosition = transform.position;
    }

    private void Start()
    {
        // Set initial camera position based on mode
        UpdateTargetPosition();
        //find target with tag "Player" if in focus mode and no target assigned one second after start
        if (target == null)
        {
            Invoke("FindPlayerTarget", .1f);
        }
    }
    private void FindPlayerTarget()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player != null)
        {
            target = player.transform;
            if (showDebugInfo)
            {
                Debug.Log("CameraController: Found player target for Focus mode.");
            }
        }
        else
        {
            if (showDebugInfo)
            {
                Debug.LogWarning("CameraController: No player found with tag 'Player' for Focus mode.");
            }
        }
    }

    private void LateUpdate()
    {
        UpdateTargetPosition();
        MoveCameraToTarget();

        if (showDebugInfo)
        {
            DisplayDebugInfo();
        }
    }

    private void OnValidate()
    {
        // Ensure valid values in inspector
        followSmoothness = Mathf.Clamp(followSmoothness, 0.001f, 1f);
        moveSmoothness = Mathf.Clamp(moveSmoothness, 0.001f, 1f);
        moveSpeed = Mathf.Max(0f, moveSpeed);
        acceleration = Mathf.Max(0f, acceleration);
        deceleration = Mathf.Max(0f, deceleration);
        maxMoveSpeed = Mathf.Max(0f, maxMoveSpeed);

        // Ensure min values are less than max values
        if (minX > maxX)
        {
            float temp = minX;
            minX = maxX;
            maxX = temp;
        }

        if (minY > maxY)
        {
            float temp = minY;
            minY = maxY;
            maxY = temp;
        }

        if (minZ > maxZ)
        {
            float temp = minZ;
            minZ = maxZ;
            maxZ = temp;
        }
    }

    private void UpdateTargetPosition()
    {
        switch (currentMode)
        {
            case CameraMode.Focus:
                UpdateFocusMode();
                break;
            case CameraMode.Set:
                UpdateSetMode();
                break;
            case CameraMode.DirectControl:
                UpdateDirectControlMode();
                break;
        }

        // Apply boundaries if enabled
        if (useBoundaries)
        {
            ApplyBoundaries();
        }
    }

    private void UpdateFocusMode()
    {
        // Skip normal update if cutscene is active
        if (isCutsceneActive)
        {
            return;
        }
        
        if (target != null)
        {
            targetPosition = target.position + offset;
        }
        else
        {
            if (showDebugInfo)
            {
                Debug.LogWarning("Focus mode active but no target assigned!");
            }
        }
    }

    private void UpdateSetMode()
    {
        targetPosition = setPosition;
    }

    private void UpdateDirectControlMode()
    {
        // Toggle FullView with E key
        if (Input.GetKeyDown(KeyCode.E))
        {
            FullView = !FullView;
            if (FullView)
            {
                savedCameraPosition = transform.position;
                if (cameraComponent != null) cameraComponent.orthographicSize = FullViewSize;
                targetPosition = new Vector3(0, 0, -10);
                transform.position = targetPosition;
            }
            else
            {
                if (cameraComponent != null) cameraComponent.orthographicSize = 4f;
                targetPosition = savedCameraPosition;
                transform.position = targetPosition;
                currentVelocity = Vector3.zero;
            }
        }

        if (!FullView)
        {
            // Get input from WASD keys
            Vector3 inputDirection = Vector3.zero;
            if (Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.UpArrow))
                inputDirection.y += 1f;
            if (Input.GetKey(KeyCode.S) || Input.GetKey(KeyCode.DownArrow))
                inputDirection.y -= 1f;
            if (Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow))
                inputDirection.x -= 1f;
            if (Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.RightArrow))
                inputDirection.x += 1f;
            inputDirection = inputDirection.normalized;
            if (useAcceleration)
            {
                if (inputDirection.magnitude > 0f)
                {
                    Vector3 targetVelocity = inputDirection * maxMoveSpeed;
                    currentVelocity = Vector3.MoveTowards(currentVelocity, targetVelocity, acceleration * Time.unscaledDeltaTime);
                }
                else
                {
                    currentVelocity = Vector3.MoveTowards(currentVelocity, Vector3.zero, deceleration * Time.unscaledDeltaTime);
                }
                targetPosition = transform.position + currentVelocity * Time.unscaledDeltaTime;
            }
            else
            {
                Vector3 movement = inputDirection * moveSpeed * Time.unscaledDeltaTime;
                targetPosition = transform.position + movement;
            }
        }
        else
        {
            // In FullView, camera is fixed at (0,0,-10) and WASD is disabled
            targetPosition = new Vector3(0, 0, -10);
        }
    }

    private void ApplyBoundaries()
    {
        targetPosition.x = Mathf.Clamp(targetPosition.x, minX, maxX);
        targetPosition.y = Mathf.Clamp(targetPosition.y, minY, maxY);
        targetPosition.z = Mathf.Clamp(targetPosition.z, minZ, maxZ);
    }

    private void MoveCameraToTarget()
    {
        Vector3 currentPosition = transform.position;

        switch (currentMode)
        {
            case CameraMode.Focus:
                if (smoothFollow)
                {
                    // Smooth follow using fixed lerp factor (frame-rate independent)
                    transform.position = Vector3.Lerp(currentPosition, targetPosition, followSmoothness * Time.deltaTime * 2);
                }
                else
                {
                    // Instant follow
                    transform.position = targetPosition;
                }
                // Apply screen shake
                if (shakeDuration > 0)
                {
                    shakeOffset = Random.insideUnitSphere * shakeDuration;
                    shakeDuration -= Time.deltaTime;
                }
                transform.position += shakeOffset;
                break;

            case CameraMode.Set:
                if (smoothMove)
                {
                    // Smooth move using fixed lerp factor (frame-rate independent)
                    transform.position = Vector3.Lerp(currentPosition, targetPosition, moveSmoothness * Time.deltaTime * 2);
                }
                else
                {
                    // Instant move
                    transform.position = targetPosition;
                }
                // Apply screen shake
                if (shakeDuration > 0)
                {
                    shakeOffset = Random.insideUnitSphere * shakeDuration;
                    shakeDuration -= Time.deltaTime;
                }
                transform.position += shakeOffset;
                break;

            case CameraMode.DirectControl:
                // Direct control uses immediate positioning (targetPosition is already calculated in UpdateDirectControlMode)
                transform.position = targetPosition;
                break;
        }
    }

    private void DisplayDebugInfo()
    {
        string modeInfo = currentMode == CameraMode.DirectControl ?
            $" | Velocity: ({currentVelocity.x:F2}, {currentVelocity.y:F2}, {currentVelocity.z:F2})" :
            "";

        Debug.Log($"Camera Mode: {currentMode} | " +
                 $"Current Pos: ({transform.position.x:F2}, {transform.position.y:F2}, {transform.position.z:F2}) | " +
                 $"Target Pos: ({targetPosition.x:F2}, {targetPosition.y:F2}, {targetPosition.z:F2}) | " +
                 $"Target Object: {(target != null ? target.name : "None")} | " +
                 $"Boundaries: {useBoundaries}{modeInfo}");
    }

    #region Unity Editor Gizmos
    private void OnDrawGizmosSelected()
    {
        if (!showBoundariesGizmos || !useBoundaries)
            return;

        // Draw boundary box
        Gizmos.color = Color.yellow;
        Vector3 center = new Vector3((minX + maxX) * 0.5f, (minY + maxY) * 0.5f, (minZ + maxZ) * 0.5f);
        Vector3 size = new Vector3(maxX - minX, maxY - minY, maxZ - minZ);
        Gizmos.DrawWireCube(center, size);

        // Draw current camera position
        Gizmos.color = Color.red;
        Gizmos.DrawWireSphere(transform.position, 0.5f);

        // Draw target position
        Gizmos.color = Color.green;
        Gizmos.DrawWireSphere(targetPosition, 0.3f);

        // Draw line from camera to target
        Gizmos.color = Color.blue;
        Gizmos.DrawLine(transform.position, targetPosition);

        // Draw focus target if in focus mode
        if (currentMode == CameraMode.Focus && target != null)
        {
            Gizmos.color = Color.magenta;
            Gizmos.DrawWireSphere(target.position, 0.2f);
            Gizmos.DrawLine(target.position, target.position + offset);
        }
    }
    #endregion

    #region Public Methods
    /// <summary>
    /// Switches to Focus mode and sets the target
    /// </summary>
    /// <param name="newTarget">The object to follow</param>
    public void SetFocusMode(Transform newTarget)
    {
        target = newTarget;
        currentMode = CameraMode.Focus;

        if (showDebugInfo)
        {
            Debug.Log($"Camera switched to Focus mode, target: {(newTarget != null ? newTarget.name : "None")}");
        }
    }

    /// <summary>
    /// Switches to Focus mode and sets the target with custom offset
    /// </summary>
    /// <param name="newTarget">The object to follow</param>
    /// <param name="newOffset">Custom offset from target</param>
    public void SetFocusMode(Transform newTarget, Vector3 newOffset)
    {
        target = newTarget;
        offset = newOffset;
        currentMode = CameraMode.Focus;

        if (showDebugInfo)
        {
            Debug.Log($"Camera switched to Focus mode, target: {(newTarget != null ? newTarget.name : "None")}, offset: {newOffset}");
        }
    }

    /// <summary>
    /// Switches to Set mode and moves to specified position
    /// </summary>
    /// <param name="position">The position to move to</param>
    public void SetPositionMode(Vector3 position)
    {
        setPosition = position;
        currentMode = CameraMode.Set;

        if (showDebugInfo)
        {
            Debug.Log($"Camera switched to Set mode, position: {position}");
        }
    }

    /// <summary>
    /// Switches to Direct Control mode for WASD camera movement
    /// </summary>
    public void SetDirectControlMode()
    {
        currentMode = CameraMode.DirectControl;
        currentVelocity = Vector3.zero; // Reset velocity when switching modes

        if (showDebugInfo)
        {
            Debug.Log("Camera switched to Direct Control mode - use WASD to move");
        }
    }

    /// <summary>
    /// Switches to Direct Control mode with custom settings
    /// </summary>
    /// <param name="moveSpeed">Movement speed</param>
    /// <param name="useAcceleration">Whether to use acceleration</param>
    public void SetDirectControlMode(float moveSpeed, bool useAcceleration = true)
    {
        this.moveSpeed = moveSpeed;
        this.useAcceleration = useAcceleration;
        currentMode = CameraMode.DirectControl;
        currentVelocity = Vector3.zero; // Reset velocity when switching modes

        if (showDebugInfo)
        {
            Debug.Log($"Camera switched to Direct Control mode - Speed: {moveSpeed}, Acceleration: {useAcceleration}");
        }
    }

    /// <summary>
    /// Sets camera boundaries
    /// </summary>
    /// <param name="minPos">Minimum position</param>
    /// <param name="maxPos">Maximum position</param>
    public void SetBoundaries(Vector3 minPos, Vector3 maxPos)
    {
        minX = minPos.x;
        minY = minPos.y;
        minZ = minPos.z;
        maxX = maxPos.x;
        maxY = maxPos.y;
        maxZ = maxPos.z;
        useBoundaries = true;

        if (showDebugInfo)
        {
            Debug.Log($"Camera boundaries set: Min({minPos}), Max({maxPos})");
        }
    }

    /// <summary>
    /// Sets camera boundaries for 2D (X and Y only)
    /// </summary>
    /// <param name="minX">Minimum X position</param>
    /// <param name="maxX">Maximum X position</param>
    /// <param name="minY">Minimum Y position</param>
    /// <param name="maxY">Maximum Y position</param>
    public void SetBoundaries2D(float minX, float maxX, float minY, float maxY)
    {
        this.minX = minX;
        this.maxX = maxX;
        this.minY = minY;
        this.maxY = maxY;
        useBoundaries = true;

        if (showDebugInfo)
        {
            Debug.Log($"Camera 2D boundaries set: X({minX} to {maxX}), Y({minY} to {maxY})");
        }
    }

    /// <summary>
    /// Enables or disables camera boundaries
    /// </summary>
    /// <param name="enabled">Whether boundaries should be active</param>
    public void SetBoundariesEnabled(bool enabled)
    {
        useBoundaries = enabled;

        if (showDebugInfo)
        {
            Debug.Log($"Camera boundaries {(enabled ? "enabled" : "disabled")}");
        }
    }

    /// <summary>
    /// Instantly moves camera to target position (no smoothing)
    /// </summary>
    public void SnapToTarget()
    {
        UpdateTargetPosition();
        transform.position = targetPosition;

        if (showDebugInfo)
        {
            Debug.Log($"Camera snapped to target position: {targetPosition}");
        }
    }

    /// <summary>
    /// Gets the current target position the camera is trying to reach
    /// </summary>
    public Vector3 GetTargetPosition()
    {
        return targetPosition;
    }

    /// <summary>
    /// Checks if camera is within specified distance of target
    /// </summary>
    /// <param name="threshold">Distance threshold</param>
    /// <returns>True if camera is close to target</returns>
    public bool IsAtTarget(float threshold = 0.1f)
    {
        return Vector3.Distance(transform.position, targetPosition) <= threshold;
    }

    public void ScreenShake(float duration)
    {
        shakeDuration = duration;
    }
    
    /// <summary>
    /// Performs a cutscene camera movement: moves from current target to a position, waits, then returns to target
    /// Also disables player movement during the cutscene
    /// </summary>
    /// <param name="cutscenePosition">The position to move to</param>
    /// <param name="waitTime">Time to wait at the cutscene position (in seconds)</param>
    /// <param name="moveSpeed">Speed of camera movement (higher = faster, default = 2)</param>
    public void PlayCutsceneCamera(Vector3 cutscenePosition, float waitTime, float moveSpeed = 2f)
    {
        if (isCutsceneActive)
        {
            if (showDebugInfo)
            {
                Debug.LogWarning("Cutscene camera already active, ignoring new request");
            }
            return;
        }
        
        StartCoroutine(CutsceneCameraCoroutine(cutscenePosition, waitTime, moveSpeed));
    }
    
    /// <summary>
    /// Coroutine that handles the cutscene camera movement sequence
    /// </summary>
    private System.Collections.IEnumerator CutsceneCameraCoroutine(Vector3 cutscenePosition, float waitTime, float moveSpeed)
    {
        isCutsceneActive = true;
        
        // Save current camera state
        savedMode = currentMode;
        savedTarget = target;
        savedOffset = offset;
        
        // Disable player movement during cutscene
        PlayerController playerController = null;
        if (savedTarget != null)
        {
            playerController = savedTarget.GetComponent<PlayerController>();
        }
        
        // Calculate total cutscene duration
        Vector3 startPosition = transform.position;
        if (savedMode == CameraMode.Focus && savedTarget != null)
        {
            startPosition = savedTarget.position + savedOffset;
        }
        float moveDistance = Vector3.Distance(startPosition, cutscenePosition);
        float moveToDuration = moveDistance / moveSpeed;
        float returnDistance = Vector3.Distance(cutscenePosition, startPosition);
        float returnToDuration = returnDistance / moveSpeed;
        float totalDuration = moveToDuration + waitTime + returnToDuration;
        
        // Set player to dummy state for entire cutscene duration
        if (playerController != null)
        {
            playerController.SetDummyState(totalDuration);
        }
        
        if (showDebugInfo)
        {
            Debug.Log($"Starting cutscene camera: Moving to {cutscenePosition}, wait {waitTime}s, speed {moveSpeed}, total duration {totalDuration}s");
        }
        
        // Move from target to cutscene position
        float elapsedTime = 0f;
        
        while (elapsedTime < moveToDuration)
        {
            elapsedTime += Time.deltaTime;
            float t = elapsedTime / moveToDuration;
            
            // Use smooth interpolation
            targetPosition = Vector3.Lerp(startPosition, cutscenePosition, t);
            transform.position = targetPosition;
            
            yield return null;
        }
        
        // Ensure we're exactly at cutscene position
        targetPosition = cutscenePosition;
        transform.position = cutscenePosition;
        
        if (showDebugInfo)
        {
            Debug.Log($"Reached cutscene position, waiting {waitTime} seconds");
        }
        
        // Wait at cutscene position
        yield return new WaitForSeconds(waitTime);
        
        if (showDebugInfo)
        {
            Debug.Log("Returning camera to target");
        }
        
        // Move back to target
        startPosition = transform.position;
        Vector3 returnPosition = savedTarget != null ? savedTarget.position + savedOffset : startPosition;
        elapsedTime = 0f;
        
        while (elapsedTime < returnToDuration)
        {
            elapsedTime += Time.deltaTime;
            float t = elapsedTime / returnToDuration;
            
            // Update return position in real-time if target is moving
            if (savedTarget != null)
            {
                returnPosition = savedTarget.position + savedOffset;
            }
            
            targetPosition = Vector3.Lerp(startPosition, returnPosition, t);
            transform.position = targetPosition;
            
            yield return null;
        }
        
        // Restore camera state
        currentMode = savedMode;
        target = savedTarget;
        offset = savedOffset;
        isCutsceneActive = false;
        
        if (showDebugInfo)
        {
            Debug.Log("Cutscene camera complete, resumed normal operation");
        }
    }
    #endregion
}
