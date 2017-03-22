# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:20:10 2015

@author: Krishna
"""

import os
import re



#keywords = open('C:\Users\Krishna\Documents\ztestt.txt','r').readlines()
q=open('C:\Users\Krishna\Desktop\gmk_d_arabi.txt','w')
keywords = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()  # this has the down keywords
c=0
for path, dirs, files in os.walk('F:\M.Tech\org segregated\Arabidopsis thaliana'):
    for file in files:

        sentences = open(os.path.join(path,file),'r').readlines();
        c = c+1
        r=0
        print c
        k=0
        for s in sentences:
            s = s.rstrip()
            if s.startswith('!Series_title'):
                for keyword in keywords:
                    key2 = re.escape(keyword.rstrip())
                    if re.search(r'\b%s\b' % key2, s):
                        q.write(file)
                        q.write('\t')
                        q.write("Found '%s' in '%s'" % (keyword.strip(), s.strip()))
                        q.write('\n')               
            if s.startswith('!Series_summary'):
                for keyword in keywords:
                    key2 = re.escape(keyword.rstrip())
                    if re.search(r'\b%s\b' % key2, s):
                        q.write(file)
                        q.write('\t')
                        q.write("Found '%s' in '%s'" % (keyword.strip(), s.strip()))
                        q.write('\n')
            if s.startswith('!Series_overall_design'):
                for keyword in keywords:
                    key2 = re.escape(keyword.rstrip())
                    if re.search(r'\b%s\b' % key2, s):
                        q.write(file)
                        q.write('\t')
                        q.write("Found '%s' in '%s'" % (keyword.strip(), s.strip()))
                        q.write('\n')
q.close()
                   
      
          
    
