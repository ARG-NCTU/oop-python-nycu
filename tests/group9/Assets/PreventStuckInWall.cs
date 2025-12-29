using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PreventStuckInWall : MonoBehaviour
{
    public bool IsStuckInWall = false;
    // This object has box collider 2D set as trigger to detect wall collisions
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("Wall"))
        {
            IsStuckInWall = true;
            Debug.Log("Player is stuck in wall");
        }
    }
    private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("Wall"))
        {
            IsStuckInWall = false;
        }
    }
}
