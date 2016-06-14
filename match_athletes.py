import csv


def read_file(file):
    lines = open(file)
    newList = []
    for line in lines:
        newerList = []
        temp1 = [x for x in line.split('\r')]
        for linex in temp1:
            temp = [y for y in line.split(",")]
            newerList.append(temp)
        newList.append(newerList)
    return newList

def pull_highschool(sorted_file, index):
    for line in range(index,len(sorted_file)):
        newList = []
        highschool = sorted_file[line][9]
        tmp_highschool = ''
        for tmp_line in range(line,len(sorted_file)):
            tmp_highschool = sorted_file[tmp_line][9]
            if tmp_highschool == highschool:
                newList.append(sorted_file[tmp_line])
            else:
                print newList

#def check_highschool(mid,end,spvar):
	


def main():
	with open("NXR TEST DATA.xlsx - Roster upload TEST DATA.csv") as csvfile:
		data = [row for row in csv.reader(csvfile.read().splitlines())]
		highschool = data[0][9]
		print len(data)
		#for num in range(958):
		newList = []
		#mid_ind = 0
		line = 0
		while line < len(data):
		#for line in range(mid_ind,len(data)):
			if (highschool.lower() or highschool.lower() + " ") == data[line][9].lower():
				newList.append(data[line-1])
				print "newList"
				highschool = data[line][9]
				line+=1
			else:

                    #tmp_file = open("%s" % (highschool + " 2016"), "w")
                    #for x in newList:
                        #tmp_file.write("%s \n" % x)
                       #newList = []
				newList.append(data[line-1])
				with open("%s" % (highschool + " 2016"), "w") as fp:
					a = csv.writer(fp, delimiter=',')
					a.writerows(newList)
				newList = []
				highschool = data[line][9]
				line+=1
			








if __name__ == '__main__':
    main()