
with open('./final.csv', 'r') as f:
	lines = f.readlines()
lines.pop(0)

total = 0
user = 1
for line in lines:
	split = line.split(',')
	index = int(split[0])
	time1 = int(split[1])
	time2 = int(split[2])
	difference = time2 - time1
	print(str(difference) + ' = ' + str(time2) + ' - ' + str(time1))
	if user != index:
		with open('./classifications.csv', 'a') as f:
			f.write(str(user) + ',' + str(total) + '\n')
		total = 0
		user = index

	total = total + difference



