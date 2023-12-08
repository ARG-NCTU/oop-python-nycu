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
    class Robot{
        configs : bool
        robot_name
        gripper
        __init__()
    }
    class Base{
        configs
        ctrl_pub
        __init__()
        stop()
        set_vel()
        go_to_relative()
        go_to_absolute()
        track_trajectory()
        get_state()
    }
    class Gripper{
        configs
        __init__()
        open()
        close()
    }
    class Camera{
        configs
        cv_bridge
        camera_info_lock
        camera_img_lock
        rgb_img : bool
        depth_img : bool
        camera_info : bool
        camera_P : bool
        rgb_sub
        depth_sub
        sync
        __init__()
        _sync_callback()
        _camera_info_callback()
        get_rgb()
        get_depth()
        get_rgb_depth()
        get_intrinsics()
    }
    class Arm{
        configs
        moveit_planner
        planning_time
        use_moveit
        joint_state_lock
        tf_listener
        arm_joint_names
        arm_dof : int
        _joint_angles : dict
        _joint_velocities : dict
        _joint_efforts : dict
        joint_pub : bool
        _ik_service
        _fk_service
        __init__()
        go_home()
        pose_ee()
        get_ee_pose()
        get_transform()
        get_joint_angles()
        get_joint_velocities()
        get_joint_torques()
        get_joint_angle()
        get_joint_velocity()
        get_joint_torque()
        set_joint_positions()
        make_plan_joint_positions()
        set_joint_velocities()
        set_joint_torques()
        set_ee_pose()
        make_plan_pose()
        move_ee_xyz()
        _cancel_moveit_goal()
        compute_fk_position()
        get_jacobian()
        compute_fk_velocity()
        compute_ik()
        _callback_joint_states()
        _pub_joint_positions()
        _pub_joint_velocities()
        _pub_joint_torques()
        _init_moveit()
        _angle_error_is_small()
        _loop_angle_pub_cmd()
        _setup_joint_pub()
    }
    class LoCoBotBase{
        configs
        sim
        agent
        transform : bool
        init_state
        __init__()
        execute_action()
        get_full_state()
        _rot_matrix()
        get_state()
        stop()
        set_vel()
        go_to_relative()
        go_to_absolute()
        _act()
        _go_to_relative_pose()
        track_trajectory()
    }
    class LoCoBotCamera{
        sim
        configs
        agent
        depth_cam
        pan : float
        tilt : float
        __init__()
        get_rgb()
        get_depth()
        get_rgb_depth()
        get_intrinsics()
        pix_to_3dpt()
        _cam2pyrobot()
        _rot_matrix()
        get_current_pcd()
        state()
        get_state()
        get_pan()
        get_tilt()
        set_pan()
        set_tilt()
        _compute_relative_pose()
        set_pan_tilt()
        reset()
    }
    class LoCoBotArm{
        CONTROL_MODES : dict
        mode_control
        joint_stop_pub
        __init__()
        set_joint_velocities()
        set_joint_torque()
        set_ee_pose_pitch_roll()
        set_joint_torques()
        go_home()
    }
    class LoCoBotGripper{
        _gripper_state_lock
        _gripper_state : None
        wait_time : float
        pub_gripper_close
        pub_gripper_open
        __init__()
        get_gripper_state()
        open()
        reset()
        close()
        _callback_gripper_state()
    }
    class SimpleCamera{
        _tf_listener
        depth_cam
        cam_cf
        base_f
        __init__()
        get_current_pcd()
        pix_to_3dpt()
        get_link_transform()
    }
    class BaseState{
        configs
        build_map
        state
        subscribers : list
        __init__()
        _get_odom_state()
        _odometry_callback()
        __del__()
    }
    class TrajectoryTracker{
        system
        _as
        __init__()
        generate_plan()
        _compute_controls()
        stop()
        execute_plan()
        plot_plan_execution()
    }
    class ILQRControl{
        _as
        configs : dict
        max_v
        min_v
        max_w
        min_w
        rate
        dt : float
        ctrl_pub
        bot_base
        system
        __init__()
        should_stop()
        should_stop()
        state()
        go_to_relative()
        go_to_absolute()
        _compute_trajectory_no_map()
        track_trajectory()
    }
    class BaseSafetyCallbacks{
        should_stop : bool
        bumper : bool
        cliff : bool
        wheel_drop : bool
        subscribers : list
        __init__()
        bumper_callback_create()
        cliff_callback()
        wheeldrop_callback()
        bumper_callback_kobuki()
        __del__()
    }
