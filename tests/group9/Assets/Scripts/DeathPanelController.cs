using System.Collections;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using UnityEngine.SceneManagement;

public class DeathPanelController : MonoBehaviour
{
    [Header("Panel Elements")]
    [SerializeField] private Image fadeinImage;
    [SerializeField] private GameObject youDieImage;
    [SerializeField] private Button menuButton;
    [SerializeField] private Button retryButton;
    
    [Header("Fadein Settings")]
    [SerializeField] private float fadeinDuration = 3f;
    
    [Header("Input Settings")]
    [SerializeField] private KeyCode selectUpKey = KeyCode.UpArrow;
    [SerializeField] private KeyCode selectDownKey = KeyCode.DownArrow;
    [SerializeField] private KeyCode confirmKey = KeyCode.Return;
    [SerializeField] private string xboxVerticalAxis = "Vertical";
    [SerializeField] private string xboxConfirmButton = "Fire1";
    
    [Header("Trigger Reset Settings")]
    [SerializeField] private DialogueTrigger[] triggerOnceTriggersToReset;
    
    // Private state
    private int currentSelection = 0; // 0 = Retry, 1 = Menu
    private bool canNavigate = false;
    private bool isNavigating = false;
    private GameObject menuButtonHighlight;
    private GameObject retryButtonHighlight;
    private float navigationCooldown = 0.2f;
    private float lastNavigationTime = 0f;

    private int StartDeath = 0;
    
    private void Awake()
    {
        // Get button highlight child images
        if (menuButton != null && menuButton.transform.childCount > 0)
        {
            menuButtonHighlight = menuButton.transform.GetChild(0).gameObject;
        }
        
        if (retryButton != null && retryButton.transform.childCount > 0)
        {
            retryButtonHighlight = retryButton.transform.GetChild(0).gameObject;
        }
        
        // Validate references
        ValidateReferences();
    }
    
    private void Update()
    {
        if (!canNavigate) return;
        
        // Handle keyboard input
        HandleKeyboardNavigation();
        
        // Handle Xbox controller input
        HandleXboxNavigation();
        
        // Handle confirmation input
        HandleConfirmInput();
        
        // Handle mouse hover
        HandleMouseHover();
    }
    
    private IEnumerator DeathSequence()
    {
        // Phase 1: Fadein black screen with YouDie appearing at 1s
        StartCoroutine(ShowYouDieAtTime(2.5f));
        yield return StartCoroutine(FadeinEffect());
        
        // Phase 2: Show buttons with fadein effect (2s to 4s)
        if (menuButton != null)
        {
            menuButton.gameObject.SetActive(true);
        }
        
        if (retryButton != null)
        {
            retryButton.gameObject.SetActive(true);
        }
        
        // Fadein buttons from alpha 0 to 1 over 2 seconds, starting at 2s mark
        yield return new WaitForSeconds(2f);
        yield return StartCoroutine(FadeinButtons());
        
        // Enable navigation
        canNavigate = true;
        
        // Set initial selection to Retry button
        UpdateButtonHighlight();
    }
    
    private IEnumerator ShowYouDieAtTime(float delay)
    {
        yield return new WaitForSeconds(delay);
        if (youDieImage != null)
        {
            youDieImage.SetActive(true);
        }
    }
    
