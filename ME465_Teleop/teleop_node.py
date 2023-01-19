import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class TeleopNode(Node):
    def __init__(self):
        super().__init__("teleop_node")
        self.create_subscription(
            Joy,
            "/joy",
            self.joy_callback,
            5,
        )
        self.robot_command = self.create_publisher(
            Twist,
            "/commands/velocity",
            5,
        )
        
    def joy_callback(self, msg):
        command = Twist()
        command.linear.x = 0.2 * msg.axes[1]
        command.angular.z = 1.5 * msg.axes[0]
        self.robot_command.publish(command)
        

def main(args=None):
    rclpy.init(args=args)
    node = TeleopNode()
    rclpy.spin(node)
    
    
if __name__ == "__main__":
    main()
