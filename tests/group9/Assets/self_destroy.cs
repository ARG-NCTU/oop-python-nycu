using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class self_destroy : MonoBehaviour
{
    // Start is called before the first frame update
    public float life_time = 1;
    void Start()
    {
        Destroy(gameObject, life_time);
    }
}
