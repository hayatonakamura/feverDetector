# Hayato Nakamura
# hn2357
# Copyright 2020 Hayato Nakamura

from datetime import datetime
import pytz as tz
est = tz.timezone('US/Eastern')


def update_recent_ten(table):

	response = table.scan()
	dates = []
	for item in response['Items']:
		if (item['picture_name'] == 'Recent'):
			continue
		time = item['picture_name']
		timeObject = datetime.strptime(time, '%Y_%m_%d_%H_%M_%S')
		dates.append(timeObject)


	now = datetime.now(tz=est).strftime("%Y_%m_%d_%H_%M_%S")
	now = datetime.now(tz=est).strptime(now, "%Y_%m_%d_%H_%M_%S")
	#now = str(now)
	#newnow = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
	
	youngest = max(dt for dt in dates if dt < now)

	recentTen = {'picture_name': 'Recent'}

	ind = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

	for x in range(10):
		youngest = max(dt for dt in dates if dt < now)
		dates.remove(youngest)
		youngest = datetime.strftime(youngest, "%Y_%m_%d_%H_%M_%S")
		recentTen[ind[x]] = str(youngest)
	return recentTen




