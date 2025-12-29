using UnityEngine;
using UnityEngine.Audio;

/// <summary>
/// Audio Manager for handling background music and sound effects
/// Persists across scene changes and provides centralized audio control
/// </summary>
public class AudioManager : MonoBehaviour
{
    [System.Serializable]
    public class AudioTrack
    {
        public string name;
        public AudioClip clip;
        [Range(0f, 1f)]
        public float volume = 1f;
        public bool loop = true;
    }

    public static AudioManager Instance { get; private set; }

    [Header("Background Music")]
    [SerializeField] private AudioTrack[] backgroundTracks;
    [SerializeField] private bool playBGMOnStart = true;
    [SerializeField] private int defaultBGMIndex = 0;
    [SerializeField] private bool fadeTransitions = true;
    [SerializeField] private float fadeTime = 1f;

    [Header("Audio Sources")]
    [SerializeField] private AudioSource bgmSource;
    [SerializeField] private AudioSource sfxSource;

    [Header("Volume Settings")]
    [Range(0f, 1f)]
    [SerializeField] private float masterVolume = 1f;
    [Range(0f, 1f)]
    [SerializeField] private float bgmVolume = 0.7f;
    [Range(0f, 1f)]
    [SerializeField] private float sfxVolume = 1f;

    [Header("Audio Mixer (Optional)")]
    [SerializeField] private AudioMixerGroup bgmMixerGroup;
    [SerializeField] private AudioMixerGroup sfxMixerGroup;

    // Private variables
    private int currentBGMIndex = -1;
    private bool isFading = false;
    private Coroutine fadeCoroutine;

    // Properties
    public float MasterVolume 
    { 
        get => masterVolume; 
        set 
        { 
            masterVolume = Mathf.Clamp01(value);
            UpdateVolumes();
        } 
    }
    
    public float BGMVolume 
    { 
        get => bgmVolume; 
        set 
        { 
            bgmVolume = Mathf.Clamp01(value);
            UpdateBGMVolume();
        } 
    }
    
    public float SFXVolume 
    { 
        get => sfxVolume; 
        set 
        { 
            sfxVolume = Mathf.Clamp01(value);
            UpdateSFXVolume();
        } 
    }

    public bool IsBGMPlaying => bgmSource.isPlaying;
    public bool IsFading => isFading;
    public string CurrentBGMName => currentBGMIndex >= 0 && currentBGMIndex < backgroundTracks.Length ? backgroundTracks[currentBGMIndex].name : "None";

