import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo, Image


class CameraNode(Node):
    def __init__(self) -> None:
        super().__init__("camera_node")
        self.image_pub = self.create_publisher(Image, "/camera/image_raw", 10)
        self.camera_info_pub = self.create_publisher(CameraInfo, "/camera/camera_info", 10)
        self.publish_timer = self.create_timer(0.1, self._publish_placeholder_camera)
        self.get_logger().info("camera_node started (placeholder mode)")

    def _publish_placeholder_camera(self) -> None:
        stamp = self.get_clock().now().to_msg()

        image_msg = Image()
        image_msg.header.stamp = stamp
        image_msg.header.frame_id = "camera_link"
        image_msg.height = 1
        image_msg.width = 1
        image_msg.encoding = "rgb8"
        image_msg.is_bigendian = 0
        image_msg.step = 3
        image_msg.data = [0, 0, 0]
        self.image_pub.publish(image_msg)

        camera_info = CameraInfo()
        camera_info.header.stamp = stamp
        camera_info.header.frame_id = "camera_link"
        camera_info.height = 1
        camera_info.width = 1
        self.camera_info_pub.publish(camera_info)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = CameraNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
