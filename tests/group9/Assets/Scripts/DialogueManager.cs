using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// Dialogue Manager for handling conversation systems
/// Supports multiple dialogue sets, character switching, and various input methods
/// </summary>
public class DialogueManager : MonoBehaviour
{
    [System.Serializable]
    public class DialogueLine
    {
        [Header("Dialogue Content")]
        [TextArea(2, 4)]
        public string text;
        
        [Header("Speaker")]
        public Speaker speaker = Speaker.Left;
        
        [Header("Image Settings")]
        [Tooltip("Index of the speaker image to use (0 = first image)")]
        public int speakerImageIndex = 0;
        [Tooltip("Index of the dialogue box to use (0 = first box, -1 = use default)")]
        public int boxImageIndex = -1;
        
        [Header("Audio (Optional)")]
        [Tooltip("Sound to play when this line appears")]
        public AudioClip dialogueSound;
        [Range(0f, 1f)]
        public float soundVolume = 1f;
        
        [Header("Timing (Optional)")]
        public float displayDelay = 0f; // Delay before showing this line
    }

    [System.Serializable]
    public class DialogueSet
    {
        [Header("Set Information")]
        public string setName = "Dialogue Set";
        public bool CallEvent = false;
        public int EventID = 0;
        
        [Header("Dialogue Lines")]
        public List<DialogueLine> dialogueLines = new List<DialogueLine>();
        
        [Header("Auto Settings")]
        public bool autoClose = true; // Close panel when set finishes
    }

    public enum Speaker
    {
        Left,
        Right,
        None // For narrator or when no character should be highlighted
    }

    [Header("UI References")]
    [SerializeField] private GameObject dialogueSystemPanel;
    [SerializeField] private List<GameObject> boxImages = new List<GameObject>();
    [SerializeField] private List<GameObject> leftImages = new List<GameObject>();
    [SerializeField] private List<GameObject> rightImages = new List<GameObject>();
    [SerializeField] private Text dialogueText;
    
    [Header("Audio Settings")]
    [SerializeField] private AudioSource audioSource;
    
    [Header("Dialogue Sets")]
    [SerializeField] private List<DialogueSet> dialogueSets = new List<DialogueSet>();
    [SerializeField] private DialogueTriggerEvent dialogueTriggerEvent;
    
    [Header("Input Settings")]
    [SerializeField] private KeyCode continueKey1 = KeyCode.Space;
    [SerializeField] private KeyCode continueKey2 = KeyCode.Return;
    [SerializeField] private string xboxContinueButton = "Fire1"; // A button
    [SerializeField] private bool allowMouseClick = true;
    
    [Header("Display Settings")]
    [SerializeField] private float textSpeed = 0.05f; // Time between characters for typewriter effect
    [SerializeField] private bool useTypewriterEffect = true;
    [SerializeField] private bool canSkipTypewriter = true;
    
    [Header("Debug")]
    [SerializeField] private bool showDebugInfo = false;
    
    [Header("Inspector Testing")]
    [SerializeField] private int testDialogueSetIndex = 0;
    [SerializeField] private bool testByName = false;
    [SerializeField] private string testDialogueSetName = "";
    
    // Private variables
    private int currentSetIndex = 0;
    private int currentLineIndex = 0;
    private bool isDialogueActive = false;
    private bool isTyping = false;
    private Coroutine typingCoroutine;
    private DialogueSet currentSet;
    
    // Events (optional - for other scripts to listen to)
    public System.Action OnDialogueStart;
    public System.Action OnDialogueEnd;
    public System.Action<int> OnDialogueSetComplete; // Passes set index
    public System.Action<DialogueLine> OnDialogueLineStart; // Passes current line
    
    // Properties for external access
    public bool IsDialogueActive => isDialogueActive;
    public bool IsTyping => isTyping;
    public int CurrentSetIndex => currentSetIndex;
    public int CurrentLineIndex => currentLineIndex;
    public DialogueSet CurrentSet => currentSet;
    
    private void Awake()
    {
        // Ensure dialogue system starts hidden
        if (dialogueSystemPanel != null)
        {
            dialogueSystemPanel.SetActive(false);
        }
        
        // Validate references
        ValidateReferences();
    }

    private void Update()
    {
        if (isDialogueActive)
        {
            HandleInput();
        }
    }

    private void ValidateReferences()
    {
        if (dialogueSystemPanel == null)
            Debug.LogError("DialogueManager: DialogueSystemPanel is not assigned!");
        
        if (boxImages.Count == 0)
            Debug.LogWarning("DialogueManager: No box images assigned! Add at least one box image.");
        
        if (leftImages.Count == 0)
            Debug.LogWarning("DialogueManager: No left images assigned!");
        
        if (rightImages.Count == 0)
            Debug.LogWarning("DialogueManager: No right images assigned!");
        
        if (dialogueText == null)
            Debug.LogError("DialogueManager: DialogueText is not assigned!");
        
        if (audioSource == null)
            Debug.LogWarning("DialogueManager: AudioSource is not assigned. Dialogue sounds will not play.");
    }

