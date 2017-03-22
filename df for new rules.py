# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:40:39 2016

@author: Krishna
"""
#import cProfile, pstats, StringIO
#pr = cProfile.Profile()
#pr.enable()

import os
import re
import time
from test_new_rules import cl, closedd
#from find_match import find_matches
start_time = time.time()
#a = open('/media/chahat/Krishna/F DRIVE/M.Tech/patterns for gmk_down.txt','r').readlines()
#a1 = open('/media/chahat/Krishna/F DRIVE/M.Tech/patterns for gmk_up.txt','r').readlines()
a = open('E:\F DRIVE\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('E:\F DRIVE\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1

#keyword1 = open('/media/chahat/Krishna/F DRIVE/M.Tech/mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
#keyword2 = open('/media/chahat/Krishna/F DRIVE/M.Tech/mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keyword1 = open('E:\F DRIVE\M.Tech\mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
keyword2 = open('E:\F DRIVE\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2
keystripped = [k.rstrip().lower() for k in keywords]
c=0

def find_matches(s, gmk, filee):
#    print gmk
#    print 34234234234234
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        l = list(filter(None, l))       # remove empty elements in the list
#        print 1212
        gs_list = [k for k in keystripped if k in s]        
        
#        for gss in keywords:
#                gss=gss.rstrip()
#                gss=gss.lower()
#                if gss in s:
#                    gs_list.append(gss) 
        
        for gs in gs_list: # gene symbols
#            print (3333)
             
#            print(gs_list)              
            if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches
                gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                gs1=list(filter(None, gs1))
                gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                gmk1=list(filter(None, gmk1))
                if any(l[i:i+len(gs1)]==gs1 for i in range(len(l)-len(gs1)+1)) and (any(l[i:i+len(gmk1)]==gmk1 for i in range(len(l)-len(gmk1)+1))): # this ensures that both gs and gmk are in l, as a unit(i.e. and in order) otherwise it was detecting things like 'beta c' from beta cells
                    #  UPTO THIS POINT WE HAVE ESTABLISHED THAT THE GMK AND GS ARE INDEED IN THE LINE                    
                    k1 = '_MKKEYWORD_1_'
                    k2 = '_SKEYWORD_2_'
#                    print 555555555555555
                    text = re.sub(re.escape(gmk), k1, s, flags=re.I) # because of this replacement, we dont have the problem of counting r from behind etc. Basically, i did this so becase when i have multiple word GS, each word will have a different index, but this allows me to assign a single index to every GS, thus making it simple to count differences. the point about counting r from back is that when your GS spans many indices then counting r is tricky because a gmk which is after this Gs would have a smaller r if i counted the differnce between it and the last word of my GS, and opposite rule if gmk is in front. but here the same rule can be used in all cases.
                                                # also, I cannot use the regex based replacement used below for gmk replacement because we do want 
                                                # cases where gmk's like -/- or + are just after or before a word, without the word boundary   
                    text = re.sub(r'(\b%s\b)' % (re.escape(gs)), k2, text, flags=re.I)
                 
                    lt = text.split()                    
                    #lt = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', text)
                    d_idx = {k1:[], k2:[]}
                    #print d_idx[k1]
                    for k,v in enumerate(lt): # k is the index, v is a word
                        if k1 in v:
                            d_idx[k1].append(k)  # find all indices of k1(gmk) and store
                        if k2 in v:
                            d_idx[k2].append(k) # find all indices of k2(gs) and store
                    distance = 8
                    data = []
                    for idx1 in d_idx[k1]:
                        for idx2 in d_idx[k2]:
                            d = abs(idx1 - idx2)
                            if d<=distance:
                                data.append((d,idx1,idx2)) # for all cases where a gs and gmk occur nearby, make pairs
                                
                    data.sort(key=lambda x: x[0])  # sort data on basis of how close they are
#                    for i in range (0, len(data)):     
#                        aq = data[i]  # in data, (2,8,6) means -> 2 = difference b/w gs and gmk, 8 = position of gs, 6 = position of gmk 
#                        print aq
#                        loq = min(aq[1], aq[2]) # find the lower position among gs and gmk
#                        hiq = max(aq[1], aq[2]) # find the higher position among gs and gmk
#                        print loq, hiq
#                        brrq = lt[max(0, loq-6):hiq+6] # generate the phrase around a closely occuring gs and gmk
#                        brq = " ".join(brrq)   
#                        print brq
                        
                    if data: 
#                        print (23)
                        cl(s, gmk, gs, gs_list, data, filee)
#                        if cll:    #those cases where there is no CL returned because of no rule match, are filtered here
#                            cll=float(cll)
#                            gs_cl.append((cll, gs))
                        #print gs_cl
                        #print 'cl for %s is %f' %(gs, cll) 
                    
                    

for path, dirs, files in os.walk(r'E:\F DRIVE\M.Tech\for assigning cl\mouse in series_ll'):                    
#for path, dirs, files in os.walk(r'/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/selected/random 500_l'):
    for file in files:
#        print 4545
        sentences = open(os.path.join(path,file),'r').readlines();
        c = c+1
        r=0
        gs_cl=[]
        print (c) # one value printed for each file
#        print file
        print("--- %s seconds ---" % (time.time() - start_time))
        k=0
        hg=0
#        for s in sentences:
#            if s.startswith('!Sample_organism_ch1\t"Mus musculus"'):
#                r=1
#        if r==1:
            #print file
        for s in sentences:
            #print 1
            s = s.rstrip()        
            if s.startswith('!Series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
                s = s.lower()
                #gs_list = [kk for kk in keystripped if kk in s]                    
                for gmk in a:
                    gmk = gmk.rstrip() #to remove the lagging \n in many GMKs
                    gmk = gmk.lower()
                    find_matches(s, gmk, file)
                     
#            gs_cl=sorted(gs_cl, key=lambda x: abs(x[0]), reverse=True) #sorted sorts them in ascending order, reverse makes it descending,
#            #key is the rule telling it to sort based on the first element of the tuples and in absolute manner
#            #print gs_cl
#            gc = [list(t) for t in gs_cl]
#            for k in xrange(len(gc)):
#                for i in range(k+1,len(gc)):
#                    if gc[k][1]==gc[i][1]:
#                        gc[k][0]=gc[k][0]+gc[i][0]
#                        gc[i][0]=0
#            if gc:
#            	
#                print (gc)
#                print (file)
#                print (the GS modified is \'%s\' with confidence %f' %(gc[0][1], gc[0][0]))
#            else:
#            	None
#                print file
#                print (match not found yet for these rules)
#        else:
#        	None
#            #print 'NOT MOUSE'
                     
closedd()
print("--- %s seconds ---" % (time.time() - start_time))

#pr.disable()
#s = StringIO.StringIO()
#sortby = 'cumulative'
#ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#ps.print_stats()
#print s.getvalue()
