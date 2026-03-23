import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from std_msgs.msg import String


class TeleopNode(Node):
    def __init__(self) -> None:
        super().__init__("teleop_node")
        self.cmd_vel_pub = self.create_publisher(Twist, "/cmd_vel", 10)
        self.gait_mode_pub = self.create_publisher(String, "/gait/mode", 10)
        self.publish_timer = self.create_timer(0.1, self._publish_placeholder_commands)
        self.get_logger().info("teleop_node started (placeholder mode)")

    def _publish_placeholder_commands(self) -> None:
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.linear.y = 0.0
        cmd.linear.z = 0.0
        cmd.angular.x = 0.0
        cmd.angular.y = 0.0
        cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(cmd)

        gait_mode = String()
        gait_mode.data = "stand"
        self.gait_mode_pub.publish(gait_mode)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = TeleopNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
