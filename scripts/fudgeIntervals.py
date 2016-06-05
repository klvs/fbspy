# For a lot of users it's common for them to go on and offline every 20-90 seconds
# When compressing the data, these users are counted as being online for 0s
# This script counts those intervals as 30 seconds long
import os
import sys

with open('./removed_uid.csv', 'r') as f:
	lines = f.readlines()
# legend = lines.pop(0) # pop first (legend)

# with open(os.getcwd()+'/final.csv', 'a') as f:
# 	f.write(legend)

for line in lines:
	split = line.split(',')
	index = int(split[0])
	time1 = int(split[1])
	time2 = int(split[2])

	if time1 == time2:
		time2 = time1 + 60

	with open(os.getcwd()+ '/' + sys.argv[1], 'a') as f:
		f.write(str(index) + ',' + str(time1) + ',' + str(time2) + '\n')





