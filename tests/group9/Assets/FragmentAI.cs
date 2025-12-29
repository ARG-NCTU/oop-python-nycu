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
using Unity.Burst.Intrinsics;

public class FragmentAI : MonoBehaviour
{
    [Header("GameObject Prefabs")]
    public GameObject kick_prefab;
    public GameObject ink_prefab;
    public GameObject drill_prefab;
    public GameObject drill_down_prefab;
    public GameObject drill_caution_prefab;
    public GameObject drill_caution_half_prefab;
    public GameObject smash_prefab;
    public GameObject dash_attack_prefab;
    public GameObject sing_prefab;
    public GameObject echo_normal_prefab;
    public GameObject echo_enlightened_prefab;
    public Rigidbody2D rb;
    private GameObject player;

    [Header("Effect Prefabs")]
    public GameObject ink_particle;
    public GameObject smoke_particle;
    public GameObject echo_normal_particle;
    public GameObject echo_enlightened_particle;


    private enum statusList
    {
        stay,
        jump,
        kick,
        ink,
        drill,
        dash,
        echo,
        walk,
        dead
    };

    [Header("progress related variable")]
    public float speed = 1f;
    public float gravityScale = 1f;
    private static bool isHalfTrigger;
    private bool isCoolDown;
    private bool isAttack;
    private float dashSpeed = 5.5f;
    private int usedSkillCount = 0;
    private bool isDying = false;

    private List<Func<IEnumerator>> initSkillPool = new List<Func<IEnumerator>>();
    private List<Func<IEnumerator>> SkillPool = new List<Func<IEnumerator>>();


    private float cooldownTime;

    public EnemyStats enemyStats;
    public PlayerStats playerStats;
    Animator anim;

    // kick: 夠近就打
    // echo: 4->3次攻擊放一次, 如果有頓悟則消除頓悟並造成傷害
    // Drill: 1次攻擊->3連擊(echo)
    // Drill, Inkjet: enlight


    void Start()
    {
        Debug.Log("Fragment AI initialized");
        isHalfTrigger = false;
        isCoolDown = false;
        rb = this.GetComponent<Rigidbody2D>();
        player = GameObject.FindGameObjectWithTag("Player");
        anim = GetComponent<Animator>();
        playerStats = player.GetComponent<PlayerStats>();

        // initial skill pool
        initSkillPool.Add(Inkjet);
        initSkillPool.Add(Drill);
        initSkillPool.Add(Jump);
        initSkillPool.Add(MoveJump);
        initSkillPool.Add(Dash);
        // initSkillPool.Add(Echo);
        SkillPool = new List<Func<IEnumerator>>(initSkillPool);
    }

    // Update is called once per frame
    void Update()
    {
        if (enemyStats.currentHealth <= 0f)
        {
            // dead effect
            isDying = true;
            rb.gravityScale = 0;
            rb.velocity = new Vector2(PlayerDirection() * -1f, 0.7f);
            anim.Play("dead");
            // delete boss
            StartCoroutine(Dead());
        }



        if (isAttack || isDying) return;
        // when cooldown, nothing should update expect the not-attack time
        if (isCoolDown)
        {
            cooldownTime -= Time.deltaTime;
            if (cooldownTime < 0f) isCoolDown = false;
            return;
        }


        if (enemyStats.CurrentHealth <= enemyStats.MaxHealth / 2)
        {
            print("Fragment enter half health phase");
            isHalfTrigger = true;
        }

        // 4 times (or 3 times if less than half) attack will insert a echo attack
        if (!isHalfTrigger && usedSkillCount >= 4)
        {
            usedSkillCount -= 4;
            StartCoroutine(Echo());
            Cooldown(3f);
            return;
        }
        else if (isHalfTrigger && usedSkillCount >= 3)
        {
            usedSkillCount -= 3;
            StartCoroutine(Echo());
            Cooldown(2f);
            return;
        }
        // too close -> kick
        else if (math.abs(CalculateHorizontDifference()) < 2f)
        {
            StartCoroutine(Kick());
            usedSkillCount += 1;
        }
        else PickSkillPool();
        if (!isHalfTrigger) Cooldown(2f);
        else Cooldown(1f);

    }

    #region Assistant Functions
    void Cooldown(float time)
    {
        // switch to rest animation

        cooldownTime = time;
        isCoolDown = true;
    }

    private float CalculateHorizontDifference()
    {
        if (player == null) return 0f;

        Vector3 playerPosition = player.transform.position;
        Vector3 bossPosition = this.transform.position;
        float horizontalDifference = playerPosition.x - bossPosition.x;

        return horizontalDifference;
    }

