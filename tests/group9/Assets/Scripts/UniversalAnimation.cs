using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Universal Animation script for cycling through GameObjects
/// Enables/disables GameObjects in sequence based on time intervals
/// </summary>
public class UniversalAnimation : MonoBehaviour
{
    [Header("Animation Control")]
    [SerializeField] private bool animationEnabled = true;
    
    [Header("Time Settings")]
    [SerializeField] private float timeBetweenFrames = 0.1f;
    public float AnimationPriority = 0; //The bigger the number, the higher the priority

    [Header("Alpha Fadein Options")]
    [SerializeField] private bool startWithZeroAlpha = false;
    [Tooltip("Number of objects to cycle through while gradually increasing alpha from 0 to 255 (0 = start at full alpha)")]
    [SerializeField] private int objectsToFadein = 0;
    
    [Header("Animation Objects")]
    [SerializeField] private List<GameObject> animationObjects = new List<GameObject>();
    
    // Private variables
    private bool wasAnimationEnabled = true;
    private float timer = 0f;
    private int currentIndex = 0;
    private int objectsShown = 0;
    
    public bool Enabled
    {
        get => animationEnabled;
        set
        {
            if (!wasAnimationEnabled && value)
            {
                InitializeValues();
            }
            animationEnabled = value;
            wasAnimationEnabled = value;
            
            // Enable/disable the GameObject when animation is enabled/disabled
            gameObject.SetActive(value);
        }
    }
    
    public float TimeBetweenFrames
    {
        get => timeBetweenFrames;
        set => timeBetweenFrames = Mathf.Max(0f, value);
    }
    
    public List<GameObject> AnimationObjects
    {
        get => animationObjects;
        set => animationObjects = value ?? new List<GameObject>();
    }

    private void Start()
    {
        InitializeValues();
        
        // Set the GameObject active state based on the animationEnabled value
        gameObject.SetActive(animationEnabled);
    }

    private void Update()
    {
        if (!animationEnabled || animationObjects.Count == 0)
            return;

        // Use GameManager's time scale if available, otherwise use Time.deltaTime
        float deltaTime = GameManager.Instance != null ? 
            Time.deltaTime : 
            Time.deltaTime;

        timer += deltaTime;

        if (timer >= timeBetweenFrames)
        {
            timer = 0f;
            AdvanceToNextFrame();
        }
    }

    private void OnValidate()
    {
        // Handle enable state change in inspector
        if (Application.isPlaying)
        {
            if (!wasAnimationEnabled && animationEnabled)
            {
                InitializeValues();
            }
            wasAnimationEnabled = animationEnabled;
        }
        
        // Clamp time between frames
        timeBetweenFrames = Mathf.Max(0f, timeBetweenFrames);
    }

    private void InitializeValues()
    {
        timer = 0f;
        currentIndex = 0;
        objectsShown = 0;
        
        if (animationObjects.Count > 0)
        {
            // Set initial alpha to 0 if startWithZeroAlpha is enabled
            if (startWithZeroAlpha)
            {
                SetAlphaForAllObjects(0f);
            }
            SetActiveFrame(currentIndex);
        }
    }

    private void AdvanceToNextFrame()
    {
        if (animationObjects.Count == 0)
            return;

        currentIndex = (currentIndex + 1) % animationObjects.Count;
        SetActiveFrame(currentIndex);
        
        // Gradually increase alpha over x objects
        if (startWithZeroAlpha && objectsToFadein > 0)
        {
            objectsShown++;
            if (objectsShown <= objectsToFadein)
            {
                // Calculate alpha based on progress (0 to 1)
                float alpha = Mathf.Clamp01((float)objectsShown / (float)objectsToFadein);
                SetAlphaForAllObjects(alpha);
            }
            else if (objectsShown == objectsToFadein + 1)
            {
                // Ensure alpha is exactly 1 after fadein completes
                SetAlphaForAllObjects(1f);
            }
        }
    }

    private void SetActiveFrame(int index)
    {
        // Disable all objects
        for (int i = 0; i < animationObjects.Count; i++)
        {
            if (animationObjects[i] != null)
            {
                animationObjects[i].SetActive(false);
            }
        }

        // Enable the current object
        if (index >= 0 && index < animationObjects.Count && animationObjects[index] != null)
        {
            animationObjects[index].SetActive(true);
        }
    }
    
    private void SetAlphaForAllObjects(float alpha)
    {
        foreach (GameObject obj in animationObjects)
        {
            if (obj == null) continue;
            
            // Try to set alpha for SpriteRenderer
            SpriteRenderer spriteRenderer = obj.GetComponent<SpriteRenderer>();
            if (spriteRenderer != null)
            {
                Color color = spriteRenderer.color;
                color.a = alpha;
                spriteRenderer.color = color;
            }
            
            // Try to set alpha for UI Image
            UnityEngine.UI.Image image = obj.GetComponent<UnityEngine.UI.Image>();
            if (image != null)
            {
                Color color = image.color;
                color.a = alpha;
                image.color = color;
            }
        }
    }
}
