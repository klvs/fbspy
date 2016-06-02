
with open('./final.csv', 'r') as f:
	lines = f.readlines()
lines.pop(0)

total = 0 # 24 hrs
totalNight = 0 # 10pm-4am 1459832400-1459854000
totalMorning = 0 # 6am - 11:59am 1459861200-1459882800

user = 1
lineList = []

# calculate total time online
for line in lines:
	split = line.split(',')
	index = int(split[0])
	time1 = int(split[1])
	time2 = int(split[2])
	difference = time2 - time1
	if time1 > 1459832400 and time2 < 1459854000:
		totalNight = totalNight + difference
	if time1 > 1459861200 and time2 < 1459882800:
		totalMorning = totalMorning + difference
	print(str(difference) + ' = ' + str(time2) + ' - ' + str(time1))
	if user != index:
		with open('./classifications.csv', 'a') as f:
			f.write(str(user) + ',' + str(total) + ',' + str(totalNight) + ',' + str(totalMorning) + '\n')

		total = 0
		totalNight = 0
		totalMorning = 0
		user = index

	total = total + difference

# # calculate total time morning 6am - 12pm
# for line in lines:
# 	split = line.split(',')
# 	index = int(split[0])
# 	time1 = int(split[1])
# 	time2 = int(split[2])
