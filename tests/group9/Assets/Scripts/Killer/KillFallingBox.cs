using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KillFallingBox : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (this.transform.position.y < 0f)
        {
            Destroy(this.gameObject);
        }
    }
}
