from std_msgs.msg import String

import rclpy
from rclpy.node import Node


tompicName = 'communication_topic'
class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, tompicName, 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, world! {self.count}'
        self.publisher_.publish(msg)
        self.count += 1
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()
    rclpy.spin(publisher_node)

    # Destroy the node explicitly
    publisher_node.destroy_node()
    rclpy.shutdown()

    if __name__ == '__main__':
        main()
        