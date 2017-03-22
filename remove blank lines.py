import fileinput
for line in fileinput.FileInput("F:\M.Tech\gene_symbols.txt",inplace=1):
    if line.rstrip():
        print line
