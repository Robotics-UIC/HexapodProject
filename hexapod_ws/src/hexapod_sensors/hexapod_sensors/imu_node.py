import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu


class ImuNode(Node):
    def __init__(self) -> None:
        super().__init__("imu_node")
        self.imu_pub = self.create_publisher(Imu, "/imu/data", 10)
        self.publish_timer = self.create_timer(0.02, self._publish_placeholder_imu)
        self.get_logger().info("imu_node started (placeholder mode)")

    def _publish_placeholder_imu(self) -> None:
        imu_msg = Imu()
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.header.frame_id = "imu_link"
        imu_msg.orientation.w = 1.0
        self.imu_pub.publish(imu_msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = ImuNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
