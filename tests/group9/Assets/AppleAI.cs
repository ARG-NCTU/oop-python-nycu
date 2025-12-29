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

public class AppleAI : MonoBehaviour
{
    [Header("GameObject Prefabs")]

    public GameObject bramble_prefab;
    public GameObject expand_thron_left_prefab;
    public GameObject expand_thron_right_prefab;
    public GameObject slap_prefab;
    public GameObject thrust_prefab;
    public GameObject bomb_prefab;
    public GameObject stay_bomb_prefab;
    public GameObject drill_prefab;
    public GameObject tree_prefab;

    public GameObject wave_particle;
    public Rigidbody2D rb;
    private GameObject player;

    [Header("progress related variable")]
    public float speed = 1f;
    private static bool isHalfTrigger;
    private bool isAttack;
    private float attackTime = 5f;
    private int attackCount;
    public float var; // for testing value
    private float cooldownTime;
    private bool isCoolDown;

    private List<Func<IEnumerator>> initSkillPool = new List<Func<IEnumerator>>();
    private List<Func<IEnumerator>> SkillPool = new List<Func<IEnumerator>>();
    private List<Func<IEnumerator>> initSecondSkillPool = new List<Func<IEnumerator>>();
    private List<Func<IEnumerator>> SecondSkillPool = new List<Func<IEnumerator>>();

    private List<GameObject> brambleList = new List<GameObject>();
    private List<float> initTeleportTarget = new List<float> { -10f, 0f, 8f };
    private List<float> teleportTarget = new List<float>();

    public EnemyStats enemyStats;
    public PlayerStats playerStats;

    public BrambleDetect brambleDetect;
    public int drilledCount;
    Animator anim;

    private enum statusList
    {
        stay,
        slap,
        thrust,
        bomb,
    };


    void Start()
    {
        Debug.Log("Fragment AI initialized");
        isHalfTrigger = false;
        attackCount = 0;
        drilledCount = 0;
        rb = this.GetComponent<Rigidbody2D>();
        anim = this.GetComponent<Animator>();
        player = GameObject.FindGameObjectWithTag("Player");
        playerStats = player.GetComponent<PlayerStats>();
        brambleDetect = player.GetComponent<BrambleDetect>();


        // initial skill pool
        initSkillPool.Add(Slap);
        initSkillPool.Add(Thrust);
        initSkillPool.Add(AppleBomb);
        initSkillPool.Add(StayAppleBomb);

        // initial second pool
        initSecondSkillPool.Add(Treeing);
        initSecondSkillPool.Add(Barrage);
        initSecondSkillPool.Add(AppleBomb);
        initSecondSkillPool.Add(StayAppleBomb);

        SkillPool = new List<Func<IEnumerator>>(initSkillPool);
        SecondSkillPool = new List<Func<IEnumerator>>(initSecondSkillPool);
        Debug.Log(SkillPool.Count);
        teleportTarget = new List<float>(initTeleportTarget);
    }

