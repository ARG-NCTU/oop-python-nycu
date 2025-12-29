using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Advanced dialogue trigger for NPCs or objects with multiple interaction types
/// Place this on any GameObject to make it start dialogue when player approaches
/// </summary>
public class DialogueTrigger : MonoBehaviour
{
    public enum TriggerType
    {
        TriggerOnce,        // Auto-trigger once only
        TriggerRepeat,      // Auto-trigger every time player enters
        NPCOnce,           // Requires input, triggers once only
        NPCOnceAndRepeat,  // Requires input, first dialogue once, then repeat dialogue
        NPCOnceAndRandom   // Requires input, first dialogue once, then random from pool
    }

    [Header("Trigger Type")]
    [SerializeField] private TriggerType triggerType = TriggerType.NPCOnce;
    
    [Header("Input Settings")]
    [SerializeField] private KeyCode interactionKey = KeyCode.UpArrow;
    [SerializeField] private string xboxInteractionButton = "Fire3"; // Xbox D-Pad Up
    
    [Header("Persistence Settings")]
    [SerializeField] private string uniqueTriggerID = ""; // Unique ID for saving state across scenes
    
    [Header("Simple Dialogue (TriggerOnce, TriggerRepeat, NPCOnce)")]
    [SerializeField] private string dialogueSetName = "NPC Dialogue";
    [SerializeField] private bool useDialogueIndex = false;
    [SerializeField] private int dialogueSetIndex = 0;
    
    [Header("Multi-Dialogue (NPCOnceAndRepeat)")]
    [SerializeField] private string firstDialogueSetName = "";
    [SerializeField] private string repeatDialogueSetName = "";
    
    [Header("Random Dialogue (NPCOnceAndRandom)")]
    [SerializeField] private string firstRandomDialogueSetName = "";
    [SerializeField] private List<string> randomDialogueSetNames = new List<string>();
    
    [Header("UI (Optional)")]
    [SerializeField] private GameObject interactionPrompt; // "Press E to talk" UI
    
    private DialogueManager dialogueManager;
    private bool playerInRange = false;
    private bool hasTriggered = false;
    private bool hasFirstInteraction = false;
    
    private void Start()
    {
        // Generate unique ID if not set
        if (string.IsNullOrEmpty(uniqueTriggerID))
        {
            uniqueTriggerID = $"{UnityEngine.SceneManagement.SceneManager.GetActiveScene().name}_{gameObject.name}_{transform.position.x}_{transform.position.y}";
        }
        
        // Load persistent state
        LoadPersistentState();
        
        // Find DialogueManager in scene
        dialogueManager = FindObjectOfType<DialogueManager>();
        
        if (dialogueManager == null)
        {
            Debug.LogError($"DialogueTrigger on {gameObject.name}: No DialogueManager found in scene!");
        }
        
        // Hide interaction prompt initially
        if (interactionPrompt != null)
        {
            interactionPrompt.SetActive(false);
        }
    }
    
    private void Update()
    {
        // Handle player input when in range for NPC types
        if (playerInRange && RequiresPlayerInput())
        {
            bool canTrigger = CanTriggerDialogue();
            
            if (canTrigger && (Input.GetKeyDown(interactionKey) || Input.GetButtonDown(xboxInteractionButton)))
            {
                StartDialogue();
            }
        }
    }
    
    private void OnTriggerEnter2D(Collider2D other)
    {
        // Check if player entered trigger
        if (other.CompareTag("Player"))
        {
            playerInRange = true;
            
            // Show interaction prompt for NPC types
            if (interactionPrompt != null && RequiresPlayerInput() && CanTriggerDialogue())
            {
                interactionPrompt.SetActive(true);
            }
            
            // Auto-start dialogue for trigger types
            if (!RequiresPlayerInput() && CanTriggerDialogue())
            {
                StartDialogue();
            }
        }
    }
    
    private void OnTriggerExit2D(Collider2D other)
    {
        // Check if player left trigger
        if (other.CompareTag("Player"))
        {
            playerInRange = false;
            
            // Hide interaction prompt
            if (interactionPrompt != null)
            {
                interactionPrompt.SetActive(false);
            }
        }
    }
    
    private void StartDialogue()
    {
        if (dialogueManager == null) return;
        if (dialogueManager.IsDialogueActive) return; // Don't interrupt active dialogue
        if (!CanTriggerDialogue()) return;
        
        string dialogueToStart = GetDialogueToStart();
        
        if (string.IsNullOrEmpty(dialogueToStart))
        {
            Debug.LogWarning($"DialogueTrigger on {gameObject.name}: No dialogue set name specified!");
            return;
        }
        
        // Start the appropriate dialogue
        if (triggerType == TriggerType.TriggerOnce || triggerType == TriggerType.NPCOnce)
        {
            // Use simple dialogue settings for these types
            if (useDialogueIndex)
            {
                dialogueManager.StartDialogue(dialogueSetIndex);
            }
            else
            {
                dialogueManager.StartDialogue(dialogueToStart);
            }
        }
        else
        {
            // Use dialogue name for multi-dialogue types
            dialogueManager.StartDialogue(dialogueToStart);
        }
        
        // Update trigger states
        UpdateTriggerState();
        
        Debug.Log($"Started dialogue: {dialogueToStart} (Type: {triggerType})");
    }
    
