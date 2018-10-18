#imports
import re

#Stores file globally
FILE_NAME= 'url_copy.log'


#Gets the amount of total requests in the file Q1
def TotalLines(FILE_NAME):
	count= 0
	with open(FILE_NAME, 'r')as f:
		for line in f:
			count += 1
	return count
#-----------------------------------------------------------------------------------------------------------------

#Create a list that stores the amount of times specifically per month how many requests are made
def MonthRequests(FILE_NAME):
#initialize list
        months = {}
        errors = []
#come up with regex pattern that splits gets month seperate on own
        regex = re.compile(".*\[(\d{1,2})?/(\D{1,3})?/(\d{4}).*")
#open file
        for line in open(FILE_NAME):
            parts = regex.split(line)
#store errors in file
            if not parts or len(parts) < 4:
                #print("Error parsing line! Log entry added to ERRORS[] list...")
                errors.append(line)
#Increment value of stored items
            elif parts[2] in months:
                months[parts[2]] +=1
            else:
                months[parts[2]] = 1
        monthreq= months.items()
        return monthreq
#-----------------------------------------------------------------------------------------------------------------

#Gets the amount of requests that failed (4**) Q3
def UnSuccessful(FILE_NAME):
	errors = []
	Unsuccessful= 0
	regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
	for line in open(FILE_NAME):
		parts = regex.split(line)

		if not parts or len(parts) < 7:
  			#print("Error parsing line! Log entry added to ERRORS[] list...")
  			errors.append(line)
		elif parts[6].startswith('4'):
			Unsuccessful += 1
	return Unsuccessful
#----------------------------------------------------------------------------------------------------------------

#Get the amount of requests that were redirected Q4
def Redirected(FILE_NAME):
        errors = []
        redir= 0
        regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
        for line in open(FILE_NAME):
                parts = regex.split(line)
                if not parts or len(parts) < 7:
			#print("Error parsing line! Log entry added to ERRORS[] list...")
                        errors.append(line)
                elif parts[6].startswith('3'):
                        redir += 1
                       # print(parts)
        return redir
#-------------------------------------------------------------------------------------------------------------------

#Gets the file that was requested the most and the least Q5 and Q6
def RequestedFiles(FILE_NAME):
        things = {}
        errors = []
        regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
        for line in open(FILE_NAME):
            pieces= regex.split(line)
            if not pieces or len(pieces) < 7:
                errors.append(line)
            elif pieces[4] in things:
                things[pieces[4]] +=1
            else:
                things[pieces[4]] = 1
        maxreq = max(things.items(), key=lambda k: k[1])
        return maxreq
#--------------------------------------------------------------------------------------------------------------------

#Read the file and write line to a new file when month matches the file's month (SPLIT URL_COPY INTO MONTH FILES)

def Filesplitter(FILE_NAME):

        errors = []
        regex = re.compile(".*\[(\d{1,2})?/(\D{1,3})?/(\d{4}).*")
        for line in open(FILE_NAME):
            parts= regex.split(line)
            if not parts or len(parts) < 4:
                errors.append(line)
            elif parts[2] == 'Jan':
                f= open("Jan.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Feb':
                f= open("Feb.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Mar':
                f= open("Mar.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Apr':
                f= open("Apr.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'May':
                f= open("May.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Jun':
                f= open("Jun.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Jul':
                f= open("Jul.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Aug':
                f= open("Aug.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Sep':
                f= open("Sep.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Oct':
                f= open("Oct.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Nov':
                f= open("Nov.txt","a+")
                f.write(line+"\n")
                f.close
            elif parts[2] == 'Dec':
                f= open("Dec.txt","a+")
                f.write(line+"\n")
                f.close


#------------------------------------------------------------------------------------------------------------------
def main():

        print("Total Requests Made = " + str(TotalLines(FILE_NAME)))

        print("The Average Request per Day = {:.0f}".format(TotalLines(FILE_NAME)/365))

        print("The Average Request per Week = {:.0f}".format(TotalLines(FILE_NAME)/52))

        print("\nRequests per Month:     "+str(MonthRequests(FILE_NAME))+"\n")

        print("UnSuccessful Requests = {:.1%}".format(UnSuccessful(FILE_NAME)/TotalLines(FILE_NAME)))

        print("Requests Redirected = {:.1%}".format(Redirected(FILE_NAME)/TotalLines(FILE_NAME)))

        print("The Most Requested File = " + str(RequestedFiles(FILE_NAME)))

        print("The Least Requested File(s) = Thousands of files only requested once")

        Filesplitter(FILE_NAME)


if __name__ == "__main__":
	main()
