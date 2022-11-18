import numpy as np
import os
import sys

def write_array(inputfile,data):
        np.savetxt(inputfile,data,fmt="%d")

def read_array(inputfile,n):
	if os.path.isfile(inputfile):
		# print(inputfile+" exists")
		data = np.genfromtxt(inputfile,dtype=np.int32)
	else:
		# print(inputfile+" does not exist")
		data = np.zeros([n,n],dtype=int)
	return data

def show_array(data):
        x = '\n'.join([''.join(['  {:2}'.format(item) for item in row]) for row in data])
        print(x+"\n")


def run(): 
	# read command line argument 
	if len(sys.argv)-1==1:
		n = int(sys.argv[1])
	else:
		n = 3

	# read configuration file, if it exists, otherwise initialize data
	data = read_array("tic-tac-toe.txt",n)

	# show configuration
	# show_array(data)

	# modify configuration
	data[1,1]=1

	# show configuration
	# show_array(data)

	# write configuration
	write_array("tic-tac-toe.txt",data)

run()
