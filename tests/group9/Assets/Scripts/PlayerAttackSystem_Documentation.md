# Player Attack System Documentation

## Overview
The Player Attack System provides a flexible framework for creating player attacks that can damage enemies. It consists of the `PlayerAttackHitbox` component that handles collision detection, damage dealing, and player feedback.

## Key Components

### PlayerAttackHitbox.cs
- **Purpose**: Handles player attack collision detection and damage dealing
- **Detection**: Targets enemies using configurable tags ("Enemy") and layer masks
- **Attack Types**: Physical and Magical (extensible for future types)
- **Auto-Destruction**: Automatically destroys itself after a configurable lifetime
- **Multi-Hit Support**: Can hit multiple enemies or single enemy with cooldowns

### PlayerStats.cs - SuccessfulHit Method
- **Purpose**: Receives feedback when player attacks hit enemies
- **Parameters**: Enemy count and attack type
- **Future Expansion**: Ready for combat systems like mana regen, combos, experience

## Attack Types

### Physical Attacks
- **Color**: Blue gizmos in editor
- **Typical Use**: Melee weapons, physical projectiles
- **Default Settings**: Has knockback, respects enemy defense

### Magical Attacks  
- **Color**: Cyan gizmos in editor
- **Typical Use**: Spells, magical projectiles
- **Default Settings**: No knockback, ignores enemy defense

## Usage Workflow

1. **Create Attack Prefab**:
   ```csharp
   GameObject attackPrefab = new GameObject("PlayerAttack");
   attackPrefab.AddComponent<BoxCollider2D>().isTrigger = true;
   attackPrefab.AddComponent<PlayerAttackHitbox>();
   ```

2. **Configure Attack Settings**:
   ```csharp
   PlayerAttackHitbox hitbox = attackPrefab.GetComponent<PlayerAttackHitbox>();
   hitbox.Damage = 25f;
   hitbox.Type = PlayerAttackHitbox.AttackType.Physical;
   hitbox.Lifetime = 0.5f;
   ```

3. **Spawn During Gameplay**:
   ```csharp
   GameObject attack = Instantiate(attackPrefab, spawnPosition, spawnRotation);
   // Attack will automatically handle collision and destruction
   ```

## Configuration Options

### Damage Settings
- **Damage**: Base damage amount
- **Attack Type**: Physical or Magical (affects behavior and future mechanics)
- **Has Knockback**: Whether attack pushes enemies
- **Ignore Defence**: Whether attack bypasses enemy defense

### Hitbox Behavior
- **Destroy On Hit**: Whether hitbox destroys itself after first hit
- **Can Hit Multiple Enemies**: Whether same hitbox can hit different enemies
- **Cooldown Between Hits**: Minimum time between hitting same enemy again
- **Lifetime**: Auto-destruction timer (0.1 - ∞ seconds)

### Detection Settings
- **Enemy Tag**: Tag to identify enemy objects ("Enemy" by default)
- **Enemy Layer Mask**: Layer mask for enemy detection (all layers by default)

### Visual/Audio Feedback
- **Hit Effect**: GameObject spawned on successful hit
- **Hit Sound**: Audio clip played on hit
- **Gizmos**: Visual debugging in scene view

## Events System

### Available Events
- **OnEnemyHit**: Triggered when hitting an enemy (provides GameObject)
- **OnDamageDealt**: Triggered when dealing damage (provides damage amount)
- **OnHitboxTriggered**: Triggered on any collision
- **OnAttackComplete**: Triggered when hitbox is destroyed (provides total hits and type)

### Event Usage Example
```csharp
PlayerAttackHitbox hitbox = GetComponent<PlayerAttackHitbox>();
hitbox.OnEnemyHit += (enemy) => Debug.Log($"Hit {enemy.name}!");
hitbox.OnAttackComplete += (hits, type) => Debug.Log($"{type} attack hit {hits} enemies");
```

## Integration with PlayerStats

### SuccessfulHit Callback
When a `PlayerAttackHitbox` is destroyed, it automatically calls:
```csharp
playerStats.SuccessfulHit(totalEnemiesHit, attackType);
```

This allows the player stats system to:
- Track combat statistics
- Trigger special effects based on successful hits
- Implement mana regeneration or other mechanics
- Handle achievement/progression systems

### Future Expansion Ideas
- **Mana Regeneration**: Restore mana on successful magical attacks
- **Health on Hit**: Restore health on successful physical attacks  
- **Combo System**: Track consecutive hits for damage multipliers
- **Critical Hits**: Random or skill-based damage bonuses
- **Elemental Types**: Expand beyond Physical/Magical

## Example Attack Patterns

### Quick Melee Attack
```csharp
hitbox.Damage = 20f;
hitbox.Type = PlayerAttackHitbox.AttackType.Physical;
hitbox.DestroyOnHit = true;
hitbox.Lifetime = 0.3f; // Very short duration
```

### Magical Projectile
```csharp
hitbox.Damage = 30f;
hitbox.Type = PlayerAttackHitbox.AttackType.Magical;
hitbox.IgnoreDefence = true;
hitbox.Lifetime = 2f; // Travels for 2 seconds
```

### Area of Effect
```csharp
hitbox.Damage = 15f;
hitbox.CanHitMultipleEnemies = true;
hitbox.DestroyOnHit = false;
hitbox.Lifetime = 1f; // Persists in area
```

## Testing and Debugging

### Debug Options
- **Show Debug Info**: Enables console logging for hit detection
- **Show Gizmos**: Visual representation in scene view
- **Manual Trigger**: Test hitbox against specific enemies

### Test Controls (PlayerAttackHitboxExample)
- **Q Key**: Create physical attack
- **E Key**: Create magical attack  
- **R Key**: Create area attack

## Future Enemy Integration

The system is designed to work with future enemy health systems:
```csharp
// Future enemy damage implementation
EnemyStats enemyStats = enemy.GetComponent<EnemyStats>();
if (enemyStats != null)
{
    Vector3 playerPosition = transform.position;
    return enemyStats.TakeDamage(damage, hasKnockback, playerPosition, ignoreDefence);
}
```

Currently returns `true` (always successful) as placeholder until enemy health system is implemented.
