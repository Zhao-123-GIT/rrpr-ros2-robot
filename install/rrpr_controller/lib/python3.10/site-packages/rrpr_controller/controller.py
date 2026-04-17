import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class JointController(Node):
    def __init__(self):
        super().__init__('joint_controller')
        self.publisher = self.create_publisher(JointState, '/joint_states', 10)
        self.timer = self.create_timer(0.1, self.publish_joint)

        self.angle = 0.0

    def publish_joint(self):
        msg = JointState()

        msg.name = ['joint1', 'joint2', 'joint3', 'joint4']

        # 👉 让关节动起来（关键）
        msg.position = [
            math.sin(self.angle),
            math.cos(self.angle),
            math.sin(self.angle * 0.5),
            math.cos(self.angle * 0.5)
        ]

        self.publisher.publish(msg)

        self.angle += 0.1

        self.get_logger().info(f'Publishing angle: {self.angle}')


def main(args=None):
    rclpy.init(args=args)
    node = JointController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
