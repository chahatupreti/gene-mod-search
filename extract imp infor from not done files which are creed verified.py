# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:11:16 2016

@author: Krishna
"""

# WHAT THIS FILE DOES ---->
# This file takes the list of filenames in the CREEDS data (1st half) in which the model organism is mouse, and checks for them in the 'not-done' files 
# in my Series database in the hard disk. On searching, it found 284 files in the not done database which were CREEDS verified files. Thn it just copies
# all those files to a folder called 'newer series' in the hard disk. In another code (E:\GAURANGA\M.Tech work\proper\extract imp info from selected files.py),
# files in this folder are taken, imp info is extracted from them and the imp info extracted files are generated and kept in 'series_imp_info_lll'
import os
import shutil
files1212=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\testing creed data\filenames with mouse in first half.txt').readlines()
for i in range(len(files1212)):
    files1212[i] = files1212[i].rstrip()
#print (len(files1212))
#if 'GSE3530' in files1212:
#print (files1212)
k=0    
c=0
for path, dirs, files in os.walk(r'L:\My Online Documents\MTech\GEO_website\series\not done'):
    for file in files:
        if file[-20:]=='series_matrix.txt.gz':
            fileparts=file.split('_')
            j=fileparts[0]
            jj=j.split('-')
            filenum=jj[0]
            if filenum in files1212: 
                o1=filenum[:-3]
                one=o1[3:]
                shutil.copy(r'L:\My Online Documents\MTech\GEO_website\series\not done\GSE'+one+'nnn\\'+filenum+'\matrix\\'+file,r'L:\My Online Documents\MTech\GEO_website\series\newer series\\'+file)
                c=c+1
                print(c)
            
            
            
#            for i in range(len(files1212)):
#                k=len(files1212[i])
#                print (files1212[i]) 
#                print (file[:k])
#                if files1212[i]==file[:k]:
#                    print (file)
#                    c=c+1
#                    print(c)
