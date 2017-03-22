f=open('C:\Users\Krishna\Desktop\qfilter_output.txt','r').readlines()
w=open('D:\M.Tech work\qfilter_output matches.txt','w')
import re
evenline = False
l='adas'
for line in f:
	if evenline:
		h=re.findall(r"'(.*?)'", line)  # this is a regex i found at http://goo.gl/su58uY which finds all entries in your line which are within single quotes which is what 
# is what i want as the 'match' is within single quotes after Found. earlier i had split the line by spaces but it was wrong as it gave only one word matches
# when we know that many matches are multiple words. 		
		w.write(h[0]) # this gives me the match. h[-1] gives me the other entry within the line which was within single quotes (strange though, since it should have been h[1] )

		w.write('\n')
	evenline = not evenline    # i want to skip every alternate line as it contains the filename GSE... therefore line 2,4 and this one
w.close()
#	print line
#	print '\n'
	


