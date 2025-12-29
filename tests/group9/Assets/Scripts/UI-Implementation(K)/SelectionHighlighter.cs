using UnityEngine;
using UnityEngine.UI;

public class SelectionHighlighter : MonoBehaviour
{
    [Header("顏色設定 (RGB 0-255)")]
    // 橘色: 242, 160, 91
    public Color weaponSelectedColor = new Color(242f/255f, 160f/255f, 91f/255f, 1f);
    // 綠色: 114, 218, 165
    public Color itemSelectedColor = new Color(114f/255f, 218f/255f, 165f/255f, 1f);
    // 預設顏色 (未選中時建議用深色或半透明，例如 Alpha 設為 0.5)
    public Color normalColor = new Color(1f, 1f, 1f, 0.5f);

    private Image lastWeaponImg;
    private Image lastItemImg;

    // 此 Function 會在 PauseMenu 按下 Enter 時被呼叫
    public void HighlightWeapon(Button selectedButton)
    {
        if (lastWeaponImg != null) lastWeaponImg.color = normalColor;
        if (selectedButton != null)
        {
            lastWeaponImg = selectedButton.GetComponent<Image>();
            if (lastWeaponImg != null) lastWeaponImg.color = weaponSelectedColor;
        }
    }

    public void HighlightItem(Button selectedButton)
    {
        if (lastItemImg != null) lastItemImg.color = normalColor;
        if (selectedButton != null)
        {
            lastItemImg = selectedButton.GetComponent<Image>();
            if (lastItemImg != null) lastItemImg.color = itemSelectedColor;
        }
    }
}
