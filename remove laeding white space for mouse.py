g=open('F:\M.Tech\mus musculus_other_designation_only.txt','r').readlines()
r = open('F:\M.Tech\mus musculus_other_designation_only1.txt','w')
for f in g:
    #print f
    f = f.lstrip().rstrip()
    r.write(f)
    r.write('\n')
    #print f
r.close()
