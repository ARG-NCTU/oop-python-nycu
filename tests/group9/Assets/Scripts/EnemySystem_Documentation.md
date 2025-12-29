# New Enemy System Documentation

## Overview
The enemy system has been completely reworked to provide a more modular and extensible architecture. The new system separates concerns between data management (EnemyStats) and behavior logic (EnemyAI), making it easier to create different enemy types while maintaining consistent core functionality.

## Architecture

### Core Components

#### 1. EnemyStats.cs
- **Purpose**: Universal stats component that every enemy should have
- **Responsibilities**: Health, damage, defense, knockback, invulnerability frames
- **Features**: 
  - Automatic AI detection and cross-referencing
  - Flexible AI communication using reflection
  - Event system for health changes, damage, death
  - Knockback system with AI control integration

#### 2. EnemyAI.cs (Base Class)
- **Purpose**: Abstract base class for all enemy AI implementations
- **Responsibilities**: Movement, player detection, control management
- **Features**:
  - Implements IEnemyAI interface for EnemyStats communication
  - Provides utility methods for player detection and movement
  - Handles control enabling/disabling during knockback
  - Abstract UpdateAI() method for derived classes

#### 3. BasicEnemyAI.cs
- **Purpose**: Concrete implementation for basic/normal enemies
- **Responsibilities**: Patrol, chase, attack behaviors
- **Features**:
  - State machine with Patrol, Chase, Attack, Idle states
  - Configurable detection and attack ranges
  - Simple patrol behavior with wait times
  - Animation system integration

#### 4. EnemySetup.cs
- **Purpose**: Utility script for easy enemy configuration in editor
- **Responsibilities**: Automatic component setup and configuration
- **Features**:
  - One-click enemy setup with all required components
  - Configurable enemy types (extensible)
  - Validation system to check proper setup
  - Tag and layer management

### Interface System

#### IEnemyAI Interface
```csharp
public interface IEnemyAI
{
    EnemyStats EnemyStats { get; set; }
    void UpdateMovementSpeed();
    void SetControlEnabled(bool enabled);
    void DeathSequence();
}
```

This interface ensures proper communication between EnemyStats and any AI implementation.

## Usage Workflow

### Creating a New Enemy

#### Method 1: Using EnemySetup (Recommended)
1. Create a new GameObject
2. Add `EnemySetup` component
3. Configure enemy type, stats, and references in inspector
4. The setup script will automatically add and configure all required components

#### Method 2: Manual Setup
1. Create a new GameObject
2. Add `EnemyStats` component
3. Add specific AI component (e.g., `BasicEnemyAI`)
4. Add `Rigidbody2D` and `Collider2D`
5. Set GameObject tag to "Enemy"
6. Configure all component references and settings

### Creating Custom Enemy AI

```csharp
public class CustomEnemyAI : EnemyAI
{
    [Header("Custom Settings")]
    [SerializeField] private float customBehaviorRange = 10f;
    
    protected override void UpdateAI()
    {
        // Implement your custom AI logic here
        if (GetDistanceToPlayer() < customBehaviorRange)
        {
            // Custom behavior when player is in range
            PerformCustomBehavior();
        }
        else
        {
            // Default patrol or idle behavior
            StopMovement();
        }
    }
    
    private void PerformCustomBehavior()
    {
        // Your custom enemy behavior
    }
}
```

## Component Communication

### EnemyStats → AI Communication
EnemyStats automatically finds and communicates with AI components using reflection:

- **Speed Changes**: Calls `UpdateMovementSpeed()` when speed adjustment changes
- **Knockback**: Calls `SetControlEnabled(false)` during knockback
- **Death**: Calls `DeathSequence()` when enemy dies

### AI → EnemyStats Communication
AI components can access EnemyStats through the `EnemyStats` property:

```csharp
// In AI script
float currentHealth = EnemyStats.CurrentHealth;
float attackDamage = EnemyStats.AttackDamage;
bool isAlive = EnemyStats.IsAlive;
```

## Migration from Old System

### Changes Made

1. **NormalEnemyStats** → **EnemyStats**
   - Renamed for generic use with all enemy types
   - Added automatic AI detection and communication
   - Enhanced reflection-based AI communication

2. **NormalEnemyAI** → **BasicEnemyAI** + **EnemyAI (base)**
   - Split into base class and specific implementation
   - Added interface system for better architecture
   - Improved state management and behavior separation

3. **NormalEnemySetup** → **EnemySetup**
   - Enhanced with more configuration options
   - Added validation system
   - Support for multiple enemy types

4. **PlayerAttackHitbox Updates**
   - Changed from `NormalEnemyStats` to `EnemyStats`
   - Maintains full compatibility with existing functionality

### Compatibility
- All existing enemy prefabs need to be updated to use new components
- PlayerAttackHitbox now works with the new EnemyStats system
- EnemyAttackHitbox remains unchanged and compatible

## Enemy Types and Extensibility

### Current Enemy Types
- **Basic**: Simple patrol, chase, and attack behavior

### Adding New Enemy Types

1. **Create New AI Script**:
   ```csharp
   public class FlyingEnemyAI : EnemyAI
   {
       // Implement flying behavior
   }
   ```

2. **Update EnemySetup**:
   - Add new enum value to `EnemyType`
   - Add case in `SetupAI()` method
   - Create setup method for new enemy type

3. **Create Prefab**:
   - Use EnemySetup or manual setup
   - Configure specific settings for new enemy type

## Animation Integration

The new system maintains full compatibility with the UniversalAnimation system:

```csharp
// In AI script
[SerializeField] private GameObject idleAnimationSet;
[SerializeField] private GameObject walkAnimationSet;
[SerializeField] private GameObject attackAnimationSet;

private void SwitchToAnimation(GameObject animationSet)
{
    UniversalAnimation animation = animationSet.GetComponent<UniversalAnimation>();
    if (animation != null)
    {
        animation.Enabled = true;
    }
}
```

## Debug and Validation

### Debug Features
- Comprehensive debug logging in all components
- Gizmos visualization for ranges and patrol areas
- Validation system in EnemySetup

### Validation Checklist
1. EnemyStats component present
2. AI component present and properly configured
3. Rigidbody2D and Collider2D present
4. "Enemy" tag assigned
5. Required prefab references assigned
6. Animation sets configured

## Best Practices

1. **Always use EnemySetup** for new enemies when possible
2. **Inherit from EnemyAI** for custom AI implementations
3. **Use the validation system** to check enemy setup
4. **Keep AI logic in AI scripts** and data in EnemyStats
5. **Use events** for loose coupling between components
6. **Test with debug logging** enabled during development

## Future Expansion Ideas

- **Status Effects System**: Poison, slow, stun effects
- **Equipment System**: Different weapons/armor for enemies
- **Formation AI**: Group behavior for multiple enemies
- **Boss AI**: Complex multi-phase boss battles
- **Environment Interaction**: Enemies that use environment
- **Spawner System**: Dynamic enemy spawning
- **Difficulty Scaling**: Stat adjustments based on game progression
