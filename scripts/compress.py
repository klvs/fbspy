import os

with open(os.getcwd()+'/raw.csv', 'r') as f:
	lines = f.readlines()

legend = lines.pop(0) # pop first (legend)
# with open(os.getcwd()+'/compressed.csv', 'a') as f:
# 	f.write(legend)
previous = lines.pop(0).split(',') # init the first point

with open(os.getcwd()+'/compressed.csv', 'a') as f:
	last = lines[0].split(',')
	lastWasOnline = last[3] == '3'

	first = last
	# delete first
	del lines[0]

	if lastWasOnline:
		del first[3:]
		f.write(','.join(first))


	for line in lines:

		split = line.split(',')
		isOnline = split[3] == '3'

		# offline to online
		if isOnline and not lastWasOnline:
			# looking for another '3'
			del split[3:]
			f.write(','.join(split))
		# online to offline
		if not isOnline and lastWasOnline:
			# finish the last one
			f.write(',' + last[2] + '\n')


		last = split
		lastWasOnline = isOnline