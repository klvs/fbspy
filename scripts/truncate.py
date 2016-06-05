
with open('./concat.csv', 'r') as f:
	lines = f.readlines()
# lines.pop(0)
with open('./truncated.csv', 'a') as f:
	f.write('index,time1,time2\n')
for line in lines:
	split = line.split(',')
	time = int(split[2])
	if (time > 1459810800) and (time < 1459897200):
		with open('./truncated.csv', 'a') as f:
			f.write(line)

