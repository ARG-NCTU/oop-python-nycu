# pyrobot Class Diagram

---
title : locobot
---
```mermaid
classDiagram
    Arm <|-- LoCoBotArm : Inhirit
    Base <|-- LoCoBotBase : Inhirit
    SimpleCamera <|-- LoCoBotCamera : Inhirit
    Camera <|-- SimpleCamera : Inhirit
    Gripper <|-- LoCoBotGripper : Inhirit
    TrajectoryTracker <|-- ILQRControl : Inhirit
    BaseSafetyCallbacks <|-- BaseState : Inhirit
    Robot o-- Base : Aggregation
    Robot o-- Gripper : Aggregation
    Robot o-- Camera : Aggregation
    Robot o-- Arm : Aggregation

```

---
title : allegro_hand
---
```mermaid
classDiagram
    Gripper <|-- AllegroHand : Inhirit
    Robot o-- Gripper : Aggregation

```

---
title : azure_kinect
---
```mermaid
classDiagram
    Camera <|-- Kinect2Camera : Inhirit
    Kinect2Camera <|-- AzureKinectCamera : Inhirit

```

---
title : core
---
```mermaid
classDiagram
    Robot o-- Base : Aggregation
    Robot o-- Gripper : Aggregation
    Robot o-- Camera : Aggregation
    Robot o-- Arm : Aggregation

```

---
title : habitat
---
```mermaid
classDiagram
    Robot o-- LoCoBotBase : Aggregation
    Robot o-- LoCoBotCamera : Aggregation

```

---
title : kinect2
---
```mermaid
classDiagram
    Camera <|-- Kinect2Camera : Inhirit

```

---
title : sawyer
---
```mermaid
classDiagram
    Arm <|-- SawyerArm : Inhirit
    Gripper <|-- SawyerGripper : Inhirit
    SawyerArm *-- SawyerGripper : Composition
    Robot o-- Arm : Aggregation
    Robot o-- Gripper : Aggregation

```

---
title : ur5
---
```mermaid
classDiagram
    Arm <|-- UR5Arm : Inhirit
    Gripper <|-- AllegroHand : Inhirit
    UR5Arm o-- AllegroHand : Aggregation
    Robot o-- Arm : Aggregation
    Robot o-- Gripper : Aggregation

```

---
title : util
---
```mermaid
classDiagram
    MoveitObjectHandler *-- PlanningSceneInterface : Composition

```

---
title : vrep_locobot
---
```mermaid
classDiagram
    Robot o-- LoCoBotBase : Aggregation
    Robot o-- LoCoBotGripper : Aggregation
    Robot o-- LoCoBotCamera : Aggregation
    Robot o-- LoCoBotArm : Aggregation

```

---
title : vx300s
---
```mermaid
classDiagram
    Arm <|-- vx300sArm : Inhirit
    Camera <|-- SimpleCamera : Inhirit
    SimpleCamera <|-- LoCoBotCamera : Inhirit
    Gripper <|-- vx300sGripper : Inhirit
    vx300sArm *-- vx300sGripper : Composition
    vx300sArm o-- LoCoBotCamera : Aggregation
    LoCoBotCamera o-- DepthImgProcesso : Aggregation
    Robot o-- Gripper : Aggregation
    Robot o-- Camera : Aggregation
    Robot o-- Arm : Aggregation

```

