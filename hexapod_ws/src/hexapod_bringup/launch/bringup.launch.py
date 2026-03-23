from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    use_state_estimator = LaunchConfiguration("use_state_estimator")
    robot_namespace = LaunchConfiguration("robot_namespace")

    declare_use_state_estimator = DeclareLaunchArgument(
        "use_state_estimator",
        default_value="true",
        description="Start the optional state estimator node.",
    )
    declare_robot_namespace = DeclareLaunchArgument(
        "robot_namespace",
        default_value="",
        description="Optional namespace for all hexapod nodes.",
    )

    nodes = [
        Node(
            package="hexapod_teleop",
            executable="teleop_node",
            name="teleop_node",
            namespace=robot_namespace,
            output="screen",
        ),
        Node(
            package="hexapod_control",
            executable="gait_controller_node",
            name="gait_controller_node",
            namespace=robot_namespace,
            output="screen",
        ),
        Node(
            package="hexapod_control",
            executable="inverse_kinematics_node",
            name="inverse_kinematics_node",
            namespace=robot_namespace,
            output="screen",
        ),
        Node(
            package="hexapod_hardware",
            executable="servo_driver_node",
            name="servo_driver_node",
            namespace=robot_namespace,
            output="screen",
        ),
        Node(
            package="hexapod_sensors",
            executable="imu_node",
            name="imu_node",
            namespace=robot_namespace,
            output="screen",
        ),
        Node(
            package="hexapod_sensors",
            executable="camera_node",
            name="camera_node",
            namespace=robot_namespace,
            output="screen",
        ),
        Node(
            package="hexapod_sensors",
            executable="state_estimator_node",
            name="state_estimator_node",
            namespace=robot_namespace,
            output="screen",
            condition=IfCondition(use_state_estimator),
        ),
    ]

    return LaunchDescription(
        [
            declare_use_state_estimator,
            declare_robot_namespace,
            *nodes,
        ]
    )
