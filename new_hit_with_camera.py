# Hayato Nakamura
# hn2357
# Copyright 2020 Hayato Nakamura
from __future__ import print_function #compatible with python 2.7
import sys, time
import numpy as np
from picamera import PiCamera 
import aws
from collections import OrderedDict
from decimal import *
from datetime import datetime
#import threading
dynamodb = aws.getResource('dynamodb', 'us-east-1')
s3 = aws.getClient('s3', 'us-east-1')

def search(mat):
	# Scan the matrix
	for y in range(24-3):
		for x in range(32-3):
			window = mat[y:y+3, x:x+3]
			print(window)
			print(np.mean(window))
			if (np.mean(window) > 28):
				print("\n\nHIT\n\n")
				return True
	return False


def process_pic(name):
	camera = PiCamera()
	camera.capture('/home/pi/Desktop/mlx90640-library/' + name + '.jpg')
	camera.close()
	try:
		file = name + '.jpg'
		s3.upload_file(file, 'hayatopia', file)
		print("File uploaded on S3")
	except:
		print("S3 failed...")


def dynamo_add(name, arr, timestamp):
	try:
		table = dynamodb.Table(name)
	except:
		print("Table with name ", name, "doesn't exist...")
		return
	items = OrderedDict()
	items['timestamp'] = timestamp
	for x in range(len(arr)):
		val = '{:3.2f}'.format(arr[x])
		val = Decimal(val)
		items[str(x)] = val
	try:
		table.put_item(Item=items)
		print("Data successfully uploaded...")
	except:
		print("Data upload unsuccessful...")

# def t_add(name, ir):
# 	try:
# 		print('Starting Thread: ', threading.currentThread().getName())
# 		take_picture(name)
# 		dynamo_add('temperature', ir)
# 		print ('Exiting Thread: ', threading.currentThread().getName())
# 	except:
# 		print("Error with threading...")



def main():
	fifo = open('/var/run/mlx9062x.sock', 'r')
	for z in range(20):
		file = open('temperature.txt', 'w')
		mat = np.zeros((24, 32))

		# 20 frames
		ir = np.frombuffer(fifo.read()[0:3072], dtype=np.float32)
		if (len(ir) == 0):
			break

		temp = ""
		for y in range(24):
			for x in range(32):
				val = '{:3.2f}'.format(ir[32 * (23-y) + x])
				temp += val + " "

				mat[y, x] = float(val)
			file.write(temp)
			file.write('\n')
			temp = ""
		file.write('\n')
		file.write('\n')

		file.close()
		if (search(mat)):
			print("here")
			now = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
			name = 'temp'
			process_pic(now)
			dynamo_add('temperature', ir, now)
			# t1 = threading.Thread(name='Upload to dynamo', target=t_add, args=(name, ir,))
			# t1.setDaemon(True)
			# t1.start()

		time.sleep(0.1) #10fps

	

if __name__ == "__main__":
	#print("Active threads: ", threading.active_count())
	main()

