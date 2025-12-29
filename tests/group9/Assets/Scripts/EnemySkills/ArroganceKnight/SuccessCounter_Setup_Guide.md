# SuccessCounter Skill Implementation - Setup Guide

## Overview
The new `SuccessCounter` skill has been successfully implemented to separate counter mechanics from horizontal attack skills. This provides more flexibility and specialized counter-attack behavior.

## New Skill Flow
**Previous Flow:** 
Boss uses Counter → Player attacks boss → Boss ends Counter → Boss uses HorizontalSwing

**New Flow:** 
Boss uses Counter → Player attacks boss → Boss ends Counter → Boss uses SuccessCounter

## What's Been Implemented

### 1. New SuccessCounterSkill.cs
- **Duration**: 1 second total (0.5s wait + spawn + 0.5s end)
- **Animation**: Switches to "CounterSwing" animation set
- **Attack**: Spawns CounterSwing attack prefab after 0.5s delay
- **Behavior**: Boss stays stationary, executes devastating counterattack

### 2. Updated CounterSkill.cs
- **New Constructor**: `Counter(GameObject attackPrefab, GameObject counterPrefab, bool useSwing1)`
- **Behavior Change**: Now queues `SuccessCounter` instead of `HorizontalSwing` when hit
- **Backward Compatibility**: Old constructor still works, uses same prefab for both

### 3. Updated ComboSkills.cs
- **All combo skills** now accept `counterSwingAttackPrefab` parameter
- **Updated Constructors**: All counter-using combos take both counter and counterSwing prefabs
- **Skills Affected**: HalfCombo, SpinnerCombo, CleanUpCombo

### 4. Updated ArroganceKnightAI.cs
- **New Animation Field**: `counterSwingAnimationSet` added to inspector
- **New Attack Field**: `counterSwingAttackPrefab` added to inspector
- **Animation Support**: Added "counterswing" case to `SwitchToAnimationSet()`
- **Skill Management**: Updated combo skill creation to pass both prefabs

## Setup Requirements

### Unity Inspector Setup
In the ArroganceKnightAI component, you need to assign:

**New Animation Reference:**
- `Counter Swing Animation Set` - Animation for SuccessCounter skill

**New Attack Prefab:**
- `Counter Swing Attack Prefab` - Attack prefab spawned by SuccessCounter

### Animation Requirements
Create a new animation GameObject for the CounterSwing animation that:
- Has a `UniversalAnimation` component
- Contains the counter-attack animation (sword swing, etc.)
- Is assigned to `counterSwingAnimationSet` field in ArroganceKnightAI

### Attack Prefab Requirements
Create or assign a CounterSwing attack prefab that:
- Has an `EnemyAttackHitbox` component
- Contains the visual effects for the counter attack
- Is assigned to `counterSwingAttackPrefab` field in ArroganceKnightAI

## Benefits of This Implementation

### 1. Separation of Concerns
- Counter skills now have their own dedicated attack behavior
- Horizontal attacks remain independent of counter mechanics
- Easier to balance and modify counter vs normal attacks

### 2. Enhanced Customization
- Counter attacks can have different damage/effects than normal attacks
- Different animation timing and visual effects
- Separate prefabs allow unique counter-specific properties

### 3. Improved Player Experience
- Clear visual distinction between counter attacks and normal attacks
- More predictable boss behavior patterns
- Better feedback for successful counter timing

## Technical Details

### Skill Execution Flow
1. **Counter Skill**: Boss enters counter stance, waits for hit
2. **Hit Detection**: Player attacks, Counter skill detects hit
3. **Queue SuccessCounter**: Counter queues SuccessCounter to front of queue
4. **Execute SuccessCounter**: 
   - Switch to CounterSwing animation
   - Wait 0.5 seconds (windup)
   - Spawn CounterSwing attack
   - Wait 0.5 seconds (recovery)
   - Return to idle

### Animation Switching
- Counter: Uses "counterprepare" animation
- SuccessCounter: Uses "counterswing" animation
- Both return to "idle" animation when complete

### Prefab Management
- `hAttack1Prefab`: Used for Counter skill initialization (backward compatibility)
- `counterSwingAttackPrefab`: Used for SuccessCounter attack spawning
- Both prefabs can be the same or different based on design needs

## Testing the Implementation

### Basic Test
1. Start boss fight
2. Wait for boss to use Counter skill (counter prepare animation)
3. Attack the boss during counter
4. Observe: Boss should switch to CounterSwing animation and spawn counter attack

### Debug Output
Enable `Show Skill Debug` in ArroganceKnightAI to see console output:
- "Counter: Hit received - will queue counter attack"
- "Counter: Queued SuccessCounter as next skill"
- "SuccessCounter: Counter attack launched!"

## Backward Compatibility

The implementation maintains backward compatibility:
- Old Counter(prefab) constructor still works
- If counterSwingPrefab is null, falls back to horizontalSwingPrefab
- Existing combo skills work with minimal changes

## Future Enhancements

This architecture allows for easy future improvements:
- Multiple counter attack types
- Conditional counter attacks based on boss health
- Chain counter attacks
- Player-specific counter responses
