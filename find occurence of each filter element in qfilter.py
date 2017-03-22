def count_string_occurrence(org):
    f = open('D:\M.Tech work\qfilter_output matches.txt','r')
    contents = f.readlines() # VERY IMP dont use f.read() - it gave wrong count for many words. always use readlines()
    f.close()
    #print  org,
    print contents.count(org)

read_f = open('D:\M.Tech work\unique filter matches from qfilter.txt','r')
for line in read_f:	
    count_string_occurrence(line)
    #print line
read_f.close()


