#Controller for robot A with all LED ON

from controller import Robot, Motor, LED

import random as rd



TIME_STEP = 64



MAX_SPEED = 6.28





#create the Robot instance.

robot = Robot()



#get a handler to the motors and set target position to infinity (speed control)



leftMotor = robot.getDevice('left wheel motor')

rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))

rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(0.0)

rightMotor.setVelocity(0.0)



led = []

ledNames = [

    'led0', 'led1', 'led2', 'led3','led4',

    'led5', 'led6', 'led7', 'led8', 'led9' 

]





led0 = robot.getDevice('led0')

led1 = robot.getDevice('led1')

led2 = robot.getDevice('led2')

led3 = robot.getDevice('led3')

led4 = robot.getDevice('led4')

led5 = robot.getDevice('led5')

led6 = robot.getDevice('led6')

led7 = robot.getDevice('led7')

led8 = robot.getDevice('led8')

led9 = robot.getDevice('led9')

    



while robot.step(1000) != -1:



    #generate random path

    random2 = rd.randint(0,2)

    led0.set(1)

    led1.set(1)

    led2.set(1)

    led3.set(1)

    led4.set(1)

    led5.set(1)

    led6.set(1)

    led7.set(1)

    led8.set(1)

    led9.set(1)

    



    #motor go forward

    if random2 == 0:

        leftSpeed  = 0.5 * MAX_SPEED

        rightSpeed = 0.5 * MAX_SPEED

    #motor turn

    elif random2 == 1:

        # turn right

        leftSpeed  = 0.5 * MAX_SPEED

        rightSpeed = -0.5 * MAX_SPEED

    elif random2 == 2:

        # turn left

        leftSpeed  = -0.5 * MAX_SPEED

        rightSpeed = 0.5 * MAX_SPEED

    #write actuators inputs

    leftMotor.setVelocity(leftSpeed)

    rightMotor.setVelocity(rightSpeed)

#Controller for Robot B with all LED OFF

from controller import Robot, Motor, LED

import random as rd



TIME_STEP = 64



MAX_SPEED = 6.28





#create the Robot instance.

robot = Robot()



#get a handler to the motors and set target position to infinity (speed control)



leftMotor = robot.getDevice('left wheel motor')

rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))

rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(0.0)

rightMotor.setVelocity(0.0)



led = []

ledNames = [

    'led0', 'led1', 'led2', 'led3','led4',

    'led5', 'led6', 'led7', 'led8', 'led9' 

]





led0 = robot.getDevice('led0')

led1 = robot.getDevice('led1')

led2 = robot.getDevice('led2')

led3 = robot.getDevice('led3')

led4 = robot.getDevice('led4')

led5 = robot.getDevice('led5')

led6 = robot.getDevice('led6')

led7 = robot.getDevice('led7')

led8 = robot.getDevice('led8')

led9 = robot.getDevice('led9')

    



while robot.step(1000) != -1:



    #generate random path

    random2 = rd.randint(0,2)

    led0.set(0)

    led1.set(0)

    led2.set(0)

    led3.set(0)

    led4.set(0)

    led5.set(0)

    led6.set(0)

    led7.set(0)

    led8.set(0)

    led9.set(0)

    



    #motor go forward

    if random2 == 0:

        leftSpeed  = 0.5 * MAX_SPEED

        rightSpeed = 0.5 * MAX_SPEED

    #motor turn

    elif random2 == 1:

        # turn right

        leftSpeed  = 0.5 * MAX_SPEED

        rightSpeed = -0.5 * MAX_SPEED

    elif random2 == 2:

        # turn left

        leftSpeed  = -0.5 * MAX_SPEED

        rightSpeed = 0.5 * MAX_SPEED

    #write actuators inputs

    leftMotor.setVelocity(leftSpeed)

    rightMotor.setVelocity(rightSpeed)