```

---
title : allegro_hand
---
```mermaid
classDiagram
    Gripper <|-- AllegroHand : Inhirit
    Robot o-- Gripper : Aggregation
    class Robot{
        __init__()
    }
    class Gripper{
        __init__()
        open()
        close()
    }
    class AllegroHand{
        __init__()
        set_primitive()
        go_home()
        move_to_neutral()
        set_joint_velocities()
        set_joint_positions()
        get_joint_angles()
        get_joint_velocities()
        get_joint_torques()
        get_joint_angle()
        get_joint_velocity()
        get_joint_torque()
        set_joint_torques()
        _pub_joint_torques()
        _callback_joint_states()
        _pub_joint_positions()
        _angle_error_is_small()
        _setup_joint_pub()
        _setup_torque_pub()
        _setup_primitive_pub()
        open()
        close()
    } 
```

---
title : azure_kinect
---
```mermaid
classDiagram
    Camera <|-- Kinect2Camera : Inhirit
    Kinect2Camera <|-- AzureKinectCamera : Inhirit
    class Camera{
        configs
        cv_bridge
        camera_info_lock
        camera_img_lock
        rgb_img : bool
        depth_img : bool
        camera_info : bool
        camera_P : bool
        rgb_sub
        depth_sub
        sync
        __init__()
        _sync_callback()
        _camera_info_callback()
        get_rgb()
        get_depth()
        get_rgb_depth()
        get_intrinsics()
    }
    class Kinect2Camera{
        DepthMapFactor : float
        intrinsic_mat : bool
        __init__()
        get_current_pcd()
        pix_to_3dpt()
    }
    class AzureKinectCamera{
        __init__()
    }
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
    class Robot{
    configs : bool
    robot_name
    gripper
    __init__()
    }
    class Base{
        configs
        ctrl_pub
        __init__()
        stop()
        set_vel()
        go_to_relative()
        go_to_absolute()
        track_trajectory()
        get_state()
    }
    class Gripper{
        configs
        __init__()
        open()
        close()
    }
    class Camera{
        configs
        cv_bridge
        camera_info_lock
        camera_img_lock
        rgb_img : bool
        depth_img : bool
        camera_info : bool
        camera_P : bool
        rgb_sub
        depth_sub
        sync
        __init__()
        _sync_callback()
        _camera_info_callback()
        get_rgb()
        get_depth()
        get_rgb_depth()
        get_intrinsics()
    }
    class Arm{
        configs
        moveit_planner
        planning_time
        use_moveit
        joint_state_lock
        tf_listener
        arm_joint_names
        arm_dof : int
        _joint_angles : dict
        _joint_velocities : dict
        _joint_efforts : dict
        joint_pub : bool
        _ik_service
        _fk_service
        __init__()
        go_home()
        pose_ee()
        get_ee_pose()
        get_transform()
        get_joint_angles()
        get_joint_velocities()
        get_joint_torques()
        get_joint_angle()
        get_joint_velocity()
        get_joint_torque()
        set_joint_positions()
        make_plan_joint_positions()
        set_joint_velocities()
        set_joint_torques()
        set_ee_pose()
        make_plan_pose()
        move_ee_xyz()
        _cancel_moveit_goal()
        compute_fk_position()
        get_jacobian()
        compute_fk_velocity()
        compute_ik()
        _callback_joint_states()
        _pub_joint_positions()
        _pub_joint_velocities()
        _pub_joint_torques()
        _init_moveit()
        _angle_error_is_small()
        _loop_angle_pub_cmd()
        _setup_joint_pub()
    }
