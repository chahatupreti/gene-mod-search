# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:37:18 2016

@author: Krishna
"""
import os
import re
import io
#import sys
#import codecs
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#def fileopener(filename):
#    filename=open(os.path.join(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurence',  filename, '.txt'), 'w')
#
#
#fileopener(del1)

del1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\del1.txt','w', encoding="utf8") # this encoding="utf8" has to be done for PYTHON-3 
del2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\del2.txt','w', encoding="utf8")
ko1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ko1.txt','w', encoding="utf8")
ko2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ko2.txt','w', encoding="utf8")
ko3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ko3.txt','w', encoding="utf8")
stim1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\stim1.txt','w', encoding="utf8")
stim2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\stim2.txt','w', encoding="utf8")
ove1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ove1.txt','w', encoding="utf8")
ove2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ove2.txt','w', encoding="utf8")
ove3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ove3.txt','w', encoding="utf8")
ove4=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ove4.txt','w', encoding="utf8")
ove5=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ove5.txt','w', encoding="utf8")
add1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\add1.txt','w', encoding="utf8")
add2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\add2.txt','w', encoding="utf8")
add3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\add3.txt','w', encoding="utf8")
kno1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\kno1.txt','w', encoding="utf8")
kno2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\kno2.txt','w', encoding="utf8")
kno3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\kno3.txt','w', encoding="utf8")
kno4=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\kno4.txt','w', encoding="utf8")
kno5=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\kno5.txt','w', encoding="utf8")
kno6=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\kno6.txt','w', encoding="utf8")
sign1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\sign1.txt','w', encoding="utf8")
sign2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\sign2.txt','w', encoding="utf8")
sign3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\sign3.txt','w', encoding="utf8")
sign4=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\sign4.txt','w', encoding="utf8")
transg1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\transg1.txt','w', encoding="utf8")
transg2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\transg2.txt','w', encoding="utf8")
mut1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\mut1.txt','w', encoding="utf8") 
mut2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\mut2.txt','w', encoding="utf8") 
mut3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\mut3.txt','w', encoding="utf8") 
mut4=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\mut4.txt','w', encoding="utf8") 
def1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\def1.txt','w', encoding="utf8") 
def2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\def2.txt','w') 
def3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\def3.txt','w', encoding="utf8") 
ag1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ag1.txt','w', encoding="utf8") 
ag2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ag2.txt','w', encoding="utf8") 
ag3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ag3.txt','w', encoding="utf8") 
ab1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ab1.txt','w', encoding="utf8") 
ab2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ab2.txt','w', encoding="utf8") 
ab3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\ab3.txt','w', encoding="utf8") 
null1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\null1.txt','w', encoding="utf8") 
null2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\null2.txt','w', encoding="utf8") 
null3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\null3.txt','w', encoding="utf8") 
shr1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\shr1.txt','w', encoding="utf8") 
shr2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\shr2.txt','w', encoding="utf8") 
shr3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\shr3.txt','w', encoding="utf8") 
shr4=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\shr4.txt','w', encoding="utf8") 
shr5=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\shr5.txt','w', encoding="utf8") 
reg1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\reg1.txt','w', encoding="utf8") 
reg2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\reg2.txt','w', encoding="utf8") 
reg3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\reg3.txt','w', encoding="utf8") 
reg4=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\reg4.txt','w', encoding="utf8") 
dep1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\dep1.txt','w', encoding="utf8") 
dep2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\dep2.txt','w', encoding="utf8") 
dep3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\dep3.txt','w', encoding="utf8") 
inh1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\inh1.txt','w', encoding="utf8") 
inh2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\inh2.txt','w', encoding="utf8") 
inh3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\inh3.txt','w', encoding="utf8") 
treat1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\treat1.txt','w', encoding="utf8") 
treat2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\treat2.txt','w', encoding="utf8") 
treat3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\treat3.txt','w', encoding="utf8") 
treat4=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\treat4.txt','w', encoding="utf8") 
treat5=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\treat5.txt','w', encoding="utf8") 
transf1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\transf1.txt','w', encoding="utf8") 
transf2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\transf2.txt','w', encoding="utf8") 
transf3=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\transf3.txt','w', encoding="utf8") 
transf4=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\transf4.txt','w', encoding="utf8") 
hap1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\hap1.txt','w', encoding="utf8") 
hap2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\hap2.txt','w', encoding="utf8") 
act1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\act1.txt','w', encoding="utf8") 
act2=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\act2.txt','w', encoding="utf8") 
golden=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurencell\golden.txt','w', encoding="utf8") 







def cl(s1, gmk, gs1, gs_list1, data1, file,gene_actual):
    gs11=gs1
    br0=''
    br3=''
    br=''
    gs_list1.remove(gs1) # AS WE WANT TO USE THIS LIST FOR GETTING THE GS'S THAT ARE APART FROM THE CURRENT GS        
    s1 = re.sub(r'(\b(%s)\b)' % (gs1), r'_8MILLION8_', s1, flags=re.I) # inserts the token wherever there is GS. The \b before & after ensures this doesnt happen in between words
    gs1='_8MILLION8_'
    l = s1.split()  # i switched from the complex split above to just space split to ensure that the splitters can be part of a rule 
#    print (gene_actual)
    def writer(filetowrite):
        filetowrite.write(file)
        filetowrite.write('\n')
        filetowrite.write(gs11)
        filetowrite.write('\n')
        filetowrite.write(gene_actual)
        filetowrite.write('\n')
#        filetowrite.write(gmk)
#        filetowrite.write('\n')
#        filetowrite.write('Found %s in -  %s' % (gs11,s1.strip()))
#        filetowrite.write('\n')
#        filetowrite.write('Found %s in -  %s' % (gs11,br0))        
#        filetowrite.write('\n')
        


    for ii in range(0,len(data1)):
        a = data1[ii]
        lo = min(a[1], a[2])
        hi = max(a[1], a[2])
        brr = l[max(0, lo-6):hi+6]
        br6= " ".join(brr) 
        br00 = l[max(0, lo):hi+1]  # we dont need the 8 words here and there as the fullstop is between gmk1 and gs1
        br0= ' '.join(br00)
        br33 = l[max(0, lo-3):hi+3] 
        br3= ' '.join(br33)       
#    print (br0)
#    print (br3)
#    print (br)


    if gmk == 'deletion':
        if re.search(r'(deletion of %s)' %gs1, br3, re.I|re.S):
            writer(del1)
        if re.search(r'(%s[- ]deletion)' %gs1, br3, re.I|re.S):
            writer(del2)
            
    if gmk == 'KO' or 'CKO': #<--------
        if re.search(r'(%s single and ([\w]+\s*){0,3} double KO)' %gs1, br6, re.I|re.S):
            writer(ko1)
        if re.search(r'(%s([- ])?KO)' %gs1, br3, re.I|re.S):
            writer(ko2)
        if re.search(r'(%s([- ])?(C)?KO)' %gs1, br3, re.I|re.S):
            writer(ko3)
            
    if gmk == ('stimulated' or 'stimulation'): #<--------
        if re.search(r'(stimulation of %s)' %gs1, br3, re.I|re.S):
            writer(stim1)
        if re.search(r'(%s[- ]stimulated)' %gs1, br3, re.I|re.S):
            writer(stim2)
            
    if gmk == 'overexpress' or 'overexpressed' or 'overexpressing' or 'overexpression':#<--------
        if re.search(r'(overexpression of %s)' %gs1, br3, re.I|re.S):
            writer(ove1)
        if re.search(r'(%s[- ]overexpression)' %gs1, br3, re.I|re.S):
            writer(ove2)
        if re.search(r'(%s was overexpressed)' %gs1, br3, re.I|re.S):
            writer(ove3)
        if re.search(r'(overexpress(ed|ing)? %s)' %gs1, br3, re.I|re.S):
            writer(ove4)
        if re.search(r'(overexpress ([\w]+\s*){0,3}(,| and) %s)' %gs1, br3, re.I|re.S):
            writer(ove5)
    
    if gmk == 'add' or 'addition' or 'added':#<--------
#        print (121212)
        if re.search(r'(added %s)' %gs1, br3, re.I|re.S):
            writer(add1)
        if re.search(r'(addition of %s)' %gs1, br3, re.I|re.S):
            writer(add2)
        if re.search(r'(%s was added)' %gs1, br3, re.I|re.S):
            writer(add3)
    
    if gmk == 'knock' or 'knockout' or 'knock out' or 'knockdown' or 'knock down'or 'knock-out' or 'knock-down' or 'knock-in' or 'knockin':#<--------
        if re.search(r'((double|triple) knock([ -])?out)', br3, re.I|re.S):
            writer(kno1)
        if re.search(r'(%s knock([ -])?(out|down) effect)' %gs1, br3, re.I|re.S):
            writer(kno2)
        if re.search(r'(%s knock([ -])?(out|down))' %gs1, br3, re.I|re.S):
            writer(kno3)
        if re.search(r'(knock([ -])?(out|down) of %s)' %gs1, br3, re.I|re.S):
            writer(kno4)
        if re.search(r'(%s knock([-])?in)' %gs1, br3, re.I|re.S):   
            writer(kno5)
        if re.search(r'(effect of %s knock([ -])?(out|down))' %gs1, br3, re.I|re.S):
            writer(kno6)
            
    if gmk == ('+ 'or '-/-' or '+ve' or '-ve' or 'positive' or 'negative'):#<--------#<--------
        if re.search(r'(%s(+|(+)))' %gs1, re.escape(br3), re.I|re.S): # see if we have to escape (+)
            writer(sign1)
        if re.search(r'(%s[- ](positive|negative))' %gs1, re.escape(br3), re.I|re.S):
            writer(sign2)
        if re.search(r'(%s(+ve|-ve))' %gs1, re.escape(br3), re.I|re.S):
            writer(sign3)
        if re.search(r'(%s(-/-|(-/-)))' %gs1, re.escape(br3), re.I|re.S): # see if need to escape (-/-)
            writer(sign4)
        
    if gmk == 'transgenic':#<--------#<--------
        if re.search(r'(%s transgenic)' %gs1, br3, re.I|re.S):
            writer(transg1)
        if re.search(r'(%s transgenic model)' %gs1, br3, re.I|re.S):
            writer(transg2)
            
    if gmk == 'mutant' or 'mutated':#<--------
        if re.search(r'(%s[ -]mutant)' %gs1, br3, re.I|re.S):
            writer(mut1)
        if re.search(r'(%s mutant (vs|versus) wild([ -])?type)' %gs1, br6, re.I|re.S):
            writer(mut2)
        if re.search(r'(mutated %s)' %gs1, br3, re.I|re.S):
            writer(mut3)
        if re.search(r'(mutant %s)' %gs1, br3, re.I|re.S):
            writer(mut4)
            
    if gmk == 'deficient' or 'deficiency':
        if re.search(r'(%s[ -]deficiency)' %gs1, br3, re.I|re.S): # why not working?
            writer(def1)
        if re.search(r'(deficient (of|in) %s)' %gs1, br3, re.I|re.S):
            writer(def2)
        if re.search(r'((effect of)? %s deficiency)' %gs1, br3, re.I|re.S):
            writer(def3)
            
    if gmk == ('agonist' or 'antagonist'):#<--------
        if re.search(r'((treated with )?%s (ant)?agonist)' %gs1, br3, re.I|re.S): # why not working?
            writer(ag1)
        if re.search(r'(agonist of %s)' %gs1, br3, re.I|re.S):
            writer(ag2)
        if re.search(r'(antagonist of %s)' %gs1, br3, re.I|re.S):
            writer(ag3)
            
    if gmk == 'ablation' or 'abalated':#<--------
       if re.search(r'(%s ablation)' %gs1, br3, re.I|re.S):
           writer(ab1)
       if re.search(r'(ablation of %s)' %gs1, br3, re.I|re.S):
           writer(ab2)
       if re.search(r'(%s[- ]ablated)' %gs1, br3, re.I|re.S):
           writer(ab3)
    
    if gmk == 'null':
        if re.search(r'(%s[ -]null)' %gs1, br3, re.I|re.S):
            writer(null1)
        if re.search(r'(%s null and ([\w]+\s*){0,3}wild([ -])?type )' %gs1, br6, re.I|re.S):
            writer(null2)
        if re.search(r'(%s(\w){0,4} null)' %gs1, br3, re.I|re.S):  # upto 4 characters after GS to signify modifications
            writer(null3)
           
    if gmk == 'shrna':#<--------
#        print (234)
        if re.search(r'(%s shrna)' %gs1, br3, re.I|re.S):
            writer(shr1)
        if re.search(r'(shrna(s)? targe(t)?ting ([\w]+\s*){0,3}%s)' %gs1, br6, re.I|re.S):
            writer(shr2)
        if re.search(r'(shrna (mediated)? knockdown of ([\w]+\s*){0,2}%s)' %gs1, br6, re.I|re.S):
            writer(shr3)
        if re.search(r'(shrna depletion(s)? of %s)' %gs1, br3, re.I|re.S):
            writer(shr4)
        if re.search(r'(shrna-%s (treated)?)' %gs1, br3, re.I|re.S):
            writer(shr5)
            
    if gmk == 'regulation' or 'regulated':#<--------
        if re.search(r'((over|up|down)( )?regulation of ([\w]+\s*){0,3}%s)' %gs1, br6, re.I|re.S):
            writer(reg1)
        if re.search(r'(%s (over|up|down)( )?regulation)' %gs1, br6, re.I|re.S):
            writer(reg2)
        if re.search(r'(%s (over|up|down)( )?regulated ([\w]+\s*){0,2}cells)' %gs1, br6, re.I|re.S):
            writer(reg3)
    if re.search(r'(%s ([\w]+\s*){0,3}over([ -])?expressed (or|and) under([ -])?expressed)' %gs1, s1, re.I|re.S):
        writer(reg4)
            
    if gmk == 'depletion' or 'depleted':#<--------
       if re.search(r'(%s depletion)' %gs1, br3, re.I|re.S):
           writer(dep1)
       if re.search(r'(depletion of %s)' %gs1, br3, re.I|re.S):
           writer(dep2)
       if re.search(r'(%s[- ]depleted)' %gs1, br3, re.I|re.S):
           writer(dep3)
          
    if gmk == 'inhibition' or 'inhibited':#<--------
       if re.search(r'(we inhibited %s)' %gs1, br3, re.I|re.S):
           writer(inh1)
       if re.search(r'(inhibition ([\w]+\s*){0,2}of %s)' %gs1, br3, re.I|re.S):
           writer(inh2)
       if re.search(r'(%s was inhibited)' %gs1, br3, re.I|re.S):     
           writer(inh3)
           
    if gmk == 'treat' or 'treated' or 'treatment':#<--------
       if re.search(r'(%s[ -]treated)' %gs1, br3, re.I|re.S):
           writer(treat1)
       if re.search(r'(treated with %s)' %gs1, br3, re.I|re.S):
           writer(treat2)
       if re.search(r'(treatment ([\w]+\s*){0,3} with %s)' %gs1, br6, re.I|re.S):
           writer(treat3)
       if re.search(r'(%s treatment)' %gs1, br3, re.I|re.S):
           writer(treat4)
       if re.search(r'(control or %s[ -]treated)' %gs1, br3, re.I|re.S):
           writer(treat5)
        
    if gmk == 'transfect' or 'transfected':#<--------
        if re.search(r'(%s[ -]transfected)' %gs1, br3, re.I|re.S):
            writer(transf1)
        if re.search(r'(transfected with (the)?%s)' %gs1, br3, re.I|re.S):
            writer(transf2)
        if re.search(r'(transfected ([\w]+\s*){0,3} sirna ([\w]+\s*){0,3}%s)' %gs1, br3, re.I|re.S):
            writer(transf3)
        if re.search(r'(transfected by %s)' %gs1, br3, re.I|re.S):
            writer(transf4)
          
    if gmk == 'haploinsufficiency' or 'haploinsufficient':#<--------
        if re.search(r'(%s haploinsufficient)' %gs1, br3, re.I|re.S):
            writer(hap1)
        if re.search(r'(%s haploinsufficiency)' %gs1, br3, re.I|re.S):
            writer(hap2)
            
    if gmk == 'activation':
        if re.search(r'(activation of %s)' %gs1, br3, re.I|re.S):
            writer(act1)
        if re.search(r'(activation by %s)' %gs1, br3, re.I|re.S): #<--- good chance of this being really rare hence useless 
            writer(act2)
        
    if re.search(r'(the object(ive)? of this study was (to identify|identifying)genes (transcriptionally )?(upregulated|downregulated))',s1) or re.search(r'(the object(ive)? of this study was (to identify|identifying) genes (transcriptionally )?((upregulated (and |or )downregulated)))',s1) or re.search(r'(the object(ive)? of this study was (to identify|identifying) genes (transcriptionally )?upregulated ([\w]+\s*){0,3}downregulated)',s1):
        writer(golden)
        
    #if re.search(r'((to determine|were assayed|designed to compare|in effect(s)? of|differential gene expression))', s1):

def closedd():
    del1.close()
    del2.close()
    ko1.close()
    ko2.close()
    ko3.close()
    stim1.close()
    stim2.close()
    ove1.close()
    ove2.close()
    ove3.close()
    ove4.close()
    ove5.close()
    add1.close()
    add2.close()
    add3.close()
    kno1.close()
    kno2.close()
    kno3.close()
    kno4.close()
    kno5.close()
    kno6.close()
    sign1.close()
    sign2.close()
    sign3.close()
    sign4.close()
    transg1.close()
    transg2.close()
    mut1.close()
    mut2.close()
    mut3.close()
    mut4.close()
    def1.close()
    def2.close()
    def3.close()
    ag1.close()
    ag2.close()
    ag3.close()
    ab1.close()
    ab2.close()
    ab3.close()
    null1.close()
    null2.close()
    null3.close()
    shr1.close()
    shr2.close()
    shr3.close()
    shr4.close()
    shr5.close()
    reg1.close()
    reg2.close()
    reg3.close()
    reg4.close()
    dep1.close()
    dep2.close()
    dep3.close()
    inh1.close()
    inh2.close()
    inh3.close()
    treat1.close()
    treat2.close()
    treat3.close()
    treat4.close()
    treat5.close()
    transf1.close()
    transf2.close()
    transf3.close()
    transf4.close()
    hap1.close()
    hap2.close()
    act1.close()
    act2.close()
    golden.close()
