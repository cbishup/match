import csv
import os
import shutil



def main():
	with open("NXR TEST DATA.xlsx - Roster upload TEST DATA.csv") as csvfile:
		data = [row for row in csv.reader(csvfile.read().splitlines())]
		highschool = data[0][9]
		#for num in range(958):
		newList = []
		newList.append(["1. Remove any athletes who are not competing for your team this year"])
		newList.append(["2. Add new athletes into the next empty rows"])
		newList.append(["3. Fill out each athletes information, be sure all required fields are completed"])
		newList.append(["4. Required fields are indicated by a d star"])
		newList.append(["5. Double check all information and make sure spelling is consistent and correct"])
		newList.append([""])
		newList.append(["FirstName", "LastName", "Gender", "GraduationYear", "BirthDate", "Address", "City", "State", "PostalCode", "SchoolAttended", "TeamName", "Email", "PhoneNumber", "EmergencyContactName", "EmergencyContactPhone"])
		#mid_ind = 0
		line = 0
		while line < len(data):
		#for line in range(mid_ind,len(data)):
			if (highschool.lower() or highschool.lower() + " ") == data[line][9].lower():
				newList.append(data[line-1])
				highschool = data[line][9]
				line+=1
			else:
				newList.append(data[line-1])
				newpath = "/Users/mattsewall/Desktop/Big/%s" % highschool
				with open("%s" % (highschool + " Athlete.csv"), "w") as fp:
					a = csv.writer(fp, delimiter=',')
					a.writerows(newList)
				newnewpath = "/Users/mattsewall/Desktop/Big/%s/%s_Athlete.csv" % (highschool,highschool)
				newnewnewpath = "/Users/mattsewall/Desktop/Big/%s /%s_Athlete.csv" % (highschool,highschool)
				filename = "%s" % (highschool + " Athlete.csv")
				unmatched_path = "/Users/mattsewall/Desktop/Big/Unmatched/%s" %filename
				if os.path.exists(newpath):
					shutil.move(filename, newnewpath)
					os.rename("/Users/mattsewall/Desktop/Big/%s" % highschool, "/Users/mattsewall/Desktop/Big/2016_%s" % highschool)
					#make directory tage have 2016
				elif os.path.exists("%s" % (newpath + " ")):
					shutil.move(filename, newnewnewpath)
					os.rename("/Users/mattsewall/Desktop/Big/%s " % highschool, "/Users/mattsewall/Desktop/Big/2016_%s" % highschool)
					#make directory tage have 2016
				else:
					shutil.move(filename, unmatched_path)
				newList = []
				newList.append(["1. Remove any athletes who are not competing for your team this year"])
				newList.append(["2. Add new athletes into the next empty rows"])
				newList.append(["3. Fill out each athletes information, be sure all required fields are completed"])
				newList.append(["4. Required fields are indicated by a * star"])
				newList.append(["5. Double check all information and make sure spelling is consistent and correct"])
				newList.append([""])
				newList.append(["*FirstName", "*LastName", "*Gender", "*GraduationYear", "*BirthDate", "Address", "*City", "*State", "*PostalCode", "*SchoolAttended", "*TeamName", "*Email", "PhoneNumber", "EmergencyContactName", "EmergencyContactPhone"])
				highschool = data[line][9]
				line+=1









if __name__ == '__main__':
    main()
