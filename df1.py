# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 18:43:15 2016

@author: Krishna
"""

import os
import re
import time
start_time = time.time()
#q=open('C:\Users\Krishna\Desktop\up down analysis for orgs\checking rules.txt','w')
a = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1


rg7 = open(r'L:\My Online Documents\MTech\ruless occurence\gs start.txt', 'w')
rg8 = open(r'L:\My Online Documents\MTech\ruless occurence\function.txt', 'w')
rg9 = open(r'L:\My Online Documents\MTech\ruless occurence\summary first line.txt', 'w')
rg10 = open(r'L:\My Online Documents\MTech\ruless occurence\effect on.txt', 'w')
rg11 = open(r'L:\My Online Documents\MTech\ruless occurence\title in wildtype.txt', 'w')
rg12 = open(r'L:\My Online Documents\MTech\ruless occurence\other in wildtype.txt', 'w')
rg13 = open(r'L:\My Online Documents\MTech\ruless occurence\gs in here we.txt', 'w')
rg14 = open(r'L:\My Online Documents\MTech\ruless occurence\overall with without.txt', 'w')
ra5 = open(r'L:\My Online Documents\MTech\ruless occurence\activation five.txt', 'w')
ri5 = open(r'L:\My Online Documents\MTech\ruless occurence\induced five.txt', 'w')
ro1 = open(r'L:\My Online Documents\MTech\ruless occurence\overexpression one.txt', 'w')
rt3 = open(r'L:\My Online Documents\MTech\ruless occurence\treatment one.txt', 'w')


keyword1 = open('F:\M.Tech\mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
keyword2 = open('F:\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2
#keywords = ['gs', 'gss']
c=0

def find_matches(s, gmk):
    #print 's and gmk are'
    #print s,gmk
    #print("FINDMATCHES--- %s seconds ---" % (time.time() - start_time))
    
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        filter(None, l)       # remove empty elements in the list   
        gs_list=[] 
        for gss in keywords:
                gss=gss.rstrip()
                gss=gss.lower()
                if gss in s:
                    gs_list.append(gss)              
        for gs in gs_list: # gene symbols

            if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches
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
                        cl(s, gmk, gs, gs_list, data)
                        
def cl(s1, gmk1, gs1, gs_list1, data1): # output will be the confidence level    
    #print("CL--- %s seconds ---" % (time.time() - start_time))
    #print 'something'    
    #print  'gmk1 is %s' %gmk1
    #print  'gs1 is %s' %gs1    
    gs11=gs1 # saving the GS to display in the final file
    br0=''
    br3=''
    br=''
    gs_list1.remove(gs1) # AS WE WANT TO USE THIS LIST FOR GETTING THE GS'S THAT ARE APART FROM THE CURRENT GS        
    s1 = re.sub(r'(\b(%s)\b)' % (gs1), r'_8MILLION8_', s1, flags=re.I) # inserts the token wherever there is GS. The \b before & after ensures this doesnt happen in between words

    #s1=s1.replace(gs1, '_8MILLION8_')
    gs1='_8MILLION8_'
    #l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|"|\'|[()]|-', s)  KEEP THIS AS AN ARCHIVE
    l = s1.split()  # i switched from the complex split above to just space split to ensure that the splitters can be part of a rule
    
    beg_gmk = ['over-activation', 'overexpression', 'loss of', 'knockout', 'haplo-insuffiency', 'haploinsufficiency', 'inactivation', 'knock-out', 'deletion', 'inhibition', 'knockdown', 'silencing']
    beg_other = ['Global gene expression', 'Gene expression profiling', 'Expression data', 'Gene expression analysis']
    for i in range(0,len(beg_gmk)):
        if re.search(r'(^!Series_.*?\s"%s)' %beg_gmk[i], s1, re.I|re.S):   # this rule looks optimum
            rr1.write(file)
            rr1.write('\n')
            rr1.write(gs11)
            rr1.write('\n')
            rr1.write('Found %s in %s' % (gmk1,s1.strip()))
            rr1.write('\n')

    for i in range(0,len(beg_other)):
        if re.search(r'(^!Series_.*?\s"%s)' %beg_other[i], s1, re.I|re.S):  # this rule looks optimum 
            rg2.write(file)
            rg2.write('\n')
            rg2.write(gs11)
            rg2.write('\n')
            rg2.write('Found %s in %s' % (gmk1,s1.strip()))
            rg2.write('\n')

    if re.search(r'(^!Series_\w.*?\s"Keywords:)', s1):
        ll=s1.split(',')
        v=0
        for i in range(0,len(ll)):
	     
           if gmk1 and gs1 in ll[i]:
               
               v=4 
               rg1.write(file)
               rg1.write('\n')
               rg1.write(gs11)
               rg1.write('\n')
               rg1.write('Found %s in %s' % (gmk1,s1.strip()))
               rg1.write('\n')        
        if v!=4:
           
           rg1.write('COMMA SEPARATED')
           rg1.write('\n')
           rg1.write(file)
           rg1.write('\n')
           rg1.write(gs11)
           rg1.write('\n')
           rg1.write('Found %s in %s' % (gmk1,s1.strip()))
           rg1.write('\n')
			
	
    if re.search(r'(%s\(control\))' %gs1, s1, re.I|re.S): #gs1(control)
        rg4.write(file)
        rg4.write('\n')
        rg4.write(gs11)
        rg4.write('\n')
        rg4.write('Found %s in %s' % (gmk1,s1.strip()))
        rg4.write('\n')
    if re.search(r'(The object of this study was to identify genes transcriptionally upregulated.*?downregulated)', s1):
        rg5.write(file)
        rg5.write('\n')
        rg5.write(gs11)
        rg5.write('\n')
        rg5.write('Found %s in %s' % (gmk1,s1.strip()))
        rg5.write('\n')
 
    
    
    for ii in range(0,len(data1)):
        #print 'loop'
        a = data1[ii]
        lo = min(a[1], a[2])
        hi = max(a[1], a[2])
        brr = l[max(0, lo-6):hi+6]
        br= " ".join(brr) 
        br00 = l[max(0, lo):hi+1]  # we dont need the 8 words here and there as the fullstop is between gmk1 and gs1
        br0= ' '.join(br00)
        br33 = l[max(0, lo-3):hi+3] 
        br3= ' '.join(br33)

            
        if gmk1 == 'activation':
            if  re.search(r'(activation of %s)' %gs1, br0, re.I|re.S):
                ra5.write(file)
                ra5.write('\n')
                ra5.write(gs11)
                ra5.write('\n')
                ra5.write(br0)
                ra5.write('\n')
                ra5.write('Found %s in %s' % (gmk1,s1.strip()))
                ra5.write('\n')
           
      
        if gmk1 == 'induced':
            if  re.search(r'(induced in response to %s)' %gs1, br0, re.I):
                ri5.write(file)
                ri5.write('\n')
                ri5.write(gs11)
                ri5.write('\n')
                ri5.write(br0)
                ri5.write('\n')
                ri5.write('Found %s in %s' % (gmk1,s1.strip()))
                ri5.write('\n')
            
        
        if gmk1 == 'treatment':
            if  re.search(r'(treatment.*?with %s)' %gs1, br0, re.I):
                rt1.write(file)
                rt1.write('\n')
                rt1.write(gs11)
                rt1.write('\n')
                rt1.write(br0)
                rt1.write('\n')
                rt1.write('Found %s in %s' % (gmk1,s1.strip()))
                rt1.write('\n')
            if  re.search(r'(control or %s-treated)' %gs1, br3, re.I|re.S):
                rt2.write(file)
                rt2.write('\n')
                rt2.write(gs11)
                rt2.write('\n')
                rt2.write(br0)
                rt2.write('\n')
                rt2.write('Found %s in %s' % (gmk1,s1.strip()))
                rt2.write('\n')
 
    return 4        


def closef():
    rg1.close()
    rg2.close()
    rg3.close()
    rg4.close()
    rg5.close() 
    rg6.close() 
    rs1.close() 
    rs2.close() 
    rs3.close() 
    ra1.close()
    ra2.close() 
    ra3.close()
    ra4.close()
    rd1.close()
    rd2.close()
    rde1.close()
    ri1.close()
    ri2.close()
    ri3.close() 
    ri4.close()
    rin1.close()
    rk1.close()
    rk2.close() 
    rko1.close()
    rm1.close()
    rm2.close()
    rn1.close()
    rr1.close() 
    rst1.close()
    rst2.close()
    rt1.close()
    rt2.close() 
    rs4.close()
    rs5.close()
    rs6.close() 
    #rrr.close()
            

    
c=0
for path, dirs, files in os.walk(r'L:\My Online Documents\MTech\series_imp_info'):
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
            s = s.lower()
#            gs_list=[]
#            for gss in keywords:
#                gss=gss.rstrip()
#                if gss in s:
#                    gs_list.append(gss)
            #if s.startswith('!Series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
            if s.startswith('!series_title') or s.startswith('!series_summary') or s.startswith('!series_overall_design'):    
                for gmk in a:
                    gmk = gmk.rstrip() #to remove the lagging \n in many GMKs
                    gmk = gmk.lower()
                    find_matches(s, gmk)
closef()
print("--- %s seconds ---" % (time.time() - start_time))
      
          
    
