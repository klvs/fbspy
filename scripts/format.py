import os

count = 0;
for i in os.listdir(os.getcwd()+'/csv'):
	count = count + 1
	with open('./csv/'+i, 'r') as f:
		lines = f.readlines()
	lines.pop(0)
	userid = i.split('.')[0]
	lines = [str(count) + ',' + userid + ','+ line for line in lines]
	with open('./concat.csv', 'a') as f:
		f.writelines(lines)

