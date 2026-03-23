import rclpy
from hexapod_interfaces.msg import HexapodJointState, HexapodLegCommand
from rclpy.node import Node


class InverseKinematicsNode(Node):
    def __init__(self) -> None:
        super().__init__("inverse_kinematics_node")
        self.create_subscription(
            HexapodLegCommand,
            "/hexapod/leg_command",
            self._leg_command_callback,
            10,
        )
        self.joint_command_pub = self.create_publisher(
            HexapodJointState,
            "/hexapod/joint_command",
            10,
        )
        self.get_logger().info("inverse_kinematics_node started (placeholder mode)")

    def _leg_command_callback(self, msg: HexapodLegCommand) -> None:
        joint_command = HexapodJointState()
        joint_command.header.stamp = self.get_clock().now().to_msg()
        joint_command.header.frame_id = msg.header.frame_id
        joint_command.joint_names = [f"joint_{idx}" for idx in range(18)]
        joint_command.position = [0.0] * 18
        joint_command.velocity = [0.0] * 18
        joint_command.effort = [0.0] * 18
        joint_command.control_mode = 0
        self.joint_command_pub.publish(joint_command)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = InverseKinematicsNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
