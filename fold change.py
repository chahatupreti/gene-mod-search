o = open('F:\M.Tech\znew_series\GSE20280.txt', 'r').readlines()
folch = 0
d = {}
flag=0
d1=1
n=0
for line in o:
    n=n+1
    line = line.rstrip()
    split_line = line.split("\t");
    if split_line[0] == "\"ID_REF\"":
        flag=1
    elif flag==1:
        for line in o[n:-1]:
            split_line = line.split("\t");
            if split_line[0] != '':
                try:
                    folch = float(split_line[3])/float(split_line[1]) # AA
                except:
                    None
             #       print split_line[3]+ 'dfgdf' + split_line[1]
        
                
            d1=d1+1
            d[split_line[0]] = folch
        break
from collections import OrderedDict
d_sorted_by_value = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
print d_sorted_by_value
o.close()
# problems with this code -
# multiple file reading
# in AA, i am arbitrarily dividing any two numbers. this division has to be between
# the 2 samples which are control and experimental
