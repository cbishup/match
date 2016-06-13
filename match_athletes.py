import sys
import csv


def read_file(file):
	newList = []
	lines = open(file)
	for line in lines:
		temp1 = [x for x in line.split(',')]
		newList.append(temp1)
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

def sortcsvbymanyfields(csvfilename, themanyfieldscolumnnumbers):
	with open(csvfilename, 'rU') as f:
		readit = csv.reader(f)
		thedata = list(readit)
		thedata.sort(key=operator.itemgetter(*themanyfieldscolumnnumbers))
	with open("new_file", 'wb') as k:
		writeit = csv.writer(k)
		writeit.writerows(thedata)

def main():
	sortcsvbymanyfields("NXR TEST DATA.xlsx - Roster upload TEST DATA.csv",15)


	
	"""reader = csv.reader(open("NXR TEST DATA.xlsx - Roster upload TEST DATA.csv"), delimiter=",")
	
	for id, path, title, date, author, platfo, type, port, dog, school, cat, pig, goat, orrr, annnn in reader:
	    print school"""
	"""for num in range(958):
		highschool = base_file[0][9]
		newList = []
		n+=1
		print n 
		for line in range(len(base_file)-1):
			highschool = base_file[line][9]
			if highschool == base_file[line+1][9]:
				newList.append(base_file[line])
			else:
				print line
				tmp_file = open("%s" % (highschool + " 2016"), "w")
				for x in newList:
					tmp_file.write("%s \n" % x)
				tmp_file.close()"""
				
	"""for i in range(958):
		d = {basefile[i]:basefile[i][9]}
		print d"""
			
  

if __name__ == '__main__':
    main()