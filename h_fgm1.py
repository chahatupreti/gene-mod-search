# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 02:57:00 2016

@author: Krishna
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 18:43:15 2016

@author: Krishna
"""

import cProfile, pstats, StringIO
pr = cProfile.Profile()
pr.enable()

import os
import re
import time
from rules1 import cl
start_time = time.time()
#q=open('C:\Users\Krishna\Desktop\up down analysis for orgs\checking rules.txt','w')
a = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1


rr1 = open(r'F:\M.Tech\for assigning cl\test\gmks start7.txt', 'w')
#ro11 = open(r'F:\M.Tech\for assigning cl\rules occurence\s\overexpression one1.txt', 'w')


keyword1 = open('F:\M.Tech\mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
keyword2 = open('F:\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2
keystripped = [k.rstrip().lower() for k in keywords]
#keywords = ['gs', 'gss']
c=0

def find_matches(s, gmk, gs_list):
    #print 's and gmk are'
     
    
    #print("FINDMATCHES--- %s seconds ---" % (time.time() - start_time))
    print 'list size is', len(gs_list)    
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        filter(None, l)       # remove empty elements in the list   
        #gs_list = [k for k in keystripped if k in s]
        #print 'list size is', len(gs_list)
        for gs in gs_list: # gene symbols
            #rrr.write('\n')            
            #rrr.write(gs)
            if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches <-----------------
                gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                gs1=filter(None, gs1)
                gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                gmk1=filter(None, gmk1)
                if any(l[i:i+len(gs1)]==gs1 for i in xrange(len(l)-len(gs1)+1)) and (any(l[i:i+len(gmk1)]==gmk1 for i in xrange(len(l)-len(gmk1)+1))): # this ensures that both gs and gmk are in l, as a unit(i.e. and in order) otherwise it was detecting things like 'beta c' from beta cells
                    #  UPTO THIS POINT WE HAVE ESTABLISHED THAT THE GMK AND GS ARE INDEED IN THE LINE                    
                    k1 = '_MKKEYWORD_1_'
                    k2 = '_SKEYWORD_2_'
                    #print gmk
                    text = re.sub(re.escape(gmk), k1, s, flags=re.I) # because of this replacement, we dont have the problem of counting r from behind etc.
                                                # also, I cannot use the regex based replacement used below for gmk replacement because we do want 
                                                # cases where gmk's like -/- or + are just after or before a word, without the word boundary   
                    text = re.sub(r'(\b%s\b)' % (re.escape(gs)), k2, text, flags=re.I)
                    #text = s.replace(gmk, k1)
                    #text = text.replace(gs, k2)
                    #print text
                    lt = text.split()                    
                    #lt = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', text)
                    d_idx = {k1:[], k2:[]}
                    #print d_idx[k1]
                    for k,v in enumerate(lt):
                        if k1 in v:
                            d_idx[k1].append(k)
                        if k2 in v:
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
                        #print "Least distance: ", data[0][0]
                        #print file
                        #print gs, gmk
                        #print "Number of occurences: ", len(data)
                        aq = data[i]
                        loq = min(aq[1], aq[2])
                        hiq = max(aq[1], aq[2])
                        brrq = lt[max(0, loq-6):hiq+6]
                        brq = " ".join(brrq) 
                        
                        
                    if data: 
                        cll=cl(s, gmk, gs, gs_list, data)
                        if cll:    #those cases where there is no CL returned because of no rule match, are filtered here
                            cll=float(cll)
                            gs_cl.append((cll, gs))

    
c=0

for path, dirs, files in os.walk(r'F:\M.Tech\for assigning cl\test\tt1'):
    for file in files:
        sentences = open(os.path.join(path,file),'r').readlines();
        c = c+1
        r=0
        gs_cl=[]
        print c # one value printed for each file
        #print file
        #print("--- %s seconds ---" % (time.time() - start_time))
#        k=0
        hg=0
        for s in sentences:
            if s.startswith('!Sample_organism_ch1\t"Mus musculus"'):
                r=1
        if r==1:
            #print file
            for s in sentences:
                #print 1
                s = s.rstrip()
                s = s.lower()
                if s.startswith('!series_title') or s.startswith('!series_summary') or s.startswith('!series_overall_design'):    
                    gs_list = [kk for kk in keystripped if kk in s]                    
                    for gmk in a:
                        gmk = gmk.rstrip() #to remove the lagging \n in many GMKs
                        gmk = gmk.lower()
                        find_matches(s, gmk, gs_list)
                     
            gs_cl=sorted(gs_cl, key=lambda x: abs(x[0]), reverse=True) #sorted sorts them in ascending order, reverse makes it descending,
            #key is the rule telling it to sort based on the first element of the tuples and in absolute manner
            #print gs_cl
            gc = [list(t) for t in gs_cl]
            for k in xrange(len(gc)):
                for i in range(k+1,len(gc)):
                    if gc[k][1]==gc[i][1]:
                        gc[k][0]=gc[k][0]+gc[i][0]
                        gc[i][0]=0
            if gc:
                
                #print gc
                print file
                print 'the GS modified is \'%s\' with confidence %f' %(gc[0][1], gc[0][0])
            else:
                None
                #print file
                #print 'match not found yet for these rules'
        else:
            None
            #print 'NOT MOUSE'
        
print("--- %s seconds ---" % (time.time() - start_time))   
   
pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()
