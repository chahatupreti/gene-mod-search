# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:44:57 2016

@author: Krishna
"""
import os,io
import json
import itertools
with open('E:\F DRIVE\M.Tech\mus musculus_synonyms1.json') as json_data:
    d = json.load(json_data)
# {k.lower():v.lower()
#     for k, v in d.items()
# }
#import ast
#dd=ast.literal_eval(str(d).lower())
gs_found=[]
gs_actual=[]
# print (type(d))
# for element in d.keys():

for path, dirs, files in os.walk(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\occurences\working 2 jan'):
    for file in files:
        c=0
        cc=0
        cl=0.00
        sentences = io.open(os.path.join(path,file), encoding="utf8").readlines();
        for i in range(len(sentences)):
            sentences[i]=sentences[i].rstrip()
        # gs_found = itertools.islice(source_sequence, 0, None, 10)
        gs_found=sentences[1::3]
        # for i in range(-2,len(sentences)-3):
        # gs_found=sentences[i+3]
        gs_actual=sentences[2::3]
#        print (gs_found)
        # print (gs_actual)
        kk=''
        for i in range(len(gs_found)):
            if gs_found[i] in d.keys():
#                print (12)
#                print (gs_found[i])
                kk=gs_found[i]
                if gs_actual[i] in d[kk]:
                    c=c+1
#                    print(gs_actual[i], kk)
                else:
                    cc=cc+1
#        if c+cc>=50:
            
#            print ('%s - %d' %(file, ccc))
            
        ccc=c+cc  
        if c>0 or cc>0:
            cl=(10**((c-cc)/(c+cc)))
        print ('%s \t %d \t (%d/%d) \t %f' %(file, ccc,c,cc, cl))
#        print (c+cc)
#        if c>0 or cc>0:
#            cl=(10**((c-cc)/(c+cc)))
#            print (cl)
