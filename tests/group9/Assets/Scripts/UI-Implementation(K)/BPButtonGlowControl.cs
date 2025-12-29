using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;

public class BPButtonGlowControl : MonoBehaviour, IPointerClickHandler
{
    public enum SlotType { Weapon, Item }
    
    [Header("設定")]
    public SlotType slotType;      // 在 Inspector 選擇這是武器還是物品
    public int slotIndex;          // 這格的編號 (例如 1, 2, 3...)
    public GameObject glowImage;   // 發光的圖片物件

    private BackpackUI uiController;

    void Start()
    {
        // 找到場景中的 BackpackUI 控制器
        uiController = Object.FindAnyObjectByType<BackpackUI>();
        RefreshGlow();
    }

    // 每一格根據控制器的記憶來決定自己要不要發光
    public void RefreshGlow()
    {
        if (uiController == null) return;

        bool shouldGlow = false;
        if (slotType == SlotType.Weapon)
        {
            shouldGlow = (uiController.selectedWeaponIndex == slotIndex);
        }
        else
        {
            shouldGlow = (uiController.selectedItemIndex == slotIndex);
        }

        if (glowImage != null) glowImage.SetActive(shouldGlow);
    }

    // 當玩家點擊此格 (滑鼠點擊)
    public void OnPointerClick(PointerEventData eventData)
    {
        EquipThis();
    }

    // 供 Enter 鍵或其他邏輯呼叫
    public void EquipThis()
    {
        if (uiController != null)
        {
            uiController.SaveSelection(slotType, slotIndex);
        }
    }
}