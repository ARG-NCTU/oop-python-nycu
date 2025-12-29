using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CautionBoxShine : MonoBehaviour
{

    public float lifetime = 1.5f;
    public float totalShine = 3f;
    private float alpha = 0f;
    private bool fading = true;
    // Start is called before the first frame update
    void Start()
    {
        Destroy(gameObject, lifetime);
    }

    // Update is called once per frame
    void Update()
    {
        if (fading)
        {
            alpha -= Time.deltaTime * totalShine * 2 / lifetime;
            if (alpha <= 0f)
            {
                fading = false;
            }
        }
        else
        {
            alpha += Time.deltaTime * totalShine * 2 / lifetime;
            if (alpha >= 1f)
            {
                fading = true;
            }
        }
        Color currentColor = GetComponent<SpriteRenderer>().color;
        currentColor.a = alpha;
        GetComponent<SpriteRenderer>().color = currentColor;
    }
}
