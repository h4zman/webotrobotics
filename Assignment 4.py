#can position

#coordinate 1: (x = 0.37 y = 0.06~ z= 0.32) m

#coordinate 3: (x = -0.35 y = 0.06~ z= -0.33)m

#coordinate 2: (x = -0.35 y= 0.06~ z= 0.39) m



from controller import Robot, DistanceSensor, Motor

import random as rand



# time in [ms] of a simulation step

TIME_STEP = 64



MAX_SPEED = 6.28



# create the Robot instance.

robot = Robot()



# initialize devices

ps = []

psNames = [

    'ps0', 'ps1', 'ps2', 'ps3',

    'ps4', 'ps5', 'ps6', 'ps7'

]



for i in range(8):

    ps.append(robot.getDevice(psNames[i]))

    ps[i].enable(TIME_STEP)



leftMotor = robot.getDevice('left wheel motor')

rightMotor = robot.getDevice('right wheel motor')

leftMotor.setPosition(float('inf'))

rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(0.0)

rightMotor.setVelocity(0.0)



#Position sensor initialization

sensor_positionL = robot.getDevice('left wheel sensor')

sensor_positionL.enable(TIME_STEP)

sensor_positionR = robot.getDevice('right wheel sensor')

sensor_positionR.enable(TIME_STEP)



# feedback loop: step simulation until receiving an exit event

while robot.step(TIME_STEP) != -1:

    # read sensors outputs

    psValues = []

    for i in range(8):

        psValues.append(ps[i].getValue())



    # a set of obstacles possibilities

    right_obstacle = psValues[0] > 80.0 and psValues[1] > 80.0

    left_obstacle = psValues[6] > 80.0 and psValues[7] > 80.0

    front_wall = psValues[0] > 80.0 and psValues[7] > 80.0 

    sidewall_left = psValues[1] > 80.0 and psValues[2] > 80.0

    sidewall_right = psValues[5] > 80.0 and psValues[6] > 80.0 

    can_front = psValues[7] > 80.0 and psValues[0] > 80.0 

    option = psValues[1] > 80.0 or psValues[6] > 80.0

    all_wall = psValues[0] > 80.0 and psValues[7] > 80.0 and psValues[1] > 80.0 and psValues[6] > 80.0

    can_right =  psValues[1] > 80.0 or psValues[0] > 80.0

    can_sharp_right = psValues[2] > 80.0 and psValues[1] < 80.0

    can_left =  psValues[6] > 80.0 or psValues[7] > 80.0

    can_sharp_left = psValues[5] > 80.0 and psValues[6] < 80.0

    no_obstacle = psValues[0] < 85.0 and psValues[1] < 85.0 and psValues[2] < 85.0 and psValues[6] < 85.0 and psValues[5] < 85.0 and psValues[7] < 85.0

    # Read position sensors:

    distanceL = sensor_positionL.getValue()

    distanceR = sensor_positionR.getValue()

    print("position sensor left:{} right:{}".format(distanceL,distanceR))



    # initialize motor speeds at 50% of MAX_SPEED.

    leftSpeed  = MAX_SPEED

    rightSpeed = MAX_SPEED

    # xd to random the turning descision  if robot detect all wall ahead

    xd = rand.randint(1, 4)

    print(xd)

    # a set of condition for robot determining on which sensor combination detect the obstacle

    if no_obstacle:

       print("no obstacle")

       leftSpeed  =  MAX_SPEED

       rightSpeed =  MAX_SPEED

    elif all_wall:

         if xd == 1:

            print("xd = 1")

            # turn right

            leftSpeed  = MAX_SPEED

            rightSpeed = -MAX_SPEED

         elif xd == 2:

            print("xd = 2")

            # turn left

            leftSpeed  = -MAX_SPEED

            rightSpeed =  MAX_SPEED

         elif xd == 3:

            print("xd = 3")

            leftSpeed  = -0.75 * MAX_SPEED

            rightSpeed =  MAX_SPEED

         elif xd == 4:

            print("xd = 4")

            leftSpeed  = MAX_SPEED

            rightSpeed = -0.75 * MAX_SPEED

    elif front_wall and psValues[1] > 80.0 :

          # turn right

          leftSpeed  = -0.9 * MAX_SPEED

          rightSpeed =  MAX_SPEED

    elif front_wall and psValues[6] > 80.0:

          leftSpeed  = MAX_SPEED

          rightSpeed = -0.9 * MAX_SPEED

          rightSpeed =  MAX_SPEED     

    elif right_obstacle:

        leftSpeed  =  -MAX_SPEED

        rightSpeed =   MAX_SPEED

    elif left_obstacle:

        leftSpeed  =  -MAX_SPEED

        rightSpeed =  MAX_SPEED

    elif sidewall_left:

        leftSpeed  = -MAX_SPEED

        rightSpeed = MAX_SPEED

    elif sidewall_right:

        leftSpeed  = MAX_SPEED

        rightSpeed = -MAX_SPEED    

    elif can_front:

        leftSpeed  = MAX_SPEED

        rightSpeed = MAX_SPEED

    elif can_right:

        leftSpeed  = MAX_SPEED

        rightSpeed = 0.9 * MAX_SPEED

    elif can_left:

        leftSpeed  = 0.9 * MAX_SPEED

        rightSpeed =  MAX_SPEED

    # write actuators inputs

    leftMotor.setVelocity(leftSpeed)

    rightMotor.setVelocity(rightSpeed)