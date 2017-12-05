iostat = open('./iostat.txt', 'r')
result = open('./iostat.csv','w')
#row1=["Device","rrqm/s","wrqm/s","r/s","w/s","rkB/s","wkB/s","avgrq-sz","avgqu-sz","await","w_await","svctm","%util"]
row1=["Device","tps","kB_read/s","kB_wrtn/s","kB_read","kB_wrtn"]
result.write(str(row1))
result.write(",\n")
for line in iostat.readlines():
	if 'sda ' in line:
		x=line.split()
		row= ",".join(map(str,x))
		result.write(row)
		result.write(",\n")
iostat.close()
result.close()

