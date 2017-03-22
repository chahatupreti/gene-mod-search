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


rg1 = open(r'L:\My Online Documents\MTech\ruless occurence\keyword start7.txt', 'w')
rg2 = open(r'L:\My Online Documents\MTech\ruless occurence\line start7.txt', 'w')
rg3 = open(r'L:\My Online Documents\MTech\ruless occurence\fullstop.txt', 'w')
rg4 = open(r'L:\My Online Documents\MTech\ruless occurence\gs control.txt', 'w')
rg5 = open(r'L:\My Online Documents\MTech\ruless occurence\golden line7.txt', 'w')
rg6 = open(r'L:\My Online Documents\MTech\ruless occurence\r four.txt', 'w')
rs1 = open(r'L:\My Online Documents\MTech\ruless occurence\minus one.txt', 'w')
rs2 = open(r'L:\My Online Documents\MTech\ruless occurence\minus two.txt', 'w')
rs3 = open(r'L:\My Online Documents\MTech\ruless occurence\plus one.txt', 'w')
ra1 = open(r'L:\My Online Documents\MTech\ruless occurence\activation one.txt', 'w')
ra2 = open(r'L:\My Online Documents\MTech\ruless occurence\activation two.txt', 'w')
ra3 = open(r'L:\My Online Documents\MTech\ruless occurence\activation three.txt', 'w')
ra4 = open(r'L:\My Online Documents\MTech\ruless occurence\activation four.txt', 'w')
rd1 = open(r'L:\My Online Documents\MTech\ruless occurence\deficient one.txt', 'w')
rd2 = open(r'L:\My Online Documents\MTech\ruless occurence\deficient two.txt', 'w')
rde1 = open(r'L:\My Online Documents\MTech\ruless occurence\deletion one.txt', 'w')
ri1 = open(r'L:\My Online Documents\MTech\ruless occurence\induced one.txt', 'w')
ri2 = open(r'L:\My Online Documents\MTech\ruless occurence\induced two.txt', 'w')
ri3 = open(r'L:\My Online Documents\MTech\ruless occurence\induced three.txt', 'w')
ri4 = open(r'L:\My Online Documents\MTech\ruless occurence\induced four.txt', 'w')
rin1 = open(r'L:\My Online Documents\MTech\ruless occurence\inhibition one.txt', 'w')
rk1 = open(r'L:\My Online Documents\MTech\ruless occurence\knockout one.txt', 'w')
rk2 = open(r'L:\My Online Documents\MTech\ruless occurence\knkockout two7.txt', 'w')
rko1 = open(r'L:\My Online Documents\MTech\ruless occurence\ko7.txt', 'w')
rm1 = open(r'L:\My Online Documents\MTech\ruless occurence\mutant one.txt', 'w')
rm2 = open(r'L:\My Online Documents\MTech\ruless occurence\mutant two.txt', 'w')
rn1 = open(r'L:\My Online Documents\MTech\ruless occurence\null.txt', 'w')
rr1 = open(r'L:\My Online Documents\MTech\ruless occurence\gmks start7.txt', 'w')
rst1 = open(r'L:\My Online Documents\MTech\ruless occurence\stimulated one.txt', 'w')
rst2 = open(r'L:\My Online Documents\MTech\ruless occurence\stimulated two.txt', 'w')
rt1 = open(r'L:\My Online Documents\MTech\ruless occurence\\treated one.txt', 'w')
rt2 = open(r'L:\My Online Documents\MTech\ruless occurence\treated two.txt', 'w')
rs4 = open(r'L:\My Online Documents\MTech\ruless occurence\minus three7.txt', 'w')
rs5 = open(r'L:\My Online Documents\MTech\ruless occurence\plus two.txt', 'w')
rs6 = open(r'L:\My Online Documents\MTech\ruless occurence\plus three.txt', 'w')
ra5 = open(r'F:\M.Tech\for assigning cl\rules occurence\s\activation five.txt', 'w')
ri5 = open(r'F:\M.Tech\for assigning cl\rules occurence\s\induced five.txt', 'w')
ro1 = open(r'F:\M.Tech\for assigning cl\rules occurence\s\overexpression one.txt', 'w')
rt3 = open(r'F:\M.Tech\for assigning cl\rules occurence\s\treatment one.txt', 'w')
#rrr = open(r'L:\My Online Documents\MTech\goodthree.txt', 'w')





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
            #rrr.write('\n')            
            #rrr.write(gs)
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
                        aq = data[i] # in data, (2,8,6) means -> 2 = difference b/w gs and gmk, 8 = position of gs, 6 = position of gmk 
                        loq = min(aq[1], aq[2]) # find the lower position among gs and gmk
                        hiq = max(aq[1], aq[2]) # find the higher position among gs and gmk
                        brrq = lt[max(0, loq-6):hiq+6] # generate the phrase around a closely occuring gs and gmk
                        brq = " ".join(brrq) 
                        
                        if data[i][0]<4:  # if r less than 4
                            rg6.write(file)
                            rg6.write('\n')
                            rg6.write (' r is %d ' % data[i][0])
                            rg6.write('\n')
                            rg6.write(gs)
                            rg6.write('\n')
                            rg6.write(gmk)
                            rg6.write('\n')
                            rg6.write(brq)
                            rg6.write('\n')
                            rg6.write('Found %s in %s' % (gmk,s.strip()))
                            rg6.write('\n')
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
    