    void Update()
    {
        if (isCoolDown)
        {
            cooldownTime -= Time.deltaTime;
            if (cooldownTime < 0f) isCoolDown = false;
            return;
        }

        if (drilledCount != brambleDetect.totalDrilled)
        {
            drilledCount = brambleDetect.totalDrilled;
            StartCoroutine(Drill());
        }

        attackTime -= Time.deltaTime;
        if (isAttack) return;


        if (attackTime <= 0f)
        {
            // isAttack = true;
            attackTime = 5f;
            print("attack:" + attackCount);
            attackCount++;
            // 第5次攻擊改為連續地刺
            if (attackCount >= 5)
            {
                print("big attack");
                StartCoroutine(Bramble());
                StartCoroutine(ExpandThorn());
                attackCount = 0;
                Cooldown(5f);
            }
            else
            {
                if (isHalfTrigger == false)
                {
                    if (enemyStats.CurrentHealth <= enemyStats.MaxHealth / 2)
                    {
                        HalfHandler();
                    }
                    else
                    {

                        StartCoroutine(Bramble());
                        // StartCoroutine(AppleBomb());
                        PickSkillPool();
                    }
                }
                else
                {
                    StartCoroutine(Bramble());
                    // StartCoroutine(AppleBomb());
                    PickSecondSkillPool();
                }
            }

            // isAttack = false;
        }


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

    private void HalfHandler()
    {
        print("apple enter half health phase");
        isHalfTrigger = true;
        for (int i = -13; i <= 13; i++)
        {
            Vector3 spawnpoint = new(i * 1.2f, 0.8f, 0f);

            Instantiate(bramble_prefab, spawnpoint, quaternion.identity);
        }
    }
    private void DetectDirection()
    {
        if (PlayerDirection() == 1f)
        {
            this.GetComponentInChildren<SpriteRenderer>().flipX = true;
        }
        else
        {
            this.GetComponentInChildren<SpriteRenderer>().flipX = false;
        }
    }

    #endregion

    #region Skills

    IEnumerator Drill()
    {
        Vector3 spawnpoint = player.transform.position;
        spawnpoint.y = 3.5f;
        Instantiate(drill_prefab, spawnpoint, Quaternion.identity);

        yield return new WaitForSeconds(0f);
    }

    IEnumerator ExpandThorn()
    {
        // swith to expand thron animation
        Vector3 spawnPosition = this.transform.position + new Vector3(-1f, 0f, 0f);
        Vector3 spawnPositionR = this.transform.position + new Vector3(1f, 0f, 0f);
        Instantiate(expand_thron_left_prefab, spawnPosition, quaternion.identity);
        Instantiate(expand_thron_right_prefab, spawnPositionR, quaternion.identity);

        StartCoroutine(Wave());
        StartCoroutine(DestroyBramble());
        yield return new WaitForSeconds(4f);


        // only teleport if more than half
        if (isHalfTrigger == false)
            StartCoroutine(Teleport());

        yield return new WaitForSeconds(0f);
    }

    IEnumerator Wave()
    {
        for (int i = 0; i < 8; i++)
        {
            Vector3 spawnPosition = this.transform.position + new Vector3(-1f * i, 0f, 0f);
            spawnPosition.y = 3.25f;
            Vector3 spawnPositionR = this.transform.position + new Vector3(1f * i, 0f, 0f);
            spawnPositionR.y = 3.25f;
            Instantiate(wave_particle, spawnPosition, quaternion.identity);
            Instantiate(wave_particle, spawnPositionR, quaternion.identity);
            yield return new WaitForSeconds(0.4f);
        }

    }

    IEnumerator DestroyBramble()
    {
        for (int i = 0; i < 5; i++)
        {
            Destroy(brambleList[i * 2]);
            Destroy(brambleList[i * 2 + 1]);
            yield return new WaitForSeconds(0.4f);
        }
        brambleList.Clear();
    }

    IEnumerator Teleport()
    {
        // switch to teleport animation

        int index = Random.Range(0, teleportTarget.Count);
        this.transform.position = new Vector3(teleportTarget[index], 3f, 0f);

        if (teleportTarget.Count == 0)
        {
            teleportTarget = new List<float>(initTeleportTarget);
        }
        yield return new WaitForSeconds(0.15f);
    }

    IEnumerator Bramble()
    {
        Vector3 spawnpointLeft = this.transform.position + new Vector3(attackCount, 0f, 0f);
        spawnpointLeft.y = 0.8f;
        Vector3 spawnpointRight = this.transform.position - new Vector3(attackCount, 0f, 0f);
        spawnpointRight.y = 0.8f;

        GameObject brambleLeft = Instantiate(bramble_prefab, spawnpointLeft, quaternion.identity);
        GameObject brambleRight = Instantiate(bramble_prefab, spawnpointRight, quaternion.identity);

        brambleList.Add(brambleLeft);
        brambleList.Add(brambleRight);

        yield return new WaitForSeconds(0f);

    }

    IEnumerator Slap()
    {
        // switch to slap animation
        anim.SetInteger("status", (int)statusList.slap);
        DetectDirection();
        yield return new WaitForSeconds(0.35f);

        Vector3 spawnpoint = this.transform.position + new Vector3(PlayerDirection() * 0.75f, -1f, 0f);
        Instantiate(slap_prefab, spawnpoint, Quaternion.identity);

        yield return new WaitForSeconds(2f);
        anim.SetInteger("status", (int)statusList.stay);
    }

    IEnumerator Thrust()
    {
        // switch to slap animation
        anim.SetInteger("status", (int)statusList.thrust);
        DetectDirection();
        yield return new WaitForSeconds(0.35f);

        Vector3 spawnpoint = this.transform.position + new Vector3(0f, 0.8f, 0f);
        Instantiate(thrust_prefab, spawnpoint, Quaternion.identity);

        yield return new WaitForSeconds(2f);
        anim.SetInteger("status", (int)statusList.stay);
    }

    List<int> PickFromRangeNTimes(int n, int range)
    {
        int retryCount = 0;
        List<int> result = new List<int>();
        if (range == 1)
        {
            return new List<int> { -1, 1 };
        }
        for (int i = 0; i < n; i++)
        {
            int tmp = Random.Range(-1 * range, range);
            while (result.Contains(tmp) && retryCount < 10)
            {
                tmp = Random.Range(-1 * range, range);
                print(tmp);
                retryCount++;
            }
            result.Add(tmp);
            retryCount = 0;
        }
        print(result.Count);
        print(n);
        print(range);
        return result;
    }

    IEnumerator AppleBomb()
    {
        // switch to bomb animation(if needed)
        List<int> positions;
        if (attackCount < 4)
        {
            positions = PickFromRangeNTimes(2, attackCount);
        }
        else
        {
            positions = PickFromRangeNTimes(4, attackCount);
        }
        foreach (int position in positions)
        {
            Vector3 spawnpoint = this.transform.position;
            Instantiate(bomb_prefab, spawnpoint + new Vector3(position, 0f, 0f), Quaternion.identity);
        }
        yield return new WaitForSeconds(0f);
    }

    IEnumerator StayAppleBomb()
    {
        // switch to bomb animation(if needed)

        Instantiate(stay_bomb_prefab, this.transform.position, Quaternion.identity);
        yield return new WaitForSeconds(0f);
    }

    IEnumerator Treeing()
    {
        List<int> positions;

        positions = PickFromRangeNTimes(3, 14);

        foreach (int position in positions)
        {
            Instantiate(tree_prefab, new Vector3(position * 1.2f, 4f, 0f), Quaternion.identity);
        }

        yield return new WaitForSeconds(0f);
    }

    IEnumerator Barrage()
    {

        int rand = Random.Range(0, 2);
        StartCoroutine(rand == 1 ? Barrage1() : Barrage2());
        yield return new WaitForSeconds(0f);
    }

    IEnumerator Barrage1()
    {
        for (int i = 9; i >= 7; i--)
        {
            Instantiate(tree_prefab, new Vector3(i * 1.2f, 4f, 0f), Quaternion.identity);
            Instantiate(tree_prefab, new Vector3(i * -1.2f, 4f, 0f), Quaternion.identity);
            yield return new WaitForSeconds(0.1f);
        }
        yield return new WaitForSeconds(1f);
        StartCoroutine(AppleBomb());
        yield return new WaitForSeconds(0f);
    }

    IEnumerator Barrage2()
    {
        // odd
        for (int i = -13; i <= 13; i += 3)
        {
            Instantiate(tree_prefab, new Vector3(i * 1.2f, 4f, 0f), Quaternion.identity);
        }
        yield return new WaitForSeconds(3f);

        for (int i = -12; i <= 13; i += 3)
        {
            Instantiate(tree_prefab, new Vector3(i * 1.2f, 4f, 0f), Quaternion.identity);
        }
        yield return new WaitForSeconds(3f);

        for (int i = -11; i <= 13; i += 3)
        {
            Instantiate(tree_prefab, new Vector3(i * 1.2f, 4f, 0f), Quaternion.identity);
        }

        yield return new WaitForSeconds(0);
    }

    #endregion

    #region Pick Skill

    void PickSkillPool()
    {
        int index = Random.Range(0, SkillPool.Count);
        print(index);

        Func<IEnumerator> skill = SkillPool[index];
        SkillPool.RemoveAt(index);
        if (SkillPool.Count == 0)
        {
            print("reset first skill pool");
            SkillPool = new List<Func<IEnumerator>>(initSkillPool);
        }

        StartCoroutine(skill());
        return;
    }
    void PickSecondSkillPool()
    {
        int index = Random.Range(0, SecondSkillPool.Count);
        print(index);

        Func<IEnumerator> skill = SecondSkillPool[index];
        SecondSkillPool.RemoveAt(index);
        if (SecondSkillPool.Count == 0)
        {
            print("reset second skill pool");
            SecondSkillPool = new List<Func<IEnumerator>>(initSecondSkillPool);
        }
        StartCoroutine(skill());
        return;
    }
}

    #endregion