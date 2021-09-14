from controller import Robot, DistanceSensor, Motor, LED





import random as rand









# time in [ms] of a simulation step





TIME_STEP = 64





MAX_SPEED = 6.28





# create the Robot instance.





robot = Robot()





# initialize devices



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





    psValues = []   





    for i in range(8):





        psValues.append(ps[i].getValue())



        





    # a set of obstacles possibilities





    right_obstacle = psValues[0] > 80.0 and psValues[1] > 80.0





    left_obstacle = psValues[6] > 80.0 and psValues[7] > 80.0





    front_wall = psValues[0] > 80.0 and psValues[7] > 80.0 





    sidewall_left = psValues[1] > 80.0 and psValues[2] > 80.0





    sidewall_right = psValues[5] > 80.0 and psValues[6] > 80.0 





    opponent_front = psValues[7] > 80.0 and psValues[0] > 80.0 





    option = psValues[1] > 80.0 or psValues[6] > 80.0





    all_wall = psValues[0] > 80.0 and psValues[7] > 80.0 and psValues[1] > 80.0 and psValues[6] > 80.0





    opponent_right =  psValues[1] > 80.0 or psValues[0] > 80.0





    opponent_left =  psValues[6] > 80.0 or psValues[7] > 80.0





    no_obstacle = psValues[0] < 85.0 and psValues[1] < 85.0 and psValues[2] < 85.0 and psValues[6] < 85.0 and psValues[5] < 85.0 and psValues[7] < 85.0





    back_wall = psValues[3] > 80.0 and psValues[4] > 80.0







    # Read position sensors:





    distanceL = sensor_positionL.getValue()





    distanceR = sensor_positionR.getValue()







    # initialize motor speeds at 50% of MAX_SPEED.





    leftSpeed  = MAX_SPEED





    rightSpeed = MAX_SPEED



    





    # xd to random the turning descision  if robot detect all wall ahead





    xd = rand.randint(1, 4)







    # a set of condition for robot determining on which sensor combination detect the obstacle





    if no_obstacle:





       leftSpeed  =  MAX_SPEED





       rightSpeed =  MAX_SPEED





    elif all_wall:





         if xd == 1:





            # turn right





            leftSpeed  = MAX_SPEED





            rightSpeed = -MAX_SPEED





         elif xd == 2:





            # turn left





            leftSpeed  = -MAX_SPEED





            rightSpeed =  MAX_SPEED





         elif xd == 3:





            leftSpeed  = -0.75 * MAX_SPEED





            rightSpeed =  MAX_SPEED





         elif xd == 4:





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



    



    elif back_wall:



    



        leftSpeed  = MAX_SPEED



        



        rightSpeed  = MAX_SPEED       





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





    elif opponent_front:





        leftSpeed  = MAX_SPEED





        rightSpeed = MAX_SPEED





    elif opponent_right:





        leftSpeed  = MAX_SPEED



        



        rightSpeed =  0.95 * MAX_SPEED





    elif opponent_left:



     



        leftSpeed  = 0.95 * MAX_SPEED





        rightSpeed =  MAX_SPEED





    # write actuators inputs





    leftMotor.setVelocity(leftSpeed)





    rightMotor.setVelocity(rightSpeed)