# ----------------- GENERAL RULES ---------------------------------------    
    
    beg_gmk = ['over-activation', 'overexpression', 'loss of', 'knockout', 'haplo-insuffiency', 'haploinsufficiency', 'inactivation', 'knock-out', 'deletion', 'inhibition', 'knockdown', 'silencing']
    beg_other = ['Global gene expression', 'Gene expression profiling', 'Expression data', 'Gene expression analysis']
    for i in range(0,len(beg_gmk)):
        if re.search(r'(^!Series_.*?\s"%s\s)' %beg_gmk[i], s1, re.I|re.S):   # this rule looks optimum
            rr1.write(file)
            rr1.write('\n')
            rr1.write(gs11)
            rr1.write('\n')
            rr1.write('Found %s in %s' % (beg_gmk[i],s1.strip()))
            rr1.write('\n')

    for i in range(0,len(beg_other)):
        if re.search(r'(^!Series_.*?\s"%s)' %beg_other[i], s1, re.I|re.S):  # this rule looks optimum 
            rg2.write(file)
            rg2.write('\n')
            rg2.write(gs11)
            rg2.write('\n')
            rg2.write('Found %s in %s' % (beg_other[i],s1.strip()))
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
 
# ------------------------- HIT(OR MATCH) SPECIFIC RULES --------------------------------------    
    
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

