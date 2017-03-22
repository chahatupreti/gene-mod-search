import os
import shutil
count = 0
with open('mus musculus_gene_symbols.txt','r') as d:
     sites = set(l.strip() for l in d)
for path, dirs, files in os.walk('F:\M.Tech\org segregated\mus musculus'):
    for file in files:
        read_f = open(os.path.join(path,file),'r');
        for line in read_f:
            elements = line.split()
        if sites.intersection(elements):
           count += 1
           print count
           shutil.copy(file, "F:\M.Tech\filtered\mus musculus")
