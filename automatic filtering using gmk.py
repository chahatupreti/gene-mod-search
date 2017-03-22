# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:26:41 2015

@author: Krishna
"""
I N C O M P L T E    C O D E 
import os
import re
q=open('C:\Users\Krishna\Desktop\gmk fitering output.txt','w')
gmk_u = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()  # this has the up-gmk's
gmk_d = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
gmk_a = open('F:\M.Tech\patterns for gmk_ambi.txt','r').readlines()
c=0
for path, dirs, files in os.walk('F:\M.Tech\org segregated\mus musculus'):
    for file in files:

        sentences = open(os.path.join(path,file),'r').readlines();
        r=0
        s=''
        k=0
        for sentence in sentences:
            if k in (0,1,3): #to select only those 3 lines
                k=k+1
                for g_u in gmk_u:
                    gu = re.escape(g_u.rstrip()) # remove meta characters
                if re.search(r'\b%s\b' % gu, sentence):
                    m='u'
                    s[r] = sentence
            
            
q.close()
                   
      
          
    
