using UnityEngine;
using UnityEngine.UI;

public class backpacktext : MonoBehaviour
{
    // 在 Inspector 裡面把左下角的 Text 物件拖進來
    public Text displayUI; 

    // 建立一個方法，讓 Manager 可以傳數字進來換文字
    public void UpdateDescription(int itemID)
    {
        string text = "";
        Debug.Log("jnjn");

        switch (itemID)
        {
            case 1: text = "【穿刺極樂】\n它就活在你的視線之中。\n當你展開自己的翅膀，向一位被遺忘的神明走近時，\n你腳下蠢蠢欲動的大地便已準備好將你送向樂園。"; break;
            case 2: text = "【決死之心】\n這是一把古老的武士刀。\n就同那副盔甲一樣，如果這把刀落在了懦夫的手裡，它便一點威力也沒有。。"; break;
            case 3: text = "【未解鎖】\n未解鎖。"; break;
            case 4: text = "【黃蜂】\n儘管王國會在歷史上備受矚目，但是又有誰會記得為它做出奉獻與犧牲的工蜂呢？舊日的榮耀仍在繼續綻放光輝。"; break;
            case 5: text = "【猩紅創痕】\n一位穿戴著血紅披風的傭兵唯一熱衷的事就是撕爛那匹惡狼！似乎只有黑暗才會等待那些從破滅中倖存的人們"; break;
            case 6: text = "【未解鎖】\n未解鎖。"; break;
            case 7: text = "【未解鎖】\n未解鎖。"; break;
            case 8: text = "【未解鎖】\n未解鎖。"; break;
            case 9: text = "【未解鎖】\n未解鎖。"; break;
            case 10: text = "【未解鎖】\n未解鎖。"; break;
            case 11: text = "【未解鎖】\n未解鎖。"; break;
            // ... 你可以繼續寫到 case 9
            default: text = "未知的物品"; break;
        }

        if (displayUI != null)
        {
            displayUI.text = text;
        }
    }
}
