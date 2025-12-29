using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;

using UnityEngine;

public class BattlePanelController : MonoBehaviour
{
    // Start is called before the first frame update
    public PlayerStats playerstats;
    public EnemyStats enemystats;
    public GameObject player_side_panel;
    public GameObject boss_side_panel;
    public Image HPbar;
    public Image SPbar;
    public Image BossHPbar;
    public GameObject Heal_1;
    public GameObject Heal_2;
    public GameObject Heal_3;

    public float previousHP = 100;
    public float currentHP;
    public float shakeDuration = 0.5f;

    void Update()
    {
        if (playerstats == null)
        {
            playerstats = FindObjectOfType<PlayerStats>();
        }
        if (enemystats == null)
        {
            enemystats = FindObjectOfType<EnemyStats>();
        }
        // Update HP and SP bars according to player stats
        float hpRatio = (float)playerstats.currentHealth / playerstats.maxHealth;
        float spRatio = (float)playerstats.currentSanity / playerstats.maxSanity;
        HPbar.fillAmount = hpRatio;
        SPbar.fillAmount = spRatio;
        //update heal icons
        int healCount = playerstats.currentHealCount;
        Heal_1.SetActive(healCount >= 1);
        Heal_2.SetActive(healCount >= 2);
        Heal_3.SetActive(healCount >= 3);

        // Update boss HP
        float bossHpRatio = (float)enemystats.currentHealth / enemystats.maxHealth;
        boss_side_panel.SetActive(true);
        BossHPbar.fillAmount = bossHpRatio;

        if (bossHpRatio <= 0f)
        {
            boss_side_panel.SetActive(false);
        }
    }
    


}
