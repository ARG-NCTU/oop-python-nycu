using System.Collections;
using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// GameManager - Core singleton class for managing game-wide functionality
/// Handles time control, frame rate management, and scene loading
/// </summary>
public class GameManager : MonoBehaviour
{
    #region Singleton
    private static GameManager _instance;
    public static GameManager Instance
    {
        get
        {
            if (_instance == null)
            {
                _instance = FindObjectOfType<GameManager>();
                if (_instance == null)
                {
                    GameObject gameManagerObject = new GameObject("GameManager");
                    _instance = gameManagerObject.AddComponent<GameManager>();
                    DontDestroyOnLoad(gameManagerObject);
                }
            }
            return _instance;
        }
    }
    #endregion

    #region Time and Frame Rate Control
    [Header("Frame Rate Settings")]
    [SerializeField] private int targetFrameRate = 60;
    [SerializeField] private bool vSyncEnabled = true;
    
    [Header("Time Control")]
    [SerializeField] private float timeScale = 1.0f;
    [SerializeField] private bool isPaused = false;
    
    // Properties for external access
    public int TargetFrameRate 
    { 
        get => targetFrameRate; 
        set => SetTargetFrameRate(value); 
    }
    
    public bool VSyncEnabled 
    { 
        get => vSyncEnabled; 
        set => SetVSync(value); 
    }
    
    public float TimeScale 
    { 
        get => timeScale; 
        set => SetTimeScale(value); 
    }
    
    public bool IsPaused 
    { 
        get => isPaused; 
        set => SetPauseState(value); 
    }
    #endregion

    #region Scene Loading
    [Header("Scene Management")]
    [SerializeField] private bool useLoadingScreen = false;
    [SerializeField] private string loadingSceneName = "LoadingScene";
    
    // Events for scene loading
    public System.Action<string> OnSceneLoadStarted;
    public System.Action<string> OnSceneLoadCompleted;
    public System.Action<float> OnSceneLoadProgress;
    #endregion

    #region Unity Lifecycle
    private void Awake()
    {
        // Ensure singleton pattern
        if (_instance == null)
        {
            _instance = this;
            DontDestroyOnLoad(gameObject);
            InitializeGameManager();
        }
        else if (_instance != this)
        {
            Destroy(gameObject);
        }
    }

    private void Start()
    {
        ApplyFrameRateSettings();
    }

    private void OnValidate()
    {
        // Apply changes made in inspector during runtime
        if (Application.isPlaying)
        {
            ApplyFrameRateSettings();
            ApplyTimeScale();
        }
    }
    #endregion

    #region Initialization
    private void InitializeGameManager()
    {
        Debug.Log("GameManager initialized");
    }
    #endregion

    #region Frame Rate Control Methods
    /// <summary>
    /// Sets the target frame rate for the game
    /// </summary>
    /// <param name="fps">Target frames per second</param>
    public void SetTargetFrameRate(int fps)
    {
        targetFrameRate = Mathf.Clamp(fps, 1, 300);
        ApplyFrameRateSettings();
        Debug.Log($"Target frame rate set to: {targetFrameRate} FPS");
    }

    /// <summary>
    /// Enables or disables VSync
    /// </summary>
    /// <param name="enabled">VSync state</param>
    public void SetVSync(bool enabled)
    {
        vSyncEnabled = enabled;
        ApplyFrameRateSettings();
        Debug.Log($"VSync {(enabled ? "enabled" : "disabled")}");
    }

    private void ApplyFrameRateSettings()
    {
        if (vSyncEnabled)
        {
            QualitySettings.vSyncCount = 1;
            Application.targetFrameRate = -1;
        }
        else
        {
            QualitySettings.vSyncCount = 0;
            Application.targetFrameRate = targetFrameRate;
        }
    }
    #endregion

    #region Time Control Methods
    /// <summary>
    /// Sets the time scale for the game
    /// </summary>
    /// <param name="scale">Time scale multiplier (1.0 = normal speed)</param>
    public void SetTimeScale(float scale)
    {
        timeScale = Mathf.Clamp(scale, 0f, 10f);
        ApplyTimeScale();
        Debug.Log($"Time scale set to: {timeScale}");
    }

    /// <summary>
    /// Pauses or unpauses the game
    /// </summary>
    /// <param name="paused">Pause state</param>
    public void SetPauseState(bool paused)
    {
        isPaused = paused;
        ApplyTimeScale();
        Debug.Log($"Game {(paused ? "paused" : "unpaused")}");
    }

    /// <summary>
    /// Toggles pause state
    /// </summary>
    public void TogglePause()
    {
        SetPauseState(!isPaused);
    }

    /// <summary>
    /// Speeds up the game temporarily
    /// </summary>
    /// <param name="multiplier">Speed multiplier</param>
    /// <param name="duration">Duration in seconds</param>
    public void SpeedUpGame(float multiplier, float duration)
    {
        StartCoroutine(TemporaryTimeScaleChange(multiplier, duration));
    }

    /// <summary>
    /// Slows down the game temporarily
    /// </summary>
    /// <param name="multiplier">Slow multiplier (0.5 = half speed)</param>
    /// <param name="duration">Duration in seconds</param>
    public void SlowDownGame(float multiplier, float duration)
    {
        StartCoroutine(TemporaryTimeScaleChange(multiplier, duration));
    }

