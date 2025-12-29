using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerUIManagerK : MonoBehaviour
{
[Header("步驟 1：請把做好的 UI Prefab 拖進這裡")]
    public GameObject uiPrefab;

    [Header("系統自動抓取的變數 (不用填)")]
    public GameObject currentUIInstance; // 目前生成的 UI 實體
    private GameObject backpackPanel;    // 背包面板
    private GameObject pausePanel;       // 暫停面板
    private GameObject deadPanel;        // 死亡面板

    // 單例模式：確保全場景只有一個管理器
    public static PlayerUIManagerK instance;

    void Awake()
    {
        // 1. 確保玩家只有一個，且換場景不消失
        if (instance == null)
        {
            instance = this;
            DontDestroyOnLoad(gameObject); // 保護玩家
            SpawnUI(); // 生成 UI
        }
        else
        {
            Destroy(gameObject); // 如果場景已經有舊的玩家，刪掉新的這個
        }
    }

    void SpawnUI()
    {
        // 2. 檢查是否已經有生成的 UI 了
        // 這裡我們用 Tag 或名稱判斷，避免重複生成
        if (currentUIInstance == null)
        {
            // 生成 UI Prefab
            currentUIInstance = Instantiate(uiPrefab);
            
            // 重要：把 UI 改名，方便管理 (非必要，但推薦)
            currentUIInstance.name = "MyGame_UI_System";

            // 重要：讓 UI 也跟著玩家一起「不被銷毀」
            DontDestroyOnLoad(currentUIInstance);

            // 3. 抓取子物件 (請確保你的 Prefab 裡的子物件名稱跟這裡一樣！)
            // 如果你的名字不一樣，請修改引號裡的字串
            backpackPanel = currentUIInstance.transform.Find("BackpackPanel").gameObject;
            pausePanel    = currentUIInstance.transform.Find("PauseMenuPanel").gameObject;
            deadPanel     = currentUIInstance.transform.Find("GameOverPanel").gameObject;

            // 4. 預設全部關閉 (除了 HUD)
            backpackPanel.SetActive(false);
            pausePanel.SetActive(false);
            deadPanel.SetActive(false);
        }
    }

    void Update()
    {
        // 如果 UI 還沒生成好，就不執行下面的按鍵判斷
        if (currentUIInstance == null) return;

        // --- 按 B 開關背包 ---
        if (Input.GetKeyDown(KeyCode.B))
        {
            TogglePanel(backpackPanel);
        }

        // --- 按 ESC 開關暫停 ---
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            TogglePanel(pausePanel);
            
            // 暫停時間 (如果面板打開就暫停，關閉就恢復)
            if (pausePanel.activeSelf) Time.timeScale = 0f;
            else Time.timeScale = 1f;
        }
    }

    // 通用的開關面板功能
    void TogglePanel(GameObject panel)
    {
        bool isActive = panel.activeSelf;
        panel.SetActive(!isActive);
    }

    // 給你的 DeadScript 呼叫用的功能
    public void ShowDeadScene()
    {
        if (deadPanel != null)
        {
            deadPanel.SetActive(true);
            // 可以在這裡加 Time.timeScale = 0; 讓遊戲暫停
        }
    }
}
