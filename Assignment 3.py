-----------------------------------------------------------------------------------------------------------------------------------------

from controller import DistanceSensor, Motor, Supervisor

from math import sqrt

import random as rd



TIME_STEP = 32



MAX_SPEED = 6.28



supervisor = Supervisor()



# get handle to robot's translation field

robot_node = supervisor.getFromDef("epuck")

trans_field = robot_node.getField("translation")

rotation = robot_node.getField("rotation")



leftMotor = supervisor.getDevice('left wheel motor')

rightMotor = supervisor.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))

rightMotor.setPosition(float('inf'))



leftMotor.setVelocity(0.0)

rightMotor.setVelocity(0.0)



sensorLeft = supervisor.getDevice("left wheel sensor")

sensorRight = supervisor.getDevice("right wheel sensor")

sensorLeft.enable(TIME_STEP)

sensorRight.enable(TIME_STEP)



for a in range(0, 25):

    for b in range(0, 33):

        

        # reset robot position and physics

        random1 = rd.uniform(-0.4,0.4)

        random2 = rd.uniform(-0.4,0.4)

        random3 = rd.uniform(-3,3)

        INITIAL = [random1, 0, random2]

        INITIAL2 = [0,1,0,random3]

        trans_field.setSFVec3f(INITIAL)

        rotation.setSFRotation(INITIAL2)

        robot_node.resetPhysics()

        

        # evaluate robot during 60 seconds (simulation time)

        t = supervisor.getTime()

        while supervisor.getTime() - t < 60:



            # perform robot control according to a, b

            # (and possibly t) parameters.



            leftSpeed  = 0.5 * MAX_SPEED

            rightSpeed = 0.5 * MAX_SPEED

    

            leftMotor.setVelocity(leftSpeed)

            rightMotor.setVelocity(rightSpeed)    

    

            valueLeft = sensorLeft.getValue()

            valueRight = sensorRight.getValue()

            print("Time step: ", TIME_STEP)

            print("Left motor sensor value is: ", valueLeft)

            print("Right motor sensor value is: ", valueRight)

            

            values = trans_field.getSFVec3f()

            if values[0] > 0.45 or values[0] < -0.45 or values[2] > 0.45 or values[2] < -0.45:

                # reset robot position and physics

                random1 = rd.uniform(-0.4,0.4)

                random2 = rd.uniform(-0.4,0.4)

                random3 = rd.uniform(-3,3)

                INITIAL = [random1, 0, random2]

                INITIAL2 = [0,1,0,random3]

                trans_field.setSFVec3f(INITIAL)

                rotation.setSFRotation(INITIAL2)

                robot_node.resetPhysics()



            # controller termination

            if supervisor.step(TIME_STEP) == -1:

                quit()

        

        supervisor.simulationSetMode(0)