    private void HandleInput()
    {
        bool continuePressed = false;
        
        // Check keyboard input
        if (Input.GetKeyDown(continueKey1) || Input.GetKeyDown(continueKey2))
        {
            continuePressed = true;
        }
        
        // Check Xbox controller input
        if (Input.GetButtonDown(xboxContinueButton))
        {
            continuePressed = true;
        }
        
        // Check mouse input
        if (allowMouseClick && Input.GetMouseButtonDown(0))
        {
            continuePressed = true;
        }
        
        if (continuePressed)
        {
            if (isTyping && canSkipTypewriter)
            {
                // Skip typewriter effect
                SkipTypewriter();
            }
            else if (!isTyping)
            {
                // Continue to next line
                ContinueDialogue();
            }
        }
    }

    private void SkipTypewriter()
    {
        if (typingCoroutine != null)
        {
            StopCoroutine(typingCoroutine);
        }
        
        isTyping = false;
        
        // Show complete text immediately
        if (currentSet != null && currentLineIndex < currentSet.dialogueLines.Count)
        {
            dialogueText.text = currentSet.dialogueLines[currentLineIndex].text;
        }
    }

    private void ContinueDialogue()
    {
        currentLineIndex++;
        
        if (currentSet != null && currentLineIndex < currentSet.dialogueLines.Count)
        {
            // Show next line
            DisplayLine(currentSet.dialogueLines[currentLineIndex]);
        }
        else
        {
            // End of current set
            EndDialogueSet(currentSet.CallEvent, currentSet.EventID);
        }
    }

    private void DisplayLine(DialogueLine line)
    {
        if (showDebugInfo)
        {
            Debug.Log($"Displaying line {currentLineIndex}: {line.text}");
        }
        
        // Set speaker images with index
        SetSpeakerImages(line.speaker, line.speakerImageIndex);

        int boxIndex = currentSet.dialogueLines[currentLineIndex].boxImageIndex;
        SetBoxImage(boxIndex);
        
        // Play dialogue sound if provided
        if (line.dialogueSound != null && audioSource != null)
        {
            audioSource.PlayOneShot(line.dialogueSound, line.soundVolume);
        }
        
        // Trigger event
        OnDialogueLineStart?.Invoke(line);
        
        // Start displaying text
        if (useTypewriterEffect && !string.IsNullOrEmpty(line.text))
        {
            StartCoroutine(DisplayLineWithDelay(line));
        }
        else
        {
            dialogueText.text = line.text;
        }
    }

    private IEnumerator DisplayLineWithDelay(DialogueLine line)
    {
        // Wait for display delay if specified
        if (line.displayDelay > 0)
        {
            yield return new WaitForSeconds(line.displayDelay);
        }
        
        // Start typewriter effect
        if (typingCoroutine != null)
        {
            StopCoroutine(typingCoroutine);
        }
        
        typingCoroutine = StartCoroutine(TypewriterEffect(line.text));
    }

    private IEnumerator TypewriterEffect(string text)
    {
        isTyping = true;
        dialogueText.text = "";
        
        for (int i = 0; i < text.Length; i++)
        {
            dialogueText.text += text[i];
            yield return new WaitForSeconds(textSpeed);
        }
        
        isTyping = false;
    }

    private void SetSpeakerImages(Speaker speaker, int imageIndex = 0)
    {
        // Deactivate all speaker images first
        foreach (GameObject img in leftImages)
        {
            if (img != null) img.SetActive(false);
        }
        foreach (GameObject img in rightImages)
        {
            if (img != null) img.SetActive(false);
        }
        
        // Activate the appropriate image based on speaker
        switch (speaker)
        {
            case Speaker.Left:
                if (imageIndex >= 0 && imageIndex < leftImages.Count && leftImages[imageIndex] != null)
                {
                    leftImages[imageIndex].SetActive(true);
                }
                else if (leftImages.Count > 0 && leftImages[0] != null)
                {
                    leftImages[0].SetActive(true); // Fallback to first image
                    if (showDebugInfo)
                    {
                        Debug.LogWarning($"Left image index {imageIndex} out of range, using default");
                    }
                }
                break;
            case Speaker.Right:
                if (imageIndex >= 0 && imageIndex < rightImages.Count && rightImages[imageIndex] != null)
                {
                    rightImages[imageIndex].SetActive(true);
                }
                else if (rightImages.Count > 0 && rightImages[0] != null)
                {
                    rightImages[0].SetActive(true); // Fallback to first image
                    if (showDebugInfo)
                    {
                        Debug.LogWarning($"Right image index {imageIndex} out of range, using default");
                    }
                }
                break;
            case Speaker.None:
                // All images already deactivated
                break;
        }
        
        if (showDebugInfo)
        {
            Debug.Log($"Speaker set to: {speaker}, Image Index: {imageIndex}");
        }
    }
    
