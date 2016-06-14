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
        filenew = open("schools", "w")
        newList = []
        for line in data:
            highschool = line[9]
            check = False
            for x in newList:
                if x == highschool:
                    check = True
            if check != True:
                newList.append(highschool)
        for y in newList:
            filenew.write("%s \n" %y)









if __name__ == '__main__':
    main()
