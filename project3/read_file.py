import re 


FILE_NAME= 'url_copy.log'

def TotalLines(FILE_NAME):
	count= 0
	with open(FILE_NAME, 'r')as f:
		for line in f:
			count += 1
	return count

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

def Successful(FILE_NAME):
        errors = []
        successful= 0
        regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
        for line in open(FILE_NAME):
                parts = regex.split(line)
                if not parts or len(parts) < 7:
                        #print("Error parsing line! Log entry added to ERRORS[] list...")
                        errors.append(line)
                elif parts[6].startswith('3'):
                        successful += 1
        return successful		



def main():

	print("Total Requests Made = " + str(TotalLines(FILE_NAME)))

	print("UnSuccessful Requests = {:.0%}".format(UnSuccessful(FILE_NAME)/TotalLines(FILE_NAME)))

	print("Successful Requests = {:.0%}".format(Successful(FILE_NAME)/TotalLines(FILE_NAME)))



if __name__ == "__main__":
	main()