    private void ApplyTimeScale()
    {
        Time.timeScale = isPaused ? 0f : timeScale;
    }

    private IEnumerator TemporaryTimeScaleChange(float multiplier, float duration)
    {
        float originalTimeScale = timeScale;
        SetTimeScale(multiplier);
        
        yield return new WaitForSecondsRealtime(duration);
        
        SetTimeScale(originalTimeScale);
    }
    #endregion

    #region Scene Loading Methods
    /// <summary>
    /// Loads a scene by name
    /// </summary>
    /// <param name="sceneName">Name of the scene to load</param>
    public void LoadScene(string sceneName)
    {
        if (string.IsNullOrEmpty(sceneName))
        {
            Debug.LogError("Scene name cannot be null or empty!");
            return;
        }

        if (useLoadingScreen && !string.IsNullOrEmpty(loadingSceneName))
        {
            StartCoroutine(LoadSceneWithLoadingScreen(sceneName));
        }
        else
        {
            StartCoroutine(LoadSceneAsync(sceneName));
        }
    }

    /// <summary>
    /// Loads the next scene in build order
    /// </summary>
    public void LoadNextScene()
    {
        int currentSceneIndex = SceneManager.GetActiveScene().buildIndex;
        int nextSceneIndex = (currentSceneIndex + 1) % SceneManager.sceneCountInBuildSettings;
        
        if (nextSceneIndex < SceneManager.sceneCountInBuildSettings)
        {
            StartCoroutine(LoadSceneAsync(nextSceneIndex));
        }
        else
        {
            Debug.LogWarning("No next scene available!");
        }
    }

    /// <summary>
    /// Loads the previous scene in build order
    /// </summary>
    public void LoadPreviousScene()
    {
        int currentSceneIndex = SceneManager.GetActiveScene().buildIndex;
        int previousSceneIndex = currentSceneIndex - 1;
        
        if (previousSceneIndex >= 0)
        {
            StartCoroutine(LoadSceneAsync(previousSceneIndex));
        }
        else
        {
            Debug.LogWarning("No previous scene available!");
        }
    }

    /// <summary>
    /// Reloads the current scene
    /// </summary>
    public void ReloadCurrentScene()
    {
        string currentSceneName = SceneManager.GetActiveScene().name;
        LoadScene(currentSceneName);
    }

    /// <summary>
    /// Quits the application
    /// </summary>
    public void QuitGame()
    {
        Debug.Log("Quitting game...");
        
        #if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
        #else
        Application.Quit();
        #endif
    }

    private IEnumerator LoadSceneAsync(string sceneName)
    {
        OnSceneLoadStarted?.Invoke(sceneName);
        
        AsyncOperation asyncLoad = SceneManager.LoadSceneAsync(sceneName);
        asyncLoad.allowSceneActivation = false;

        while (!asyncLoad.isDone)
        {
            float progress = Mathf.Clamp01(asyncLoad.progress / 0.9f);
            OnSceneLoadProgress?.Invoke(progress);

            if (asyncLoad.progress >= 0.9f)
            {
                asyncLoad.allowSceneActivation = true;
            }

            yield return null;
        }

        OnSceneLoadCompleted?.Invoke(sceneName);
        Debug.Log($"Scene '{sceneName}' loaded successfully");
    }

    private IEnumerator LoadSceneAsync(int sceneIndex)
    {
        string sceneName = $"Scene Index {sceneIndex}";
        OnSceneLoadStarted?.Invoke(sceneName);
        
        AsyncOperation asyncLoad = SceneManager.LoadSceneAsync(sceneIndex);
        asyncLoad.allowSceneActivation = false;

        while (!asyncLoad.isDone)
        {
            float progress = Mathf.Clamp01(asyncLoad.progress / 0.9f);
            OnSceneLoadProgress?.Invoke(progress);

            if (asyncLoad.progress >= 0.9f)
            {
                asyncLoad.allowSceneActivation = true;
            }

            yield return null;
        }

        OnSceneLoadCompleted?.Invoke(sceneName);
        Debug.Log($"Scene index '{sceneIndex}' loaded successfully");
    }

    private IEnumerator LoadSceneWithLoadingScreen(string targetSceneName)
    {
        // Load loading screen first
        yield return StartCoroutine(LoadSceneAsync(loadingSceneName));
        
        // Wait a frame for loading screen to initialize
        yield return null;
        
        // Load target scene
        yield return StartCoroutine(LoadSceneAsync(targetSceneName));
    }
    #endregion

    #region Public Utility Methods
    /// <summary>
    /// Gets the current FPS
    /// </summary>
    /// <returns>Current frames per second</returns>
    public float GetCurrentFPS()
    {
        return 1.0f / Time.unscaledDeltaTime;
    }

    /// <summary>
    /// Checks if a scene exists in build settings
    /// </summary>
    /// <param name="sceneName">Scene name to check</param>
    /// <returns>True if scene exists</returns>
    public bool SceneExists(string sceneName)
    {
        for (int i = 0; i < SceneManager.sceneCountInBuildSettings; i++)
        {
            string scenePath = SceneUtility.GetScenePathByBuildIndex(i);
            string sceneNameFromPath = System.IO.Path.GetFileNameWithoutExtension(scenePath);
            if (sceneNameFromPath == sceneName)
            {
                return true;
            }
        }
        return false;
    }
    #endregion
}
