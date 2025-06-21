from std_msgs.msg import String

import rclpy
from rclpy.node import Node

topicName = 'communication_topic'
class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            String,
            topicName,
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    subscriber_node = SubscriberNode()
    rclpy.spin(subscriber_node)

    # Destroy the node explicitly
    subscriber_node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()