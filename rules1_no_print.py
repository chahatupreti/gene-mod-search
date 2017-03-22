# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:42:45 2016
@author: Krishna
"""
import re
def cl(s1, gmk1, gs1, gs_list1, data1): # output will be the confidence level
#    print (data1)
    gs11=gs1
    br0=''
    br3=''
    br=''
    gs_list1.remove(gs1) # AS WE WANT TO USE THIS LIST FOR GETTING THE GS'S THAT ARE APART FROM THE CURRENT GS        
    s1 = re.sub(r'(\b(%s)\b)' % (gs1), r'_8MILLION8_', s1, flags=re.I) # inserts the token wherever there is GS. The \b before & after ensures this doesnt happen in between words
    k=1
    d=0
    vv=0    
    gs1='_8MILLION8_'
    #l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|"|\'|[()]|-', s)  KEEP THIS AS AN ARCHIVE
    l = s1.split()  # i switched from the complex split above to just space split to ensure that the splitters can be part of a rule 
    beg_gmk_up = ['over-activation', 'overexpression']
    beg_gmk_down = ['loss of', 'knockout', 'haplo-insuffiency', 'haploinsufficiency', 'inactivation', 'knock-out', 'deletion', 'inhibition', 'knockdown', 'silencing']    
    beg_other = ['Global gene expression', 'Gene expression profiling', 'Expression data', 'Gene expression analysis']
    for i in range(0,len(beg_gmk_up)):
        if re.search(r'(^!Series_.*?\s"%s\s)' %beg_gmk_up[i], s1, re.I|re.S):   # manipulation - UP
            k=k*0.63
            vv=1
            d= 1
#            print ('gmks start7')
    for i in range(0,len(beg_gmk_down)):
        if re.search(r'(^!Series_.*?\s"%s\s)' %beg_gmk_down[i], s1, re.I|re.S):   # manipulation - DOWN
            k=k*1.99
            vv=1
            d= -1
#            print ('gmks start7')
    for i in range(0,len(beg_other)):
        if re.search(r'(^!Series_.*?\s"%s\s)' %beg_other[i], s1, re.I|re.S):  # line starts with a golden PHRASE - no manipulation info
            k=k*3.71
            vv=1
#            print ('line start7')
    if re.search(r'(^!Series_\w.*?\s"Keywords:)', s1, re.I):  # line starts with KEYWORDS - manipulation dependent on the gmk linked
        ll=s1.split(',')
        v=0
        for i in range(0,len(ll)):	     
           if gmk1 and gs1 in ll[i]:               
               v=4 
               k=k*4.43
               vv=1
               if gmk1 in ['loss of', 'deficient', 'knockout', 'haploinsufficiency', 'haploin-sufficiency', 'inactivation', 'knock-out', 'deletion', 'inhibition', 'silencing', '-/-', 'null', 'KO', 'knockdown', 'ko', 'lacking', 'mutant']:
                   d=-1
               if gmk1 in ['treated', 'exposure', 'activation', 'induced', 'expressing', 'overexpression', 'overexpressing', 'stimulated', 'stimulation', 'over-activation', '+', 'treatment']:
                   d=1
#               print ('keyword start7')
        if v!=4:        # THINK OF REMOVING THIS RULE
           k=k*1.83
           vv=1
    
#           print ('opposite of keyword start7')
    if re.search(r'(%s\(control\))' %gs1, s1, re.I|re.S): #gs1(control) - no manipulation info
        #print 'control rule'        ###############################
        None
    if re.search(r'(The object of this study was to identify genes transcriptionally upregulated.*?downregulated)', s1):
        None
        #print 'golden line rule'
    if re.search(r'(The object of this study was to identify genes transcriptionally upregulated)', s1):
        #print 'golden line rule'
        d=1
    if re.search(r'(The object of this study was to identify genes transcriptionally downregulated)', s1): 
        #print 'golden line rule'
        d=-1        
    for ii in range(0,len(data1)):
        a = data1[ii]
        lo = min(a[1], a[2])
        hi = max(a[1], a[2])
        brr = l[max(0, lo-6):hi+6] # this takes 6 words before and 6 after the gs and gmk
        br= " ".join(brr) 
        br00 = l[max(0, lo):hi+1]  # we dont need the 8 words here and there as the fullstop is between gmk1 and gs1
        br0= ' '.join(br00) # this is the smallest
        br33 = l[max(0, lo-3):hi+3]  # this takes 3 words before and 3 after the gs and gmk
        br3= ' '.join(br33)
#        print(br3)                    
        if (re.search(r'(%s.*?\..*?%s)' % (re.escape(gs1), re.escape(gmk1)), br0, re.I|re.S)) or (re.search(r'(%s.*?\..*?%s)' % (re.escape(gmk1), re.escape(gs1)), br0, re.I|re.S)): #gs1 fullstop gmk1 and viceversa - no manipulation info
            k=k*0.87    	
#            print ('--fullstop')            
        if gmk1 == 'activation':
            if  re.search(r'(activation by %s)' %gs1, br0, re.I|re.S): # this was meant to be a negative rule
                k=k*0.21
                vv=1
                d=1
                #print 'activation one' ##########################
            if  re.search(r'(probably.*?%s activation)' %gs1, br, re.I|re.S|re.DOTALL):
                k=k*1
                vv=1
                d=1
                #print 'activation two' ##############################
            if  re.search(r'(critical for.*?%s activation)' %gs1, br, re.I|re.S):
                k=k*0.1
                vv=1
                d=1
                #print 'activation three' ################################
            if  re.search(r'(%s.*?activation of)' %gs1, br3, re.I|re.S):
                k=k*0.73
                vv=1
                d=1
                #print 'activation four' ################################
        if gmk1 == 'deficient':
            if  re.search(r'(%s deficient)' %gs1, br0, re.I|re.S): # modification is DOWN
                k=k*3.45
                vv=1
                d=-1
                #print 'deficient one' 
            if  re.search(r'(deficient.+?exhibited.+?%s)' %gs1, br0, re.I|re.S|re.DOTALL): 
                k=k*0.1
                vv=1
                d=-1
                #print 'deficient two' ########################### 
                
        if gmk1 == '-/-':
            if  re.search(r'(-/-%s)' %gs1, br0, re.I|re.S): # 
                #print 'minus one rule'  ###########################
                d=-1                
            if  re.search(r'(%s-/-)' %gs1, br0, re.I|re.S):
                k=k*2.78
                vv=1
                d=-1
                #print 'minus two'
        if gmk1 == '+':
            if  re.search(r'(%s+)' %gs1, br0, re.I|re.S):
                #print 'plus one rule'
                d=1
            if  re.search(r'(%s\(\+\))' %gs1, br3, re.I|re.S):
                k=k*0.1
                vv=1
                d=1
                #print 'plus two'
            else:
                #print 'plus last option'
                None
        if gmk1 == 'induced':
            if  re.search(r'(%s.*?was shown.+?induced)' %gs1, br0, re.I|re.S|re.DOTALL):
                k=k*0.1
                vv=1
                d=1    
                #print 'induced one' ###########################
            if  re.search(r'(%s.*?-induced)' %gs1, br0, re.I|re.S):
                #print 'induced two rule' ###########################
                d=1
            if  re.search(r'(induced.*?to %s)' %gs1, br0, re.I|re.S):
                k=k*0.41
                vv=1
                d=1
                #print 'induced three' ###########################
            if  re.search(r'(induced.*?while %s)' %gs1, br0, re.I|re.S):
                k=k*0.1
                vv=1
                #print 'induced four' ###########################
        if gmk1 == 'inhibition':
            if  re.search(r'(hypothesized\s.*?\sinhibition\s.*?\s%s )' %gs1, br, re.I|re.S):
                #print 'inhibition one rule' ###########################
                d=-1
        if gmk1 == 'knockout':
            if  re.search(r'(effect of %s knockout)' %gs1, br3, re.I|re.S):
                k=k*10
                vv=1
                d=-1
#                print ('knockout one')
            if  re.search(r'(double knockout)', br3, re.I|re.S): # for the time being
                k=k*0.1
                vv=1
                d=-1
                #print 'knockout two'
        if gmk1 == 'KO':
            if  re.search(r'(double KO\W)', br3, re.I|re.S): # for the time being
                #print 'double KO rule' 
                d=-1                                    
        if gmk1 == 'mutant':
            if  re.search(r'(harboring.*?%s mutant)' %gs1, br, re.I|re.S):
                #print 'mutant one rule'
                d=-1
            if  re.search(r'(mutant.*?causes.*?%s)' %gs1, br0, re.I|re.S):
                #print 'mutant two rule' ###########################               
                d=-1
        if gmk1 == 'stimulated':
#            if  re.search(r'(.*?-stimulated.*?%s)' %gs1, br, re.I|re.S):
#                k=k*-0.23
#                vv=1                            --------TO BE DONE------------
#                d=1
#                #print 'stimulated two' ###########################
            if  re.search(r'(%s-stimulated)' %gs1, br0, re.I|re.S):
                k=k*0.46
                vv=1
                d=1
                #print 'stimulated one'
        if gmk1 == 'treated':
            # if  re.search(r'(treated.*?control.*?%s)' %gs1, br0, re.I|re.S):
            #     k=k*-0.18
            #     vv=1                ------------TO BE DONE-------------
            #     d=1
            #     #print 'treated one' ###########################
            if  re.search(r'(control or %s-treated)' %gs1, br3, re.I|re.S):
                k=k*10
                vv=1
                d=1
#                print ('treated two')                
        if gmk1 == 'activation':
            if  re.search(r'(activation of %s)' %gs1, br0, re.I):
                k=k*0.24
                vv=1
                d=1
                #print 'activation five'
        if gmk1 == 'induced':
            if  re.search(r'(induced in response to %s)' %gs1, br0, re.I):
                k=k*2.15
                vv=1
                d=1
                #print 'induced five'
        if gmk1 == 'overexpression':
            if  (re.search(r'(%s.*?overexpression)' %gs1, br0, re.I) or re.search(r'(%s.*?overexpression)' %gs1, br0, re.I)):
                k=k*0.37
                vv=1
                d=1
                #print 'overexpression one'
        if gmk1 == 'treatment':
            if  re.search(r'(treatment.*?with %s)' %gs1, br0, re.I):
                k=k*1.53
                vv=1
                d=1
                #print 'treatment one'    	           			
        if vv==1: # so that k=1 is not returned if there are no matches. only if k changes, k should be returned (right?)
            return k
        else:
            return None