# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:25:45 2016

@author: Krishna
"""

a=open(r'F:\M.Tech\mouse_gs_small_simple.txt','r').readlines()
b=open(r'C:\Users\Krishna\Desktop\up down analysis for orgs\GS to remove.txt','r').readlines()
c=open(r'F:\M.Tech\mouse_gs_small_simple_reduced.txt','w')
d=[]
for word in a:
    if (word.lower() not in b):
        d.append(word)
n=0        
while n < len(d):
    c.write(d[n])
    n=n+1
c.close()