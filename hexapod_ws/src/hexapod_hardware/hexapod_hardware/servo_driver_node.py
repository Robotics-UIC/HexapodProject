import rclpy
from hexapod_interfaces.msg import HexapodJointState
from rclpy.node import Node
from sensor_msgs.msg import JointState


class ServoDriverNode(Node):
    def __init__(self) -> None:
        super().__init__("servo_driver_node")
        self.latest_joint_command = HexapodJointState()
        self.create_subscription(
            HexapodJointState,
            "/hexapod/joint_command",
            self._joint_command_callback,
            10,
        )
        self.joint_state_pub = self.create_publisher(JointState, "/joint_states", 10)
        self.publish_timer = self.create_timer(0.05, self._publish_placeholder_joint_state)
        self.get_logger().info("servo_driver_node started (placeholder mode)")

    def _joint_command_callback(self, msg: HexapodJointState) -> None:
        self.latest_joint_command = msg

    def _publish_placeholder_joint_state(self) -> None:
        joint_state = JointState()
        joint_state.header.stamp = self.get_clock().now().to_msg()
        joint_state.name = list(self.latest_joint_command.joint_names)
        joint_state.position = list(self.latest_joint_command.position)
        joint_state.velocity = list(self.latest_joint_command.velocity)
        joint_state.effort = list(self.latest_joint_command.effort)
        self.joint_state_pub.publish(joint_state)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = ServoDriverNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