    /// <summary>
    /// Manually trigger dialogue (for buttons, events, etc.)
    /// </summary>
    public void TriggerDialogue()
    {
        if (playerInRange || !RequiresPlayerInput())
        {
            StartDialogue();
        }
    }
    
    /// <summary>
    /// Reset the trigger so it can be used again
    /// </summary>
    public void ResetTrigger()
    {
        hasTriggered = false;
        hasFirstInteraction = false;
        SavePersistentState();
    }
    
    /// <summary>
    /// Load persistent state from DialogueStateManager
    /// </summary>
    private void LoadPersistentState()
    {
        if (string.IsNullOrEmpty(uniqueTriggerID)) return;
        
        var state = DialogueStateManager.Instance.GetDialogueState(uniqueTriggerID);
        hasTriggered = state.hasTriggered;
        hasFirstInteraction = state.hasFirstInteraction;
    }
    
    /// <summary>
    /// Save persistent state to DialogueStateManager
    /// </summary>
    private void SavePersistentState()
    {
        if (string.IsNullOrEmpty(uniqueTriggerID)) return;
        
        DialogueStateManager.Instance.UpdateDialogueState(uniqueTriggerID, hasTriggered, hasFirstInteraction);
    }
    
    /// <summary>
    /// Set a custom unique ID for this trigger (useful for scripted setup)
    /// </summary>
    public void SetUniqueTriggerID(string customID)
    {
        uniqueTriggerID = customID;
        LoadPersistentState(); // Reload state with new ID
    }
    
    /// <summary>
    /// Check if this trigger type requires player input
    /// </summary>
    private bool RequiresPlayerInput()
    {
        return triggerType == TriggerType.NPCOnce || 
               triggerType == TriggerType.NPCOnceAndRepeat || 
               triggerType == TriggerType.NPCOnceAndRandom;
    }
    
    /// <summary>
    /// Check if dialogue can be triggered based on current state and type
    /// </summary>
    private bool CanTriggerDialogue()
    {
        switch (triggerType)
        {
            case TriggerType.TriggerOnce:
                return !hasTriggered;
            
            case TriggerType.TriggerRepeat:
                return true; // Always can trigger
            
            case TriggerType.NPCOnce:
                return !hasTriggered;
            
            case TriggerType.NPCOnceAndRepeat:
            case TriggerType.NPCOnceAndRandom:
                return true; // Always can trigger, but dialogue content changes
            
            default:
                return false;
        }
    }
    
    /// <summary>
    /// Get the dialogue set name to start based on trigger type and current state
    /// </summary>
    private string GetDialogueToStart()
    {
        switch (triggerType)
        {
            case TriggerType.TriggerOnce:
            case TriggerType.TriggerRepeat:
            case TriggerType.NPCOnce:
                return dialogueSetName;
            
            case TriggerType.NPCOnceAndRepeat:
                return !hasFirstInteraction ? firstDialogueSetName : repeatDialogueSetName;
            
            case TriggerType.NPCOnceAndRandom:
                if (!hasFirstInteraction)
                {
                    return firstRandomDialogueSetName;
                }
                else if (randomDialogueSetNames.Count > 0)
                {
                    int randomIndex = Random.Range(0, randomDialogueSetNames.Count);
                    return randomDialogueSetNames[randomIndex];
                }
                else
                {
                    Debug.LogWarning($"DialogueTrigger on {gameObject.name}: No random dialogue sets defined!");
                    return firstRandomDialogueSetName; // Fallback to first dialogue
                }
            
            default:
                return dialogueSetName;
        }
    }
    
    /// <summary>
    /// Update trigger states after dialogue starts
    /// </summary>
    private void UpdateTriggerState()
    {
        switch (triggerType)
        {
            case TriggerType.TriggerOnce:
            case TriggerType.NPCOnce:
                hasTriggered = true;
                // Hide interaction prompt permanently for these types
                if (interactionPrompt != null)
                {
                    interactionPrompt.SetActive(false);
                }
                break;
            
            case TriggerType.NPCOnceAndRepeat:
            case TriggerType.NPCOnceAndRandom:
                hasFirstInteraction = true;
                break;
            
            case TriggerType.TriggerRepeat:
                // No state change needed - always repeats
                break;
        }
        
        // Save persistent state
        SavePersistentState();
    }
    
    /// <summary>
    /// Get info about current trigger state (for debugging)
    /// </summary>
    public string GetTriggerInfo()
    {
        return $"Type: {triggerType}, ID: {uniqueTriggerID}, HasTriggered: {hasTriggered}, HasFirstInteraction: {hasFirstInteraction}, PlayerInRange: {playerInRange}";
    }

}