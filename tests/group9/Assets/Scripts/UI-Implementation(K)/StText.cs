using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI; // 必須要有這行才能用 Text

public class StText : MonoBehaviour
{
    // 修改為正確的 UnityEngine.UI.Text 類型
    public Text displayUI; 

    public void UpdateDescriptionST(int itemID)
    {
        string text = "";
        switch (itemID)
        {
            case 1: text = "【武器 W1】\n這是一把鋒利的匕首。"; break;
            case 2: text = "【武器 W2】\n這是一把精準的狙擊槍。"; break;
            case 3: text = "【武器 W3】\n充滿魔力的權杖。"; break;
            case 4: text = "【道具 I1】\n威力強大的定時炸彈。"; break;
            case 5: text = "【道具 I2】\n裝有珍貴物資的寶箱。"; break;
            case 6: text = "【道具 I3】\n珍貴的醫療包。"; break;
            case 7: text = "【道具 I4】\n古老的神秘碎片。"; break;
            case 8: text = "【道具 I5】\n高等能量藥水。"; break;
            case 9: text = "【道具 I6】\n毀滅性的手榴彈。"; break;
            default: text = "未知的物品"; break;
        }

        if (displayUI != null)
        {
            displayUI.text = text;
        }
    }
}