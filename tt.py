import os
n=0
# THIS CODE REMOVES COMMON ENGLISH WORDS FROM THE HUMAN GENE LIST	
with open(os.path.join('F:\M.Tech', 'top 1000 english common words.txt'),'r') as d:
     rlist = d.readlines()
with open('C:\Users\Krishna\Desktop\gene symbols\homo sapiens_gene_symbols1.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('homo sapiens_gene_symbols1.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()
