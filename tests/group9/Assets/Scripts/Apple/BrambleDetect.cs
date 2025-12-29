using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BrambleDetect : MonoBehaviour
{
    private float touchedTime;
    private int brambleContactCount;
    public int totalDrilled;

    public PlayerStats playerStats;

    void Start()
    {
        touchedTime = 5f;
        brambleContactCount = 0;
        playerStats = this.GetComponent<PlayerStats>();
    }
    void Update()
    {
        if (brambleContactCount > 0)
        {
            touchedTime -= Time.deltaTime;
            if (touchedTime <= 0)
            {
                totalDrilled++;
                touchedTime = 5f;
            }
        }
    }



    void OnTriggerEnter2D(Collider2D collision)
    {
        // print("test0");
        if (collision.gameObject.CompareTag("bramble"))
        {
            print("test1");
            brambleContactCount++;
        }
    }

    void OnTriggerExit2D(Collider2D collision)
    {
        // print("test2");
        if (collision.gameObject.CompareTag("bramble"))
        {
            print("test3");
            brambleContactCount--;
            if (brambleContactCount == 0)
            {
                touchedTime = 5f;
            }
            playerStats.RemoveBuff("Slow");
            playerStats.WalkSpeedAdjustment = 10f / 8f;
            print(playerStats.WalkSpeedAdjustment);
        }
    }
}