#        if gmk1 == 'deletion':
#   
#            for all_gs in gs_list1:
#             
#                if re.search(r'(%s-deletion.*?%s)' % (re.escape(all_gs), re.escape(gs1)), br3, re.I|re.S):
#                
#                    rde1.write(file)
#                    rde1.write('\n')
#                    rde1.write(gs11)
#                    rde1.write('\n')
#                    rde1.write('Found %s in: %s' % (gmk1,br)) #change to s1.strip() later
#                    rde1.write('\n')  
#                   
#       
#        if gmk1 == 'null':
#            for all_gs in gs_list1:
#           
#                if re.search(r'(%s.*?%s.*?null)' % (re.escape(gs1), re.escape(all_gs)), br3, re.I|re.S): #doing %gs, %all_gs gave syntax error. THIS NEW WAY IS THE RIGHT WAY TO DO IT
#                    
#                    rn1.write(file) 
#                    rn1.write('\n')
#                    rn1.write(gs11)
#                    rn1.write('\n')
#                    rn1.write('Found %s in: %s' % (gmk1,br3)) #change to s1.strip() later
#                    rn1.write('\n')
                    
        if (re.search(r'(%s.*?\..*?%s)' % (re.escape(gs1), re.escape(gmk1)), br0, re.I|re.S)) or (re.search(r'(%s.*?\..*?%s)' % (re.escape(gmk1), re.escape(gs1)), br0, re.I|re.S)): #gs1 fullstop gmk1 and viceversa
            rg3.write(file)
            rg3.write('\n')
            rg3.write(gs11)
            rg3.write('\n')
            rg3.write(br0)
            rg3.write('\n')
            rg3.write('Found %s in %s' % (gmk1, s1.strip())) # change to s1 
            rg3.write('\n')
    	
            
        if gmk1 == 'activation':
            if  re.search(r'(activation by %s)' %gs1, br0, re.I|re.S):
                ra1.write(file)
                ra1.write('\n')
                ra1.write(gs11)
                ra1.write('\n')
                ra1.write(br0)
                ra1.write('\n')
                ra1.write('Found %s in %s' % (gmk1,s1.strip()))
                ra1.write('\n')
            if  re.search(r'(probably.*?%s activation)' %gs1, br, re.I|re.S|re.DOTALL):

                ra2.write(file)
                ra2.write('\n')
                ra2.write(gs11)
                ra2.write('\n')
                ra2.write(br0)
                ra2.write('\n')
                ra2.write('Found %s in %s' % (gmk1,s1.strip()))
                ra2.write('\n')
            if  re.search(r'(critical for.*?%s activation)' %gs1, br, re.I|re.S):
                ra3.write(file)
                ra3.write('\n')
                ra3.write(gs11)
                ra3.write('\n')
                ra3.write(br0)
                ra3.write('\n')
                ra3.write('Found %s in %s' % (gmk1,s1.strip()))
                ra3.write('\n') 
            if  re.search(r'(%s.*?activation of)' %gs1, br3, re.I|re.S):
                ra4.write(file)
                ra4.write('\n')
                ra4.write(gs11)
                ra4.write('\n')
                ra4.write(br0)
                ra4.write('\n')
                ra4.write('Found %s in %s' % (gmk1,s1.strip()))
                ra4.write('\n')
        if gmk1 == 'deficient':

            if  re.search(r'(%s deficient)' %gs1, br0, re.I|re.S):

                rd1.write(file)
                rd1.write('\n')
                rd1.write(gs11)
                rd1.write('\n')
                rd1.write(br0)
                rd1.write('\n')
                rd1.write('Found %s in %s' % (gmk1, br))
                rd1.write('\n')
            if  re.search(r'(deficient.+?exhibited.+?%s)' %gs1, br0, re.I|re.S|re.DOTALL):

                rd2.write(file)
                rd2.write('\n')
                rd2.write(gs11)
                rd2.write('\n')
                rd2.write(br0)
                rd2.write('\n')
                rd2.write('Found %s in %s' % (gmk1,br))
                rd2.write('\n')
                
        if gmk1 == '-/-':
            #print br0
    #        if r<3:   # THIS RULE IS PROBABLY NOT NEEDED
    #            rs4.write(file)
    #            rs4.write('\n')
    #            rs4.write(gs11)
    #           rs4.write('\n')
    #            rs4.write('Found %s in %s' % (gmk1,s1.strip()))
    #            rs4.write('\n')
            if  re.search(r'(-/-%s)' %gs1, br0, re.I|re.S):
                rs1.write(file)
                rs1.write('\n')
                rs1.write(gs11)
                rs1.write('\n')
                rs1.write(br0)
                rs1.write('\n')
                rs1.write('Found %s in %s' % (gmk1,s1.strip()))
                rs1.write('\n')
            if  re.search(r'(%s-/-)' %gs1, br0, re.I|re.S):
                rs2.write(file)
                rs2.write('\n')
                rs2.write(gs11)
                rs2.write('\n')
                rs2.write(br0)
                rs2.write('\n')
                rs2.write('Found %s in %s' % (gmk1,s1.strip()))
                rs2.write('\n')      
        if gmk1 == '+':
            if  re.search(r'(%s+)' %gs1, br0, re.I|re.S):
                rs3.write(file)
                rs3.write('\n')
                rs3.write(gs11)
                rs3.write('\n')
                rs3.write(br0)
                rs3.write('\n')
                rs3.write('Found %s in %s' % (gmk1,s1.strip()))
                rs3.write('\n')
            if  re.search(r'(%s\(\+\))' %gs1, br3, re.I|re.S):
                rs5.write(file)
                rs5.write('\n')
                rs5.write(gs11)
                rs5.write('\n')
                rs5.write(br0)
                rs5.write('\n')
                rs5.write('Found %s in %s' % (gmk1,s1.strip()))
                rs5.write('\n')   
            else:
                rs6.write(file)
                rs6.write('\n')
                rs6.write(gs11)
                rs6.write('\n')
                rs6.write(br0)
                rs6.write('\n')
                rs6.write('Found %s in %s' % (gmk1,s1.strip()))
                rs6.write('\n')
        if gmk1 == 'induced':
            if  re.search(r'(%s.*?was shown.+?induced)' %gs1, br0, re.I|re.S|re.DOTALL):
                ri1.write(file)
                ri1.write('\n')
                ri1.write(gs11)
                ri1.write('\n')
                ri1.write(br0)
                ri1.write('\n')
                ri1.write('Found %s in %s' % (gmk1,s1.strip()))
                ri1.write('\n')
            if  re.search(r'(%s.*?-induced)' %gs1, br0, re.I|re.S):
                ri2.write(file)
                ri2.write('\n')
                ri2.write(gs11)
                ri2.write('\n')
                ri2.write(br0)
                ri2.write('\n')
                ri2.write('Found %s in %s' % (gmk1,s1.strip()))
                ri2.write('\n')
            if  re.search(r'(induced.*?to %s)' %gs1, br0, re.I|re.S):
                ri3.write(file)
                ri3.write('\n')
                ri3.write(gs11)
                ri3.write('\n')
                ri3.write(br0)
                ri3.write('\n')
                ri3.write('Found %s in %s' % (gmk1,s1.strip()))
                ri3.write('\n') 
            if  re.search(r'(induced.*?while %s)' %gs1, br0, re.I|re.S):
                ri4.write(file)
                ri4.write('\n')
                ri4.write(gs11)
                ri4.write('\n')
                ri4.write(br0)
                ri4.write('\n')
                ri4.write('Found %s in %s' % (gmk1,s1.strip()))
                ri4.write('\n')
        if gmk1 == 'inhibition':
            if  re.search(r'(hypothesized\s.*?\sinhibition\s.*?\s%s )' %gs1, br, re.I|re.S):
                rin1.write(file)
                rin1.write('\n')
                rin1.write(gs11)
                rin1.write('\n')
                rin1.write(br0)
                rin1.write('\n')
                rin1.write('Found %s in %s' % (gmk1,s1.strip()))
                rin1.write('\n')
        if gmk1 == 'knockout':
            if  re.search(r'(effect of %s knockout)' %gs1, br3, re.I|re.S):
                rk1.write(file)
                rk1.write('\n')
                rk1.write(gs11)
                rk1.write('\n')
                rk1.write(br0)
                rk1.write('\n')
                rk1.write('Found %s in %s' % (gmk1,s1.strip()))
                rk1.write('\n')
            if  re.search(r'(double knockout)', br3, re.I|re.S): # for the time being
                rk2.write(file)
                rk2.write('\n')
                rk2.write(gs11)
                rk2.write('\n')
                rk2.write(br0)
                rk2.write('\n')
                rk2.write('Found %s in %s' % (gmk1,s1.strip()))
                rk2.write('\n')
        if gmk1 == 'KO':
            if  re.search(r'(double KO\W)', br3, re.I|re.S): # for the time being
                rko1.write(file)
                rko1.write('\n')
                rko1.write(gs11)
                rko1.write('\n')
                rko1.write(br0)
                rko1.write('\n')
                rko1.write('Found %s in %s' % (gmk1,s1.strip()))
                rko1.write('\n')                
                
        if gmk1 == 'mutant':
            if  re.search(r'(harboring.*?%s mutant)' %gs1, br, re.I|re.S):
                rm1.write(file)
                rm1.write('\n')
                rm1.write(gs11)
                rm1.write('\n')
                rm1.write(br0)
                rm1.write('\n')
                rm1.write('Found %s in %s' % (gmk1,s1.strip()))
                rm1.write('\n')
            if  re.search(r'(mutant.*?causes.*?%s)' %gs1, br0, re.I|re.S):
                rm2.write(file)
                rm2.write('\n')
                rm2.write(gs11)
                rm2.write('\n')
                rm2.write(br0)
                rm2.write('\n')
                rm2.write('Found %s in %s' % (gmk1,s1.strip()))
                rm2.write('\n')
                
        if gmk1 == 'stimulated':
            if  re.search(r'(.*?-stimulated.*?%s)' %gs1, br, re.I|re.S):
                rst2.write(file)
                rst2.write('\n')
                rst2.write(gs11)
                rst2.write('\n')
                rst2.write(br0)
                rst2.write('\n')
                rst2.write('Found %s in %s' % (gmk1,s1.strip()))
                rst2.write('\n')
            if  re.search(r'(%s-stimulated)' %gs1, br0, re.I|re.S):
                rst1.write(file)
                rst1.write('\n')
                rst1.write(gs11)
                rst1.write('\n')
                rst1.write(br0)
                rst1.write('\n')
                rst1.write('Found %s in %s' % (gmk1,s1.strip()))
                rst1.write('\n')
        if gmk1 == 'treated':
            if  re.search(r'(treated.*?control.*?%s)' %gs1, br0, re.I|re.S):
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
                
        if gmk1 == 'activation':
            if  re.search(r'(activation of %s)' %gs1, br0, re.I):
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
        if gmk1 == 'overexpression':
            if  (re.search(r'(%s.*?overexpression)' %gs1, br0, re.I) or re.search(r'(%s.*?overexpression)' %gs1, br0, re.I)):
                ro1.write(file)
                ro1.write('\n')
                ro1.write(gs11)
                ro1.write('\n')
                ro1.write(br0)
                ro1.write('\n')
                ro1.write('Found %s in %s' % (gmk1,s1.strip()))
                ro1.write('\n')
        if gmk1 == 'treatment':
            if  re.search(r'(treatment.*?with %s)' %gs1, br0, re.I):
                rt3.write(file)
                rt3.write('\n')
                rt3.write(gs11)
                rt3.write('\n')
                rt3.write(br0)
                rt3.write('\n')
                rt3.write('Found %s in %s' % (gmk1,s1.strip()))
                rt3.write('\n')
 
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
    ra5.close()
    ri5.close()
    ro1.close()
    rt3.close()
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
    