```

---
title : habitat
---
```mermaid
classDiagram
    Robot o-- LoCoBotBase : Aggregation
    Robot o-- LoCoBotCamera : Aggregation
    class Robot{
        configs : bool
        robot_name
        gripper
        __init__()
    }
    class LoCoBotBase{
        configs
        sim
        agent
        transform : bool
        init_state
        __init__()
        execute_action()
        get_full_state()
        _rot_matrix()
        get_state()
        stop()
        set_vel()
        go_to_relative()
        go_to_absolute()
        _act()
        _go_to_relative_pose()
        track_trajectory()
    }
    class LoCoBotCamera{
        sim
        configs
        agent
        depth_cam
        pan : float
        tilt : float
        __init__()
        get_rgb()
        get_depth()
        get_rgb_depth()
        get_intrinsics()
        pix_to_3dpt()
        _cam2pyrobot()
        _rot_matrix()
        get_current_pcd()
        state()
        get_state()
        get_pan()
        get_tilt()
        set_pan()
        set_tilt()
        _compute_relative_pose()
        set_pan_tilt()
        reset()
    }
```

---
title : kinect2
---
```mermaid
classDiagram
    Camera <|-- Kinect2Camera : Inhirit
    class Camera{
        configs
        cv_bridge
        camera_info_lock
        camera_img_lock
        rgb_img : bool
        depth_img : bool
        camera_info : bool
        camera_P : bool
        rgb_sub
        depth_sub
        sync
        __init__()
        _sync_callback()
        _camera_info_callback()
        get_rgb()
        get_depth()
        get_rgb_depth()
        get_intrinsics()
    }
    class Kinect2Camera{
        DepthMapFactor : float
        intrinsic_mat : bool
        __init__()
        get_current_pcd()
        pix_to_3dpt()
    }
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
    class Robot{
    configs : bool
    robot_name
    gripper
    __init__()
    }
    class Gripper{
        configs
        __init__()
        open()
        close()
    }
    class Arm{
        configs
        moveit_planner
        planning_time
        use_moveit
        joint_state_lock
        tf_listener
        arm_joint_names
        arm_dof : int
        _joint_angles : dict
        _joint_velocities : dict
        _joint_efforts : dict
        joint_pub : bool
        _ik_service
        _fk_service
        __init__()
        go_home()
        pose_ee()
        get_ee_pose()
        get_transform()
        get_joint_angles()
        get_joint_velocities()
        get_joint_torques()
        get_joint_angle()
        get_joint_velocity()
        get_joint_torque()
        set_joint_positions()
        make_plan_joint_positions()
        set_joint_velocities()
        set_joint_torques()
        set_ee_pose()
        make_plan_pose()
        move_ee_xyz()
        _cancel_moveit_goal()
        compute_fk_position()
        get_jacobian()
        compute_fk_velocity()
        compute_ik()
        _callback_joint_states()
        _pub_joint_positions()
        _pub_joint_velocities()
        _pub_joint_torques()
        _init_moveit()
        _angle_error_is_small()
        _loop_angle_pub_cmd()
        _setup_joint_pub()
    }
    class SawyerArm{
        collision_state_sub
        configs
        moveit_planner : str
        use_moveit : bool
        __init__()
        go_home()
        move_to_neutral()
        get_collision_state()
        _setup_joint_pub()
        _callback_collision()
        _pub_joint_positions()
        _pub_joint_velocities()
        _pub_joint_torques()
    }
    class SawyerGripper{
        wait_time : float
        gripper
        __init__()
        open()
        reset()
        close()
    }
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
    class Robot{
    configs : bool
    robot_name
    gripper
    __init__()
    }
    class Gripper{
        configs
        __init__()
        open()
        close()
    }
    class Arm{
        configs
        moveit_planner
        planning_time
        use_moveit
        joint_state_lock
        tf_listener
        arm_joint_names
        arm_dof : int
        _joint_angles : dict
        _joint_velocities : dict
        _joint_efforts : dict
        joint_pub : bool
        _ik_service
        _fk_service
        __init__()
        go_home()
        pose_ee()
        get_ee_pose()
        get_transform()
        get_joint_angles()
        get_joint_velocities()
        get_joint_torques()
        get_joint_angle()
        get_joint_velocity()
        get_joint_torque()
        set_joint_positions()
        make_plan_joint_positions()
        set_joint_velocities()
        set_joint_torques()
        set_ee_pose()
        make_plan_pose()
        move_ee_xyz()
        _cancel_moveit_goal()
        compute_fk_position()
        get_jacobian()
        compute_fk_velocity()
        compute_ik()
        _callback_joint_states()
        _pub_joint_positions()
        _pub_joint_velocities()
        _pub_joint_torques()
        _init_moveit()
        _angle_error_is_small()
        _loop_angle_pub_cmd()
        _setup_joint_pub()
    }
    class AllegroHand{
        __init__()
        set_primitive()
        go_home()
        move_to_neutral()
        set_joint_velocities()
        set_joint_positions()
        get_joint_angles()
        get_joint_velocities()
        get_joint_torques()
        get_joint_angle()
        get_joint_velocity()
        get_joint_torque()
        set_joint_torques()
        _pub_joint_torques()
        _callback_joint_states()
        _pub_joint_positions()
        _angle_error_is_small()
        _setup_joint_pub()
        _setup_torque_pub()
        _setup_primitive_pub()
        open()
        close()
    } 
    class UR5Arm{
        __init__()
        go_home()
        move_to_neutral()
        _setup_joint_pub()
        _pub_joint_positions()
        _pub_joint_velocities()
        _pub_joint_torques()
        set_joint_velocities()
    }
