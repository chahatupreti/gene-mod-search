import os
n=0
with open(os.path.join('F:\M.Tech', 'top 1000 english common words.txt'),'r') as d:
     rlist = d.readlines()
with open('C:\Users\Krishna\Desktop\gene symbols\mus musculus_gene_symbols1.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
#output = open(os.path.join('C:\Users\Krishna\Desktop\new gene symbols', 'mus musculus_gene_symbols.txt'),'w')
#output = open('C:\Users\Krishna\Desktop\new gene symbols\mus musculus_gene_symbols.txt','w')
output = open('mus musculus_gene_symbols1.txt','w')
print '1'
while n < len(klist):
    output.write(klist[n])
    n=n+1
output.close()
