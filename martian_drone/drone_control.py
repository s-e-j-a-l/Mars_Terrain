import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class DroneController(Node):
    def __init__(self):
        super().__init__('drone_controller')
        self.publisher_ = self.create_publisher(Twist, '/X3/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_drone)  # Control loop every 100ms
        self.start_time = time.time()

    def control_drone(self):
        msg = Twist()
        elapsed_time = time.time() - self.start_time

        if elapsed_time < 5:
            msg.linear.z = 1.0  # Take off
        elif elapsed_time < 35:  # Hover for at least 30 seconds
            msg.linear.z = 0.0  # Maintain altitude
        elif elapsed_time < 40:
            msg.linear.z = -1.0  # Land
        else:
            msg.linear.z = 0.0
            self.get_logger().info("Mission Complete")
            self.timer.cancel()
            return

        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg}")

def main(args=None):
    rclpy.init(args=args)
    node = DroneController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

