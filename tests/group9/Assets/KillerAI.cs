using System.Collections;
using System.Collections.Generic;
using Unity.Mathematics;
using Unity.VisualScripting;
using UnityEditor.Callbacks;
using UnityEngine;
using System;
using Random = UnityEngine.Random;
using Object = UnityEngine.Object;
using Unity.VisualScripting.FullSerializer;

/// <summary>
/// Killer Boss AI - First boss in the map
/// Only interact with the EnemyStats to reduce complexity 
/// </summary>
public class KillerAI : MonoBehaviour
{
    [Header("GameObject Prefabs")]
    public GameObject headbutt_prefab;
    public GameObject scream1_prefab;
    public GameObject scream2_prefab;
    public GameObject scream3_prefab;
    public GameObject smash_prefab;
    public GameObject caution_prefab;
    public GameObject falling_prefab;
    public GameObject raving_prefab;
    public Rigidbody2D rb;

    [Header("Effect Prefabs")]
    public GameObject head_attack_particle;
    public GameObject dead_bomb_particle;
    public GameObject smoke_particle;
    public GameObject floor_smoke_particle;
    public GameObject scream_particle;
    public GameObject raving_particle;


    public GameObject egg_prefab;
    private GameObject player;

    [Header("progress related flags")]
    private static bool isHalfTrigger;
    private bool isCoolDown;
    private bool isAttack;

    private float horizontalDetectionRange = 2.5f;
    public float speed = 1f;
    const float SLOW = 3f;
    const float FAST = 7f;

    [Header("Skill Pools")]
    private List<Func<IEnumerator>> initFirstSkillPool = new List<Func<IEnumerator>>();
    private List<Func<IEnumerator>> firstSkillPool = new List<Func<IEnumerator>>();
    private List<Func<IEnumerator>> initSecondSkillPool = new List<Func<IEnumerator>>();
    private List<Func<IEnumerator>> secondSkillPool = new List<Func<IEnumerator>>();

    [Header("Cooldown Management")]
    private float cooldownTime;
    public float lastAttackTime;
    const float WAIT_TOO_LONG = 6f;
    const float WAIT_TOO_LONG_SECOND = 3f;
    private bool isDying = false;
    public CameraController cameraController;

    public EnemyStats enemyStats;
    Quaternion no_rotation = Quaternion.Euler(0, 0, 0);
    public float var = 0f;

    private enum statusList
    {
        stop,
        walk,
        headbutt,
        charging,
        jump,
        scream,
        dead,
        bigjump
    }
    Animator anim;


    void Start()
    {
        Debug.Log("Killer AI initialized");
        isHalfTrigger = false;
        isCoolDown = false;
        lastAttackTime = 0f;
        rb = this.GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
        player = GameObject.FindGameObjectWithTag("Player");
        // Find CameraController for screen shake effect
        cameraController = FindObjectOfType<CameraController>();
        if (cameraController == null)
        {
            Debug.LogWarning("KillerAI: CameraController not found. Screen shake effects will not work.");
        }

        // init first skill pools
        initFirstSkillPool.Add(HeadButtAttack);
        initFirstSkillPool.Add(() => Scream(SLOW));
        initFirstSkillPool.Add(Smash);
        firstSkillPool = new List<Func<IEnumerator>>(initFirstSkillPool);

        // init second skill pools
        initSecondSkillPool.Add(HeadButtAttack);
        initSecondSkillPool.Add(EarthQuake);
        initSecondSkillPool.Add(EarthQuake);
        initSecondSkillPool.Add(Smash);
        initSecondSkillPool.Add(Raving);
        initSecondSkillPool.Add(Raving);
        secondSkillPool = new List<Func<IEnumerator>>(initSecondSkillPool);


    }

    void Update()
    {
        if (isAttack || isDying) return;
        lastAttackTime += Time.deltaTime;
        // when cooldown, nothing should update expect the not-attack time
        if (isCoolDown)
        {
            cooldownTime -= Time.deltaTime;
            if (cooldownTime < 0f) isCoolDown = false;
            return;
        }

        if (enemyStats.currentHealth <= 0)
        {
            isDying = true;
            rb.gravityScale = 0;
            rb.velocity = new Vector2(PlayerDirection() * -1f, 0.2f);
            anim.Play("dead");
            // delete boss
            StartCoroutine(Dead());
        }

        if (isHalfTrigger == false)
        {
            if (enemyStats.CurrentHealth <= enemyStats.MaxHealth / 2)
            {
                isHalfTrigger = true;
            }
            if (IsPlayerInHorizontalRange() == false)
            {
                // move to player
                moveToPlayer();
                cooldown(1f);

            }
            else
            {
                cooldown(2.5f);
                PickFirstSkillPool();
                lastAttackTime = 0f;
            }
            if (lastAttackTime > WAIT_TOO_LONG)
            {
                // use scream(fast)
                StartCoroutine(Scream(FAST));
                lastAttackTime = 0f;
            }
        }
        else
        {
            if (IsPlayerInHorizontalRange() == false)
            {
                // move to player
                moveToPlayer();
                cooldown(0.5f);
            }
            else
            {
                cooldown(2.5f);
                PickSecondSkillPool();
                lastAttackTime = 0f;
            }
            if (lastAttackTime > WAIT_TOO_LONG_SECOND)
            {
                // use scream(fast)
                StartCoroutine(Scream(FAST));
                lastAttackTime = 0f;
            }
        }
    }

