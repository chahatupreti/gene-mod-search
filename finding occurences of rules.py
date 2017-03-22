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


rg1 = open(r'I:\My Online Documents\MTech\rules occurence\keyword start.txt', 'w')
rg2 = open(r'I:\My Online Documents\MTech\rules occurence\line start.txt', 'w')
rg3 = open(r'I:\My Online Documents\MTech\rules occurence\fullstop.txt', 'w')
rg4 = open(r'I:\My Online Documents\MTech\rules occurence\gs control.txt', 'w')
rg5 = open(r'I:\My Online Documents\MTech\rules occurence\golden line.txt', 'w')
rg6 = open(r'I:\My Online Documents\MTech\rules occurence\r four.txt', 'w')
rs1 = open(r'I:\My Online Documents\MTech\rules occurence\minus one.txt', 'w')
rs2 = open(r'I:\My Online Documents\MTech\rules occurence\minus two.txt', 'w')
rs3 = open(r'I:\My Online Documents\MTech\rules occurence\plus one.txt', 'w')
ra1 = open(r'I:\My Online Documents\MTech\rules occurence\activation one.txt', 'w')
ra2 = open(r'I:\My Online Documents\MTech\rules occurence\activation two.txt', 'w')
ra3 = open(r'I:\My Online Documents\MTech\rules occurence\activation three.txt', 'w')
ra4 = open(r'I:\My Online Documents\MTech\rules occurence\activation four.txt', 'w')
rd1 = open(r'I:\My Online Documents\MTech\rules occurence\deficient one.txt', 'w')
rd2 = open(r'I:\My Online Documents\MTech\rules occurence\deficient two.txt', 'w')
rde1 = open(r'I:\My Online Documents\MTech\rules occurence\deletion one.txt', 'w')
ri1 = open(r'I:\My Online Documents\MTech\rules occurence\induced one.txt', 'w')
ri2 = open(r'I:\My Online Documents\MTech\rules occurence\induced two.txt', 'w')
ri3 = open(r'I:\My Online Documents\MTech\rules occurence\induced three.txt', 'w')
ri4 = open(r'I:\My Online Documents\MTech\rules occurence\induced four.txt', 'w')
rin1 = open(r'I:\My Online Documents\MTech\rules occurence\inhibition one.txt', 'w')
rk1 = open(r'I:\My Online Documents\MTech\rules occurence\knockout one.txt', 'w')
rk2 = open(r'I:\My Online Documents\MTech\rules occurence\knkockout two.txt', 'w')
rko1 = open(r'I:\My Online Documents\MTech\rules occurence\ko.txt', 'w')
rm1 = open(r'I:\My Online Documents\MTech\rules occurence\mutant one.txt', 'w')
rm2 = open(r'I:\My Online Documents\MTech\rules occurence\mutant two.txt', 'w')
rn1 = open(r'I:\My Online Documents\MTech\rules occurence\null.txt', 'w')
rr1 = open(r'I:\My Online Documents\MTech\rules occurence\gmks start.txt', 'w')
rst1 = open(r'I:\My Online Documents\MTech\rules occurence\stimulated one.txt', 'w')
rst2 = open(r'I:\My Online Documents\MTech\rules occurence\stimulated two.txt', 'w')
rt1 = open(r'I:\My Online Documents\MTech\rules occurence\\treated one.txt', 'w')
rt2 = open(r'I:\My Online Documents\MTech\rules occurence\treated two.txt', 'w')
rs4 = open(r'I:\My Online Documents\MTech\rules occurence\minus three.txt', 'w')
rs5 = open(r'I:\My Online Documents\MTech\rules occurence\plus two.txt', 'w')
rs6 = open(r'I:\My Online Documents\MTech\rules occurence\plus three.txt', 'w')






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
           
            gs = gs.rstrip()     #remove lagging whitespace characters                   

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
                        print "Least distance: ", data[0][0]
                        print file
                        print gs, gmk
                        print "Number of occurences: ", len(data)
                        if data[i][0]<4:  # if r less than 4
                            rg6.write(file)
                            rg6.write('\n')
                            rg6.write (' r is %d ' % data[i][0])
                            rg6.write('\n')
                            rg6.write(gs)
                            rg6.write('\n')
                            rg6.write('Found %s in %s' % (gmk,s.strip()))
                            rg6.write('\n')
                    r=cl(s, gmk, gs)
                    print r # tells how many times the rules function was called
                                