    private IEnumerator FadeinButtons()
    {
        float duration = 2f; // 2 seconds to fade in
        float elapsedTime = 0f;
        
        // Get button images
        Image menuImage = menuButton != null ? menuButton.GetComponent<Image>() : null;
        Image retryImage = retryButton != null ? retryButton.GetComponent<Image>() : null;
        
        // Get button text components (if any)
        Text menuText = menuButton != null ? menuButton.GetComponentInChildren<Text>() : null;
        Text retryText = retryButton != null ? retryButton.GetComponentInChildren<Text>() : null;
        
        // Store original colors
        Color menuImgColor = menuImage != null ? menuImage.color : Color.white;
        Color retryImgColor = retryImage != null ? retryImage.color : Color.white;
        Color menuTxtColor = menuText != null ? menuText.color : Color.white;
        Color retryTxtColor = retryText != null ? retryText.color : Color.white;
        
        // Set initial alpha to 0
        if (menuImage != null)
        {
            menuImgColor.a = 0f;
            menuImage.color = menuImgColor;
        }
        if (retryImage != null)
        {
            retryImgColor.a = 0f;
            retryImage.color = retryImgColor;
        }
        if (menuText != null)
        {
            menuTxtColor.a = 0f;
            menuText.color = menuTxtColor;
        }
        if (retryText != null)
        {
            retryTxtColor.a = 0f;
            retryText.color = retryTxtColor;
        }
        youDieImage.SetActive(true);
        
        // Fade in over 2 seconds
        while (elapsedTime < duration)
        {
            elapsedTime += Time.deltaTime;
            float alpha = Mathf.Lerp(0f, 1f, elapsedTime / duration);
            
            if (menuImage != null)
            {
                menuImgColor.a = alpha;
                menuImage.color = menuImgColor;
            }
            if (retryImage != null)
            {
                retryImgColor.a = alpha;
                retryImage.color = retryImgColor;
            }
            if (menuText != null)
            {
                menuTxtColor.a = alpha;
                menuText.color = menuTxtColor;
            }
            if (retryText != null)
            {
                retryTxtColor.a = alpha;
                retryText.color = retryTxtColor;
            }
            
            yield return null;
        }
        
        // Ensure alpha is exactly 1 at the end
        if (menuImage != null)
        {
            menuImgColor.a = 1f;
            menuImage.color = menuImgColor;
        }
        if (retryImage != null)
        {
            retryImgColor.a = 1f;
            retryImage.color = retryImgColor;
        }
        if (menuText != null)
        {
            menuTxtColor.a = 1f;
            menuText.color = menuTxtColor;
        }
        if (retryText != null)
        {
            retryTxtColor.a = 1f;
            retryText.color = retryTxtColor;
        }
    }
    
    private IEnumerator FadeinEffect()
    {
        if (fadeinImage == null) yield break;
        
        float elapsedTime = 0f;
        Color color = fadeinImage.color;
        
        while (elapsedTime < fadeinDuration)
        {
            elapsedTime += Time.deltaTime;
            float alpha = Mathf.Lerp(0f, 1f, elapsedTime / fadeinDuration);
            color.a = alpha;
            fadeinImage.color = color;
            yield return null;
        }
        
        // Ensure alpha is exactly 1 at the end
        color.a = 1f;
        fadeinImage.color = color;
    }
    
    private void HandleKeyboardNavigation()
    {
        if (Input.GetKeyDown(selectUpKey))
        {
            NavigateUp();
        }
        else if (Input.GetKeyDown(selectDownKey))
        {
            NavigateDown();
        }
    }
    
    private void HandleXboxNavigation()
    {
        // Prevent rapid navigation
        if (Time.time - lastNavigationTime < navigationCooldown) return;
        
        float verticalInput = Input.GetAxis(xboxVerticalAxis);
        
        if (verticalInput > 0.5f) // Up on analog stick or D-Pad
        {
            NavigateUp();
            lastNavigationTime = Time.time;
        }
        else if (verticalInput < -0.5f) // Down on analog stick or D-Pad
        {
            NavigateDown();
            lastNavigationTime = Time.time;
        }
    }
    
    private void NavigateUp()
    {
        currentSelection--;
        if (currentSelection < 0)
        {
            currentSelection = 1; // Wrap to Menu button
        }
        UpdateButtonHighlight();
    }
    
    private void NavigateDown()
    {
        currentSelection++;
        if (currentSelection > 1)
        {
            currentSelection = 0; // Wrap to Retry button
        }
        UpdateButtonHighlight();
    }
    
    private void HandleMouseHover()
    {
        // Check if mouse is over Retry button
        if (retryButton != null && IsPointerOverButton(retryButton))
        {
            if (currentSelection != 0)
            {
                currentSelection = 0;
                UpdateButtonHighlight();
            }
        }
        // Check if mouse is over Menu button
        else if (menuButton != null && IsPointerOverButton(menuButton))
        {
            if (currentSelection != 1)
            {
                currentSelection = 1;
                UpdateButtonHighlight();
            }
        }
    }
    
    private bool IsPointerOverButton(Button button)
    {
        if (button == null) return false;
        
        RectTransform rectTransform = button.GetComponent<RectTransform>();
        if (rectTransform == null) return false;
        
        return RectTransformUtility.RectangleContainsScreenPoint(
            rectTransform, 
            Input.mousePosition, 
            null
        );
    }
    
    private void HandleConfirmInput()
    {
        bool confirmPressed = false;
        
        // Check keyboard
        if (Input.GetKeyDown(confirmKey))
        {
            confirmPressed = true;
        }
        
        // Check Xbox controller
        if (Input.GetButtonDown(xboxConfirmButton))
        {
            confirmPressed = true;
        }
        
        // Check mouse click on selected button
        if (Input.GetMouseButtonDown(0))
        {
            if ((currentSelection == 0 && retryButton != null && IsPointerOverButton(retryButton)) ||
                (currentSelection == 1 && menuButton != null && IsPointerOverButton(menuButton)))
            {
                confirmPressed = true;
            }
        }
        
        if (confirmPressed)
        {
            ExecuteSelectedButton();
        }
    }
    
