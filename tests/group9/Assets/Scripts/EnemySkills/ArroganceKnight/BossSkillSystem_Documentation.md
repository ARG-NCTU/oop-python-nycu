# Boss Skill System Documentation

## Overview
The Boss Skill System provides a flexible, queue-based architecture for creating complex boss behaviors. Bosses execute skills from an action queue, and skills are randomly selected from a skill pool to maintain unpredictability while ensuring variety.

## Architecture

### Core Components

#### 1. BossSkill (Abstract Base Class)
- **Purpose**: Base class for all boss skills/abilities
- **Features**: 
  - Duration-based execution
  - Initialization with boss references
  - Progress tracking and completion detection
  - Interrupt capability
  - Abstract methods for skill-specific logic

#### 2. BossSkillManager
- **Purpose**: Manages skill execution, queueing, and pool management
- **Features**:
  - Action Queue: List of skills to be executed in order
  - Skill Pool: Available skills for random selection
  - Automatic skill queueing
  - Pool reset when empty
  - Skill interruption support
  - Event system for skill state changes

#### 3. ArroganceKnightAI
- **Purpose**: First boss implementation using the skill system
- **Features**:
  - Extends base EnemyAI class
  - Integrates BossSkillManager
  - Animation system integration
  - Debug visualization and logging

### Current Skills

#### IdleSkill
- **Duration**: Configurable (default: 10 seconds)
- **Behavior**: Boss stays stationary, stops all horizontal movement
- **Purpose**: Testing the skill system and providing breathing room for players

## System Flow

### Initialization
1. ArroganceKnight initializes BossSkillManager
2. Skill pool is populated with available skills
3. Initial skills are queued
4. Skill execution begins

### Execution Loop
1. BossSkillManager updates current skill
2. If skill is completed, start next skill in queue
3. If queue is low, automatically queue random skills
4. Skills are removed from pool when queued
5. When pool is empty, it resets to original state

### Skill Lifecycle
1. **Selection**: Skill is randomly selected from pool
2. **Queueing**: Skill is added to action queue
3. **Initialization**: Skill receives boss references and starts
4. **Execution**: Skill updates every frame with custom logic
5. **Completion**: Skill finishes naturally or is interrupted

## Usage Examples

### Creating a Custom Skill

```csharp
public class DashAttackSkill : BossSkill
{
    private Vector2 dashDirection;
    private float dashSpeed = 10f;
    
    public DashAttackSkill() : base("Dash Attack", 2f)
    {
        canBeInterrupted = false; // Cannot be interrupted
    }
    
    protected override void OnSkillStart()
    {
        base.OnSkillStart();
        
        // Determine dash direction towards player
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player != null)
        {
            dashDirection = (player.transform.position - bossTransform.position).normalized;
        }
        else
        {
            dashDirection = Vector2.right; // Default direction
        }
    }
    
    protected override void OnSkillUpdate()
    {
        // Apply dash movement
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = dashDirection * dashSpeed;
        }
    }
    
    protected override void OnSkillEnd()
    {
        base.OnSkillEnd();
        
        // Stop movement
        if (bossRigidbody != null)
        {
            bossRigidbody.velocity = Vector2.zero;
        }
    }
    
    public override BossSkill CreateCopy()
    {
        return new DashAttackSkill();
    }
}
```

### Adding Skills to Boss

```csharp
private void SetupSkillPool()
{
    // Add various skills to the pool
    skillManager.AddSkillToPool(new IdleSkill(5f));
    skillManager.AddSkillToPool(new DashAttackSkill());
    skillManager.AddSkillToPool(new BackupSkill(3f));
    skillManager.AddSkillToPool(new ComboAttackSkill());
}
```

### Manual Skill Control

```csharp
// Queue specific skill
boss.QueueSkill("Dash Attack");

// Queue random skill
boss.QueueRandomSkill();

// Interrupt current skill
boss.InterruptCurrentSkill();
```

## Configuration Options

