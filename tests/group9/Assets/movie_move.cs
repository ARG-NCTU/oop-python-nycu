using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class movie_move : MonoBehaviour
{


    // Update is called once per frame
    void Update()
    {
        //move up and down in a rhythm
        transform.position = new Vector3(transform.position.x, transform.position.y + Mathf.Sin(4*Time.time) * 0.005f, transform.position.z);

    }
}
