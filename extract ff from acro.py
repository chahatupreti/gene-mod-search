# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:28:15 2016

@author: Krishna
"""

import re
import os

def find_acros(sentence):
    rr=re.findall('(?:\(\w*?\))', sentence) # the capturing group is being kept as the acronym with the brackets
                    
    if rr:
        for rr_element in rr:
            acrolist.append(rr_element)
            
    return acrolist
#   acrolist=set(acrolist)



def ffPl(sentence):
    # in each sentence check for FF probables before the (acronyms)
    for acro in acrolist:
        acrolen=len(acro) + 1 # we want to capture 3+|acro| number of words and the 2 bracket signs take 2 characters 
        fullformProbables= re.search(r'((?:\w+\W+){1,%d}%s)'  %(acrolen, re.escape(acro)), s, re.I) #if this proves the speed bottleneck later, i can try to precompile the regex in the beginning and calling it in the loop
        if fullformProbables:
            ffP = fullformProbables.group(1)
            fullformProbables_list.append(ffP)
    return fullformProbables_list



for path, dirs, files in os.walk(r'/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/selected/test'):
    for file in files:
        sentences = open(os.path.join(path,file)).readlines();        
        rr=0
        for s in sentences:
            if s.startswith('!Series_type'):
                if s.startswith('!Series_type\t"Expression profiling by array"'):
                    rr=1
            
        if (rr==1):
            acrolist=[]
            for s in sentences:
                s = s.rstrip()
                
                if s.startswith('!Series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
                    s = s.lower()
                    acrolist=find_acros(s)
#                    print (file)
#                    print (acrolist)
#        print (file)
#        print (acrolist)
        
        fullformProbables_list=[]

        for s in sentences:
            fullformProbables_list = ffPl(s)
#        print (fullformProbables_list)
        
        sflf_list=[]

        for ffP in fullformProbables_list:           
            Acron=''
            Longform=''
            acrofirstletter = re.search(r'(?:\((\w).*\))' , ffP)
            acrofirstletter = acrofirstletter.group(1) 
            acron = re.search(r'(?:\(\w*?\))' , ffP)
            if acron:
                Acron=acron.group(0)
            longform = re.search(r'(?:(\b%s.*)\()' %acrofirstletter, ffP, re.I)
            if longform:
                Longform=longform.group(1)
            sflf_list.append((Acron, Longform))
        print (file)
        print (sflf_list)                    








#                for er in refind:
#                    rt.append(er)
#                if rt:          
#                    for rtt in rt:
#                        print (rtt)
                    
#a='Sporadic colorectal cancer (CRC) insurgence and progression depend on the activation of Wnt/β-catenin signaling. Dickkopf (DKK)-1 is an extracellular inhibitor of Wnt/β-catenin signaling that also has undefined β-catenin-independent actions. Here we report for the first time that a proportion of DKK-1 locates within the nucleus of healthy small intestine and colon mucosa, and of CRC cells at specific chromatin sites of active transcription. Moreover, we show that DKK-1 regulates several cancer-related genes including the cancer stem cell marker aldehyde dehydrogenase 1A1 (ALDH1A1) and Ral-binding protein 1-associated Eps domain-containing 2 (REPS2), which are involved in detoxification of chemotherapeutic agents. Nuclear DKK-1 expression is lost along CRC progression; however, it remains high in a subset (15%) of CRC patients (n = 699) and associates with decreased progression-free survival (PFS) after chemotherapy administration and overall survival (OS) [adjusted HR, 1.65; 95% confidence interval (CI), 1.23-2.21; P = 0.002)]. Overexpression of ALDH1A1 and REPS2 associates with nuclear DKK-1 expression in tumors and correlates with decreased OS (P = 0.001 and 0.014) and PFS.'
#if re.search(r'(\(.*?\))):
#rr=re.findall('(\(.*?\))', a)
#if rr:
##    print (type(rr))
#    print (rr)