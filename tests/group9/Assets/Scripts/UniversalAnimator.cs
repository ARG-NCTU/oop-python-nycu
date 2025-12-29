using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Universal Animator manages multiple animation sets with priority system
/// Handles switching between animation sets based on priorities
/// Each animation set should be a GameObject with a UniversalAnimation component
/// </summary>
public class UniversalAnimator : MonoBehaviour
{
    [Header("Animation Sets")]
    [SerializeField] private List<GameObject> animationSets = new List<GameObject>();
    
    [Header("Current State")]
    [SerializeField] private int currentAnimationIndex = 0;
    
    [Header("Debug")]
    [SerializeField] private bool showDebugInfo = false;
    
    // Cached UniversalAnimation components for performance
    private List<UniversalAnimation> animationComponents = new List<UniversalAnimation>();
    
    // Properties
    public int CurrentAnimationIndex
    {
        get => currentAnimationIndex;
        private set => currentAnimationIndex = value;
    }
    
    public List<GameObject> AnimationSets
    {
        get => animationSets;
        set
        {
            animationSets = value ?? new List<GameObject>();
            CacheAnimationComponents();
        }
    }
    
    public int AnimationSetCount => animationSets.Count;
    
    private void Awake()
    {
        // Cache all animation components for performance
        CacheAnimationComponents();
        
        // Force enable the default animation (index 0)
        if (animationSets.Count > 0)
        {
            ForceEnableAnimation(0);
        }
        else if (showDebugInfo)
        {
            Debug.LogWarning($"UniversalAnimator '{gameObject.name}': No animation sets assigned!");
        }
    }
    
    private void OnValidate()
    {
        // Ensure currentAnimationIndex is within bounds
        if (animationSets.Count > 0)
        {
            currentAnimationIndex = Mathf.Clamp(currentAnimationIndex, 0, animationSets.Count - 1);
        }
        else
        {
            currentAnimationIndex = 0;
        }
    }
    
    /// <summary>
    /// Enable animation by index if it has equal or higher priority than current animation
    /// </summary>
    /// <param name="index">Index of the animation set to enable</param>
    /// <returns>True if animation was enabled, false if blocked by priority</returns>
    public bool EnableAnimation(int index)
    {
        // Validate index
        if (!IsValidIndex(index))
        {
            if (showDebugInfo)
            {
                Debug.LogWarning($"UniversalAnimator '{gameObject.name}': Invalid animation index {index}. Valid range: 0-{animationSets.Count - 1}");
            }
            return false;
        }
        
        // Get priorities
        float currentPriority = GetAnimationPriority(currentAnimationIndex);
        float newPriority = GetAnimationPriority(index);
        
        // Check if new animation has equal or higher priority
        if (newPriority >= currentPriority)
        {
            ForceEnableAnimation(index);
            return true;
        }
        else
        {
            if (showDebugInfo)
            {
                string currentName = GetAnimationName(currentAnimationIndex);
                string newName = GetAnimationName(index);
                Debug.Log($"UniversalAnimator '{gameObject.name}': Cannot enable '{newName}' (priority: {newPriority}) over '{currentName}' (priority: {currentPriority})");
            }
            return false;
        }
    }
    
    /// <summary>
    /// Force enable animation by index regardless of priority
    /// </summary>
    /// <param name="index">Index of the animation set to enable</param>
    /// <returns>True if animation was enabled, false if index is invalid</returns>
    public bool ForceEnableAnimation(int index)
    {
        // Validate index
        if (!IsValidIndex(index))
        {
            if (showDebugInfo)
            {
                Debug.LogWarning($"UniversalAnimator '{gameObject.name}': Invalid animation index {index}. Valid range: 0-{animationSets.Count - 1}");
            }
            return false;
        }
        
        // Disable all animation sets
        DisableAllAnimations();
        
        // Enable the selected animation
        if (animationComponents[index] != null)
        {
            animationComponents[index].Enabled = true;
            currentAnimationIndex = index;
            
            if (showDebugInfo)
            {
                string animationName = GetAnimationName(index);
                float priority = GetAnimationPriority(index);
                Debug.Log($"UniversalAnimator '{gameObject.name}': Force enabled animation '{animationName}' (index: {index}, priority: {priority})");
            }
            
            return true;
        }
        else
        {
            if (showDebugInfo)
            {
                Debug.LogWarning($"UniversalAnimator '{gameObject.name}': Animation set at index {index} does not have UniversalAnimation component!");
            }
            return false;
        }
    }
    
    /// <summary>
    /// Get the current animation's priority
    /// </summary>
    /// <returns>Priority of the currently active animation</returns>
    public float GetCurrentAnimationPriority()
    {
        return GetAnimationPriority(currentAnimationIndex);
    }
    
    /// <summary>
    /// Get animation priority by index
    /// </summary>
    /// <param name="index">Index of the animation set</param>
    /// <returns>Priority value, or -1 if invalid</returns>
    public float GetAnimationPriority(int index)
    {
        if (IsValidIndex(index) && animationComponents[index] != null)
        {
            return animationComponents[index].AnimationPriority;
        }
        return -1f;
    }
    
