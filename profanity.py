def read_file():
    doc= open ('C:\user\Desctop\file.txt')
    contents = doc.read()
    print contents
    doc.close()
    return contents

# function with google api to check profanity in contents
def check_contenct_profanity(contents):
    	connection = urllib.urlopen ('http://www.wdylike.appspot.com/?q='+contents)
output = connection.read()
    	print output
    	connection.close()
   	 if 'true' in output :
        		print " Profanity Alert !! "
   	 elif 'false' in output :
        	print " This document has not curse words :-)"
    	else :
        		print "sorry could not scan the doc "

# read the file and grab contents
contents = read_file()

# check for profanity
check_contenct_profanity(contents)
