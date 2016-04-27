import os

with open(os.getcwd()+'/concat.csv', 'r') as f:
	lines = f.readlines()

lines.pop(0) # pop first (legend)
# previous = lines.pop(0).split(',') # init the first point

with open(os.getcwd()+'/compressed.csv', 'a') as f:
	# f.write(','.join(previous)) # write first
	for line in lines:
		split = line.split(',')
		# print(split[3])
		if split[3] == '3':
			del split[4:]
			f.write(','.join(split) + '\n')
