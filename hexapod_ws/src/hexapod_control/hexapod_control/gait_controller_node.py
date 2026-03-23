import rclpy
from geometry_msgs.msg import Point, Twist
from hexapod_interfaces.msg import HexapodLegCommand
from rclpy.node import Node
from std_msgs.msg import String


LEG_NAMES = ["lf", "lm", "lr", "rf", "rm", "rr"]


class GaitControllerNode(Node):
    def __init__(self) -> None:
        super().__init__("gait_controller_node")
        self.current_mode = "stand"
        self.latest_cmd_vel = Twist()

        self.create_subscription(Twist, "/cmd_vel", self._cmd_vel_callback, 10)
        self.create_subscription(String, "/gait/mode", self._gait_mode_callback, 10)
        self.leg_command_pub = self.create_publisher(HexapodLegCommand, "/hexapod/leg_command", 10)
        self.publish_timer = self.create_timer(0.05, self._publish_placeholder_leg_command)
        self.get_logger().info("gait_controller_node started (placeholder mode)")

    def _cmd_vel_callback(self, msg: Twist) -> None:
        self.latest_cmd_vel = msg

    def _gait_mode_callback(self, msg: String) -> None:
        self.current_mode = msg.data

    def _publish_placeholder_leg_command(self) -> None:
        leg_command = HexapodLegCommand()
        leg_command.header.stamp = self.get_clock().now().to_msg()
        leg_command.header.frame_id = "base_link"
        leg_command.gait_mode = self.current_mode
        leg_command.cycle_phase = 0.0
        leg_command.leg_names = LEG_NAMES
        leg_command.foot_positions = [Point(x=0.0, y=0.0, z=0.0) for _ in range(6)]
        leg_command.stance_mask = [True] * 6
        self.leg_command_pub.publish(leg_command)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = GaitControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
