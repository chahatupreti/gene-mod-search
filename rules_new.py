# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:19:39 2016

@author: Krishna
"""

import re

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
            rg3.write('Found %s in %s' % (gmk1, br.strip())) # change to s1 
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
 
    return 4        
