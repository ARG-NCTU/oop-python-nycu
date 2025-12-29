using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LobotomyEvents : MonoBehaviour
{
    public enum EventType
    {
        BattleStart,
        BattleEnd,
        ItemReceived,
        CutScene
    }
    [SerializeField] private List<GameObject> EnemyToAct;
    [SerializeField] private Vector3 CameraPosition;
    [SerializeField] private float waitTime;
    [SerializeField] private float CameraSpeed;
    [SerializeField] GameObject BattleTrigger;
    public EventType eventType;
    public CameraController cameraController;
    public void TriggerEvent()
    {
        if (eventType == EventType.BattleStart)
        {
            if (EnemyToAct != null)
            {
                foreach (var enemy in EnemyToAct)
                {
                    enemy.SetActive(true);
                }
            }
        }
        else if (eventType == EventType.ItemReceived)
        {
            // Code to give item to player
        }
        else if (eventType == EventType.BattleEnd)
        {
            if (EnemyToAct != null)
            {
                foreach (var enemy in EnemyToAct)
                {
                    enemy.SetActive(false);
                }
            }
        }
        else if (eventType == EventType.CutScene)
        {
            if (cameraController != null)
            {
                cameraController.PlayCutsceneCamera(CameraPosition, waitTime, CameraSpeed);
                StartCoroutine(ActivateBattleTriggerAfterDelay(8f));
            }
        }
    }

    private IEnumerator ActivateBattleTriggerAfterDelay(float delay)
    {
        yield return new WaitForSeconds(delay);
        if (BattleTrigger != null)
        {
            BattleTrigger.SetActive(true);
        }
    }
}
