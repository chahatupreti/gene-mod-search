import itertools
a=open(r'C:\Users\Krishna\Desktop\up down analysis for orgs\vicinity matches_14k files_lowercase.txt','r').readlines()
b=open(r'gs matches for 14k files with occurence.txt','w')
c=[]
d=[]
i=0
ii=0
gsline = itertools.islice(a,2,None,4)
for g in gsline:
    h=g.split()
    j=h[0]
    c.append(j)
    

def unique(source):
    sofar = {}
    for val in source:
      if not sofar.get(val):
        yield val.strip()
        sofar[val] = 1
  
for lyne in unique(c):
    d.append(lyne)
    ii=ii+1
    
def count_string_occurrence(org):
    contents = c
    b.write(org)
    b.write('\t')
    b.write(str(contents.count(org)))
    b.write('\n')

for line in d:
    count_string_occurrence(line)



      

    

