# -*- coding: utf-8 -*-
# import cProfile, pstats, StringIO
# pr = cProfile.Profile()
# pr.enable()
import os
import re
import time
from newer_rules import cl, closedd
start_time = time.time()

a = open('E:\F DRIVE\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('E:\F DRIVE\M.Tech\patterns for gmk_up.txt','r').readlines()
allgmk=a+a1
for i in range(len(allgmk)):
    allgmk[i] = allgmk[i].rstrip() #to remove the lagging \n in many GMKs
    allgmk[i] = allgmk[i].lower()
allgmk=filter(None, allgmk)
print (allgmk)
keyword1 = open('E:\F DRIVE\M.Tech\mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
keyword2 = open('E:\F DRIVE\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2
keystripped = [k.rstrip().lower() for k in keywords]

c=0
def find_matches(s, gmk, file):
   
    if gmk in s:  # checking if gmk is in the line
        gs_list = [k for k in keystripped if k in s]
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        filter(None, l)       # remove empty elements in the list   
        for gs in gs_list: # gene symbols

            if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches <-----------------
                gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                gs1=list(filter(None, gs1))
                gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                gmk1=list(filter(None, gmk1))
                if any(l[i:i+len(gs1)]==gs1 for i in range(len(l)-len(gs1)+1)) and (any(l[i:i+len(gmk1)]==gmk1 for i in range(len(l)-len(gmk1)+1))): # this ensures that both gs and gmk are in l, as a unit(i.e. and in order) otherwise it was detecting things like 'beta c' from beta cells
                    #  UPTO THIS POINT WE HAVE ESTABLISHED THAT THE GMK AND GS ARE INDEED IN THE LINE                    
                    k1 = '_MKKEYWORD_1_'
                    k2 = '_SKEYWORD_2_'
                    #print gmk
                    text = re.sub(re.escape(gmk), k1, s, flags=re.I) # because of this replacement, we dont have the problem of counting r from behind etc.
                                                # also, I cannot use the regex based replacement used below for gmk replacement because we do want 
                                                # cases where gmk's like -/- or + are just after or before a word, without the word boundary   
                    text = re.sub(r'(\b%s\b)' % (re.escape(gs)), k2, text, flags=re.I)

                    lt = text.split()                    
                    d_idx = {k1:[], k2:[]}
                    for k,v in enumerate(lt): # store all instances of both gs and gmk separately
                        if k1 in v:
                            d_idx[k1].append(k)
                        if k2 in v:
                            d_idx[k2].append(k)
                    distance = 8
                    data = []
                    
                    for idx1 in d_idx[k1]:
                        for idx2 in d_idx[k2]:
                            d = abs(idx1 - idx2) # find distance between gs and gmk

                            if d<=distance:
                                data.append((d,idx1,idx2))

                                
                    data.sort(key=lambda x: x[0])
                    for i in range (0, len(data)):  
                        aq = data[i]
                        loq = min(aq[1], aq[2])
                        hiq = max(aq[1], aq[2])
                        brrq = lt[max(0, loq-6):hiq+6]
                        brq = " ".join(brrq) 
                        
                        
                    if data: 
                        cll=cl(s, gmk, gs, gs_list, data, file)
#                        if cll:    #those cases where there is no CL returned because of no rule match, are filtered here
#                            cll=float(cll)
#                            gs_cl.append((cll, gs))


c=0
for path, dirs, files in os.walk(r'E:\F DRIVE\M.Tech\for assigning cl\selected\mouse in random 500_l'):
    for file in files:
        sentences = open(os.path.join(path,file)).readlines();
        c = c+1
        r=0
        rr=0
        rt=0
        gs_cl=[]

        hg=''
        for s in sentences:
            if s.startswith('!Sample_organism_ch1\t"Mus musculus"'):
                r=1
            if s.startswith('!Series_type'):
                if s.startswith('!Series_type\t"Expression profiling by array"'):
#                     print 'OUR TYPE'
#                     print s, file
                     rr=1
            #         hg=s
            #     else:
            #         print 'OTHER TYPES'
            #         print s
            #         rt=1

            
        if (rr==1):
            # if rt==1:
            #     print 'else type in mouse'
            # if rr==1:
            #     print 'good'
            for s in sentences:
                #print 1
                s = s.rstrip()
                
                if s.startswith('!Series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
                    s = s.lower()  
                    #gs_list = [kk for kk in keystripped if kk in s] 
#                    print(45)                   
                    for gmk in allgmk:
                        find_matches(s, gmk, file)
                     
#            gs_cl=sorted(gs_cl, key=lambda x: abs(x[0]), reverse=True) #sorted sorts them in ascending order, reverse makes it descending,
#            #key is the rule telling it to sort based on the first element of the tuples and in absolute manner
#            #print gs_cl
#            gc = [list(t) for t in gs_cl]
#            for k in range(len(gc)):
#                for i in range(k+1,len(gc)):
#                    if gc[k][1]==gc[i][1]:
#                        gc[k][0]=gc[k][0]+gc[i][0]
#                        gc[i][0]=0
#                if gc:
#                    None
#                    # print (gc)
#                    # print (file)
##                     print ('File is %s, the GS modified is \'%s\' with confidence %f' %(file, gc[0][1], gc[0][0]))
#                    # print('\n')
#                else:
#                    # None
#                    print (file)
#                    print ('match not found yet for these rules')
#                    print('\n')
#
#            #else:
#                #print 'GENOME BINDING'
#                #print hg
#        else:
#            # None
#            print (file)
#            print ('NOT Microarray')
#            print('\n')
closedd()
print("--- %s seconds ---" % (time.time() - start_time))   
   
#pr.disable()
#s = StringIO.StringIO()
#sortby = 'cumulative'
#ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#ps.print_stats()
#print s.getvalue()