    private void SetBoxImage(int boxIndex)
    {
        // Deactivate all box images first
        foreach (GameObject box in boxImages)
        {
            if (box != null) box.SetActive(false);
        }
        
        // Activate the specified box image
        if (boxIndex >= 0 && boxIndex < boxImages.Count && boxImages[boxIndex] != null)
        {
            boxImages[boxIndex].SetActive(true);
        }
        else if (boxImages.Count > 0 && boxImages[0] != null)
        {
            boxImages[0].SetActive(true); // Fallback to first box
            if (showDebugInfo && boxIndex != -1)
            {
                Debug.LogWarning($"Box image index {boxIndex} out of range, using default");
            }
        }
        
    }

    private void EndDialogueSet(bool callEvent=false,int eventID=0)
    {
        if (showDebugInfo)
        {
            Debug.Log($"Dialogue set '{currentSet?.setName}' completed");
        }
        
        // Trigger event
        OnDialogueSetComplete?.Invoke(currentSetIndex);
        
        // Auto close if enabled
        if (currentSet != null && currentSet.autoClose)
        {
            EndDialogue();
        }
        if (callEvent)
        {
            dialogueTriggerEvent.TriggerDialogueEndEvent(eventID);
        }
    }

    #region Public Methods
    
    /// <summary>
    /// Starts a dialogue set by index
    /// </summary>
    /// <param name="setIndex">Index of the dialogue set to play</param>
    public void StartDialogue(int setIndex)
    {
        if (setIndex < 0 || setIndex >= dialogueSets.Count)
        {
            Debug.LogError($"DialogueManager: Invalid set index {setIndex}. Available sets: {dialogueSets.Count}");
            return;
        }
        
        if (isDialogueActive)
        {
            Debug.LogWarning("DialogueManager: Dialogue is already active!");
            return;
        }
        
        currentSetIndex = setIndex;
        currentSet = dialogueSets[setIndex];
        currentLineIndex = 0;
        
        // Check if this is an empty dialogue set used as event trigger
        if (currentSet.dialogueLines.Count == 0)
        {
            if (showDebugInfo)
            {
                Debug.Log($"Empty dialogue set '{currentSet.setName}' - triggering event immediately");
            }
            
            // Trigger event immediately without showing dialogue UI
            if (currentSet.CallEvent && dialogueTriggerEvent != null)
            {
                dialogueTriggerEvent.TriggerDialogueEndEvent(currentSet.EventID);
            }
            
            // Don't set dialogue as active since we're not showing any UI
            return;
        }
        
        // Normal dialogue with lines - show UI and start dialogue
        isDialogueActive = true;
        
        // Show dialogue panel
        if (dialogueSystemPanel != null)
        {
            dialogueSystemPanel.SetActive(true);
        }
        
        // Set box image (use first line's box index if specified, otherwise default)
        int boxIndex = currentSet.dialogueLines[0].boxImageIndex;
        SetBoxImage(boxIndex);
        
        // Start first line
        DisplayLine(currentSet.dialogueLines[0]);
        
        // Trigger event
        OnDialogueStart?.Invoke();
        
        if (showDebugInfo)
        {
            Debug.Log($"Started dialogue set: '{currentSet.setName}' with {currentSet.dialogueLines.Count} lines");
        }
    }
    
    /// <summary>
    /// Starts a dialogue set by name
    /// </summary>
    /// <param name="setName">Name of the dialogue set to play</param>
    public void StartDialogue(string setName)
    {
        int setIndex = dialogueSets.FindIndex(set => set.setName == setName);
        if (setIndex >= 0)
        {
            StartDialogue(setIndex);
        }
        else
        {
            Debug.LogError($"DialogueManager: No dialogue set found with name '{setName}'");
        }
    }
    
    /// <summary>
    /// Ends the current dialogue
    /// </summary>
    public void EndDialogue()
    {
        if (!isDialogueActive) return;
        
        // Stop any typing effect
        if (typingCoroutine != null)
        {
            StopCoroutine(typingCoroutine);
            typingCoroutine = null;
        }
        
        isDialogueActive = false;
        isTyping = false;
        
        // Hide dialogue panel
        if (dialogueSystemPanel != null)
        {
            dialogueSystemPanel.SetActive(false);
        }
        
        // Hide all speaker images
        SetSpeakerImages(Speaker.None);
        
        // Hide all box images
        foreach (GameObject box in boxImages)
        {
            if (box != null) box.SetActive(false);
        }
        
        // Clear text
        if (dialogueText != null)
        {
            dialogueText.text = "";
        }
        
        // Trigger event
        OnDialogueEnd?.Invoke();
        
        if (showDebugInfo)
        {
            Debug.Log("Dialogue ended");
        }
    }
    
