using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class deco_enemy : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //if there exsist a enemy game object, kill self
        if (GameObject.FindWithTag("Enemy") != null)
        {
            Destroy(gameObject);
        }
    }
}
