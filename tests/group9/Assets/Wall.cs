using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Wall : MonoBehaviour
{
    //When player collides with wall, push them back
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.collider.CompareTag("Player"))
        {
            Vector2 pushDirection = collision.transform.position - transform.position;
            pushDirection.Normalize();
            collision.collider.GetComponent<Rigidbody2D>().AddForce(pushDirection * 500f);
            Debug.Log("Player hit wall, pushing back.");
        }
    }
}
