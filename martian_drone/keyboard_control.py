import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty

class KeyboardControl(Node):
    def __init__(self):
        super().__init__('keyboard_control')
        self.publisher = self.create_publisher(Twist, '/X3/cmd_vel', 10)
        self.settings = termios.tcgetattr(sys.stdin)
        self.run()

    def run(self):
        print("Use keys: w/s = forward/back | a/d = strafe left/right | i/k = up/down | q/e = yaw left/right | Ctrl-C to quit")
        try:
            while True:
                key = self.get_key()
                twist = Twist()

                if key == 'w':
                    twist.linear.x = 1.0
                elif key == 's':
                    twist.linear.x = -1.0
                elif key == 'a':
                    twist.linear.y = 1.0
                elif key == 'd':
                    twist.linear.y = -1.0
                elif key == 'i':
                    twist.linear.z = 1.0
                elif key == 'k':
                    twist.linear.z = -1.0
                elif key == 'q':
                    twist.angular.z = 1.0
                elif key == 'e':
                    twist.angular.z = -1.0
                elif key == '\x03':  # Ctrl+C
                    break
                else:
                    # No valid key — publish zero velocities
                    twist.linear.x = 0.0
                    twist.linear.y = 0.0
                    twist.linear.z = 0.0
                    twist.angular.z = 0.0

                self.publisher.publish(twist)

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            return sys.stdin.read(1)
        return ''

def main():
    rclpy.init()
    node = KeyboardControl()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
