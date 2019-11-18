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


def lin(Q, des):
    r0 = ((Tbase * FK(Q)))[0:3, 3]
    r0 = transpose(r0)
    r = r0

    delta_q = (np.asarray(des - r0))[0]

    t = np.zeros(3, dtype=np.float)
    T = np.zeros(3, dtype=np.float)
    Tf = np.zeros(3, dtype=np.float)
    Vmax = np.copy(V_cart_max)
    amax = np.copy(a_cart_max)

    for i in range(len(t)):
        if np.sqrt(amax[i] * abs(Q[i])) > Vmax[i]:
            t[i] = Vmax[i] / amax[i]
            T[i] = abs(Q[i]) / Vmax[i]
            Tf[i] = t[i] * 2 + T[i]
        else:
            Vmax[i] = np.sqrt(amax[i] * abs(Q[i]))
            t[i] = np.sqrt(abs(Q[i]) / amax[i])
            T[i] = t[i]
            Tf[i] = 2 * t[i]

    tmax = ceil(max(t) / t_discr) * t_discr
    Tmax = ceil(max(T) / t_discr) * t_discr

    dir = abs(delta_q) / delta_q
    vel_profile = [t[0], T[0], Tf[0], Vmax, amax]

    while prev_time - start_time < vel_profile[2]:
        freq = 0.
        steps = 0

        cur_time = time()
        dt = cur_time - prev_time
        freq += dt
        steps += 1

        QRet = np.zeros(3, dtype=np.float)
        [t, T, Tf, Vmax, amax, trapezia] = traj_params
        for i in range(len(QRet)):
            if trapezia[i]:
                if time <= t:
                    QRet[i] = amax[i] * time
                elif time > t and time <= T:
                    QRet[i] = Vmax[i]
                elif time > T and time <= Tf:
                    QRet[i] = Vmax[i] - amax[i] * (time - T)
                else:
                    QRet[i] = 0
            else:
                if time <= t:
                    QRet[i] = amax[i] * time
                elif time > t and time <= Tf:
                    QRet[i] = Vmax[i] - amax[i] * (time - T)
                else:
                    QRet[i] = 0

        vel = np.assaray(QRet)
        while time() - cur_time < t_discr:
            sleep(0.00001)
        prev_time = cur_time


def ptp(Q, des):
    delta_q = (np.asarray(des - Q))
    t = np.zeros(6, dtype=np.float)
    T = np.zeros(6, dtype=np.float)
    Tf = np.zeros(6, dtype=np.float)
    Vmax = np.copy(V_cart_max)
    amax = np.copy(a_cart_max)

    for i in range(len(t)):
        if np.sqrt(amax[i] * abs(Q[i])) > Vmax[i]:
            t[i] = Vmax[i] / amax[i]
            T[i] = abs(Q[i]) / Vmax[i]
            Tf[i] = t[i] * 2 + T[i]
        else:
            Vmax[i] = np.sqrt(amax[i] * abs(Q[i]))
            t[i] = np.sqrt(abs(Q[i]) / amax[i])
            T[i] = t[i]
            Tf[i] = 2 * t[i]

    tmax = ceil(max(t) / t_discr) * t_discr
    Tmax = ceil(max(T) / t_discr) * t_discr
    trapezia = []
    for i in range(len(t)):
        Vmax[i] = abs(Q[i]) / Tmax
        amax[i] = Vmax[i] / tmax
        if np.sqrt(amax[i] * abs(Q[i])) > Vmax[i]:
            t[i] = Vmax[i] / amax[i]
            T[i] = abs(Q[i]) / Vmax[i]
            Tf[i] = T[i] + t[i]
            trapezia.append(True)
        else:
            Vmax[i] = np.sqrt(amax[i] * abs(Q[i]))
            t[i] = np.sqrt(abs(Q[i]) / amax[i])
            T[i] = t[i]
            Tf[i] = 2 * t[i]
            trapezia.append(False)
    dir = abs(delta_q) / delta_q

    vel_profile = [t[0], T[0], Tf[0], Vmax, amax, trapezia]

    while prev_time - start_time < vel_profile[2]:
        freq = 0.
        steps = 0

        cur_time = time()
        dt = cur_time - prev_time
        freq += dt
        steps +=
        QRet = np.zeros(6, dtype=np.float)

        [t, T, Tf, Vmax, amax, trapezia] = traj_params
        for i in range(len(QRet)):
            if trapezia[i]:
                if time <= t:
                    QRet[i] = amax[i] * time
                elif time > t and time <= T:
                    QRet[i] = Vmax[i]
                elif time > T and time <= Tf:
                    QRet[i] = Vmax[i] - amax[i] * (time - T)
                else:
                    QRet[i] = 0
            else:
                if time <= t:
                    QRet[i] = amax[i] * time
                elif time > t and time <= Tf:
                    QRet[i] = Vmax[i] - amax[i] * (time - T)
                else:
                    QRet[i] = 0
        vel = np.assaray(QRet)

        while time() - cur_time < t_discr:
            sleep(0.00001)
        prev_time = cur_time


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

    exit(0)


if __name__ == '__main__':
    д = le()
    try:
        talker()
    except rospy.ROSInterruptException:
        exit(0)
        pass