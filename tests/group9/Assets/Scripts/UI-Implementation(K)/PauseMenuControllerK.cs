using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class PauseMenuControllerK : MonoBehaviour
{
    public static PauseMenuControllerK Instance;

    [Header("Panels")]
    public GameObject darkBackground;
    public GameObject pauseMenuPanel;
    public BackpackUI backpackUI; 
    public StatusUI statusUI;     

    [Header("Main Menu Focus")]
    public Button firstPauseMenuButton;

    public bool isPaused = false;
    public MonoBehaviour playerMovementScript;


    void Awake()
    {
        if (Instance != null && Instance != this) 
        { 
            Destroy(gameObject); 
            return; 
        }
        Instance = this;
        DontDestroyOnLoad(gameObject);

        // 如果你希望每次載入場景都強制重置狀態，可以寫在這裡或 Start
        //InitializeGameState();
    }

    
    void Start()
    {
        Debug.Log("start--------------");
        // 遊戲開始時確保一切是正常的
        Time.timeScale = 1f;
        isPaused = false;
        
        // 呼叫 CloseAllMenus 確保所有面板初始為關閉狀態
        CloseAllMenus();
    } 

    /*
    void Start()
    {
        // 如果 Awake 沒印，看這裡有沒有印
        Debug.Log("PauseMenu Start Executed"); 
        InitializeGameState();
    }

    void InitializeGameState()
    {
        Time.timeScale = 1f;
        isPaused = false;
        CloseAllMenus();
    }

    */

    void Update()
    {
        // 偵測 Enter 鍵確認選擇 (支援主鍵盤與小鍵盤 Enter)
        if (isPaused && (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.KeypadEnter)))
        {
            if (UnityEngine.EventSystems.EventSystem.current != null)
            {
                GameObject currentSelected = UnityEngine.EventSystems.EventSystem.current.currentSelectedGameObject;
                if (currentSelected != null)
                {
                    Button btn = currentSelected.GetComponent<Button>();
                    if (btn != null && btn.interactable)
                    {
                        // 執行按鈕點擊事件
                        btn.onClick.Invoke();
                    }
                }
            }
        }
        
        // 偵測 Esc 鍵
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            // 如果目前在背包或狀態欄，按 Esc 應該先回到主暫停選單
            if (backpackUI != null && backpackUI.panelObject.activeInHierarchy)
            {
                BackToMainMenu();
            }
            else if (statusUI != null && statusUI.panelObject.activeInHierarchy)
            {
                BackToMainMenu();
            }
            // 如果已經在暫停狀態（主選單），則恢復遊戲
            else if (isPaused)
            {
                Resume();
            }
            // 如果是正常遊戲中，則暫停遊戲
            else
            {
                Pause();
            }
        }
    }

    /*
    void Awake()
    {
        if (Instance != null && Instance != this) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);
    } */

public void Pause()
{
    isPaused = true;
    Time.timeScale = 0f;

    // 1. 開啟面板
    if (darkBackground != null) darkBackground.SetActive(true);
    if (pauseMenuPanel != null) pauseMenuPanel.SetActive(true);

    // 2. 角色腳本處理 (加入安全檢查)
    if (playerMovementScript == null)
    {
        GameObject playerObj = GameObject.FindGameObjectWithTag("Player");
        if (playerObj != null)
        {
            // 確保這裡的 PlayerController 與你實際的腳本名稱一致
            playerMovementScript = playerObj.GetComponent<PlayerController>(); 
        }
    }

    // 只有在真的拿到腳本時才停用它
    if (playerMovementScript != null) 
    {
        playerMovementScript.enabled = false;
    }
    else 
    {
        Debug.LogWarning("PauseMenu: 找不到角色移動腳本，請檢查 Tag 或腳本名稱。");
    }
    
    // 3. 確保焦點回到按鈕上
    if (firstPauseMenuButton != null)
    {
        StartCoroutine(SelectButtonLater(firstPauseMenuButton));
    }
}

    public void Resume()
    {
        isPaused = false;
        Time.timeScale = 1f;
        CloseAllMenus();
        if (playerMovementScript != null) playerMovementScript.enabled = true;
    }

    public void OnClick_Menu(string sceneName)
    {
        // 1. 恢復時間流動 (非常重要，否則新場景會動彈不得)
        Time.timeScale = 1f;
        isPaused = false;

        // 2. 如果你的 Controller 是 DontDestroyOnLoad，建議載入前關閉所有面板
        CloseAllMenus();

        // 3. 載入目標場景
        Debug.Log("正在前往場景: " + sceneName);
        SceneManager.LoadScene(sceneName);
    }

    public void CloseAllMenus()
    {
        Debug.Log("-------------");
        if (darkBackground != null) darkBackground.SetActive(false);
        if (pauseMenuPanel != null) pauseMenuPanel.SetActive(false);
        if (backpackUI != null) backpackUI.ClosePanel();
        if (statusUI != null) statusUI.ClosePanel();
    }

    public void OpenBackpack()
    {   
        Debug.Log("1. OpenBackpack 被觸發了");
        if (pauseMenuPanel != null) pauseMenuPanel.SetActive(false);
        if (backpackUI != null) backpackUI.OpenPanel();
    }

    public void OpenStatus()
    {
        Debug.Log("1. OpenStatus 被觸發了");
        if (pauseMenuPanel != null) pauseMenuPanel.SetActive(false);
        if (statusUI != null) statusUI.OpenPanel();
    }

    public void BackToMainMenu()
    {
        if (backpackUI != null) backpackUI.ClosePanel();
        if (statusUI != null) statusUI.ClosePanel();
        if (pauseMenuPanel != null) pauseMenuPanel.SetActive(true);
        StartCoroutine(SelectButtonLater(firstPauseMenuButton));
    }

    // 剛才遺漏的關鍵協程，補上它錯誤才會消失
    IEnumerator SelectButtonLater(Button btn)
    {
        yield return null; 
        if (btn != null && UnityEngine.EventSystems.EventSystem.current != null)
        {
            UnityEngine.EventSystems.EventSystem.current.SetSelectedGameObject(null);
            btn.Select();
            UnityEngine.EventSystems.EventSystem.current.SetSelectedGameObject(btn.gameObject);
        }
    }
}