def cl(s, gmk, gs): # output will be the confidence level    
 
    beg_gmk = ['over-activation', 'overexpression', 'loss of', 'knockout', 'haplo-insuffiency', 'haploinsufficiency', 'inactivation', 'knock-out', 'deletion', 'inhibition', 'knockdown', 'silencing']
    beg_other = ['Global gene expression', 'Gene expression profiling', 'Expression data', 'Gene expression analysis']
    for i in range(0,len(beg_gmk)):
        if re.search(r'(^!Series_.*?\s"%s)' %beg_gmk[i], s, re.I|re.S):   # this rule looks optimum
            rr1.write(file)
            rr1.write('\n')
            rr1.write(gs)
            rr1.write('\n')
            rr1.write('Found %s in %s' % (gmk,s.strip()))
            rr1.write('\n')
    for i in range(0,len(beg_other)):
        if re.search(r'(^!Series_.*?\s"%s)' %beg_other[i], s, re.I|re.S):  # this rule looks optimum 
            rg2.write(file)
            rg2.write('\n')
            rg2.write(gs)
            rg2.write('\n')
            rg2.write('Found %s in %s' % (gmk,s.strip()))
            rg2.write('\n')
    if re.search(r'(^!Series_\w.*?\s"Keywords:)', s):
        if re.search(r'(%s.*?,.*?%s)' % (re.escape(gs), re.escape(gmk)), s, re.I|re.S) or (re.search(r'(%s.*?,.*?%s)' % (re.escape(gmk), re.escape(gs)), s, re.I|re.S)):
            rg1.write(file)
            rg1.write('\n')
            rg1.write(gs)
            rg1.write('\n')
            rg1.write('Found %s in %s' % (gmk,s.strip()))
            rg1.write('\n')
    if (re.search(r'(%s.*?\..*?%s)' % (re.escape(gs), re.escape(gmk)), s, re.I|re.S)) or (re.search(r'(%s.*?\..*?%s)' % (re.escape(gmk), re.escape(gs)), s, re.I|re.S)): #gs fullstop gmk and viceversa
        rg3.write(file)
        rg3.write('\n')
        rg3.write(gs)
        rg3.write('\n')
        rg3.write('Found %s in %s' % (gmk,s.strip()))
        rg3.write('\n')
    if re.search(r'(%s\(control\))' %gs, s, re.I|re.S): #gs(control)
        rg4.write(file)
        rg4.write('\n')
        rg4.write(gs)
        rg4.write('\n')
        rg4.write('Found %s in %s' % (gmk,s.strip()))
        rg4.write('\n')
    if re.search(r'(The object of this study was to identify genes transcriptionally upregulated.*?downregulated)', s):
        rg5.write(file)
        rg5.write('\n')
        rg5.write(gs)
        rg5.write('\n')
        rg5.write('Found %s in %s' % (gmk,s.strip()))
        rg5.write('\n')
        
    if gmk == 'activation':
        if  re.search(r'(activation by %s)' %gs, s, re.I|re.S):
            ra1.write(file)
            ra1.write('\n')
            ra1.write(gs)
            ra1.write('\n')
            ra1.write('Found %s in %s' % (gmk,s.strip()))
            ra1.write('\n')
        if  re.search(r'(probably\s.*?\s %s activation)' %gs, s, re.I|re.S):
            ra2.write(file)
            ra2.write('\n')
            ra2.write(gs)
            ra2.write('\n')
            ra2.write('Found %s in %s' % (gmk,s.strip()))
            ra2.write('\n')
        if  re.search(r'(critical for.*?%s activation)' %gs, s, re.I|re.S):
            ra3.write(file)
            ra3.write('\n')
            ra3.write(gs)
            ra3.write('\n')
            ra3.write('Found %s in %s' % (gmk,s.strip()))
            ra3.write('\n') 
        if  re.search(r'(%s.*?activation of)' %gs, s, re.I|re.S):
            ra4.write(file)
            ra4.write('\n')
            ra4.write(gs)
            ra4.write('\n')
            ra4.write('Found %s in %s' % (gmk,s.strip()))
            ra4.write('\n')
    if gmk == 'deficient':
        if  re.search(r'(%s deficient)' %gs, s, re.I|re.S):
            rd1.write(file)
            rd1.write('\n')
            rd1.write(gs)
            rd1.write('\n')
            rd1.write('Found %s in %s' % (gmk,s.strip()))
            rd1.write('\n')
        if  re.search(r'(deficient\s.*?\sexhibited\s.*?\s%s)' %gs, s, re.I|re.S):
            rd2.write(file)
            rd2.write('\n')
            rd2.write(gs)
            rd2.write('\n')
            rd2.write('Found %s in %s' % (gmk,s.strip()))
            rd2.write('\n')
