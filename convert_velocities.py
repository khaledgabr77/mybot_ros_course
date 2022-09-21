#! /usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class ConvertVelocities():
    def __init__(self):
        self.sub = rospy.Subscriber('cmd_vel', Twist, self.callback)
        self.right_wheel_pub = rospy.Publisher('/right_wheel_controller/command', Float64, queue_size=1)
        self.left_wheel_pub = rospy.Publisher('/left_wheel_controller/command', Float64, queue_size=1)
        self.twist_vels = Twist()
        self.vr = Float64()
        self.vl = Float64()
        self.rate = rospy.Rate(1)

    def callback(self, msg):
        self.twist_vels = msg
    
    def pub_wheel_vels(self):
        while not rospy.is_shutdown():
            self.convert_velocities()
            self.right_wheel_pub.publish(self.vr)
            self.left_wheel_pub.publish(self.vl)
            self.rate.sleep()

    def convert_velocities(self):
        # L = 0.2
        # R = 0.1
        self.vr = ((2*self.twist_vels.linear.x) + (self.twist_vels.angular.z*0.2))/(2*0.1)
        self.vl = ((2*self.twist_vels.linear.x) - (self.twist_vels.angular.z*0.2))/(2*0.1)

if __name__ == '__main__':
    rospy.init_node('convert_vels_node', anonymous=True)
    rospy.loginfo("Convert velocities node initialized.")
    cv = ConvertVelocities()
    cv.pub_wheel_vels()   
