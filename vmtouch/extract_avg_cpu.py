iostat = open('./Output/Random/iostat5gb.txt', 'r')
result = open('./Output/Random/Extracted/avgcpu_result5gb.csv','w')
for line in iostat:
	if 'avg-cpu' in line:
		l=next(iostat) 
		x=l.split()
		row= ",".join(map(str,x))
		result.write(row)
		result.write(",\n")
iostat.close()
result.close()

