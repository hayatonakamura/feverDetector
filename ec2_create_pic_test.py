# Hayato Nakamura
# hn2357
# Copyright 2020 Hayato Nakamura
from __future__ import print_function #compatible with python 2.7
import sys, time
import numpy as np
import aws
from collections import OrderedDict
from decimal import *
from datetime import datetime
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

dynamodb = aws.getResource('dynamodb', 'us-east-1')


def retrieve_item(name):
	table = dynamodb.Table(name)
	item = table.get_item(Key={
		'picture_name': '2020_05_04_23_03_54'
		})
	if (len(item) == 1):
		return False
	return item['Item']

def make_photo(name):
	item = retrieve_item(name)
	
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
	plt.savefig('imagetest', dpi = 300)
	plt.close()


def main():
	make_photo('processed_temp')


if __name__ == "__main__":
	main()