#    if gmk == 'deletion':
#        for all_gs in keywords:
            #all_gs=all_gs.rstrip()
#            if re.search(r'(\s%s-deletion\s.*?\s%s)' % (re.escape(all_gs), re.escape(gs)), s, re.I|re.S):
#                rde1.write(file)
#                rde1.write('\n')
#                rde1.write(gs)
#                rde1.write('\n')
#                rde1.write('Found %s in %s' % (gmk,s.strip()))
#                rde1.write('\n')       
    if gmk == '-/-':
        if r<3:
            rs4.write(file)
            rs4.write('\n')
            rs4.write(gs)
            rs4.write('\n')
            rs4.write('Found %s in %s' % (gmk,s.strip()))
            rs4.write('\n')
        if  re.search(r'(-/-%s)' %gs, s, re.I|re.S):
            rs1.write(file)
            rs1.write('\n')
            rs1.write(gs)
            rs1.write('\n')
            rs1.write('Found %s in %s' % (gmk,s.strip()))
            rs1.write('\n')
        if  re.search(r'(%s-/-)' %gs, s, re.I|re.S):
            rs2.write(file)
            rs2.write('\n')
            rs2.write(gs)
            rs2.write('\n')
            rs2.write('Found %s in %s' % (gmk,s.strip()))
            rs2.write('\n')      
    if gmk == '+':
        if  re.search(r'(%s+)' %gs, s, re.I|re.S):
            rs3.write(file)
            rs3.write('\n')
            rs3.write(gs)
            rs3.write('\n')
            rs3.write('Found %s in %s' % (gmk,s.strip()))
            rs3.write('\n')
        elif  re.search(r'(%s\(\+\))' %gs, s, re.I|re.S):
            rs5.write(file)
            rs5.write('\n')
            rs5.write(gs)
            rs5.write('\n')
            rs5.write('Found %s in %s' % (gmk,s.strip()))
            rs5.write('\n')   
        else:
            rs6.write(file)
            rs6.write('\n')
            rs6.write(gs)
            rs6.write('\n')
            rs6.write('Found %s in %s' % (gmk,s.strip()))
            rs6.write('\n')
    if gmk == 'induced':
        if  re.search(r'(%s.*?was shown\s.*?\sinduced)' %gs, s, re.I|re.S):
            ri1.write(file)
            ri1.write('\n')
            ri1.write(gs)
            ri1.write('\n')
            ri1.write('Found %s in %s' % (gmk,s.strip()))
            ri1.write('\n')
        if  re.search(r'(%s.*?-induced)' %gs, s, re.I|re.S):
            ri2.write(file)
            ri2.write('\n')
            ri2.write(gs)
            ri2.write('\n')
            ri2.write('Found %s in %s' % (gmk,s.strip()))
            ri2.write('\n')
        if  re.search(r'(induced.*?to %s)' %gs, s, re.I|re.S):
            ri3.write(file)
            ri3.write('\n')
            ri3.write(gs)
            ri3.write('\n')
            ri3.write('Found %s in %s' % (gmk,s.strip()))
            ri3.write('\n') 
        if  re.search(r'(induced.*?while %s)' %gs, s, re.I|re.S):
            ri4.write(file)
            ri4.write('\n')
            ri4.write(gs)
            ri4.write('\n')
            ri4.write('Found %s in %s' % (gmk,s.strip()))
            ri4.write('\n')
    if gmk == 'inhibition':
        if  re.search(r'(hypothesized\s.*?\sinhibition\s.*?\s%s )' %gs, s, re.I|re.S):
            rin1.write(file)
            rin1.write('\n')
            rin1.write(gs)
            rin1.write('\n')
            rin1.write('Found %s in %s' % (gmk,s.strip()))
            rin1.write('\n')
    if gmk == 'knockout':
        if  re.search(r'(effect of %s knockout)' %gs, s, re.I|re.S):
            rk1.write(file)
            rk1.write('\n')
            rk1.write(gs)
            rk1.write('\n')
            rk1.write('Found %s in %s' % (gmk,s.strip()))
            rk1.write('\n')
        if  re.search(r'(double knockout)', s, re.I|re.S): # for the time being
            rk2.write(file)
            rk2.write('\n')
            rk2.write(gs)
            rk2.write('\n')
            rk2.write('Found %s in %s' % (gmk,s.strip()))
            rk2.write('\n')
    if gmk == 'KO':
        if  re.search(r'(double KO\W)', s, re.I|re.S): # for the time being
            rko1.write(file)
            rko1.write('\n')
            rko1.write(gs)
            rko1.write('\n')
            rko1.write('Found %s in %s' % (gmk,s.strip()))
            rko1.write('\n')
    if gmk == 'mutant':
        if  re.search(r'(harboring.*?%s mutant)' %gs, s, re.I|re.S):
            rm1.write(file)
            rm1.write('\n')
            rm1.write(gs)
            rm1.write('\n')
            rm1.write('Found %s in %s' % (gmk,s.strip()))
            rm1.write('\n')
        if  re.search(r'(mutant.*?causes.*?%s)' %gs, s, re.I|re.S):
            rm2.write(file)
            rm2.write('\n')
            rm2.write(gs)
            rm2.write('\n')
            rm2.write('Found %s in %s' % (gmk,s.strip()))
            rm2.write('\n')
