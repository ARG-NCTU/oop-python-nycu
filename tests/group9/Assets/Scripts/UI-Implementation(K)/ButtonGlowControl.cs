using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;

// 新增 IPointerClickHandler 接口來處理點擊事件
public class ButtonGlowControl : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler, IPointerClickHandler
{
    [Header("把做好的 Glow Image 物件拖到這裡")]
    public GameObject glowImageObject;

    private bool isMouseHovering = false;

    void Update()
    {
        if (EventSystem.current == null) return;

        // 🔍 主動偵測：現在 EventSystem 選中的是不是我？
        // 當你點擊一個按鈕，EventSystem 會把選中物件切換到該按鈕，其他按鈕的 isSelected 就會變 false
        bool isSelected = (EventSystem.current.currentSelectedGameObject == gameObject);

        // 💡 邏輯：(我是被選取的焦點) 或者 (滑鼠正指著我) -> 開燈
        if (isSelected || isMouseHovering)
        {
            if (glowImageObject != null && !glowImageObject.activeSelf)
            {
                glowImageObject.SetActive(true);
            }
        }
        else
        {
            if (glowImageObject != null && glowImageObject.activeSelf)
            {
                glowImageObject.SetActive(false);
            }
        }
    }

    // --- 新增：當滑鼠點擊按鈕時 ---
    public void OnPointerClick(PointerEventData eventData)
    {
        // 關鍵：點擊時強制叫 EventSystem 選中自己
        // 這樣就算滑鼠移開了，這個按鈕也會因為是「Selected」狀態而保持發光
        EventSystem.current.SetSelectedGameObject(gameObject);
    }

    // --- 滑鼠移入 ---
    public void OnPointerEnter(PointerEventData eventData)
    {
        isMouseHovering = true;
    }

    // --- 滑鼠移出 ---
    public void OnPointerExit(PointerEventData eventData)
    {
        isMouseHovering = false;
    }
}