#!/usr/bin/env python


from numpy import transpose
from main import *
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header, Float32
import time
import numpy as np

a_joint_max = np.ones(6) * 0.1
V_joint_max = np.ones(6)

a_cart_max = 1000 * np.ones(3)
V_cart_max = 1000 * np.ones(3)
x0 = 0
y0 = 0
z0 = 0

Tb = np.matrix([[1.0, 0.0, 0.0, x0], [0.0, 1.0, 0.0,y0], [0.0, 0.0, 1.0, z0], [0, 0, 0, 1.0]],
               dtype=float)

t_discr = 0.01

junc = 5 * t_discr
ptp1 = np.matrix([0.7, 0.2, 1, 0.3, 0.8, 1.5])
lin1 = np.matrix([500, 500, 600])
ptp2 = np.matrix([0.2, 0.3, 1.2, 0.2, 0.2, 0.2])
lin2 = np.matrix([600, 1000, 1500])

from time import time, sleep
from math import ceil



def talker():
    rospy.init_node('trajectory')
    rate = rospy.Rate(100)
    joints_control = JointState()
    joints_control.header = Header()
    joints_control.name = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
    joints_control.velocity = np.zeros(6, dtype=np.float)
    joints_control.effort = np.zeros(6, dtype=np.float)
    joints_control.position = np.zeros(6, dtype=np.float)
    joints_control.header.stamp = rospy.Time.now()

    rate.sleep()
    joints_control.header.stamp = rospy.Time.now()
    q_des = [ptp1, lin1, ptp2, lin2]
    commands = ["PTP", "LIN", "PTP", "LIN"]

    for i in range(l):
        q = joints_control.position
        start_time = time()
        cur_time = time()
        prev_time = time(
        print("start move")
        joints_control.velocity = np.zeros(6)
        if i == 'LIN': lin(q,q_des[i])
        else: ptp(q,q_des[i])
        exit(0)


if __name__ == '__main__':
    д = le()
    try:
        talker()
    except rospy.ROSInterruptException:
        exit(0)
        pass
