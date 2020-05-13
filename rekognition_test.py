# Hayato Nakamura
# hn2357
# Copyright 2020 Hayato Nakamura
import sys, time
import numpy as np
from collections import OrderedDict
from decimal import *
from datetime import datetime
from PIL import Image 
sys.path.append('amazon/')
import aws
dynamodb = aws.getResource('dynamodb', 'us-east-1')
s3 = aws.getClient('s3', 'us-east-1')
rekog = aws.getClient('rekognition', 'us-east-1')


def check_picture(attributes = ['ALL']):
	name = 'temp_5_20' + '.jpg'
	response = rekog.detect_faces(
		Image={
			"S3Object": {
				"Bucket": 'hayatopia',
				"Name": name,
			}
		},
	    Attributes=attributes,
		)

	for face in response['FaceDetails']:
		print(face)
		boundingBox = face['BoundingBox']
		download_photo(name)
		PIL_crop(name, boundingBox)


def download_photo(name):
	s3.download_file('hayatopia', name, name)

def PIL_crop(name, boundingBox):
	im = Image.open(name)
	width, height = im.size
	print("original photo size:", im.size)
	boxHeight = int(boundingBox['Height'] * height)
	boxWidth = int(boundingBox['Width'] * width)

	left = int(boundingBox['Left']*width)
	top = int(boundingBox['Top']*height)
	right = boxWidth+left
	bottom = boxHeight+top
	print(left, right)
	print(top, bottom)
	im1 = im.crop((left, top, right, bottom))
	im1.save('temp.jpg') 

def main():
	check_picture()

if __name__ == "__main__":
	main()