    private void Awake()
    {
        // Singleton pattern - ensure only one AudioManager exists
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            InitializeAudioSources();
        }
        else
        {
            Destroy(gameObject);
            return;
        }
    }

    private void Start()
    {
        if (playBGMOnStart && backgroundTracks.Length > 0 && defaultBGMIndex >= 0 && defaultBGMIndex < backgroundTracks.Length)
        {
            PlayBGM(defaultBGMIndex);
        }
    }

    private void InitializeAudioSources()
    {
        // Create BGM audio source if not assigned
        if (bgmSource == null)
        {
            GameObject bgmObject = new GameObject("BGM Source");
            bgmObject.transform.SetParent(transform);
            bgmSource = bgmObject.AddComponent<AudioSource>();
        }

        // Create SFX audio source if not assigned
        if (sfxSource == null)
        {
            GameObject sfxObject = new GameObject("SFX Source");
            sfxObject.transform.SetParent(transform);
            sfxSource = sfxObject.AddComponent<AudioSource>();
        }

        // Configure BGM source
        bgmSource.loop = true;
        bgmSource.playOnAwake = false;
        if (bgmMixerGroup != null)
            bgmSource.outputAudioMixerGroup = bgmMixerGroup;

        // Configure SFX source
        sfxSource.loop = false;
        sfxSource.playOnAwake = false;
        if (sfxMixerGroup != null)
            sfxSource.outputAudioMixerGroup = sfxMixerGroup;

        UpdateVolumes();
    }

    /// <summary>
    /// Play background music by index
    /// </summary>
    /// <param name="trackIndex">Index of the track in backgroundTracks array</param>
    /// <param name="forceRestart">If true, restarts the track even if it's already playing</param>
    public void PlayBGM(int trackIndex, bool forceRestart = false)
    {
        if (trackIndex < 0 || trackIndex >= backgroundTracks.Length)
        {
            Debug.LogWarning($"AudioManager: Invalid BGM track index {trackIndex}");
            return;
        }

        // Check if the same track is already playing
        if (currentBGMIndex == trackIndex && bgmSource.isPlaying && !forceRestart)
        {
            return;
        }

        AudioTrack track = backgroundTracks[trackIndex];
        
        if (track.clip == null)
        {
            Debug.LogWarning($"AudioManager: BGM track '{track.name}' has no audio clip assigned");
            return;
        }

        if (fadeTransitions && bgmSource.isPlaying)
        {
            // Fade transition
            if (fadeCoroutine != null)
                StopCoroutine(fadeCoroutine);
            
            fadeCoroutine = StartCoroutine(FadeBGMTransition(track, trackIndex));
        }
        else
        {
            // Direct switch
            PlayBGMDirect(track, trackIndex);
        }
    }

    /// <summary>
    /// Play background music by name
    /// </summary>
    /// <param name="trackName">Name of the track</param>
    /// <param name="forceRestart">If true, restarts the track even if it's already playing</param>
    public void PlayBGM(string trackName, bool forceRestart = false)
    {
        int index = System.Array.FindIndex(backgroundTracks, track => track.name == trackName);
        if (index >= 0)
        {
            PlayBGM(index, forceRestart);
        }
        else
        {
            Debug.LogWarning($"AudioManager: BGM track '{trackName}' not found");
        }
    }

    /// <summary>
    /// Stop background music
    /// </summary>
    /// <param name="fadeOut">If true, fades out the music</param>
    public void StopBGM(bool fadeOut = true)
    {
        if (!bgmSource.isPlaying) return;

        if (fadeOut && fadeTransitions)
        {
            if (fadeCoroutine != null)
                StopCoroutine(fadeCoroutine);
            
            fadeCoroutine = StartCoroutine(FadeOutBGM());
        }
        else
        {
            bgmSource.Stop();
            currentBGMIndex = -1;
        }
    }

    /// <summary>
    /// Pause background music
    /// </summary>
    public void PauseBGM()
    {
        bgmSource.Pause();
    }

    /// <summary>
    /// Resume background music
    /// </summary>
    public void ResumeBGM()
    {
        bgmSource.UnPause();
    }

    /// <summary>
    /// Play a sound effect
    /// </summary>
    /// <param name="clip">Audio clip to play</param>
    /// <param name="volume">Volume multiplier (0-1)</param>
    public void PlaySFX(AudioClip clip, float volume = 1f)
    {
        if (clip == null) return;
        
        sfxSource.PlayOneShot(clip, volume * sfxVolume * masterVolume);
    }

    /// <summary>
    /// Get available BGM track names
    /// </summary>
    /// <returns>Array of track names</returns>
    public string[] GetBGMTrackNames()
    {
        string[] names = new string[backgroundTracks.Length];
        for (int i = 0; i < backgroundTracks.Length; i++)
        {
            names[i] = backgroundTracks[i].name;
        }
        return names;
    }

    private void PlayBGMDirect(AudioTrack track, int trackIndex)
    {
        bgmSource.clip = track.clip;
        bgmSource.loop = track.loop;
        bgmSource.volume = track.volume * bgmVolume * masterVolume;
        bgmSource.Play();
        currentBGMIndex = trackIndex;
    }

    private System.Collections.IEnumerator FadeBGMTransition(AudioTrack newTrack, int newTrackIndex)
    {
        isFading = true;
        float startVolume = bgmSource.volume;
        
        // Fade out current track
        float elapsed = 0f;
        while (elapsed < fadeTime * 0.5f)
        {
            elapsed += Time.unscaledDeltaTime;
            bgmSource.volume = Mathf.Lerp(startVolume, 0f, elapsed / (fadeTime * 0.5f));
            yield return null;
        }
        
        // Switch to new track
        PlayBGMDirect(newTrack, newTrackIndex);
        
        // Fade in new track
        float targetVolume = newTrack.volume * bgmVolume * masterVolume;
        elapsed = 0f;
        while (elapsed < fadeTime * 0.5f)
        {
            elapsed += Time.unscaledDeltaTime;
            bgmSource.volume = Mathf.Lerp(0f, targetVolume, elapsed / (fadeTime * 0.5f));
            yield return null;
        }
        
        bgmSource.volume = targetVolume;
        isFading = false;
        fadeCoroutine = null;
    }

    private System.Collections.IEnumerator FadeOutBGM()
    {
        isFading = true;
        float startVolume = bgmSource.volume;
        float elapsed = 0f;
        
        while (elapsed < fadeTime)
        {
            elapsed += Time.unscaledDeltaTime;
            bgmSource.volume = Mathf.Lerp(startVolume, 0f, elapsed / fadeTime);
            yield return null;
        }
        
        bgmSource.Stop();
        bgmSource.volume = startVolume;
        currentBGMIndex = -1;
        isFading = false;
        fadeCoroutine = null;
    }

    private void UpdateVolumes()
    {
        UpdateBGMVolume();
        UpdateSFXVolume();
    }

    private void UpdateBGMVolume()
    {
        if (bgmSource != null && currentBGMIndex >= 0 && currentBGMIndex < backgroundTracks.Length)
        {
            bgmSource.volume = backgroundTracks[currentBGMIndex].volume * bgmVolume * masterVolume;
        }
    }

    private void UpdateSFXVolume()
    {
        if (sfxSource != null)
        {
            sfxSource.volume = sfxVolume * masterVolume;
        }
    }

    private void OnValidate()
    {
        // Update volumes in editor when values change
        if (Application.isPlaying)
        {
            UpdateVolumes();
        }
    }
}
