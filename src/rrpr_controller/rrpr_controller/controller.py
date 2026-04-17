import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import time
import math

class Controller(Node):
    def __init__(self):
        super().__init__('controller')
        self.pub = self.create_publisher(JointState, '/joint_states', 10)
        self.t = 0.0

        self.timer = self.create_timer(0.1, self.update)

    def update(self):
        msg = JointState()
        msg.name = ['joint1', 'joint2', 'joint3', 'joint4']

        self.t += 0.1

        msg.position = [
            math.sin(self.t),
            math.cos(self.t),
            0.1 + 0.1 * math.sin(self.t),  # prismatic 伸缩
            math.sin(self.t)
        ]

        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Controller()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()