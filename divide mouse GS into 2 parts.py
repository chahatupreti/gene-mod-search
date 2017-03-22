# -*- coding: utf-8 -*-
"""
Created on Tue Dec 08 11:28:59 2015

@author: Krishna
"""
import re
import time
start_time = time.time()
q=open('F:\M.Tech\mouse_gs_small_simple.txt','w')
q1=open('F:\M.Tech\mouse_gs_number_large.txt','w')
p = open('F:\M.Tech\org segregated\mus musculus\zaq\mouse_keywords123_3.txt','r').readlines()
#p = open('F:\M.Tech\znew_series\ga1.txt','r').readlines()
for p1 in p:
    if len(re.split(',|-| ',p1)) == 1:
        if any(i.isdigit() for i in p1) == False:
            q.write(p1)
        else:
            q1.write(p1)
         #   q.write('\n')
    else:
        q1.write(p1)
        #q1.write('\n')
        
q.close()
q1.close()
print("--- %s seconds ---" % (time.time() - start_time))                
        
        