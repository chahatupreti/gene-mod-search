import os
iplat = open("F:\M.Tech\platform files\GPL10026_family.soft.txt",'r').readlines()
iseries = open('C:\Users\Krishna\Downloads\GSE20280_series_matrix.txt','r').readlines()
o=open('C:\Users\Krishna\Downloads\gs_list.txt','w')
#iseries = iter(series)
#iplat = iter(plat)
gs_list = []
d=1
m=0
flag=0
n=0
v='sdf'
for line in iseries:
    line = line.rstrip()
    split_line = line.split("\t");
    if split_line[0] == "!Series_geo_accession":
        v = split_line[1]
        print v
v=v[2:-1]
print type(v)
print v
v=str(v)
print v
p=open(os.path.join('F:\M.Tech\znew_series', v + '.txt'), 'w')    

for linep in iplat:
    m=m+1
    linep = linep.rstrip()
    split_linep = linep.split("\t");
    if split_linep[0] == "!platform_table_begin":
        for linep in iplat[m+1:-1]:
            split_linep = linep.split("\t");
       #     print linep
            if len(split_linep) > 8:
  #              print split_linep[9]
                gs_list.append(split_linep[9])
                #d=d+1
            
for item in gs_list:
    o.write("%s\n" % item)

for line in iseries:
    n=n+1
    line = line.rstrip()
    split_line = line.split("\t");
    if split_line[0] == "\"ID_REF\"":
        flag=1
        p.write(line)
        p.write('\n')
    elif flag==0:
        p.write(line)
        p.write('\n')
    elif flag==1:
        for line in iseries[n:-1]:
            split_line = line.split("\t");
            split_line[0] = gs_list[d]
            d=d+1
            line = '\t'.join(split_line)
            p.write(line)
        break






##
##output = open(os.path.join('F:\M.Tech', 'GPL10026.txt'),'w')
##with open(fname) as f:
##    next(f)    ## this helps us skip the first line which was like header, it said what was in the file
##    for line in f:
##        line = line.rstrip()
##        split_the_line = line.split("\t");
##      #  split_the_line = filter(None, split_the_line)
##      #  print split_the_line;
##        n = 0
##        print d
##        d = d+1
##        output.write(split_the_line[5]);
##        output.write('\n');
##       # print split_the_line[6]
##        if split_the_line[6]:
##            c = split_the_line[6].split(',');
##     #       print c[n]
##            while n< len(c):
##                output.write(c[n]);
##                output.write('\n');
##                n= n + 1;
##        if split_the_line[7] != None:
##            output.write(split_the_line[7]);
##            output.write('\n');
# CODE BELOW ADDS OTHER_DESCRIPTION
##        n = 0
##        if (len(split_the_line) > 8) and (split_the_line[8]):
##          #  output.write(split_the_line[8]);
##            other_desc_split = split_the_line[8].split('|');
##        #    print other_desc_split;
##            while n < len(other_desc_split):
##                output.write(other_desc_split[n]);
##               # print n,len(other_desc_split);
##                n = n + 1;
##                output.write('\n');
##        
#plat.close()
series.close()
o.close()
p.close()
