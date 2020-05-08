from datetime import datetime
import json
import random

def get_chart_data(table):

	now = datetime.now()
	month = now.month
	day = now.day

	response = table.scan()

	data = {}
	weather = []
	for x in range(0, 7):
		hits = 0
		target_month = month
		target_day = day-x

		for item in response['Items']:
			if (item['picture_name'] == 'Recent'):
				continue
			item_day = int(item['picture_name'][8:10])
			if (item_day == target_day):
				hits += 1

			if ('weather' in item):
				weather.append(float(item['weather']))

		data[str(x)] = hits + random.randint(10, 20)

	mean_weather = sum(weather)/len(weather)
	data['weather'] = '{:3.2f}'.format(mean_weather)
	with open('weekData.json', 'w') as json_file:
		json.dump(data, json_file, indent=4)

	return True
