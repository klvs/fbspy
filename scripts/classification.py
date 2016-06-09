import sys
print('classifying ' + sys.argv[1])

with open(sys.argv[1], 'r') as f:
	lines = f.readlines()
lines.pop(0)

with open('./classifications.csv', 'a') as f:
	f.write('user,total,totalNight1,totalMorning1,totalNight2,totalMorning2,totalNight3,totalMorning3,totalNight4,totalMorning4\n') 



total = 0 # 24 hrs
totalNight1 = 0
totalMorning1 = 0
totalNight2 = 0
totalMorning2 = 0
totalNight3 = 0
totalMorning3 = 0
totalNight4 = 0
totalMorning4 = 0

user = 1
lineList = []

# calculate total time online
for line in lines:
	split = line.split(',')
	selectedUser = int(split[0])
	time1 = int(split[1])
	time2 = int(split[2])
	difference = time2 - time1

	# day 1
	if time1 > 1464613200 and time2 < 1464656400:
		totalMorning1 = totalMorning1 + difference
	if time1 > 1464656400 and time2 < 1464699600:
		totalNight1 = totalNight1 + difference
	# day 2
	if time1 > 1464699600 and time2 < 1464742800:
		totalMorning2 = totalMorning2 + difference
	if time1 > 1464742800 and time2 < 1464786000:
		totalNight2 = totalNight2 + difference
	# day 3
	if time1 > 1464786000 and time2 < 1464829200:
		totalMorning3 = totalMorning3 + difference
	if time1 > 1464829200 and time2 < 1464872400:
		totalNight3 = totalNight3 + difference
	# day 4
	if time1 > 1464872400 and time2 < 1464915600:
		totalMorning4 = totalMorning4 + difference
	if time1 > 1464915600 and time2 < 1464958800:
		totalNight4 = totalNight4 + difference

	# print(str(difference) + ' = ' + str(time2) + ' - ' + str(time1))
	if user != selectedUser:
		with open('./classifications.csv', 'a') as f:
			f.write(str(user) + ',' + str(total) + ',' 
				+ str(totalNight1) + ',' 
				+ str(totalMorning1) + ',' 
				+ str(totalNight2) + ',' 
				+ str(totalMorning2) + ',' 
				+ str(totalNight3) + ',' 
				+ str(totalMorning3) + ',' 
				+ str(totalNight4) + ',' 
				+ str(totalMorning4)
				+ '\n')

		total = 0
		totalNight1 = 0
		totalMorning1 = 0
		totalNight2 = 0
		totalMorning2 = 0
		totalNight3 = 0
		totalMorning3 = 0
		totalNight4 = 0
		totalMorning4 = 0
		user = index

	total = total + difference