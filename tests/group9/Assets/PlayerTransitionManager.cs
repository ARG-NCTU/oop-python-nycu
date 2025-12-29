using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerTransitionManager : MonoBehaviour
{
    // Start is called before the first frame update
    public int SpawnIndex = 0;
    public float globalTimer = 0f;
    void Start()
    {
        if (FindObjectsOfType<PlayerTransitionManager>().Length > 1)
        {
            //destroy the one with less timer to keep the old one
            PlayerTransitionManager existingManager = FindObjectsOfType<PlayerTransitionManager>()[0];
            PlayerTransitionManager newManager = FindObjectsOfType<PlayerTransitionManager>()[1];
            if (existingManager.globalTimer > newManager.globalTimer)
            {
                Destroy(newManager.gameObject);
            }
            else
            {
                Destroy(existingManager.gameObject);
            }              
        }
        DontDestroyOnLoad(this.gameObject);
        //find object with tag "spawn" , look for the one with the correct index and move player to that position
        GameObject[] spawns = GameObject.FindGameObjectsWithTag("Spawn");
        foreach (GameObject spawn in spawns)
        {
            SpawnPoint sp = spawn.GetComponent<SpawnPoint>();
            if (sp != null && sp.Index == SpawnIndex)
            {
                Debug.Log("Spawning player at index: " + SpawnIndex);
                GameObject player = this.gameObject;
                if (player != null)
                {
                    player.transform.position = spawn.transform.position;
                }
                break;
            }
        }
    }
    //once scene is loaded, move player to spawn point with correct index
    void OnLevelWasLoaded(int level)
    {
        //find object with tag "spawn" , look for the one with the correct index and move player to that position
        GameObject[] spawns = GameObject.FindGameObjectsWithTag("Spawn");
        foreach (GameObject spawn in spawns)
        {
            SpawnPoint sp = spawn.GetComponent<SpawnPoint>();
            if (sp != null && sp.Index == SpawnIndex)
            {
                Debug.Log("Spawning player at index: " + SpawnIndex);
                GameObject player = this.gameObject;
                if (player != null)
                {
                    player.transform.position = spawn.transform.position;
                }
                break;
            }
        }
    }
    void Update()
    {
        globalTimer += Time.deltaTime;
    }

    
}