    #region Assistant Functions

    // calculate both direction and distance
    private float CalculateHorizontDifference()
    {
        if (player == null) return 0f;

        Vector3 playerPosition = player.transform.position;
        Vector3 bossPosition = this.transform.position;
        float horizontalDifference = playerPosition.x - bossPosition.x;

        return horizontalDifference;
    }
    // check distance
    private bool IsPlayerInHorizontalRange()
    {
        float horizontalDistance = Mathf.Abs(CalculateHorizontDifference());
        return horizontalDistance <= var;
    }

    // check player direction (-1 for left, 1 for right)
    private float PlayerDirection()
    {
        float horizontalDirection = Mathf.Sign(CalculateHorizontDifference());
        return horizontalDirection;
    }

    void moveToPlayer()
    {
        // switch to move animation
        anim.SetInteger("status", (int)statusList.walk);
        // move
        rb.velocity = new Vector2(PlayerDirection() * speed, rb.velocity.y);
    }


    void cooldown(float time)
    {
        // switch to rest animation

        cooldownTime = time;
        isCoolDown = true;
    }

    /// template code to create prefab
    // void createTestPrefab()
    // {
    //     if (timer <= 0f)
    //     {
    //         // GameObject ya = Instantiate(test_prefab, posnew, Quaternion.Euler(rotnew));
    //         timer = 2f;
    //         Debug.Log("Killer AI spawned an object");
    //     }
    //     timer -= Time.deltaTime;
    // }

    IEnumerator Dead()
    {
        yield return new WaitForSeconds(2.5f);
        // add explosion effect
        Vector3 particle_spawnPosition = this.transform.position + new Vector3(0, 0, -2f);
        Object.Instantiate(dead_bomb_particle, particle_spawnPosition, no_rotation);

        // destroy object
        Destroy(this.gameObject);
    }

    #endregion

    #region Skills
    IEnumerator HeadButtAttack()
    {
        isAttack = true;
        anim.SetInteger("status", (int)statusList.charging);
        yield return new WaitForSeconds(1.5f);
        // switch to headbutt animation
        anim.Play("headbutt");
        anim.SetInteger("status", (int)statusList.headbutt);

        // first attack
        Vector3 spawnPosition = this.transform.position + new Vector3(PlayerDirection() * 2.2f, 0, 0);
        spawnPosition.y = 1f;
        Object.Instantiate(headbutt_prefab, spawnPosition, no_rotation);
        Vector3 particle_spawnPosition = new Vector3(spawnPosition.x, spawnPosition.y + 0.5f, -2);
        Object.Instantiate(head_attack_particle, particle_spawnPosition, no_rotation);
        yield return new WaitForSeconds(1f);

        // stop
        anim.SetInteger("status", (int)statusList.stop);
        yield return new WaitForSeconds(1f);

        // second attack
        anim.Play("headbutt");
        anim.SetInteger("status", (int)statusList.headbutt);
        Object.Instantiate(headbutt_prefab, spawnPosition, no_rotation);
        particle_spawnPosition = new Vector3(spawnPosition.x, spawnPosition.y + 0.5f, -2);
        Object.Instantiate(head_attack_particle, particle_spawnPosition, no_rotation);
        yield return new WaitForSeconds(1.5f);

        // stop
        anim.SetInteger("status", (int)statusList.stop);
        isAttack = false;
    }
    IEnumerator Scream(float speedRate)
    {
        isAttack = true;
        // switch to scream animation
        anim.SetInteger("status", (int)statusList.scream);
        yield return new WaitForSeconds(1.5f);

        // show scream effect
        Vector3 particle_spawnPosition = new Vector3(this.transform.position.x, 5f, -2);
        Object.Instantiate(scream_particle, particle_spawnPosition, no_rotation);

        // 6 direction AOE
        int[] direction = new int[] { -5, 30, 70, 110, 150, 185 }; // test for different direction
        for (int i = 0; i < direction.Length; i++)
        {
            Vector3 spawnPosition = this.transform.position;
            spawnPosition.y = 3;
            Vector3 dire = new Vector3(0, 0, direction[i]);
            int rand = Random.Range(1, 4);
            GameObject screamPrefab = rand == 1 ? scream1_prefab : (rand == 2 ? scream2_prefab : scream3_prefab);
            GameObject testPrefab = Object.Instantiate(screamPrefab, spawnPosition, no_rotation);

            // make it move to correct direction
            Rigidbody2D newrb = testPrefab.GetComponent<Rigidbody2D>();
            newrb.gravityScale = 0f;
            Vector2 dir = Quaternion.AngleAxis(direction[i], Vector3.forward) * transform.right;
            newrb.velocity = dir.normalized * speed * speedRate;
        }

        yield return new WaitForSeconds(2f);
        anim.SetInteger("status", (int)statusList.stop);
        isAttack = false;
    }

