using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DirectionEnlarge : MonoBehaviour
{

    public float Rate = 1.5f;
    private int direction = 1; // 1 for right, -1 for left
    // Update is called once per frame
    void Start()
    {
        if (this.transform.localScale.x < 0)
        {
            direction = -1;
        }
    }
    void Update()
    {
        float enlargeRate = Rate * Time.deltaTime;
        this.transform.localScale += new Vector3(enlargeRate * direction, enlargeRate, 0);
    }
}
