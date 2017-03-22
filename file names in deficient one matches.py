# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:25:47 2016

@author: Krishna
"""
import itertools
a=open(r'E:\F DRIVE\M.Tech\for assigning cl\new rule occurence\improved new rules\here_we.txt', encoding="utf8").readlines()
#b=open(r'gs matches for 14k files with occurence.txt','w')
c=[]
d=[]
i=0
ii=0
gsline = itertools.islice(a,0,None,3)
for g in gsline:
    h=g.split('_')
    j=h[0]
    c.append(j)
    

def unique(source):
    sofar = {}
    for val in source:
      if not sofar.get(val):
        yield val.strip()
        sofar[val] = 1
  
for lyne in unique(c):
    d.append(lyne)
    ii=ii+1
    
# def count_string_occurrence(org):
#     contents = c
#     b.write(org)
#     b.write('\t')
#     b.write(str(contents.count(org)))
#     b.write('\n')

# for line in d:
#     count_string_occurrence(line)

for e in d:
    e=e[3:8]
    print (e)

      

    

