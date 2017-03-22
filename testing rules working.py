# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 18:32:07 2017

@author: Krishna
"""
#import cProfile, pstats
#from io import StringIO
#pr = cProfile.Profile()
#pr.enable()
import os
import re
import time
import io
#from mtech_newer_rules_for_testing_purposes_only import cl, closedd
start_time = time.time()


#************THIS SECTION CREATES LIST FOR GMKs AND GSs
a = open('E:\F DRIVE\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('E:\F DRIVE\M.Tech\patterns for gmk_up.txt','r').readlines()
allgmk=a+a1
for i in range(len(allgmk)):
    allgmk[i] = allgmk[i].rstrip() #to remove the lagging \n in many GMKs
    allgmk[i] = allgmk[i].lower()
#allgmk=filter(None, allgmk) # PYTHON-2 VERSION
allgmk=list(filter(None, allgmk)) # PYTHON-3 VERSION
#print (allgmk)
keyword1 = open('E:\F DRIVE\M.Tech\mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
keyword2 = open('E:\F DRIVE\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
allgs = keyword1+keyword2
allgs_stripped = [k.rstrip().lower() for k in allgs]


#************THIS SECTION CREATES A DICTIONARY OF THE CORRECT FILE AND GENE_PERTURBED USING CREEDS DATA
files1212=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\testing creed data\filenames with mouse in first half.txt').readlines()
genes=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\testing creed data\modofied genes with mouse in first half.txt').readlines()
for i in range(len(files1212)):
    files1212[i] = files1212[i].rstrip() #to remove the lagging \n 
    files1212[i] = files1212[i].lower()    
    genes[i] = genes[i].rstrip()
    genes[i] = genes[i].lower()
files1='files12'
genes1='genes'
verified={files1:[], genes1:[]}
for f in files1212:
    verified[files1].append(f)
for g in genes: 
    verified[genes1].append(g)


#************THIS SECTION ENSURES GS-GMK PRESENCE AND PROXIMITY, THEN SENDS DATA TO RULES FILE
def find_matches(s, gmk, file,gene_actual):
    
    if gmk in s:  # checking if gmk is in the line
        if gmk == ('haploinsufficiency' or 'haploinsufficient'):
            print (file)
#            break
            gs_list = [k for k in allgs_stripped if k in s]
            l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT. Basically tokenizing the whole thing
            filter(None, l)       # remove empty elements in the list 
            for gs in gs_list: # gene symbols
                
                if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches <-----------------
                                        
                    gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                    gs1=list(filter(None, gs1))
                    gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                    gmk1=list(filter(None, gmk1))
                    if any(l[i:i+len(gs1)]==gs1 for i in range(len(l)-len(gs1)+1)) and (any(l[i:i+len(gmk1)]==gmk1 for i in range(len(l)-len(gmk1)+1))): # this ensures that both gs and gmk are in l, as a unit(i.e. and in order) otherwise it was detecting things like 'beta c' from beta cells
                        #  UPTO THIS POINT WE HAVE ESTABLISHED THAT THE GMK AND GS ARE INDEED IN THE LINE                    
#                        print (77777777)                        
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
    #                    for i in range (0, len(data)):  
    #                        aq = data[i]
    #                        loq = min(aq[1], aq[2])
    #                        hiq = max(aq[1], aq[2])
    #                        brrq = lt[max(0, loq-6):hiq+6]
    #                        brq = " ".join(brrq)
    #                        brr0 = lt[max(0, loq):hiq]
    #                        br0 = " ".join(brr0)
                        
                       # if gmk == 'agonist':   print (br0)
                        s1=s
                        gs1=gs
                        gs_list1=gs_list
                        if data:
    #                        print (999999)
                            gs11=gs1
                            br0=''
                            br3=''
                            br=''
                            gs_list1.remove(gs1) # AS WE WANT TO USE THIS LIST FOR GETTING THE GS'S THAT ARE APART FROM THE CURRENT GS        
                            s1 = re.sub(r'(\b(%s)\b)' % (gs1), r'_8MILLION8_', s1, flags=re.I) # inserts the token wherever there is GS. The \b before & after ensures this doesnt happen in between words
                            gs1='_8MILLION8_'
                            l = s1.split()
                            for ii in range(0,len(data)):
                                a = data[ii]
                                lo = min(a[1], a[2])
                                hi = max(a[1], a[2])
                                brr = l[max(0, lo-6):hi+6]
                                br6= " ".join(brr) 
                                br00 = l[max(0, lo):hi+1]  # we dont need the 8 words here and there as the fullstop is between gmk1 and gs1
                                br0= ' '.join(br00)
                                br33 = l[max(0, lo-3):hi+3] 
                                br3= ' '.join(br33)
                                if gmk == ('haploinsufficiency' or 'haploinsufficient'):#<--------
                                    print (121212)
                                    print (file)
                                    print (gs11)
                                    if re.search(r'(%s haploinsufficiency)' %gs1, br3, re.I|re.S): # why not working?
                                        print(br3)
#                                    if re.search(r'(agonist of %s)' %gs1, br3, re.I|re.S):
#                                        print(br3)
#                                    if re.search(r'(antagonist of %s)' %gs1, br3, re.I|re.S):
#                                        print(br3)
#                        cll=cl(s, gmk, gs, gs_list, data, file,gene_actual)
#                        if cll:    #those cases where there is no CL returned because of no rule match, are filtered here
#                            cll=float(cll)
#                            gs_cl.append((cll, gs))


#************THIS SECTION READS FILES, SELECTS RELEVANT ONES AND SENDS THE SENTENCES ALONG WITH ALL GMKs 
c=0
cc=0
for path, dirs, files in os.walk(r'E:\F DRIVE\M.Tech\for assigning cl\newest mouse files'):
    for file in files:
        sentences = io.open(os.path.join(path,file), encoding="utf8").readlines();
        c = c+1
        r=0
        rr=0
        rt=0
        gs_cl=[]
        #----------PROCESSING THE FILE NUMBER
        h=file.split('_')
        j=h[0]
        jj=j.split('-')
        filenum=jj[0]
        #---------        
#        print ('----%d-----'%c)
#        print (file)
#        print("--- %s seconds ---" % (time.time() - start_time)) 
        hg=''
        gene_actual=''        
        #-----------CHECKING IF THIS FILE HAS BEEN CURATED, IF YES THEN NOTE GENE_ACTUAL AND GO FORWARD
        for i in range(len(verified[files1])):
            if verified[files1][i]==filenum.lower():
                gene_actual=verified[genes1][i]
                rt=1
                cc=cc+1
#                print (cc)
        #------------
#        for s in sentences:
#            if s.startswith('!Sample_organism_ch1\t"Mus musculus"'):
#                r=1    
        if (rt==1):
            # if rt==1:
            #     print 'else type in mouse'
            # if rr==1:
            #     print 'good'
            for s in sentences: 
                #print 1
                s = s.rstrip()
                
                s = s.lower()  
                #gs_list = [kk for kk in keystripped if kk in s] 
#                    print(45)                   
                for gmk in allgmk:
                    find_matches(s, gmk, file, gene_actual)
                     
##            gs_cl=sorted(gs_cl, key=lambda x: abs(x[0]), reverse=True) #sorted sorts them in ascending order, reverse makes it descending,
##            #key is the rule telling it to sort based on the first element of the tuples and in absolute manner
##            #print gs_cl
##            gc = [list(t) for t in gs_cl]
##            for k in range(len(gc)):
##                for i in range(k+1,len(gc)):
##                    if gc[k][1]==gc[i][1]:
##                        gc[k][0]=gc[k][0]+gc[i][0]
##                        gc[i][0]=0
##                if gc:
##                    None
##                    # print (gc)
##                    # print (file)
###                     print ('File is %s, the GS modified is \'%s\' with confidence %f' %(file, gc[0][1], gc[0][0]))
##                    # print('\n')
##                else:
##                    # None
##                    print (file)
##                    print ('match not found yet for these rules')
##                    print('\n')
##
##            #else:
##                #print 'GENOME BINDING'
##                #print hg
##        else:
##            # None
##            print (file)
##            print ('NOT Microarray')
##            print('\n')
closedd()
print("--- %s seconds ---" % (time.time() - start_time))   
   
#pr.disable()
#s = StringIO.StringIO()
#sortby = 'cumulative'
#ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#ps.print_stats()
#print (s.getvalue())
