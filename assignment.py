from __future__ import print_function

import time
from sr.robot import *

R = Robot()

a_th = 2.0

d_th = 0.4

silver_token_list = []

golden_token_list = []

def drive(speed, seconds):
    
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
    

def turn(speed, seconds):
    
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    
    

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
   	
   	

def grab_silver_token():
	dist, rot_y, code = find_silver_token()
	while 1:
		if dist==-1:
			print("I don't see any token!!")
			turn(+10, 1)
		elif dist <d_th: 
        		print("Found it!")
        		R.grab()
        		silver_token_list.append(code)
        		print(silver_token_list)
        		print(golden_token_list)
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
        	
        	
        	
def go_close_to_golden_token():
	dist, rot_y, code = find_golden_token()
	while 1:
		if dist==-1:
			print("I don't see any token!!")
			turn(+10, 1)
		elif dist <d_th*1.5: 
        		print("Found it!")
        		R.release()
        		golden_token_list.append(code)
        		print(silver_token_list)
        		print(golden_token_list)
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


while 1:
    grab_silver_token()
    go_close_to_golden_token()
    drive(-20,0.5)
    if len(golden_token_list) == 6:
    	print("I'm done! All silver tokens have been paired with a golden one!")
    	break
