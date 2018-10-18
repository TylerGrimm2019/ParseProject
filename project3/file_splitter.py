import re
FILE_NAME= 'url_copy.log'

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

def main():

        Filesplitter(FILE_NAME)

if __name__ == "__main__":
        main()
