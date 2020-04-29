# Hayato Nakamura Copyright 2018 

#Dependencies
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import os
import time

os.chdir('/Users/Hayato/Desktop/Columbia_University/Spring_2020/IoT/final_project/videos')

def read_data(filename):

	h = 0

	mini = 15
	maxi = 35


	# Making the plot
	linecount = 0
	numcount = 0
	loopcount = 0
	var = ""

	matlist1 = []
	matlist2 = []
	matlist3 = []
	matlist4 = []
	matlist5 = []
	matlist6 = []
	matlist7 = []
	matlist8 = []
	matlist9 = []
	matlist10 = []
	matlist11 = []
	matlist12 = []
	matlist13 = []
	matlist14 = []
	matlist15 = []
	matlist16 = []
	matlist17 = []
	matlist18 = []
	matlist19 = []
	matlist20 = []
	matlist21 = []
	matlist22 = []
	matlist23 = []
	matlist24 = []


	h = 0

	file = open(filename, "r")
	for line in file:

		#just for show
		print(h)
		h += 1
		if (len(line) < 10):
			print("new line")
		else:
			if (linecount == 0):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist1.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 1):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist2.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 2):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist3.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 3):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist4.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 4):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist5.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 5):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist6.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 6):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist7.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 7):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist8.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 8):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist9.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 9):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist10.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 10):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist11.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 11):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist12.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 12):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist13.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 13):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist14.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 14):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist15.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 15):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist16.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 16):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist17.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 17):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist18.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 18):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist19.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 19):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist20.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 20):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist21.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 21):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist22.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 22):
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist23.append(f)
							var = ""
					else:
						numcount = 0
						var = ""
			elif (linecount == 23):
				linecount = -1
				loopcount += 1
				for x in range(0, len(line)):
					if (line[x] != " "):
						var = var + line[x]
						numcount += 1
						if (numcount == 4 and var[1] == '.'):
							numcount = 5
						if (numcount == 5):
							numcount = 0
							f = float(var)
							matlist24.append(f)
							var = ""
					else:
						numcount = 0
						var = ""



				#Making the image and saving it
				frame = [matlist1, matlist2, matlist3, matlist4, matlist5, matlist6, matlist7, matlist8, matlist9, matlist10, matlist11, matlist12, matlist13, matlist14, matlist15, matlist16, matlist17, matlist18, matlist19, matlist20, matlist21, matlist22, matlist23, matlist24]
				matlist1 = []
				matlist2 = []
				matlist3 = []
				matlist4 = []
				matlist5 = []
				matlist6 = []
				matlist7 = []
				matlist8 = []
				matlist9 = []
				matlist10 = []
				matlist11 = []
				matlist12 = []
				matlist13 = []
				matlist14 = []
				matlist15 = []
				matlist16 = []
				matlist17 = []
				matlist18 = []
				matlist19 = []
				matlist20 = []
				matlist21 = []
				matlist22 = []
				matlist23 = []
				matlist24 = []



				fig, ax = plt.subplots()

				norm = plt.Normalize(mini, maxi)


				#cm = matplotlib.colors.ListedColormap(C/255.0)
				#im = ax.imshow(frame, cmap='rainbow', norm=norm, interpolation = "bilinear") #Greys, gray, rainbow
				#im = ax.imshow(frame, cmap='gray', norm=norm, interpolation = "bilinear")
				#im = ax.imshow(frame, cmap='gray', norm=norm)

				im = ax.imshow(frame, cmap='rainbow', norm=norm)
				fig.colorbar(im, ax=ax)

				# draw gridlines
				#ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.5)
				#ax.set_xticks(np.arange(0, 16, 1));
				#ax.set_yticks([0, 1, 2, 3])
				#ax.set(yticks = [0, 1, 2, 3], xticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
				plt.gca().axes.get_xaxis().set_visible(False)
				plt.gca().axes.get_yaxis().set_visible(False)
				#plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
				#plt.yticks(np.arange(0,4,1))
				#ax.set_title("Melexis Colormap")

				tempname = 'sample' + str(loopcount)
				#plt.colorbar()
				plt.savefig(tempname, dpi = 300)
				plt.close()
			

			linecount += 1;


	file.close()


#************************************ FFMPEG ********************************************************

def make_video(filename):
	temp_string = "ffmpeg -framerate 10 -i 'sample%d.png' -c:v libx264 -pix_fmt yuv420p -crf 23 " + filename + ".mp4"
	os.system(temp_string)
	#framerate can also be kept at somewhere between 3 and 16



#************************************ Delete pic ********************************************************

def delete_photo():
	deletecounter = 0
	while (1):
		try:
			deletecounter = deletecounter + 1 
			file = 'sample' + str(deletecounter) + '.png'
			deletepic = "rm " + file
			os.system(deletepic)
			# added additional code so not really a delete counter
			if (deletecounter > 200):
				break
		except:
			print("All photos deleted")
			break


#************************************ Main Function ********************************************************

def main():
	file_names = ['temptest']

	i = 0
	while i < len(file_names):
		#Enter your own directory here
		temp_string = '/Users/Hayato/Desktop/Columbia_University/Spring_2020/IoT/final_project/data/' + file_names[i] + '.txt'
		read_data(temp_string)	
		make_video(file_names[i])
		delete_photo()
		time.sleep(8)
		i += 1

	#print at the end
	print("")
	print("******************************")
	print("******************************")
	print("")
	print("                                 DONE")
	print("******************************")
	print("******************************")
	print("")	


if __name__ == "__main__":
	# execute only if run as a script
	main()