    private float PlayerDirection()
    {
        float horizontalDirection = Mathf.Sign(CalculateHorizontDifference());
        return horizontalDirection;
    }

    void moveToPlayerAssist()
    {
        // switch to move animation
        anim.SetInteger("status", (int)statusList.walk);
        // move
        rb.velocity = new Vector2(PlayerDirection() * 1f, rb.velocity.y);
    }

    IEnumerator Dead()
    {
        yield return new WaitForSeconds(2.5f);
        // add explosion effect

        // destroy object
        yield return new WaitForSeconds(0.5f);
        Destroy(this.gameObject);
    }

    #endregion

    #region Skills
    IEnumerator Kick()
    {
        isAttack = true;
        moveToPlayerAssist();
        // switch to kick animation
        anim.SetInteger("status", (int)statusList.kick);
        yield return new WaitForSeconds(0.3f);

        // kick attack
        Vector3 spawnPosition = this.transform.position + new Vector3(PlayerDirection() * 1f, 0f, 0f);
        Instantiate(kick_prefab, spawnPosition, quaternion.identity);

        yield return new WaitForSeconds(2f);
        anim.SetInteger("status", (int)statusList.stay);
        isAttack = false;
    }

    IEnumerator Inkjet()
    {
        isAttack = true;
        // switch to inkjet animation
        anim.SetInteger("status", (int)statusList.kick);
        yield return new WaitForSeconds(0.5f);

        // 3 inkjet attacks
        int[] angles = new int[] { 40, 60, 75 };
        for (int i = 0; i < 3; i++)
        {
            GameObject inkPrefab = Instantiate(ink_prefab, transform.position, quaternion.identity);
            Rigidbody2D newrb = inkPrefab.GetComponent<Rigidbody2D>();
            newrb.gravityScale = gravityScale;
            Vector2 dir = Quaternion.AngleAxis(angles[i], Vector3.forward) * transform.right;

            // flip direction (I don't know how to optimize)
            if (PlayerDirection() < 0)
            {
                dir = new Vector2(-dir.x, dir.y);
            }
            newrb.velocity = dir.normalized * 12;
        }
        Vector3 particlePosition = transform.position + new Vector3(2f, 0.4f, 0);
        Instantiate(ink_particle, particlePosition, quaternion.identity);

        yield return new WaitForSeconds(1f);
        anim.SetInteger("status", (int)statusList.stay);
        isAttack = false;
    }

    IEnumerator Drill()
    {
        isAttack = true;
        // switch to drill animation
        anim.SetInteger("status", (int)statusList.drill);
        // drill into ground
        Instantiate(drill_down_prefab, new Vector3(this.transform.position.x, 0f, 0f), quaternion.identity);

        // wait for drilling
        yield return new WaitForSeconds(1f);

        // caution at player position
        Vector3 playerPos = new(player.transform.position.x, 0, -2);
        if (isHalfTrigger == false)
        {
            Instantiate(drill_caution_prefab, playerPos, quaternion.identity);
            yield return new WaitForSeconds(2f);
        }
        else
        {
            Instantiate(drill_caution_half_prefab, playerPos, quaternion.identity);
            yield return new WaitForSeconds(1.2f);
        }

        // drill out from ground towards player
        GameObject DrillOutPrefab = Instantiate(drill_prefab, playerPos + new Vector3(0f, 3f, 0f), quaternion.identity);
        if (isHalfTrigger) { DrillOutPrefab.transform.localScale = new Vector3(1.5f, 8f, 1f); }

        anim.SetInteger("status", (int)statusList.stay);
        yield return new WaitForSeconds(0.5f);
        isAttack = false;
    }
    IEnumerator Triple_Drill()
    {
        isAttack = true;
        yield return StartCoroutine(Drill());
        yield return StartCoroutine(Drill());
        yield return StartCoroutine(Drill());
        yield return new WaitForSeconds(1f);
        usedSkillCount += 2;

        isAttack = false;
    }

