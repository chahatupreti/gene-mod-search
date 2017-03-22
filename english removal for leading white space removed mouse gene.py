# import os
# n=0
# with open(os.path.join('F:\M.Tech', 'top 1000 english common words.txt'),'r') as d:
#      rlist = d.readlines()
# with open(os.path.join('F:\M.Tech', 'scientific but non gene words.txt'),'r') as p:
#      plist = p.readlines()     
# #with open(os.path.join('D:\M.Tech work', 'more non gene words.txt'),'r') as h:
# #     hlist = h.readlines()
# with open('F:\M.Tech\org segregated\mus musculus\zaq\mouse_keywords123_2.txt','r') as m:
#      slist = m.readlines()
# klist = []
# for word in slist:
#     if (word not in rlist) and (word not in plist):
#         klist.append(word)
# #output = open(os.path.join('C:\Users\Krishna\Desktop\new gene symbols', 'mus musculus_gene_symbols.txt'),'w')
# #output = open('C:\Users\Krishna\Desktop\new gene symbols\mus musculus_gene_symbols.txt','w')
# output = open('F:\M.Tech\org segregated\mus musculus\zaq\mouse_keywords123_3.txt','w')
# print '1'
# while n < len(klist):
#     output.write(klist[n])
#     n=n+1
# output.close()


import os
n=0
with open(os.path.join('F:\M.Tech', 'top 1000 english common words.txt'),'r') as d:
     rlist = d.readlines()
with open(os.path.join('F:\M.Tech', 'scientific but non gene words.txt'),'r') as p:
     plist = p.readlines()     
#with open(os.path.join('D:\M.Tech work', 'more non gene words.txt'),'r') as h:
#     hlist = h.readlines()
with open('F:\M.Tech\mus musculus_other_designation_only1.txt','r') as m:
     slist = m.readlines()
klist = []
for word in slist:
    if (word not in rlist) and (word not in plist):
        klist.append(word)
#output = open(os.path.join('C:\Users\Krishna\Desktop\new gene symbols', 'mus musculus_gene_symbols.txt'),'w')
#output = open('C:\Users\Krishna\Desktop\new gene symbols\mus musculus_gene_symbols.txt','w')
output = open('F:\M.Tech\mus musculus_other_designation_only.txt','w')
print '1'
while n < len(klist):
    output.write(klist[n])
    n=n+1
output.close()
