
import os

with open(os.getcwd()+'/compressed.csv', 'r') as f:
	lines = f.readlines()

for line in lines:
	split = line.split(',')
	del split[1]

	with open('./removed_uid.csv', 'a') as f:
		f.write(','.join(split))