    /// <summary>
    /// Get animation name by index
    /// </summary>
    /// <param name="index">Index of the animation set</param>
    /// <returns>Name of the animation GameObject, or "Invalid" if index is invalid</returns>
    public string GetAnimationName(int index)
    {
        if (IsValidIndex(index) && animationSets[index] != null)
        {
            return animationSets[index].name;
        }
        return "Invalid";
    }
    
    /// <summary>
    /// Check if an animation index is valid
    /// </summary>
    /// <param name="index">Index to check</param>
    /// <returns>True if index is within bounds</returns>
    public bool IsValidIndex(int index)
    {
        return index >= 0 && index < animationSets.Count;
    }
    
    /// <summary>
    /// Add an animation set to the list
    /// </summary>
    /// <param name="animationSet">GameObject with UniversalAnimation component</param>
    /// <returns>Index of the added animation set, or -1 if failed</returns>
    public int AddAnimationSet(GameObject animationSet)
    {
        if (animationSet == null)
        {
            if (showDebugInfo)
            {
                Debug.LogWarning($"UniversalAnimator '{gameObject.name}': Cannot add null animation set!");
            }
            return -1;
        }
        
        UniversalAnimation animComponent = animationSet.GetComponent<UniversalAnimation>();
        if (animComponent == null)
        {
            if (showDebugInfo)
            {
                Debug.LogWarning($"UniversalAnimator '{gameObject.name}': Animation set '{animationSet.name}' does not have UniversalAnimation component!");
            }
            return -1;
        }
        
        animationSets.Add(animationSet);
        animationComponents.Add(animComponent);
        
        if (showDebugInfo)
        {
            Debug.Log($"UniversalAnimator '{gameObject.name}': Added animation set '{animationSet.name}' at index {animationSets.Count - 1}");
        }
        
        return animationSets.Count - 1;
    }
    
    /// <summary>
    /// Remove an animation set by index
    /// </summary>
    /// <param name="index">Index of the animation set to remove</param>
    /// <returns>True if removed successfully</returns>
    public bool RemoveAnimationSet(int index)
    {
        if (!IsValidIndex(index))
        {
            if (showDebugInfo)
            {
                Debug.LogWarning($"UniversalAnimator '{gameObject.name}': Cannot remove animation at invalid index {index}");
            }
            return false;
        }
        
        string removedName = GetAnimationName(index);
        
        // If removing the current animation, switch to index 0
        if (index == currentAnimationIndex && animationSets.Count > 1)
        {
            ForceEnableAnimation(0);
        }
        
        animationSets.RemoveAt(index);
        animationComponents.RemoveAt(index);
        
        // Adjust current index if necessary
        if (currentAnimationIndex >= animationSets.Count)
        {
            currentAnimationIndex = Mathf.Max(0, animationSets.Count - 1);
        }
        
        if (showDebugInfo)
        {
            Debug.Log($"UniversalAnimator '{gameObject.name}': Removed animation set '{removedName}' from index {index}");
        }
        
        return true;
    }
    
    /// <summary>
    /// Cache UniversalAnimation components for all animation sets
    /// </summary>
    private void CacheAnimationComponents()
    {
        animationComponents.Clear();
        
        foreach (GameObject animSet in animationSets)
        {
            if (animSet != null)
            {
                UniversalAnimation animComponent = animSet.GetComponent<UniversalAnimation>();
                animationComponents.Add(animComponent);
                
                if (animComponent == null && showDebugInfo)
                {
                    Debug.LogWarning($"UniversalAnimator '{gameObject.name}': Animation set '{animSet.name}' does not have UniversalAnimation component!");
                }
            }
            else
            {
                animationComponents.Add(null);
                if (showDebugInfo)
                {
                    Debug.LogWarning($"UniversalAnimator '{gameObject.name}': Null animation set found in list!");
                }
            }
        }
    }
    
    /// <summary>
    /// Disable all animation sets
    /// </summary>
    private void DisableAllAnimations()
    {
        for (int i = 0; i < animationComponents.Count; i++)
        {
            if (animationComponents[i] != null)
            {
                animationComponents[i].Enabled = false;
            }
        }
    }
    
    #region Debug Methods
    
    /// <summary>
    /// Print debug information about all animation sets
    /// </summary>
    [ContextMenu("Debug: Print Animation Info")]
    public void DebugPrintAnimationInfo()
    {
        Debug.Log($"=== UniversalAnimator '{gameObject.name}' Debug Info ===");
        Debug.Log($"Current Animation Index: {currentAnimationIndex}");
        Debug.Log($"Total Animation Sets: {animationSets.Count}");
        
        for (int i = 0; i < animationSets.Count; i++)
        {
            string name = GetAnimationName(i);
            float priority = GetAnimationPriority(i);
            bool isActive = animationComponents[i] != null && animationComponents[i].Enabled;
            bool isCurrent = i == currentAnimationIndex;
            
            Debug.Log($"[{i}] '{name}' - Priority: {priority} - Active: {isActive} - Current: {isCurrent}");
        }
    }
    
    #endregion
}