    /// <summary>
    /// Skips to the next dialogue set (if available)
    /// </summary>
    public void NextDialogueSet()
    {
        if (currentSetIndex + 1 < dialogueSets.Count)
        {
            EndDialogue();
            StartDialogue(currentSetIndex + 1);
        }
        else
        {
            if (showDebugInfo)
            {
                Debug.Log("No more dialogue sets available");
            }
        }
    }
    
    /// <summary>
    /// Adds a new dialogue set at runtime
    /// </summary>
    /// <param name="newSet">The dialogue set to add</param>
    public void AddDialogueSet(DialogueSet newSet)
    {
        dialogueSets.Add(newSet);
        
        if (showDebugInfo)
        {
            Debug.Log($"Added dialogue set: '{newSet.setName}'");
        }
    }
    
    /// <summary>
    /// Gets a dialogue set by name
    /// </summary>
    /// <param name="setName">Name of the set to find</param>
    /// <returns>The dialogue set, or null if not found</returns>
    public DialogueSet GetDialogueSet(string setName)
    {
        return dialogueSets.Find(set => set.setName == setName);
    }
    
    /// <summary>
    /// Gets all dialogue set names
    /// </summary>
    /// <returns>Array of dialogue set names</returns>
    public string[] GetDialogueSetNames()
    {
        string[] names = new string[dialogueSets.Count];
        for (int i = 0; i < dialogueSets.Count; i++)
        {
            names[i] = dialogueSets[i].setName;
        }
        return names;
    }
    
    /// <summary>
    /// Sets the typewriter text speed
    /// </summary>
    /// <param name="speed">Characters per second</param>
    public void SetTextSpeed(float speed)
    {
        textSpeed = Mathf.Max(0.01f, speed);
    }
    
    /// <summary>
    /// Enables or disables typewriter effect
    /// </summary>
    /// <param name="enabled">Whether typewriter effect should be active</param>
    public void SetTypewriterEffect(bool enabled)
    {
        useTypewriterEffect = enabled;
    }
    
    #endregion

    #region Inspector Testing Methods
    
    /// <summary>
    /// Test method for inspector button - starts dialogue by index
    /// </summary>
    [ContextMenu("Test Start Dialogue (By Index)")]
    public void TestStartDialogueByIndex()
    {
        if (Application.isPlaying)
        {
            StartDialogue(testDialogueSetIndex);
        }
        else
        {
            Debug.LogWarning("DialogueManager: Test dialogue can only be used in Play Mode!");
        }
    }
    
    /// <summary>
    /// Test method for inspector button - starts dialogue by name
    /// </summary>
    [ContextMenu("Test Start Dialogue (By Name)")]
    public void TestStartDialogueByName()
    {
        if (Application.isPlaying)
        {
            if (!string.IsNullOrEmpty(testDialogueSetName))
            {
                StartDialogue(testDialogueSetName);
            }
            else
            {
                Debug.LogWarning("DialogueManager: Test dialogue set name is empty!");
            }
        }
        else
        {
            Debug.LogWarning("DialogueManager: Test dialogue can only be used in Play Mode!");
        }
    }
    
    /// <summary>
    /// Test method for inspector button - ends current dialogue
    /// </summary>
    [ContextMenu("Test End Dialogue")]
    public void TestEndDialogue()
    {
        if (Application.isPlaying)
        {
            EndDialogue();
        }
        else
        {
            Debug.LogWarning("DialogueManager: Test dialogue can only be used in Play Mode!");
        }
    }
    
    /// <summary>
    /// Test method for inspector button - starts next dialogue set
    /// </summary>
    [ContextMenu("Test Next Dialogue Set")]
    public void TestNextDialogueSet()
    {
        if (Application.isPlaying)
        {
            NextDialogueSet();
        }
        else
        {
            Debug.LogWarning("DialogueManager: Test dialogue can only be used in Play Mode!");
        }
    }
    
    /// <summary>
    /// Test method to display all available dialogue sets
    /// </summary>
    [ContextMenu("Show Available Dialogue Sets")]
    public void ShowAvailableDialogueSets()
    {
        if (dialogueSets.Count == 0)
        {
            Debug.Log("DialogueManager: No dialogue sets available.");
            return;
        }
        
        Debug.Log("DialogueManager: Available dialogue sets:");
        for (int i = 0; i < dialogueSets.Count; i++)
        {
            string setInfo = $"  [{i}] {dialogueSets[i].setName} ({dialogueSets[i].dialogueLines.Count} lines)";
            Debug.Log(setInfo);
        }
    }
    
    #endregion
}
