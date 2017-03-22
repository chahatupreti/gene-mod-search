# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 17:45:02 2016

@author: Krishna
"""

# -*- coding: utf-8 -*-
import cProfile, pstats
from io import StringIO
pr = cProfile.Profile()
pr.enable()
import os
import re
import time
import io
from mtech_newer_rules import cl, closedd
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
                        brr0 = lt[max(0, loq):hiq]
                        br0 = " ".join(brr0)
                        
                    if data: 
                        cll=cl(s, gmk, gs, gs_list, data, file,gene_actual)



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

        print ('----%d-----'%c)
        print("--- %s seconds ---" % (time.time() - start_time)) 
        hg=''
        gene_actual=''        
        
        for i in range(len(verified[files1])): # create a variable 'gene_actual' for the actual gene name when the file picked up has been CREED verified
            if verified[files1][i]==filenum.lower():
                gene_actual=verified[genes1][i]
                rt=1
                cc=cc+1
                print (cc)
        
        
        #           FURTHER WORK IS ONLY DONE ON FILES WHICH HAVE BEEN CREEDS CURATED. DOING IT ON OTHERS MAKES NO SENSE 
        #           SINCE THEN WE CANT EVALUATE IF THE GS_FOUND IS CORRECT OR NOT, BECAUSE THERE IS NO GS_ACTUAL KNOWN
        
        if (rt==1):
            for s in sentences: 
                #print 1
                s = s.rstrip()                
                s = s.lower()                   
                for gmk in allgmk:
                    find_matches(s, gmk, file, gene_actual)
                     

closedd()
print("--- %s seconds ---" % (time.time() - start_time))   
   
pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print (s.getvalue())
