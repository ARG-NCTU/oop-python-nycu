using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;

// 💡 加上 ISubmitHandler 來偵測鍵盤 Enter 鍵
public class MultipleButtonGlow : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, IPointerClickHandler, ISubmitHandler
{
    [Header("發光圖片物件")]
    public GameObject glowImageObject;

    [Header("設定")]
    public bool toggleMode = true; // 是否點擊切換開關

    private bool isMouseHovering = false;
    private bool isGlowingLocked = false; 

    void Update()
    {
        if (EventSystem.current == null) return;

        // 偵測目前 EventSystem 選中的是不是我
        bool isCurrentlySelected = EventSystem.current.currentSelectedGameObject == gameObject;

        // --- 🔑 新增：如果被選中且按下 Enter 鍵 ---
        if (isCurrentlySelected && (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.KeypadEnter)))
        {
            HandleToggleLogic();
        }

        // 邏輯：(滑鼠指著) OR (被選中) OR (鎖定亮起) -> 顯示發光
        bool shouldShowGlow = isMouseHovering || isCurrentlySelected || isGlowingLocked;

        if (glowImageObject != null)
        {
            if (shouldShowGlow && !glowImageObject.activeSelf)
            {
                glowImageObject.SetActive(true);
            }
            else if (!shouldShowGlow && glowImageObject.activeSelf)
            {
                glowImageObject.SetActive(false);
            }
        }
    }

    // --- 🔑 新增：處理鍵盤 Enter / 手把 Submit 事件 ---
    public void OnSubmit(BaseEventData eventData)
    {
        HandleToggleLogic();
    }

    // --- 處理滑鼠點擊事件 ---
    public void OnPointerClick(PointerEventData eventData)
    {
        HandleToggleLogic();
        // 點擊後確保設為選中，維持導航
        EventSystem.current.SetSelectedGameObject(gameObject);
    }

    // 將發光切換邏輯獨立出來，讓滑鼠與鍵盤共用
    private void HandleToggleLogic()
    {
        if (toggleMode)
        {
            isGlowingLocked = !isGlowingLocked;
        }
        else
        {
            isGlowingLocked = true;
        }
    }

    public void OnPointerEnter(PointerEventData eventData) { isMouseHovering = true; }
    public void OnPointerExit(PointerEventData eventData) { isMouseHovering = false; }

    public void ResetGlow()
    {
        isGlowingLocked = false;
        isMouseHovering = false;
    }
}