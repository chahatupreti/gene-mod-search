# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:05:56 2016

@author: Krishna
"""

files=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\testing creed data\filenames with mouse in first half.txt').readlines()
genes=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\testing creed data\modofied genes with mouse in first half.txt').readlines()
for i in range(len(files)):
    files[i] = files[i].rstrip() #to remove the lagging \n 
    files[i] = files[i].lower()    
    genes[i] = genes[i].rstrip()
    genes[i] = genes[i].lower()
files1='files'
genes1='genes'
print (files)
verified={files1:[], genes1:[]}
#d_idx = {files:[], genes:[]}
for f in files:
    verified[files1].append(f)
for g in genes: 
    verified[genes1].append(g)
print (len(verified[files1]))
if verified[files1][0]=='gse5496':
    print (verified[genes1][0])    
#print (verified)
#files.close()
#genes.close()