using UnityEngine;
using UnityEngine.EventSystems;

public class BPUISelectionFollower : MonoBehaviour
{
    [Header("移動設定")]
    public float smoothSpeed = 15f;
    public InventoryManager invManager;
    public Sprite[] itemSprites;
    public backpacktext bpt;
    
    private RectTransform myRect;

    void Start()
    {
        myRect = GetComponent<RectTransform>();
        // 選取框的 Pivot 務必設為中心，座標抓取才會準確
        myRect.pivot = new Vector2(0.5f, 0.5f);
    }

    void Update()
    {
        if (EventSystem.current == null || EventSystem.current.currentSelectedGameObject == null) return;

        GameObject selected = EventSystem.current.currentSelectedGameObject;
        UpdatePositionOnly(selected, false);
    }

    public void SnapToTarget(GameObject target)
    {
        UpdatePositionOnly(target, true);
    }

    private void UpdatePositionOnly(GameObject target, bool instant)
    {
        RectTransform selectedRect = target.GetComponent<RectTransform>();
        if (selectedRect != null)
        {
            // 取得按鈕在螢幕上的四個角落座標
            Vector3[] corners = new Vector3[4];
            selectedRect.GetWorldCorners(corners);
            
            // 計算藍色矩形的精確幾何中心
            Vector3 centerPos = (corners[0] + corners[2]) / 2f + new Vector3(360,700,0);

            // ⭐ Debug: 在 Console 印出按鈕在哪裡，框框在哪裡
            // 定義容許誤差值（例如 1 個單位內都算對）
            float threshold = 10.0f;

            if (Vector3.Distance(centerPos, new Vector3(1654.77f, 1438.65f, 0f)) < threshold)
            {
                bpt.UpdateDescription(1);    // 更新左下文字 (傳入 1)
                invManager.UpdatePreview(itemSprites[0], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(1901.50f, 1440.38f, 0f)) < threshold)
            {
                bpt.UpdateDescription(2); 
                invManager.UpdatePreview(itemSprites[1], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(2142.50f, 1440.38f, 0f)) < threshold)
            {
                bpt.UpdateDescription(3); 
                invManager.UpdatePreview(itemSprites[2], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(1473.11f, 1050.81f, 0f)) < threshold)
            {
                bpt.UpdateDescription(4); 
                invManager.UpdatePreview(itemSprites[3], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(1689.40f, 1050.02f, 0f)) < threshold)
            {
                bpt.UpdateDescription(5); 
                invManager.UpdatePreview(itemSprites[4], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(1926.32f, 1051.48f, 0f)) < threshold)
            {
                bpt.UpdateDescription(6); 
                invManager.UpdatePreview(itemSprites[5], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(2146.95f, 1047.58f, 0f)) < threshold)
            {
                bpt.UpdateDescription(7); 
                invManager.UpdatePreview(itemSprites[6], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(1470.38f, 830.16f, 0f)) < threshold)
            {
                bpt.UpdateDescription(8); 
                invManager.UpdatePreview(itemSprites[7], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(1692.24f, 831.32f, 0f)) < threshold)
            {
                bpt.UpdateDescription(9); 
                invManager.UpdatePreview(itemSprites[8], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(1920.24f, 830.60f, 0f)) < threshold)
            {
                bpt.UpdateDescription(10); 
                invManager.UpdatePreview(itemSprites[9], "");
            }
            else if (Vector3.Distance(centerPos, new Vector3(2147.48f, 833.00f, 0f)) < threshold)
            {
                bpt.UpdateDescription(11); 
                invManager.UpdatePreview(itemSprites[10], "");
            }


            //bpt.changetext();
            //Debug.Log($"目標按鈕: {target.name}, 計算出的世界座標: {centerPos}, 框框當前座標: {transform.position}");

            if (instant)
            {
                transform.position = centerPos;
            }
            else
            {
                transform.position = Vector3.Lerp(transform.position, centerPos, Time.unscaledDeltaTime * smoothSpeed);
            }
                if (instant)
                {
                    transform.position = centerPos;
                }
                else
                {
                    // 使用 unscaledDeltaTime 確保暫停時框框依然會動
                    transform.position = Vector3.Lerp(transform.position, centerPos, Time.unscaledDeltaTime * smoothSpeed);
                }

                // ⭐ 大小部分完全不更新，維持你在 Inspector 設定的 Width / Height
        }
    }
}