#    if gmk == 'null':
#        for all_gs in keywords:
            #all_gs=all_gs.rstrip()
#            if re.search(r'(matched %s\s.*?\s%s.*?null)' % (re.escape(gs), re.escape(all_gs)), s, re.I|re.S): #doing %gs, %all_gs gave syntax error. THIS NEW WAY IS THE RIGHT WAY TO DO IT
#                rn1.write(file)
#                rn1.write('\n')
#                rn1.write(gs)
#                rn1.write('\n')
#                rn1.write('Found %s in %s' % (gmk,s.strip()))
#                rn1.write('\n')
    if gmk == 'stimulated':
        if  re.search(r'(.*?-stimulated.*?%s)' %gs, s, re.I|re.S):
            rst2.write(file)
            rst2.write('\n')
            rst2.write(gs)
            rst2.write('\n')
            rst2.write('Found %s in %s' % (gmk,s.strip()))
            rst2.write('\n')
        if  re.search(r'(%s-stimulated)' %gs, s, re.I|re.S):
            rst1.write(file)
            rst1.write('\n')
            rst1.write(gs)
            rst1.write('\n')
            rst1.write('Found %s in %s' % (gmk,s.strip()))
            rst1.write('\n')
    if gmk == 'treated':
        if  re.search(r'(treated.*?control.*?%s)' %gs, s, re.I|re.S):
            rt1.write(file)
            rt1.write('\n')
            rt1.write(gs)
            rt1.write('\n')
            rt1.write('Found %s in %s' % (gmk,s.strip()))
            rt1.write('\n')
        if  re.search(r'(control or %s-treated)' %gs, s, re.I|re.S):
            rt2.write(file)
            rt2.write('\n')
            rt2.write(gs)
            rt2.write('\n')
            rt2.write('Found %s in %s' % (gmk,s.strip()))
            rt2.write('\n')
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
      
          
    
