using UnityEngine;
using UnityEditor;

#if UNITY_EDITOR
/// <summary>
/// Custom inspector for DialogueManager with test buttons
/// </summary>
[CustomEditor(typeof(DialogueManager))]
public class DialogueManagerEditor : Editor
{
    public override void OnInspectorGUI()
    {
        // Draw default inspector
        DrawDefaultInspector();
        
        EditorGUILayout.Space();
        EditorGUILayout.LabelField("Inspector Testing", EditorStyles.boldLabel);
        
        DialogueManager dialogueManager = (DialogueManager)target;
        
        // Only show buttons in play mode
        if (Application.isPlaying)
        {
            EditorGUILayout.HelpBox("Test buttons are active in Play Mode. Use these to test your dialogue system.", MessageType.Info);
            
            EditorGUILayout.BeginHorizontal();
            
            // Start dialogue by index button
            if (GUILayout.Button("Start Dialogue (By Index)"))
            {
                dialogueManager.TestStartDialogueByIndex();
            }
            
            // Start dialogue by name button
            if (GUILayout.Button("Start Dialogue (By Name)"))
            {
                dialogueManager.TestStartDialogueByName();
            }
            
            EditorGUILayout.EndHorizontal();
            
            EditorGUILayout.BeginHorizontal();
            
            // End dialogue button
            if (GUILayout.Button("End Dialogue"))
            {
                dialogueManager.TestEndDialogue();
            }
            
            // Next dialogue set button
            if (GUILayout.Button("Next Dialogue Set"))
            {
                dialogueManager.TestNextDialogueSet();
            }
            
            EditorGUILayout.EndHorizontal();
            
            EditorGUILayout.Space();
            
            // Show available sets button
            if (GUILayout.Button("Show Available Dialogue Sets"))
            {
                dialogueManager.ShowAvailableDialogueSets();
            }
            
            // Current dialogue status
            EditorGUILayout.Space();
            EditorGUILayout.LabelField("Current Status:", EditorStyles.boldLabel);
            EditorGUILayout.LabelField($"Dialogue Active: {dialogueManager.IsDialogueActive}");
            EditorGUILayout.LabelField($"Currently Typing: {dialogueManager.IsTyping}");
            
            if (dialogueManager.IsDialogueActive)
            {
                EditorGUILayout.LabelField($"Current Set: {dialogueManager.CurrentSetIndex} ({dialogueManager.CurrentSet?.setName})");
                EditorGUILayout.LabelField($"Current Line: {dialogueManager.CurrentLineIndex}");
            }
        }
        else
        {
            EditorGUILayout.HelpBox("Test buttons will appear here when in Play Mode. Set up your dialogue sets above, then enter Play Mode to test them.", MessageType.Warning);
            
            // Show available sets in edit mode
            EditorGUILayout.Space();
            if (GUILayout.Button("Show Available Dialogue Sets"))
            {
                dialogueManager.ShowAvailableDialogueSets();
            }
        }
        
        // Quick setup help
        EditorGUILayout.Space();
        EditorGUILayout.LabelField("Quick Setup Guide:", EditorStyles.boldLabel);
        EditorGUILayout.HelpBox(
            "1. Assign UI References (DialogueSystemPanel, BoxImage, etc.)\n" +
            "2. Create Dialogue Sets in the list above\n" +
            "3. Add Dialogue Lines to each set\n" +
            "4. Set Speaker (Left/Right/None) for each line\n" +
            "5. Enter Play Mode and use test buttons below",
            MessageType.Info
        );
    }
}
#endif