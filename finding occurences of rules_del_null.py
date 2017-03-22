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


# rg1 = open(
rde1 = open(r'I:\My Online Documents\MTech\rules occurence\deletion one.txt', 'w')
# ri1 = open(r'I:\
rn1 = open(r'I:\My Online Documents\MTech\rules occurence\null.txt', 'w')







keyword1 = open('F:\M.Tech\mouse_gs_small_simple.txt','r').readlines()  # this has the small GS
keyword2 = open('F:\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2
#keywords = ['Fos', 'K5']
#gmk = 'knockout'
c=0
def find_matches(s, gmk):
    gs_list=[]
    for gss in keywords:
        gss=gss.rstrip()
        if gss in s:
            gs_list.append(gss)
    r=0
    print gs_list
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        filter(None, l)       # remove empty elements in the list                  
        for gs in keywords: # gene symbols
           
            gs = gs.rstrip()     #remove lagging whitespace characters                   
            #print gs
            if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches
                gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                gs1=filter(None, gs1)
                gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                gmk1=filter(None, gmk1)
                if any(l[i:i+len(gs1)]==gs1 for i in xrange(len(l)-len(gs1)+1)) and (any(l[i:i+len(gmk1)]==gmk1 for i in xrange(len(l)-len(gmk1)+1))): # this ensures that both gs and gmk are in l, as a unit(i.e. and in order) otherwise it was detecting things like 'beta c' from beta cells
                    #print gs
                    

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
                        print "Least distance: ", data[0][0]
                        print file
                        print gs, gmk
                        print "Number of occurences: ", len(data)
                 
                    r=cl(s, gmk, gs, gs_list, data)
                    #print r # tells how many times the rules function was called
                            





def cl(s1, gmk1, gs1, gs_list1, data1): # output will be the confidence level  
    br0=''
    br3=''
    br=''
    s1=s1.replace(gs1, '_8MILLION8_')
    gs1='_8MILLION8_'
    #l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|"|\'|[()]|-', s)
    l = s1.split() 
    for ii in range(0,len(data1)):
        print 'loop'
        a = data1[ii]
        lo = min(a[1], a[2])
        hi = max(a[1], a[2])
        brr = l[max(0, lo-8):hi+8]
        br= " ".join(brr) 
        br00 = l[max(0, lo):hi]  # we dont need the 8 words here and there as the fullstop is between gmk1 and gs1
        br0= ' '.join(br00)
        br33 = l[max(0, lo-3):hi+3] 
        br3= ' '.join(br33)  
    if gmk1 == 'deletion':
        print 56
        print gs1
        for all_gs in gs_list1:

            if re.search(r'(\s%s-deletion\s.*?\s%s)' % (re.escape(all_gs), re.escape(gs1)), br0, re.I|re.S):
                print 57
                print all_gs
                rde1.write(file)
                rde1.write('\n')
                rde1.write(gs1)
                rde1.write('\n')
                rde1.write('Found %s in %s' % (gmk1,s1.strip()))
                rde1.write('\n')  
                print 61     
   
    if gmk1 == 'null':
        for all_gs in gs_list1:

            if re.search(r'(matched %s\s.*?\s%s.*?null)' % (re.escape(gs1), re.escape(all_gs)), br3, re.I|re.S): #doing %gs, %all_gs gave syntax error. THIS NEW WAY IS THE RIGHT WAY TO DO IT
                rn1.write(file)
                rn1.write('\n')
                rn1.write(gs1)
                rn1.write('\n')
                rn1.write('Found %s in %s' % (gmk1,s.strip()))
                rn1.write('\n')
 
    return 4        
            

    
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

print("--- %s seconds ---" % (time.time() - start_time))
      
          
    