```

---
title : util
---
```mermaid
classDiagram
    MoveitObjectHandler *-- PlanningSceneInterface : Composition
    class MoveitObjectHandler{
        planning_scene_interface
        scene_objects : list
        attached_objects : list
        __init__()
        add_world_object()
        remove_world_object()
        attach_arm_object()
        detach_arm_object()
        remove_all_objects()
        add_table()
        add_kinect()
        add_gripper()
        remove_table()
        remove_gripper()
    }
    class PlanningSceneInterface{
        _fixed_frame
        _scene_pub
        _apply_service
        _mutex
        _attached : list
        _collision : list
        _objects : dict
        _attached_objects : dict
        _removed : dict
        _attached_removed : dict
        _colors : dict
        __init__()
        sendUpdate()
        clear()
        makeMesh()
        makeSolidPrimitive()
        makeAttached()
        addMesh()
        attachMesh()
        addSolidPrimitive()
        addCylinder()
        addBox()
        attachBox()
        removeCollisionObject()
        removeAttachedObject()
        sceneCb()
        getKnownCollisionObjects()
        getKnownAttachedObjects()
        waitForSync()
        setColor()
        sendColors()
    }
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
    class Robot{
        configs : bool
        robot_name
        gripper
        __init__()
    }
    class LoCoBotBase{
        configs
        sim
        agent
        transform : bool
        init_state
        __init__()
        execute_action()
        get_full_state()
        _rot_matrix()
        get_state()
        stop()
        set_vel()
        go_to_relative()
        go_to_absolute()
        _act()
        _go_to_relative_pose()
        track_trajectory()
    }
    class LoCoBotCamera{
        sim
        configs
        agent
        depth_cam
        pan : float
        tilt : float
        __init__()
        get_rgb()
        get_depth()
        get_rgb_depth()
        get_intrinsics()
        pix_to_3dpt()
        _cam2pyrobot()
        _rot_matrix()
        get_current_pcd()
        state()
        get_state()
        get_pan()
        get_tilt()
        set_pan()
        set_tilt()
        _compute_relative_pose()
        set_pan_tilt()
        reset()
    }
    class LoCoBotArm{
        CONTROL_MODES : dict
        mode_control
        joint_stop_pub
        __init__()
        set_joint_velocities()
        set_joint_torque()
        set_ee_pose_pitch_roll()
        set_joint_torques()
        go_home()
    }
    class LoCoBotGripper{
        _gripper_state_lock
        _gripper_state : None
        wait_time : float
        pub_gripper_close
        pub_gripper_open
        __init__()
        get_gripper_state()
        open()
        reset()
        close()
        _callback_gripper_state()
    }
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
    class Robot{
        configs : bool
        robot_name
        gripper
        __init__()
    }
    class LoCoBotCamera{
        sim
        configs
        agent
        depth_cam
        pan : float
        tilt : float
        __init__()
        get_rgb()
        get_depth()
        get_rgb_depth()
        get_intrinsics()
        pix_to_3dpt()
        _cam2pyrobot()
        _rot_matrix()
        get_current_pcd()
        state()
        get_state()
        get_pan()
        get_tilt()
        set_pan()
        set_tilt()
        _compute_relative_pose()
        set_pan_tilt()
        reset()
    }
    class Gripper{
        configs
        __init__()
        open()
        close()
    }
    class Camera{
        configs
        cv_bridge
        camera_info_lock
        camera_img_lock
        rgb_img : bool
        depth_img : bool
        camera_info : bool
        camera_P : bool
        rgb_sub
        depth_sub
        sync
        __init__()
        _sync_callback()
        _camera_info_callback()
        get_rgb()
        get_depth()
        get_rgb_depth()
        get_intrinsics()
    }
    class Arm{
        configs
        moveit_planner
        planning_time
        use_moveit
        joint_state_lock
        tf_listener
        arm_joint_names
        arm_dof : int
        _joint_angles : dict
        _joint_velocities : dict
        _joint_efforts : dict
        joint_pub : bool
        _ik_service
        _fk_service
        __init__()
        go_home()
        pose_ee()
        get_ee_pose()
        get_transform()
        get_joint_angles()
        get_joint_velocities()
        get_joint_torques()
        get_joint_angle()
        get_joint_velocity()
        get_joint_torque()
        set_joint_positions()
        make_plan_joint_positions()
        set_joint_velocities()
        set_joint_torques()
        set_ee_pose()
        make_plan_pose()
        move_ee_xyz()
        _cancel_moveit_goal()
        compute_fk_position()
        get_jacobian()
        compute_fk_velocity()
        compute_ik()
        _callback_joint_states()
        _pub_joint_positions()
        _pub_joint_velocities()
        _pub_joint_torques()
        _init_moveit()
        _angle_error_is_small()
        _loop_angle_pub_cmd()
        _setup_joint_pub()
    }
    class SimpleCamera{
        _tf_listener
        depth_cam
        cam_cf
        base_f
        __init__()
        get_current_pcd()
        pix_to_3dpt()
        get_link_transform()
    }
    class vx300sArm{
        configs
        moveit_planner
        use_moveit : bool
        __init__()
        go_home()
        move_to_neutral()
        _setup_joint_pub()
        _pub_joint_positions()
        _pub_joint_velocities()
        _pub_joint_torques()
        set_joint_velocities()
    }
    class vx300sGripper{
        gripper
        wait_time : float
        __init__()
        open()
        set_gripper_pressure()
        close()
    }
    class DepthImgProcesso{
        subsample_pixs : int
        depth_threshold : tuples
        cfg_data
        intrinsic_mat
        intrinsic_mat_inv
        uv_one
        uv_one_in_cam
        __init__()
        get_pix_3dpt()
        get_pcd_ic()
        get_pcd_iw()
        read_cfg()
        get_intrinsic()
    }
```

