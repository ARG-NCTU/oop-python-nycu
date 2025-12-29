using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DialogueTriggerEvent : MonoBehaviour
{
    //Handle events triggered on dialogue end 
    public int currentEventID = 0;
    // List of events to trigger
    public List<LobotomyEvents> dialogueEndEvents;
    public void TriggerDialogueEndEvent(int eventID)
    {
        dialogueEndEvents[eventID].TriggerEvent();
    }
}
