# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 18:22:43 2016

@author: Krishna
"""
import re
keyword1 = open('F:\M.Tech\mouse_gs_small_simple.txt','r').readlines()  # this has the small GS
keyword2 = open('F:\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2

def cl(s, gmk, gs,r): # output will be the confidence level    
    k1 = "_KEYWORD_1_"
    k2 = "_KEYWORD_2_"
    text = s.replace(gmk, k1)  # because of this replacement, we dont have the problem of counting r from behind etc.
    text = text.replace(gs, k2)
    lt = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', text)
    d_idx = {k1:[], k2:[]}
    print d_idx[k1]
    for k,v in enumerate(lt):
        if v == k1:
            d_idx[k1].append(k)
        elif v == k2:
            d_idx[k2].append(k)
    distance = 5
    data = []
    for idx1 in d_idx[k1]:
        for idx2 in d_idx[k2]:
            d = abs(idx1 - idx2)
            if d<=distance:
                data.append((d,idx1,idx2))
                
    data.sort(key=lambda x: x[0])
    #print data
    print "Least distance: ", data[0][0]
    print "Index of kw1 and kw2: ", data[0][1:]
    print "Number of occurences: ", len(data)
#    l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s)
    
    v=0
    cl=1.0
    beg_gmk = ['over-activation', 'overexpression', 'stimulation', 'loss of', 'knockout', 'haplo-insuffiency', 'haploinsufficiency', 'inactivation', 'knock-out', 'deletion', 'inhibition', 'knockdown', 'silencing']
    beg_other = ['Global gene expression', 'Gene expression profiling', 'Expression data', 'Gene expression analysis']
    for i in range(0,len(beg_gmk)):
        if re.search(r'(^%s)' %beg_gmk[i], s, re.I|re.S):
            cl=cl*4
            v=1
    for i in range(0,len(beg_other)):
        if re.search(r'(^%s)' %beg_other[i], s, re.I|re.S):
            cl=cl*7
            v=1
    if re.search(r'(^!Series_\w.*?\s"Keywords:)', s):
        if re.search(r'(%s.*?,.*?%s)' % (gs, gmk), s, re.I|re.S) or (re.search(r'(%s.*?,.*?%s)' % (gmk, gs), s, re.I|re.S)):
            cl=cl*0.5
            v=1
    if (re.search(r'(%s.*?\..*?%s)' % (gs, gmk), s, re.I|re.S)) or (re.search(r'(%s.*?\..*?%s)' % (gmk, gs), s, re.I|re.S)): #gs fullstop gmk and viceversa
        cl=cl*0.6
        v=1
    if re.search(r'(%s\(control\))' %gs, s, re.I|re.S): #gs(control)
        cl=cl*0.3
        v=1
    if re.search(r'(The object of this study was to identify genes transcriptionally upregulated.*?downregulated)', s):
        cl=cl*8
        v=1
        
    if gmk == 'activation':
        if  re.search(r'(activation by %s)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
        if  re.search(r'(probably\s.*?\s %s activation)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
        if  re.search(r'(critical for.*?%s activation)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1 
        if  re.search(r'(%s.*?activation of)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
    if gmk == 'deficient':
        if  re.search(r'(%s deficient)' %gs, s, re.I|re.S):
            cl=cl*8
            v=1
        if  re.search(r'(deficient\s.*?\sexhibited\s.*?\s%s)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
    if gmk == 'deletion':
        for all_gs in keywords:
            if re.search(r'(%s-deletion\s.*?\s%s)' % (all_gs, gs), s, re.I|re.S):
                cl=cl*0.1 # i will have to see if cl=0 is a good idea
                v=1       
    if gmk == '-/-':
        if r<3:  # i think this should be removed as the last rule takes care of it and i dont think there is a situation where 1<r<3 and its relevant
            cl=cl*8
            v=1
        if  re.search(r'(-/-%s)' %gs, s, re.I|re.S):
            cl=cl*0.1
            v=1
        if  re.search(r'(%s-/-)' %gs, s, re.I|re.S):
            cl=cl*9 # no need to multiply this with the first rule of -/- as it renders it redundant (r=1 >> r<3)
            v=1      
    if gmk == '+':
        if  re.search(r'(%s+)' %gs, s, re.I|re.S):
            cl=cl*7
            v=1
        elif  re.search(r'(%s\(\+\))' %gs, s, re.I|re.S):
            cl=cl*7
            v=1    
        else:
            cl=cl*0.1
            v=1
    if gmk == 'induced':
        if  re.search(r'(%s.*?was shown\s.*?\sinduced)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
        if  re.search(r'(%s.*?-induced)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
        if  re.search(r'(induced.*?to %s)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1 
        if  re.search(r'(induced.*?while %s)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
    if gmk == 'inhibition':
        if  re.search(r'(hypothesized\s.*?\sinhibition\s.*?\s%s )' %gs, s, re.I|re.S):
            cl=cl*0.5
            v=1
    if gmk == 'knockout':
        if  re.search(r'(effect of %s knockout)' %gs, s, re.I|re.S):
            cl=cl*8
            v=1
        if  re.search(r'(double knockout)' %gs, s, re.I|re.S): # for the time being
            cl=cl*0.3
            v=1
    if gmk == 'KO':
        if  re.search(r'(double KO)' %gs, s, re.I|re.S): # for the time being
            cl=cl*0.3
            v=1
    if gmk == 'mutant':
        if  re.search(r'(harboring.*?%s mutant)' %gs, s, re.I|re.S):
            cl=cl*6
            v=1
        if  re.search(r'(mutant.*?causes.*?GS)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
    if gmk == 'null':
        for all_gs in keywords:
            if re.search(r'(matched %s\s.*?\s%s.*?null)' % (gs, all_gs), s, re.I|re.S): #doing %gs, %all_gs gave syntax error. THIS NEW WAY IS THE RIGHT WAY TO DO IT
                cl=cl*0.3
                v=1
    if gmk == 'stimulated':
        if  re.search(r'(.*?-stimulated.*?%s)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
        if  re.search(r'(%s-stimulated)' %gs, s, re.I|re.S):
            cl=cl*6
            v=1
    if gmk == 'treated':
        if  re.search(r'(treated.*?control.*?%s)' %gs, s, re.I|re.S):
            cl=cl*0.3
            v=1
        if  re.search(r'(control or %s-treated)' %gs, s, re.I|re.S):
            cl=cl*8
            v=1
    return cl        
            
s = 'Found treated in !Series_overall_design	"Control or IL-22-treated mouse colon in triplicate."'
gmk = 'treated'
gs = 'IL-22'
r=4
print cl(s,gmk,gs,r)