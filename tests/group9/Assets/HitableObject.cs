using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HitableObject : MonoBehaviour
{
    // Start is called before the first frame update
    public EnemyStats enemyStats;
    void Update()
    {
        if (enemyStats.currentHealth <= 0)
        {
            Destroy(gameObject);
        }
    }
}
