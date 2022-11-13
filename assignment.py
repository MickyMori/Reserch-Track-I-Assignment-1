from __future__ import print_function

import time
from sr.robot import *

R = Robot()

a_th = 2.0

d_th = 0.4

'''This list is used to keep track of which silver marker have already been grabbed'''
silver_token_list = []


'''This list is used to keep track of which golden marker are already paired with a silver one'''
golden_token_list = []


'''drive is a function that makes the robot move forward or backwards, depending on the sign of the 
   speed value, for a certain amount of time specified by the variable seconds'''
def drive(speed, seconds):
    
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
    
'''turn is a function that makes the robot turn left or right, depending on the sign of the 
   speed value, for a certain amount of time specified by the variable seconds'''
def turn(speed, seconds):
    
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
    
'''The find_silver_token function is used to locate the closest silver marker not already used 
   that the robot sees. The funtion returns the distance and the angle in respect to the y-axis 
   at which the marker is. It also returns the id of the marker.'''
def find_silver_token():
    
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and token.info.code not in silver_token_list:
            dist=token.dist
	    rot_y=token.rot_y
	    code = token.info.code
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, code
   	
   	
'''The find_golden_token function is used to locate the closest golden marker not already used 
   that the robot sees. The funtion returns the distance and the angle in respect to the y-axis 
   at which the marker is. It also returns the id of the marker.'''   	
def find_golden_token():
    
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and token.info.code not in golden_token_list:
            dist=token.dist
	    rot_y=token.rot_y
	    code = token.info.code
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, code
   	
   	
'''The grab_silver_token fuction calls the find_silver_function. If the robot sees a silver
   marker that is not been already used it will get closer to it using the drive function to
   move forward and the turn function to adjust its rotation as it proceeds. If the robot doesn't
   see any new silver marker it will turn a bit to the right and look again. Once the robot is
   close enough to the marker it will grab it.'''
def grab_silver_token():
	dist, rot_y, code = find_silver_token()
	while 1:
		if dist==-1:
			print("I don't see any token!!")
			turn(+10, 1)
		elif dist <d_th: 
        		print("Found it!")
        		if R.grab():
        			silver_token_list.append(code)
        			return
        	elif -a_th<= rot_y <= a_th: 
			print("Ah, that'll do.")
        		drive(20, 0.5)
    		elif rot_y < -a_th: 
        		print("Left a bit...")
        		turn(-2, 0.5)
    		elif rot_y > a_th:
        		print("Right a bit...")
        		turn(+2, 0.5)
        	dist, rot_y, code = find_silver_token()
        	
        	
'''The go_close_to_golden_token fuction calls the find_golden_function. If the robot sees a golden
   marker that is not been already used it will get closer to it using the drive function to
   move forward and the turn function to adjust its rotation as it proceeds. If the robot doesn't
   see any new golden marker it will turn a bit to the right and look again. Once the robot is
   close enough to the marker it will release the silver token previously grabbed.'''        	
def go_close_to_golden_token():
	dist, rot_y, code = find_golden_token()
	while 1:
		if dist==-1:
			print("I don't see any token!!")
			turn(+10, 1)
		elif dist <d_th*1.5: 
        		print("Found it!")
        		if R.release():
        			golden_token_list.append(code)
        			return
        	elif -a_th<= rot_y <= a_th: 
			print("Ah, that'll do.")
        		drive(20, 0.5)
    		elif rot_y < -a_th: 
        		print("Left a bit...")
        		turn(-2, 0.5)
    		elif rot_y > a_th:
        		print("Right a bit...")
        		turn(+2, 0.5)
		dist, rot_y, code = find_golden_token()

'''The main body of the program consits in a while loop that calls the grab_silver_token and
   go_close_to_golden_token. Once the robot released the silver marker it will drive backwards
   a bit to avoid dragging the marker around as it proceeds towards the next one. Once all six
   golden markers have been used, and thus the golden_token_list's length is equal to six, the
   program will break out of the loop.'''
while 1:
    grab_silver_token()
    go_close_to_golden_token()
    drive(-20,0.5)
    if len(golden_token_list) == 6:
    	print("I'm done! All silver tokens have been paired with a golden one!")
    	break
