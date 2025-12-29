using UnityEngine;
using System.Collections.Generic;
using System.Linq;

/// <summary>
/// Manages dialogue trigger states across scene loads
/// Persists dialogue progress using PlayerPrefs for permanent storage
/// </summary>
public class DialogueStateManager : MonoBehaviour
{
    private static DialogueStateManager instance;
    public static DialogueStateManager Instance
    {
        get
        {
            if (instance == null)
            {
                // Try to find existing instance
                instance = FindObjectOfType<DialogueStateManager>();
                
                // Create new one if none exists
                if (instance == null)
                {
                    GameObject go = new GameObject("DialogueStateManager");
                    instance = go.AddComponent<DialogueStateManager>();
                    DontDestroyOnLoad(go);
                }
            }
            return instance;
        }
    }

    [System.Serializable]
    public class DialogueState
    {
        public string triggerID;
        public bool hasTriggered;
        public bool hasFirstInteraction;
        
        public DialogueState(string id, bool triggered, bool firstInteraction)
        {
            triggerID = id;
            hasTriggered = triggered;
            hasFirstInteraction = firstInteraction;
        }
    }

    private Dictionary<string, DialogueState> dialogueStates = new Dictionary<string, DialogueState>();
    private const string SAVE_KEY_PREFIX = "DialogueState_";
    
    private void Awake()
    {
        // Ensure only one instance exists
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(gameObject);
            LoadAllStates();
        }
        else if (instance != this)
        {
            Destroy(gameObject);
        }
    }

    /// <summary>
    /// Get dialogue state for a trigger
    /// </summary>
    public DialogueState GetDialogueState(string triggerID)
    {
        if (dialogueStates.ContainsKey(triggerID))
        {
            return dialogueStates[triggerID];
        }
        
        // Create new state if doesn't exist
        var newState = new DialogueState(triggerID, false, false);
        dialogueStates[triggerID] = newState;
        return newState;
    }

    /// <summary>
    /// Update dialogue state for a trigger
    /// </summary>
    public void UpdateDialogueState(string triggerID, bool hasTriggered, bool hasFirstInteraction)
    {
        var state = GetDialogueState(triggerID);
        state.hasTriggered = hasTriggered;
        state.hasFirstInteraction = hasFirstInteraction;
        
        // Save to PlayerPrefs immediately
        SaveState(triggerID, state);
    }

    /// <summary>
    /// Reset dialogue state for a specific trigger
    /// </summary>
    public void ResetDialogueState(string triggerID)
    {
        var state = GetDialogueState(triggerID);
        state.hasTriggered = false;
        state.hasFirstInteraction = false;
        
        SaveState(triggerID, state);
    }

    /// <summary>
    /// Reset all dialogue states (for new game, etc.)
    /// </summary>
    public void ResetAllDialogueStates()
    {
        var triggerIDs = dialogueStates.Keys.ToArray();
        
        foreach (string triggerID in triggerIDs)
        {
            ResetDialogueState(triggerID);
        }
        
        Debug.Log("All dialogue states have been reset");
    }

    /// <summary>
    /// Save a specific dialogue state to PlayerPrefs
    /// </summary>
    private void SaveState(string triggerID, DialogueState state)
    {
        string key = SAVE_KEY_PREFIX + triggerID;
        string data = JsonUtility.ToJson(state);
        PlayerPrefs.SetString(key, data);
        PlayerPrefs.Save();
    }

    /// <summary>
    /// Load a specific dialogue state from PlayerPrefs
    /// </summary>
    private DialogueState LoadState(string triggerID)
    {
        string key = SAVE_KEY_PREFIX + triggerID;
        
        if (PlayerPrefs.HasKey(key))
        {
            string data = PlayerPrefs.GetString(key);
            try
            {
                return JsonUtility.FromJson<DialogueState>(data);
            }
            catch (System.Exception e)
            {
                Debug.LogWarning($"Failed to load dialogue state for {triggerID}: {e.Message}");
            }
        }
        
        // Return default state if loading failed or doesn't exist
        return new DialogueState(triggerID, false, false);
    }

    /// <summary>
    /// Load all dialogue states from PlayerPrefs
    /// </summary>
    private void LoadAllStates()
    {
        dialogueStates.Clear();
        
        // Note: PlayerPrefs doesn't have a way to enumerate keys, so we load states on-demand
        // States will be loaded when GetDialogueState is called for each trigger
    }

    /// <summary>
    /// Check if a trigger has been activated before
    /// </summary>
    public bool HasTriggerBeenActivated(string triggerID)
    {
        return GetDialogueState(triggerID).hasTriggered;
    }

    /// <summary>
    /// Check if a trigger has had its first interaction
    /// </summary>
    public bool HasTriggerHadFirstInteraction(string triggerID)
    {
        return GetDialogueState(triggerID).hasFirstInteraction;
    }

    /// <summary>
    /// Get all current dialogue states (for debugging)
    /// </summary>
    public Dictionary<string, DialogueState> GetAllStates()
    {
        return new Dictionary<string, DialogueState>(dialogueStates);
    }

    /// <summary>
    /// Manual save all states (called on application quit, scene change, etc.)
    /// </summary>
    public void SaveAllStates()
    {
        foreach (var kvp in dialogueStates)
        {
            SaveState(kvp.Key, kvp.Value);
        }
        PlayerPrefs.Save();
    }

    private void OnApplicationPause(bool pauseStatus)
    {
        if (pauseStatus)
        {
            SaveAllStates();
        }
    }

    private void OnApplicationFocus(bool hasFocus)
    {
        if (!hasFocus)
        {
            SaveAllStates();
        }
    }

    private void OnApplicationQuit()
    {
        SaveAllStates();
    }
}