using UnityEngine;
using UnityEngine.UI; // 這是給傳統 Text 使用的

public class InventoryManager : MonoBehaviour {
    public Image previewImage;  // 左上角的圖片
    public Text previewText;    // 左下角的說明文字 (若是 TMP 請改用 TextMeshProUGUI)

    // 修改 Function，增加一個 string 參數
    public void UpdatePreview(Sprite itemSprite, string itemDescription) {
        // 更新圖片
        previewImage.sprite = itemSprite;
        previewImage.enabled = true;

        // 更新文字
        //previewText.text = itemDescription;
    }
}