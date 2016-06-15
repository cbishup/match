import csv
import os
import shutil





def main():
	with open("Coach info all regionsCLEAN.csv") as csvfile:
		data = [row for row in csv.reader(csvfile.read().splitlines())]
		highschool = data[0][4]
		#for num in range(958):
		newList = []
		#mid_ind = 0
		line = 0
		while line < len(data):
		#for line in range(mid_ind,len(data)):
			if (highschool.lower() or highschool.lower() + " ") == data[line][4].lower():
				newList.append(data[line-1])
				highschool = data[line][4]
				line+=1
			else:

                    #tmp_file = open("%s" % (highschool + " 2016"), "w")
                    #for x in newList:
                        #tmp_file.write("%s \n" % x)
                       #newList = []
				newList.append(data[line-1])
				newpath = "/Users/mattsewall/Desktop/Big/%s" % highschool
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				with open("%s" % (highschool + " Coach.csv"), "w") as fp:
					a = csv.writer(fp, delimiter=',')
					a.writerows(newList)
				newnewpath = "/Users/mattsewall/Desktop/Big/%s/%s_Coach.csv" % (highschool,highschool)
				filename = "%s" % (highschool + " Coach.csv")
				oldpath = "/Users/mattsewall/Desktop/coaches/%s_Coach.csv" % highschool
				shutil.move(filename, newnewpath)
				newList = []
				highschool = data[line][4]
				line+=1









if __name__ == '__main__':
    main()
