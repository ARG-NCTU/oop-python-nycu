using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enlarge : MonoBehaviour
{

    public float Rate = 1.5f;
    // Start is called before the first frame update
    // Update is called once per frame
    void Update()
    {
        float enlargeRate = Rate * Time.deltaTime;
        this.transform.localScale += new Vector3(enlargeRate, enlargeRate, 0);
    }
}
