import rclpy
from geometry_msgs.msg import PoseStamped
from rclpy.node import Node
from sensor_msgs.msg import Imu


class StateEstimatorNode(Node):
    def __init__(self) -> None:
        super().__init__("state_estimator_node")
        self.latest_imu = Imu()
        self.create_subscription(Imu, "/imu/data", self._imu_callback, 10)
        self.state_pub = self.create_publisher(PoseStamped, "/hexapod/state", 10)
        self.publish_timer = self.create_timer(0.05, self._publish_placeholder_state)
        self.get_logger().info("state_estimator_node started (placeholder mode)")

    def _imu_callback(self, msg: Imu) -> None:
        self.latest_imu = msg

    def _publish_placeholder_state(self) -> None:
        state_msg = PoseStamped()
        state_msg.header.stamp = self.get_clock().now().to_msg()
        state_msg.header.frame_id = "base_link"
        state_msg.pose.orientation = self.latest_imu.orientation
        self.state_pub.publish(state_msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = StateEstimatorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
