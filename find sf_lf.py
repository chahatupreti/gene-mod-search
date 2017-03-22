# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:37:35 2016

@author: chahat
"""
import re
import os
from acronym_extract_github_code import extract_acronym
for path, dirs, files in os.walk(r'/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/selected/mouse in random 500_l'):
    for file in files:
        sentences = open(os.path.join(path,file)).readlines();        
        r=0
        rr=0
        rt=0
        gs_cl=[]
        hg=''
        for s in sentences:
            if s.startswith('!Series_type'):
                if s.startswith('!Series_type\t"Expression profiling by array"'):
                    rr=1
            
        if (rr==1):
            acrolist=[]
            for s in sentences:
                s = s.rstrip()                
                if s.startswith('!Series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
#                    s = s.lower()
                    SfLf_list = extract_acronym(s, search='complex')
                    if SfLf_list:                        
                        print (SfLf_list)
                    
# After trying the code as it is, with the complex and reduced2 modes - 4 matches were found.
# In the reduced1 and simple modes - acro's were found with their counts - no definitions