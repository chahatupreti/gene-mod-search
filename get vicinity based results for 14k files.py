# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 18:43:15 2016

@author: Krishna
"""

import os
import re
import time
start_time = time.time()
q=open(r'C:\Users\Krishna\Desktop\up down analysis for orgs\vicinity matches for 14k files.txt','w')
a = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1
#print a
keyword1 = open('F:\M.Tech\mouse_gs_small_simple.txt','r').readlines()  # this has the small GS
keyword2 = open('F:\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2
#gmk = 'knockout'
c=0
def find_matches(s, gmk):
    r=0
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        filter(None, l)       # remove empty elements in the list                  
        for gs in keywords: # gene symbols
            #q.write(gs)
            #q.write('\n')            
            gs = gs.rstrip()     #remove lagging whitespace characters                   
            #q.write(gs)            
            #print gs
            #re.compile(gs)
            #print hg=hg+1
            if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches
                gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                gs1=filter(None, gs1)
                gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                gmk1=filter(None, gmk1)
                if any(l[i:i+len(gs1)]==gs1 for i in xrange(len(l)-len(gs1)+1)) and (any(l[i:i+len(gmk1)]==gmk1 for i in xrange(len(l)-len(gmk1)+1))): # this ensures that both gs and gmk are in l, as a unit(i.e. and in order) otherwise it was detecting things like 'beta c' from beta cells
                    k1 = "_KEYWORD_1_"
                    k2 = "_KEYWORD_2_"
                    text = s.replace(gmk, k1)  # because of this replacement, we dont have the problem of counting r from behind etc.
                    text = text.replace(gs, k2)
                    lt = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', text)
                    d_idx = {k1:[], k2:[]}
                    #print d_idx[k1]
                    for k,v in enumerate(lt):
                        if v == k1:
                            d_idx[k1].append(k)
                        elif v == k2:
                            d_idx[k2].append(k)
                    distance = 8
                    data = []
                    for idx1 in d_idx[k1]:
                        for idx2 in d_idx[k2]:
                            d = abs(idx1 - idx2)
                            if d<=distance:
                                data.append((d,idx1,idx2))
                                
                    data.sort(key=lambda x: x[0])
                    for i in range (0, len(data)):                    
                        q.write(file)
                        q.write('\n')
                        q.write('Number of occurences: %d' % len(data))
                        q.write('\n')
                        q.write(gs)
                        q.write (' r is %d ' % data[i][0])
                        q.write('\n')
                        q.write('Found %s in %s' % (gmk,s.strip()))
                        q.write('\n')
#                    print "Least distance: ", data[0][0]
#                    print "Index of kw1 and kw2: ", data[0][1:]
#                    print "Number of occurences: ", len(data)                                    

    
c=0
for path, dirs, files in os.walk('I:\My Online Documents\MTech\series_imp_info'):
    for file in files:
        sentences = open(os.path.join(path,file),'r').readlines();
        c = c+1
        r=0
        print c # one value printed for each file
        #print file
        print("--- %s seconds ---" % (time.time() - start_time))
        k=0
        hg=0
        for s in sentences:
                s = s.rstrip()
                if s.startswith('!Series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
                    for gmk in a:
                        gmk = gmk.rstrip() #to remove the lagging \n in many GMKs
                        find_matches(s, gmk)
q.close()
print("--- %s seconds ---" % (time.time() - start_time))
      
          
    