### BossSkillManager Settings
- **AutoQueueSkills**: Automatically queue skills when queue gets low
- **MaxQueueSize**: Maximum number of skills that can be queued
- **Debug Logging**: Enable detailed skill execution logging

### Skill Properties
- **Duration**: How long the skill lasts
- **CanBeInterrupted**: Whether the skill can be forcibly stopped
- **SkillName**: Identifier for the skill

## Events System

### Available Events
- **OnSkillStarted**: Triggered when a skill begins execution
- **OnSkillCompleted**: Triggered when a skill finishes
- **OnSkillPoolReset**: Triggered when skill pool is reset

### Event Usage
```csharp
skillManager.OnSkillStarted += (skill) => 
{
    Debug.Log($"Boss started skill: {skill.skillName}");
    // Update UI, play sound effects, etc.
};

skillManager.OnSkillCompleted += (skill) => 
{
    Debug.Log($"Boss completed skill: {skill.skillName}");
    // Trigger rewards, update phase, etc.
};
```

## ArroganceKnight Implementation

### Current Features
- **Single Test Skill**: 10-second idle skill for system testing
- **Animation Integration**: Switches animations based on current skill
- **Debug Visualization**: Gizmos and debug output for development
- **Control Integration**: Properly handles knockback and death states

### Boss Controls
- **StartBoss()**: Begin skill execution
- **StopBoss()**: Stop all skill execution
- **QueueSkill(name)**: Queue specific skill by name
- **InterruptCurrentSkill()**: Force interrupt current skill

### Debug Features
- Real-time skill state display in Scene view
- Console logging of skill transitions
- Skill queue and pool status monitoring

## Future Expansion

### Planned Skills for ArroganceKnight
1. **Dash Attack**: Quick forward dash with damage
2. **Backup Skill**: Retreat if player gets too close
3. **Combo Attack**: Multi-hit attack sequence
4. **Guard Skill**: Defensive stance with damage reduction
5. **Taunt Skill**: Brief animation that boosts next attack

### System Enhancements
- **Skill Conditions**: Prerequisites for skill execution
- **Skill Priorities**: Weight-based skill selection
- **Phase System**: Different skill pools for boss phases
- **Combo System**: Skills that chain into specific other skills
- **Cooldown System**: Prevent skills from being used too frequently

### Advanced Features
- **Skill Trees**: Unlock skills as boss takes damage
- **Adaptive AI**: Learn from player behavior and adjust skill usage
- **Environmental Skills**: Skills that interact with the arena
- **Multi-Part Skills**: Skills that have multiple phases

## Testing and Debugging

### Debug Commands (Inspector)
- **Start Boss**: Begin skill execution
- **Stop Boss**: Stop all skills
- **Queue Random Skill**: Add random skill to queue
- **Interrupt Current**: Stop current skill

### Debug Information
- Current skill name and remaining time
- Action queue contents
- Skill pool status
- Boss state (active/inactive, control enabled/disabled)

### Validation Checklist
1. BossSkillManager properly initialized
2. Skill pool contains at least one skill
3. Skills have valid durations
4. Boss references (transform, rigidbody, stats) are set
5. Animation sets are assigned
6. Event handlers are properly connected

## Performance Considerations

- **Skill Pool Management**: Pool reset is efficient, only creates new instances when needed
- **Update Frequency**: Only current skill updates each frame
- **Memory Usage**: Skills are lightweight and reusable
- **Garbage Collection**: Minimal allocations during runtime

## Best Practices

1. **Keep Skills Focused**: Each skill should have a single, clear purpose
2. **Use Events**: Leverage the event system for loose coupling
3. **Test Thoroughly**: Verify skill transitions and edge cases
4. **Debug Early**: Use debug logging during development
5. **Balance Duration**: Ensure skills have appropriate durations for gameplay flow
6. **Handle Interruptions**: Design skills to handle graceful interruption
7. **Validate References**: Always check for null references in skills
