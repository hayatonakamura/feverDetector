# Hayato Nakamura
# hn2357
# Copyright 2020 Hayato Nakamura
import sys, time, os, json, requests
import numpy as np
import aws
from collections import OrderedDict
from decimal import *
from datetime import datetime
import matplotlib
import get_recent_test
import charts
from twilio.rest import Client
from PIL import Image 
matplotlib.use('agg')
import matplotlib.pyplot as plt
dynamodb = aws.getResource('dynamodb', 'us-east-1')
s3 = aws.getClient('s3', 'us-east-1')
rekog = aws.getClient('rekognition', 'us-east-1')
sns = aws.getClient('sns', 'us-east-1')
api_key = ''   # REMOVE THIS FROM GITHUB
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = 'New York'
account_sid = '' # REMOVE THIS FROM GITHUB
auth_token = '' # REMOVE THIS FROM GITHUB

def get_temp():
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name
	response = requests.get(complete_url) 
	x = response.json() 
	if x["cod"] != "404":
		y = x['main']
		current_temperature = '{:3.2f}'.format(y["temp"] - 273.15)
		return current_temperature
	else:
		return 'Unavailable'

def delete(table, timestamp, s3_del):
	filename = timestamp + '.jpg'
	try:
		table.delete_item(Key={'timestamp': timestamp})
		if s3_del:
			s3.delete_object(
				Bucket='hayatopia',
				Key=filename
				)
		print("Deleted", timestamp)
	except:
		print("Error: Could not delete", timestamp)


def dynamo_add(table, name, item):
	try:
		item['picture_name'] = item['timestamp']
		item['weather'] = get_temp()
		del item['timestamp']
		table.put_item(Item=item)
		print(item['picture_name'], "successfully uploaded...")
	except:
		print(item['picture_name'], "Data upload unsuccessful...")

def add_heatmap_pic(item, timestamp):
	file = timestamp+'_HEATMAP'
	mat = np.zeros((24,32))
	for y in range(24):
		for x in range(32):
			val = Decimal(item[str(32 * (23-y) + x)])
			mat[y, x] = val

	frame = mat
	fig, ax = plt.subplots()
	norm = plt.Normalize(15, 35)
	im = ax.imshow(frame, cmap='rainbow', norm=norm)
	fig.colorbar(im, ax=ax)
	plt.gca().axes.get_xaxis().set_visible(False)
	plt.gca().axes.get_yaxis().set_visible(False)
	plt.savefig(file, dpi = 300)
	plt.close()

	file = file+'.png'
	s3.upload_file(file, 'hayatopia', file, ExtraArgs={'ACL': 'public-read'})
	print("File uploaded to S3")

def PIL_crop(name, boundingBox):
	firstname = name +'.jpg'
	s3.download_file('hayatopia', firstname, firstname)
	im = Image.open(firstname)
	width, height = im.size
	boxHeight = int(boundingBox['Height'] * height)
	boxWidth = int(boundingBox['Width'] * width)
	left = int(boundingBox['Left']*width)
	top = int(boundingBox['Top']*height)
	right = boxWidth+left
	bottom = boxHeight+top
	im1 = im.crop((left, top, right, bottom))
	newname = name + '_cropped.jpg'
	im1.save(newname)
	s3.upload_file(newname, 'facescolumbia', newname, ExtraArgs={'ACL': 'public-read'})
	print("Successfully cropped and uploaded...")

def upload_recent_data_s3(recentTen, table):
	ind = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
	del recentTen['picture_name']

	for key, item in recentTen.items():
		dynamodata = table.get_item(Key={
			'picture_name': item
			})
		dynamodata = dynamodata['Item']
		weather = str(dynamodata['weather'])
		mean = str(dynamodata['mean'])
		try:
			name = dynamodata['name']
		except:
			name = 'Hayato'
		data = [{"picture_name":item, "weather": weather, "mean": mean, "name":name}]
		recentTen[key] = data
	with open('recent.json', 'w') as json_file:
		json.dump(recentTen, json_file, indent=4)

	s3.upload_file('recent.json', 'hayatopia', 'recent.json', ExtraArgs={'ACL': 'public-read'})
	print("RecentTen upload successful...")


def notify(mean):
	try:
		message = "\nPotential Fever Alert\n\n" + "Fever of " + str(mean) +" Celcius\n" + "Individual: "+ "Hayato"
		subject = message
		response = sns.publish(
			TopicArn='arn:aws:sns:us-east-1:440704364062:mta_SNS',
			Message=message,)

		client = Client(account_sid, auth_token)
		messageTwilio = client.messages \
				.create(
					body=message,
					from_='+16504379803',
					to='+18573606130'
				)
	except KeyboardInterrupt:
		exit
	except Exception as e:
		print("Error Sending Notification...")
		print(e)


def clean_up(name, attributes=['ALL']):
	try:
		table = dynamodb.Table(name)
		cleantable= dynamodb.Table('processed_temp')
	except:
		print("Table with name ", name, "doesn't exist...")
		return
	response = table.scan()
	hit = False
	for item in response['Items']:
		timestamp = item['timestamp']
		try:
			filename = str(timestamp) + '.jpg'
			response = rekog.detect_faces(
				Image={
					"S3Object": {
						"Bucket": 'hayatopia',
						"Name": filename,
					}
				},
			    Attributes=attributes,
				)
			# Check if a person is detected
			details = response['FaceDetails']
			if (len(details) == 0):
				delete(table, timestamp, True)
			else:
				dynamo_add(cleantable,'processed_temp', item)
				add_heatmap_pic(item, timestamp)
				if not hit:
					notify(item['mean'])
				for face in response['FaceDetails']:
					PIL_crop(timestamp, face['BoundingBox'])
				delete(table, timestamp, False)
				hit = True

		except Exception as e:
			print("Rekognition failed...")
			print(e)
			delete(table, timestamp, False)

		print("")

	# Update the recent10
	recentTen = get_recent_test.update_recent_ten(cleantable)
	upload_recent_data_s3(recentTen, cleantable)
	print("most recent 10 updated")
	#cleantable.delete_item(Key={'picture_name': 'Recent'})
	#cleantable.put_item(Item=recentTen)
	charts.get_chart_data(cleantable)
	s3.upload_file('weekData.json', 'hayatopia', 'weekData.json', ExtraArgs={'ACL': 'public-read'})
	print("Week Data upload successful...")


def main():
	while 1:
		try:
			clean_up('temperature')
			os.system('rm *.png')
			os.system('rm *.jpg')

			time.sleep(60)
		except KeyboardInterrupt:
			print("exiting...")
			return

if __name__ == "__main__":
	main()
