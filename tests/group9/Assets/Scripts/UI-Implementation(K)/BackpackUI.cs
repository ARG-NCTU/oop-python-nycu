using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI; // 必須加上這一行，才能識別 Button
using UnityEngine.EventSystems; // 必須引用，Update 裡的 EventSystem 才能運作

public class BackpackUI : MonoBehaviour
{
    public GameObject panelObject;
    public Button returnButton;
    public BPUISelectionFollower bpFollower;
    
    [Header("Memory")]
    public Button lastSelectedWeapon;
    public Button lastSelectedItem;



    [Header("存檔記憶 (預設為 1)")]
    public int selectedWeaponIndex = 1;
    public int selectedItemIndex = 1;



    void Update()
    {
        // 檢查面板是否開啟，並處理 Enter 鍵觸發
        if (panelObject != null && panelObject.activeInHierarchy)
        {
            if (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.KeypadEnter))
            {
                if (EventSystem.current != null)
                {
                    GameObject current = EventSystem.current.currentSelectedGameObject;
                    if (current != null)
                    {
                        // 1. 檢查是否為背包格子
                        BPButtonGlowControl glowCtrl = current.GetComponent<BPButtonGlowControl>();
                        if (glowCtrl != null)
                        {
                            glowCtrl.EquipThis();
                        }
                        
                        // 2. 檢查是否為返回按鈕
                        Button btn = current.GetComponent<Button>();
                        if (btn == returnButton) 
                        {
                            OnClick_Return();
                        }
                    }
                }
            }
        }
    }

    public void OpenPanel()
    {
        if (panelObject != null) panelObject.SetActive(true);
        if (bpFollower != null) bpFollower.enabled = true;
        
        // 每次開啟面板，重新整理所有格子的發光狀態
        RefreshAllGlows();
        
        StartCoroutine(InitializeFocus());
    }

    // 儲存選擇並通知所有格子更新
    public void SaveSelection(BPButtonGlowControl.SlotType type, int index)
    {
        if (type == BPButtonGlowControl.SlotType.Weapon)
            selectedWeaponIndex = index;
        else
            selectedItemIndex = index;

        RefreshAllGlows();
    }

    public void RefreshAllGlows()
    {
        BPButtonGlowControl[] allSlots = GetComponentsInChildren<BPButtonGlowControl>(true);
        foreach (var slot in allSlots)
        {
            slot.RefreshGlow();
        }
    }

    // ... 原有的 ClosePanel, OnClick_Return, InitializeFocus 保持不變 ...
    

    public void ClosePanel()
    {
        if (panelObject != null) panelObject.SetActive(false);
        if (bpFollower != null) bpFollower.enabled = false;
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
            if (bpFollower != null) bpFollower.SnapToTarget(returnButton.gameObject);
        }
    }
}