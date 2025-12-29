using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class MenuManager : MonoBehaviour
{
    [Header("Menu Buttons")]
    public Button startButton;
    public Button optionButton;
    public Button quitButton;
    
    [Header("Button Images")]
    [SerializeField] private Sprite startButtonChosen;
    [SerializeField] private Sprite startButtonUnchosen;
    [SerializeField] private Sprite optionButtonChosen;
    [SerializeField] private Sprite optionButtonUnchosen;
    [SerializeField] private Sprite quitButtonChosen;
    [SerializeField] private Sprite quitButtonUnchosen;
    
    [Header("Scene Settings")]
    public string gameSceneName = "GameScene";
    
    [Header("Transition")]
    public TransitionScript transitionAnimator;
    
    [Header("Input Settings")]
    [SerializeField] private KeyCode selectUpKey = KeyCode.UpArrow;
    [SerializeField] private KeyCode selectDownKey = KeyCode.DownArrow;
    [SerializeField] private KeyCode confirmKey = KeyCode.Return;
    [SerializeField] private string xboxVerticalAxis = "Vertical";
    [SerializeField] private string xboxConfirmButton = "Fire1";
    
    // Private state
    private int currentSelection = 0; // 0 = Start, 1 = Options, 2 = Quit
    private Image startButtonImage;
    private Image optionButtonImage;
    private Image quitButtonImage;
    private float navigationCooldown = 0.2f;
    private float lastNavigationTime = 0f;

    void Start()
    {

        // Get button Image components
        if (startButton != null)
        {
            startButtonImage = startButton.GetComponent<Image>();
        }
        
        if (optionButton != null)
        {
            optionButtonImage = optionButton.GetComponent<Image>();
        }
        
        if (quitButton != null)
        {
            quitButtonImage = quitButton.GetComponent<Image>();
        }
        
        // Set up button click listeners
        startButton.onClick.AddListener(StartGame);
        optionButton.onClick.AddListener(() => {
            // Placeholder for options menu functionality
            Debug.Log("Options button clicked");
        });
        quitButton.onClick.AddListener(QuitGame);
        
        // Set initial selection
        UpdateButtonHighlight();
    }
    
    void Update()
    {
        //if Esc pressed set Time scale to 1
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            Time.timeScale = 1f;
        }
        // Handle keyboard navigation
        HandleKeyboardNavigation();
        
        // Handle Xbox controller navigation
        HandleXboxNavigation();
        
        // Handle confirmation input
        HandleConfirmInput();
        
        // Handle mouse hover
        HandleMouseHover();
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
            currentSelection = 2; // Wrap to Quit button
        }
        UpdateButtonHighlight();
    }
    
    private void NavigateDown()
    {
        currentSelection++;
        if (currentSelection > 2)
        {
            currentSelection = 0; // Wrap to Start button
        }
        UpdateButtonHighlight();
    }
    
    private void HandleMouseHover()
    {
        // Check if mouse is over Start button
        if (startButton != null && IsPointerOverButton(startButton))
        {
            if (currentSelection != 0)
            {
                currentSelection = 0;
                UpdateButtonHighlight();
            }
        }
        // Check if mouse is over Option button
        else if (optionButton != null && IsPointerOverButton(optionButton))
        {
            if (currentSelection != 1)
            {
                currentSelection = 1;
                UpdateButtonHighlight();
            }
        }
        // Check if mouse is over Quit button
        else if (quitButton != null && IsPointerOverButton(quitButton))
        {
            if (currentSelection != 2)
            {
                currentSelection = 2;
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
            if ((currentSelection == 0 && startButton != null && IsPointerOverButton(startButton)) ||
                (currentSelection == 1 && optionButton != null && IsPointerOverButton(optionButton)) ||
                (currentSelection == 2 && quitButton != null && IsPointerOverButton(quitButton)))
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
        // Set all buttons to unchosen state first
        if (startButtonImage != null && startButtonUnchosen != null)
        {
            startButtonImage.sprite = startButtonUnchosen;
        }
        
        if (optionButtonImage != null && optionButtonUnchosen != null)
        {
            optionButtonImage.sprite = optionButtonUnchosen;
        }
        
        if (quitButtonImage != null && quitButtonUnchosen != null)
        {
            quitButtonImage.sprite = quitButtonUnchosen;
        }
        
        // Set selected button to chosen state
        if (currentSelection == 0 && startButtonImage != null && startButtonChosen != null)
        {
            startButtonImage.sprite = startButtonChosen;
        }
        else if (currentSelection == 1 && optionButtonImage != null && optionButtonChosen != null)
        {
            optionButtonImage.sprite = optionButtonChosen;
        }
        else if (currentSelection == 2 && quitButtonImage != null && quitButtonChosen != null)
        {
            quitButtonImage.sprite = quitButtonChosen;
        }
    }
    
    private void ExecuteSelectedButton()
    {
        if (currentSelection == 0)
        {
            StartGame();
        }
        else if (currentSelection == 1)
        {
            // Options functionality
            Debug.Log("Options button clicked");
        }
        else if (currentSelection == 2)
        {
            QuitGame();
        }
    }

    void StartGame()
    {
        transitionAnimator.StartCoroutine(transitionAnimator.LoadGameScene(gameSceneName));
    }

    void QuitGame()
    {
        Application.Quit();
        Debug.Log("Quit button clicked - Application.Quit() called");
    }

    
}
