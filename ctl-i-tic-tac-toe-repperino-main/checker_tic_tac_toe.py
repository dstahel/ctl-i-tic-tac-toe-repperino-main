import numpy as np
import sys
import os
from time import process_time

# 4 aug 2022 mk@mat.ethz.ch

# use as: python3 checker_tic_tac_toe.py <yourcode.py> <argument>

inputfile 	= "tic-tac-toe.txt"
credits 	= 0
max_credits     = 0

def printinfo(text):
	print("         "+text)

def credit(points):
	global credits
	credits += points
	printinfo(str(credits)+"/"+str(max_credits)+" checks passed")

def ok(text):
	global max_credits
	max_credits += 1
	print("+ok:  "+text)
	credit(1)

def bad(text):
	global max_credits
	max_credits += 1
	print("-bad: "+text)
	printinfo(str(credits)+"/"+str(max_credits)+" checks passed")
	print("This checker tool exited with an error. Repair the problem and try again")
	sys.exit(-1)

def call_code(code,argument):	
	call_string = "python3 "+code+" "+str(argument)
	# print("calling: "+call_string)
	status = os.system(call_string)
	status = int(status/256)
	return status

def read_array(inputfile,myn):
	if os.path.isfile(inputfile):
		ok(inputfile+" exists")
	else:
		bad(inputfile+" has not been created")
	data = np.genfromtxt(inputfile,dtype=np.int)
	show_array(data)
	(n,cols)=data.shape
	if n==cols:
        	ok("rows = cols");
	else:
       		bad("rows <> cols");
	if data.size==n**2:
        	ok("data size "+str(n)+"x"+str(cols))
	else:
        	bad("data size")
	if n==myn:
		ok("code argument sys.argv[1] was recognized properly")
	else:
		bad("code argument sys.argv[1] was NOT recognized properly n = "+str(n)+" <> "+str(myn))

	ones=0
	twos=0
	for i in range(n):
		for j in range(n):
			if data[i,j] not in [0,1,2]:
				bad("your array contains numbers not in {0,1,2}")
			if (data[i,j]==1):
				ones+=1
			if (data[i,j]==2):
				twos+=1

	zeros = n**2-ones-twos
	printinfo("array contains "+str(zeros)+" zeros, "+str(ones)+" ones and "+str(twos)+" twos")
	return data,n,zeros,ones,twos

def write_array(inputfile,data):
	np.savetxt(inputfile,data,fmt="%d")

def show_array(data):
	x = '\n'.join([''.join(['  {:2}'.format(item) for item in row]) for row in data])
	print(x)

def check_some_config(wanted,data,code,myn):
	# prepare final config
	write_array(inputfile,data)
	status = call_code(code,myn)
	if status==-1:
		ok("exit (winner) status "+str(status))
	else:
		show_array(data)
		bad("winner = exit value should be -1 in that case")

def checker(code,myn):
	printinfo("testing "+code+" "+str(myn))

	# delete inputfile
	if os.path.isfile(inputfile):
		os.remove(inputfile)

	# start code for n=myn
	status = call_code(code,myn)

	# investigate the resulting inputfile
	data,n,zeros,ones,twos = read_array(inputfile,myn)
	if ones==1:
		ok("a single 1")
	if twos!=0:
		bad("the first move is by player 1")
	if zeros!=n**2-1:
		bad("there should be a single 1 after the first move")	

	# continue code
	status = call_code(code,myn)

	# investigate the resulting inputfile
	data,n,zeros,ones,twos = read_array(inputfile,myn)

	if ones==1:
	        ok("a single 1")
	else:	
		bad("there should be a single 1 after two moves")
	if twos==1:
	        ok("a single 2")
	else:
		bad("there should be a single 2 after two moves")

	# continue code
	if os.path.isfile(inputfile):
		os.remove(inputfile)
	movecount = 0
	for loop in range(n**2):
		movecount += 1
		status = call_code(code,myn)
		data,n,zeros,ones,twos = read_array(inputfile,myn)
		if (movecount % 2)==1:
			if ones==twos+1:
				ok("move ok")
			else:
				bad("incorrect move")
		else:
			if ones==twos:
				ok("move ok")
			else:
				bad("incorrect move")
	
	if status in [1,2,3]:
		ok("exit (winner) status "+str(status))
	else:
		show_array(data)
		bad("your code should exit with 1,2, or 3")
	
	if myn==3:
		check_some_config(1,[[1,2,0],[1,0,2],[1,0,0]],code,myn)
		check_some_config(2,[[2,1,1],[1,2,0],[0,0,2]],code,myn)
		check_some_config(-1,[[2,2,2],[2,2,1],[2,0,2]],code,myn)
		check_some_config(-1,[[0,2,4],[0,2,0],[0,2,0]],code,myn)
	elif myn==4:
		check_some_config(1,[[1,2,0,0],[0,1,2,0],[2,0,1,0],[0,2,0,1]],code,myn)

	# speed test
	printinfo("stand by, performing speed test ..")		
	tic = process_time()
	for speedtest in range(5):
		printinfo(str(speedtest)+"/5")
		if os.path.isfile(inputfile):
       			os.remove(inputfile)
		for loop in range(n**2):
       	 		status = call_code(code,myn)
	toc = process_time()-tic
	printinfo("cpu time: "+str(toc))
	ok("speed test passed")

mypath = os.getcwd()	
	
if len(sys.argv)>=2:
	code = mypath+"/"+sys.argv[1]
	checker(code,int(sys.argv[2]))
else:
	code = mypath+"/tic_tac_toe.py"
	checker(code,3)
	checker(code,4)
