using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Freeze : MonoBehaviour
{
    public float boundary;
    Rigidbody2D rb;
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        if (this.transform.position.y <= boundary)
        {

            rb.velocity = Vector3.zero;
            rb.gravityScale = 0;
        }
    }
}