    IEnumerator Jump()
    {
        isAttack = true;

        // switch to jump animation
        anim.SetInteger("status", (int)statusList.jump);
        // jump
        rb.velocity = new Vector2(rb.velocity.x, 10);
        yield return new WaitForSeconds(2.1f);

        // smash attack
        Vector3 spawnPosition = this.transform.position;
        spawnPosition.y = 1f;
        Object.Instantiate(smash_prefab, spawnPosition, quaternion.identity);
        for (int i = -3; i <= 3; i++)
        {
            Vector3 particle_spawnPosition = new Vector3(spawnPosition.x + 0.7f * i, 0.75f, -2);
            Object.Instantiate(smoke_particle, particle_spawnPosition, quaternion.identity);
        }

        // cooldown 0.5 second
        anim.SetInteger("status", 0);
        yield return new WaitForSeconds(0.5f);
        isAttack = false;
    }

    IEnumerator MoveJump()
    {
        isAttack = true;

        // switch to jump animation
        anim.SetInteger("status", (int)statusList.jump);
        // move and jump
        rb.velocity = new Vector2(rb.velocity.x + PlayerDirection() * 2, 10);
        yield return new WaitForSeconds(2.1f);

        // smash attack
        Vector3 spawnPosition = this.transform.position;
        spawnPosition.y = 1f;
        Object.Instantiate(smash_prefab, spawnPosition, quaternion.identity);
        for (int i = -3; i <= 3; i++)
        {
            Vector3 particle_spawnPosition = new Vector3(spawnPosition.x + 0.7f * i, 0.75f, -2);
            Object.Instantiate(smoke_particle, particle_spawnPosition, quaternion.identity);
        }

        // cooldown 1.5 second
        anim.SetInteger("status", 0);
        yield return new WaitForSeconds(1.5f);
        isAttack = false;
    }

    IEnumerator Dash()
    {
        isAttack = true;
        // switch to dash animation
        anim.SetInteger("status", (int)statusList.dash);
        // dash towards player
        float attackDirection = PlayerDirection();
        rb.velocity = new Vector2(PlayerDirection() * dashSpeed, rb.velocity.y);

        // cooldown 2 second
        yield return new WaitForSeconds(1f);
        rb.velocity = new Vector2(0f, rb.velocity.y);

        // attack after dash
        anim.SetInteger("status", (int)statusList.kick);
        Vector3 spawnPosition = this.transform.position + new Vector3(attackDirection * 1.5f, 0f, 0f);
        Instantiate(dash_attack_prefab, spawnPosition, quaternion.identity);

        yield return new WaitForSeconds(0.5f);
        anim.SetInteger("status", (int)statusList.stay);
        isAttack = false;
    }

    // abandoned attack
    // IEnumerator Sing()
    // {
    //     isAttack = true;
    //     // switch to sing animation

    //     // sing attack
    //     GameObject singPrefab = Instantiate(sing_prefab, transform.position, quaternion.identity);
    //     if (PlayerDirection() < 0)
    //     {
    //         singPrefab.transform.localScale = new Vector3(-1f, 1f, 1f);
    //     }


    //     yield return new WaitForSeconds(2f);
    //     isAttack = false;
    // }

    IEnumerator Echo()
    {
        isAttack = true;
        // switch to echo animation
        anim.SetInteger("status", (int)statusList.echo);
        yield return new WaitForSeconds(1.5f);
        // echo attack
        GameObject echoPrefab;

        Vector3 spawnPosition = this.transform.position + new Vector3(0f, 1.8f, 0f);
        if (!playerStats.Enlight)
        {
            echoPrefab = Instantiate(echo_normal_prefab, spawnPosition, quaternion.identity);
            spawnPosition.z = -2;
            echoPrefab = Instantiate(echo_normal_particle, spawnPosition, quaternion.identity);
        }
        else
        {
            echoPrefab = Instantiate(echo_enlightened_prefab, spawnPosition, quaternion.identity);
            spawnPosition.z = -2;
            echoPrefab = Instantiate(echo_enlightened_particle, spawnPosition, quaternion.identity);
        }
        yield return new WaitForSeconds(3f);
        anim.SetInteger("status", (int)statusList.stay);
        isAttack = false;
    }

    #endregion

    #region Pick Skill

    void PickSkillPool()
    {
        usedSkillCount += 1;
        int index = Random.Range(0, SkillPool.Count);
        print(index);

        Func<IEnumerator> skill = SkillPool[index];
        SkillPool.RemoveAt(index);
        if (SkillPool.Count == 0)
        {
            print("reset first skill pool");
            SkillPool = new List<Func<IEnumerator>>(initSkillPool);
        }
        if (isHalfTrigger && skill.Method.Name == nameof(Drill))
        {
            StartCoroutine(Triple_Drill());
            return;
        }
        StartCoroutine(skill());
        return;
    }
}

    #endregion