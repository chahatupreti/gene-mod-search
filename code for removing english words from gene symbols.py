# THIS WILL BE ''THE'' CODE FOR REMOVAL OF 1000-ENGLISH-WORDS AND SCIENTIFIC-BUT-NON-GENE WORDS
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
output = open('mus musculus_gene_symbols.txt','w')
print '1'
while n < len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\C_elegans_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('C_elegans_gene_symbols.txt','w')
print '2'
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\danio_rerio_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('danio_rerio_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\Drosophila melanogaster_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('Drosophila melanogaster_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\Escherichia coli_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('Escherichia coli_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\Gallus gallus_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('Gallus gallus_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\homo sapiens_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('homo sapiens_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\human_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('human_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\M_arabidopsis_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('M_arabidopsis_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\M_rattus norvegicus_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('M_rattus norvegicus_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\Oryza sativa_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('Oryza sativa_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\saccharomyces_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('saccharomyces_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()

n=0
with open('C:\Users\Krishna\Desktop\gene symbols\Sus scrofa_gene_symbols.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if word not in rlist:
        klist.append(word)
output = open('Sus scrofa_gene_symbols.txt','w')
while n< len(klist):
    output.write(klist[n])
    n=n+1
output.close()
