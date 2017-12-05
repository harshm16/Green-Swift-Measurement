iozone = open('./iozone1.txt', 'r')
result = open('./iozone.csv','w')
for line in iozone:
	x=line.split()
	row= ",".join(map(str,x))
	result.write(row)
	result.write(",\n")
iozone.close()
result.close()

