using System.Collections;
using System.Collections.Generic;
using Unity.Mathematics;
using UnityEngine;

public class BombSplit : MonoBehaviour
{

    public GameObject small_bomb_prefab;
    public int var;
    public List<int> angles;
    public float timer = 1f;
    Animator anim;

    void Start()
    {
        anim = GetComponent<Animator>();
    }


    void Update()
    {
        timer -= Time.deltaTime;
        if (timer <= 0f)
        {
            // switch to bomb animation
            anim.SetInteger("status", 1);

            // small bomb
            for (int i = 0; i < angles.Count; i++)
            {
                GameObject inkPrefab = Instantiate(small_bomb_prefab, transform.position, quaternion.identity);
                Rigidbody2D newrb = inkPrefab.GetComponent<Rigidbody2D>();
                Vector2 dir = Quaternion.AngleAxis(angles[i], Vector3.forward) * transform.right;

                newrb.velocity = dir.normalized * var;
            }
            Destroy(this.gameObject);
        }
    }
}
