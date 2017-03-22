# -*- coding: utf-8 -*-
import os
import json
fname = "E:\F DRIVE\M.Tech\gene list\mus musculus genes.txt"
d = 0
output = open(r'E:\F DRIVE\M.Tech\mus musculus_synonyms1.json','w')
# maingene='maingene'
# syns='syns'
#from collections import defaultdict
synlist = {}
# synlist={}
with open(fname) as f:
    next(f)    ## this helps us skip the first line which was like header, it said what was in the file
    for line in f:
        line = line.rstrip()
        split_the_line = line.split("\t");
      #  split_the_line = filter(None, split_the_line)
      #  print split_the_line;
        n = 0
        print (d)
        d = d+1
        main=''
        slist=[]
        
                    # SYMBOLS
        main=split_the_line[5]
        slist.append(main)
        # synlist[maingene]=split_the_line[5]
        # output.write(split_the_line[5]);
        # output.write('\n');

                   # ALIASES
        
        if split_the_line[6]:
            c = split_the_line[6].split(', ');
     
            while n< len(c):
                slist.append(c[n])
                # try:
                #     synlist[split_the_line[5]].append(c[n])
                # except KeyError:
                #     synlist[split_the_line[5]].append('')
                # output.write(c[n]);
                # output.write('\n');
                n= n + 1;

                	  # DESCRIPTION	

        if split_the_line[7] != None:	
            
            slist.append(split_the_line[7])
            #     synlist[split_the_line[5]].append(split_the_line[7])
            # except KeyError:
            #     synlist[split_the_line[5]].append('')    
           # output.write(split_the_line[7]);
           # output.write('\n');

				 # OTHER_DESIGNATION

        n = 0
        if (len(split_the_line) > 8) and (split_the_line[8]):
         
            other_desc_split = split_the_line[8].split('|');
       
            while n < len(other_desc_split):
                slist.append(other_desc_split[n])
                # output.write(other_desc_split[n]);
              
                n = n + 1;
        # print (type(main))
        # print (slist)
#        synlist[main]=slist
        slist1=slist
        for syn in slist1: # CREATE DICTIONARY ENTRY FOR ALL WORDS
            synlist[syn]=slist
#        for k in slist:
#            synlist[main].append(slist[k])
        # synlist.setdefault(main, (slist[k] for k in slist))
        # synlist=dict((main, slist[k]) for k in slist)
                # output.write('\n');
##        
import ast
synlist_lcase=ast.literal_eval(str(synlist).lower()) # CONVERT THE ENTIRE DICTIONARY TO LOWERCASE TO HELP IN MATCHING LATER
json.dump(synlist_lcase, output, sort_keys=True, indent=4, separators=(',', ':'))
fname.close()
output.close()
#for k in other_words:
#    synlist[main].append(other_words[k])