    private void UpdateButtonHighlight()
    {
        // Deactivate all highlights first
        if (menuButtonHighlight != null)
        {
            menuButtonHighlight.SetActive(false);
        }
        
        if (retryButtonHighlight != null)
        {
            retryButtonHighlight.SetActive(false);
        }
        
        // Activate selected button's highlight
        if (currentSelection == 0 && retryButtonHighlight != null)
        {
            retryButtonHighlight.SetActive(true);
        }
        else if (currentSelection == 1 && menuButtonHighlight != null)
        {
            menuButtonHighlight.SetActive(true);
        }
    }
    
    private void ExecuteSelectedButton()
    {
        if (currentSelection == 0)
        {
            OnRetryButtonPressed();
        }
        else if (currentSelection == 1)
        {
            OnMenuButtonPressed();
        }
    }
    
    private void OnRetryButtonPressed()
    {
        Debug.Log("Retry button pressed - Restarting level...");
        
        // Reset TriggerOnce triggers in this scene
        if (triggerOnceTriggersToReset != null)
        {
            foreach (DialogueTrigger trigger in triggerOnceTriggersToReset)
            {
                if (trigger != null)
                {
                    trigger.ResetTrigger();
                }
            }
        }
        
        // Reset player stats
        PlayerStats playerStats = FindObjectOfType<PlayerStats>();
        PlayerController playerController = FindObjectOfType<PlayerController>();
        if (playerController != null)
        {
            playerController.enableMovement = true;
            playerController.ResetDeathState();
        }
        if (playerStats != null)
        {
            playerStats.currentHealth = playerStats.maxHealth;
            playerStats.currentSanity = playerStats.maxSanity;
            playerStats.currentHealCount = playerStats.maxHealCount;
        }
        
        // Reload current scene
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
    
    private void OnMenuButtonPressed()
    {
        Debug.Log("Menu button pressed - Returning to main menu...");
        if (triggerOnceTriggersToReset != null)
        {
            foreach (DialogueTrigger trigger in triggerOnceTriggersToReset)
            {
                if (trigger != null)
                {
                    trigger.ResetTrigger();
                }
            }
        }
        // Reset player stats
        PlayerStats playerStats = FindObjectOfType<PlayerStats>();
        PlayerController playerController = FindObjectOfType<PlayerController>();
        if (playerController != null)
        {
            playerController.enableMovement = true;
        }
        if (playerStats != null)
        {
            playerStats.currentHealth = playerStats.maxHealth;
            playerStats.currentSanity = playerStats.maxSanity;
            playerStats.currentHealCount = playerStats.maxHealCount;
        }
        
        SceneManager.LoadScene("Menu");
    }
    
    private void ValidateReferences()
    {
        if (fadeinImage == null)
            Debug.LogError("DeathPanelController: Fadein Image is not assigned!");
        
        if (youDieImage == null)
            Debug.LogError("DeathPanelController: YouDie Image is not assigned!");
        
        if (menuButton == null)
            Debug.LogError("DeathPanelController: Menu Button is not assigned!");
        
        if (retryButton == null)
            Debug.LogError("DeathPanelController: Retry Button is not assigned!");
        
        if (menuButtonHighlight == null)
            Debug.LogWarning("DeathPanelController: Menu Button has no child image for highlight!");
        
        if (retryButtonHighlight == null)
            Debug.LogWarning("DeathPanelController: Retry Button has no child image for highlight!");
    }
    
    /// <summary>
    /// Public method to trigger the death panel from other scripts
    /// </summary>
    public void ShowDeathPanel()
    {
        gameObject.SetActive(true);
        StartDeath = 1;
        // Reset state when panel is enabled
        canNavigate = false;
        currentSelection = 0;
        
        // Ensure fadein image starts transparent
        if (fadeinImage != null)
        {
            Color color = fadeinImage.color;
            color.a = 0f;
            fadeinImage.color = color;
        }
        
        // Hide YouDie and buttons initially
        if (youDieImage != null)
        {
            youDieImage.SetActive(false);
        }
        
        if (menuButton != null)
        {
            menuButton.gameObject.SetActive(false);
        }
        
        if (retryButton != null)
        {
            retryButton.gameObject.SetActive(false);
        }
        
        // Start death sequence
        if (StartDeath == 1)
        {
            StartCoroutine(DeathSequence());
        }
    }
}
