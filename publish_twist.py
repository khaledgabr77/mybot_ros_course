#! /usr/bin/env python


import rospy
from geometry_msgs.msg import Twist

rospy.init_node("publish_twist_node")
pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
vels = Twist()
vels.linear.x = 1.0
vels.angular.z = 1.0
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    pub.publish(vels)
    rate.sleep()
