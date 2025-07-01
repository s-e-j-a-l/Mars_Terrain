# File: unpause_world.py
import rclpy
from rclpy.node import Node
from gz.msgs.msg import WorldControl
from gz.transport import Node as GzNode
import time

class WorldUnpauser(Node):
    def __init__(self):
        super().__init__('world_unpauser')
        self.gz_node = GzNode()
        self.service = "/world/quadcopter_teleop/control"  # Change to match your world name
        self.msg = WorldControl()
        self.msg.pause = False
        self.timer = self.create_timer(1.0, self.send_unpause)

    def send_unpause(self):
        success = self.gz_node.request(self.service, self.msg, 1000)
        if success:
            self.get_logger().info("World unpause command sent.")
        else:
            self.get_logger().warn("Retrying to unpause world...")

def main(args=None):
    rclpy.init(args=args)
    node = WorldUnpauser()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
