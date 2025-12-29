using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BattleEndChecker : MonoBehaviour
{
    // Start is called before the first frame update
    [SerializeField] private LobotomyEvents battleEndEvent;
    void LateUpdate()
    {
        //check if any Enemy tag gameobject exsists
        if (GameObject.FindGameObjectWithTag("Enemy") == null)
        {
            battleEndEvent.TriggerEvent();
        }
    }

}