    IEnumerator Smash()
    {
        isAttack = true;

        // switch to smash animation
        anim.SetInteger("status", (int)statusList.jump);
        anim.Play("jump");
        rb.velocity = new Vector2(rb.velocity.x, 5);

        // wait the smash animation
        yield return new WaitForSeconds(1.2f);

        // instantiate
        Vector3 spawnPosition = this.transform.position;
        spawnPosition.y = 1f;
        Object.Instantiate(smash_prefab, spawnPosition, no_rotation);
        for (int i = -3; i <= 3; i++)
        {
            Vector3 particle_spawnPosition = new Vector3(spawnPosition.x + 0.7f * i, 0.75f, -2);
            Object.Instantiate(floor_smoke_particle, particle_spawnPosition, no_rotation);
        }

        // cooldown 2 second
        yield return new WaitForSeconds(2f);
        anim.SetInteger("status", (int)statusList.stop);
        isAttack = false;
    }

    IEnumerator Raving()
    {
        isAttack = true;
        // switch to raving animation
        anim.SetInteger("status", (int)statusList.charging);
        yield return new WaitForSeconds(1f);
        // instantiate raving attack
        Vector3 spawnPosition = this.transform.position;
        Object.Instantiate(raving_prefab, spawnPosition, no_rotation);
        Vector3 particle_spawnPosition = new Vector3(spawnPosition.x, spawnPosition.y, -2);
        Object.Instantiate(raving_particle, particle_spawnPosition, no_rotation);


        // cooldown 2 second
        yield return new WaitForSeconds(2f);
        anim.SetInteger("status", (int)statusList.stop);
        isAttack = false;
    }

    IEnumerator EarthQuake()
    {
        isAttack = true;

        // switch to earthquake animation
        anim.SetInteger("status", (int)statusList.bigjump);
        rb.velocity = new Vector2(rb.velocity.x, 10);
        yield return new WaitForSeconds(2f);

        // back to ground and instantiate first attack
        Vector3 spawnPosition = this.transform.position;
        spawnPosition.y = 1f;
        Object.Instantiate(smash_prefab, spawnPosition, no_rotation);
        
        // Trigger screen shake effect
        if (cameraController != null)
        {
            cameraController.ScreenShake(0.5f);
        }
        
        for (int i = -3; i <= 3; i++)
        {
            Vector3 particle_spawnPosition = new Vector3(spawnPosition.x + 0.7f * i, 0.75f, -2);
            Object.Instantiate(floor_smoke_particle, particle_spawnPosition, no_rotation);
        }

        // show 5 cautioun areas
        float[] x_pos = new float[] { -6f, -3f, 0f, 3f, 6f };
        for (int i = 0; i < x_pos.Length; i++)
        {
            Vector3 cautionPosition = new Vector3(x_pos[i], 0, -2);
            Quaternion cautionRotation = Quaternion.Euler(0, 0, 0);
            Object.Instantiate(caution_prefab, cautionPosition, cautionRotation);
            Vector3 particle_spawnPosition = new Vector3(x_pos[i], 9.5f, -2);
            Object.Instantiate(smoke_particle, particle_spawnPosition, no_rotation);
        }

        // create falling attacks
        yield return new WaitForSeconds(0.5f);
        for (int i = 0; i < x_pos.Length; i++)
        {
            Vector3 cautionPositio = new Vector3(x_pos[i], 10, 0);
            Quaternion cautionRotatio = Quaternion.Euler(0, 0, 0);
            Object.Instantiate(falling_prefab, cautionPositio, cautionRotatio);
        }
        // cooldown 3 second
        yield return new WaitForSeconds(3f);
        anim.SetInteger("status", (int)statusList.stop);
        isAttack = false;
    }

    void PickFirstSkillPool()
    {
        Vector3 playerPosition = player.transform.position;
        Vector3 bossPosition = this.transform.position;
        Debug.Log(playerPosition.x);
        Debug.Log(bossPosition.x);

        int index = Random.Range(0, firstSkillPool.Count);
        print(index);

        Func<IEnumerator> skill = firstSkillPool[index];
        firstSkillPool.RemoveAt(index);
        if (firstSkillPool.Count == 0)
        {
            print("reset first skill pool");
            firstSkillPool = new List<Func<IEnumerator>>(initFirstSkillPool);
        }
        StartCoroutine(skill());
        return;

    }
    #endregion

    #region Pick Skill

    void PickSecondSkillPool()
    {
        int index = Random.Range(0, secondSkillPool.Count);
        print(index);

        Func<IEnumerator> skill = secondSkillPool[index];
        anim.SetInteger("status", (int)statusList.stop);
        StartCoroutine(skill());
        secondSkillPool.RemoveAt(index);
        if (secondSkillPool.Count == 0)
        {
            secondSkillPool = new List<Func<IEnumerator>>(initSecondSkillPool);
        }
    }

    #endregion
}