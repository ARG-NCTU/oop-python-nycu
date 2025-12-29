using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class StatusUI : MonoBehaviour 
{
    public GameObject panelObject;
    public Button returnButton;
    public StUISelectionFollower1 stFollower; 


    /*
    void Start()
    {
        if (returnButton != null)
        {
            // 加上監聽器：當按鈕被點擊時，執行 BackToPauseMenu 方法
            returnButton.onClick.AddListener(BackToPauseMenu);
        }
    }

    void BackToPauseMenu()
    {
        Debug.Log("返回暫停選單");
    
        // 1. 關閉當前狀態 UI
        ClosePanel();
    
        // 2. 在這裡寫下返回暫停系統的邏輯
        // 例如：PauseManager.Instance.ShowMainMenu();
    }  */

    void Update()
    {
        // 檢查面板是否開啟，且玩家是否按下 Enter 或 NumpadEnter
        if (panelObject != null && panelObject.activeSelf)
        {
            if (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.KeypadEnter))
            {
                // 取得當前 EventSystem 選中的物件
                GameObject currentSelected = UnityEngine.EventSystems.EventSystem.current.currentSelectedGameObject;
            
                if (currentSelected != null)
                {
                    // 嘗試獲取按鈕組件並執行點擊
                    Button btn = currentSelected.GetComponent<Button>();
                    if (btn != null && btn.interactable)
                    {
                        btn.onClick.Invoke();
                    }
                }
            }
        }
    }

    public void OpenPanel()
    {
        if (panelObject != null) panelObject.SetActive(true);
        if (stFollower != null) stFollower.enabled = true;
        StartCoroutine(InitializeFocus());
    }

    public void ClosePanel()
    {
        if (panelObject != null) panelObject.SetActive(false);
        if (stFollower != null) stFollower.enabled = false;
    }


    public void OnClick_Return()
    {
        // 檢查 PauseMenuControllerK 是否存在
        if (PauseMenuControllerK.Instance != null)
        {
            // 呼叫暫停系統裡面的「返回主選單」方法
            PauseMenuControllerK.Instance.BackToMainMenu();
        }
        else
        {
            Debug.LogWarning("找不到 PauseMenuControllerK 實例！");
            // 如果找不到，至少要把自己關掉
            ClosePanel();
        }
    }

    IEnumerator InitializeFocus()
    {
        yield return new WaitForEndOfFrame();
        if (returnButton != null)
        {
            returnButton.Select();
            if (stFollower != null) stFollower.SnapToTarget(returnButton.gameObject);
        }
    }
}