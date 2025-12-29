using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TransitionCollider : MonoBehaviour
{
    public TransitionScript transitionAnimator;
    public string gameSceneName = "NextSceneName";
    public PlayerController playerController;
    private float TransitionCoolDown = 1f;
    public int spawnIndex = 0;

    
    void Start()
    {
        TransitionCoolDown = 1f;
        //find playerController if not set
        if (playerController == null)
        {
            playerController = GameObject.FindGameObjectWithTag("Player").GetComponent<PlayerController>();
        }
    }
    void Update()
    {
        if (TransitionCoolDown > 0)
        {
            TransitionCoolDown -= Time.deltaTime;
        }
    }
    //when player enters trigger, load next scene
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (playerController != null)
        {
            playerController = GameObject.FindGameObjectWithTag("Player").GetComponent<PlayerController>();
        }
        if (collision.CompareTag("Player") && TransitionCoolDown <= 0)
        {
            playerController.SetDummyState(1.1f);
            transitionAnimator.StartCoroutine(transitionAnimator.LoadGameScene(gameSceneName));
            PlayerTransitionManager transitionManager = FindObjectOfType<PlayerTransitionManager>();
            if (transitionManager != null)
            {
                transitionManager.SpawnIndex = spawnIndex; // Set the spawn index for the next scene
            }
        }
    }
}
