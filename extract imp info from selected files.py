# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 14:55:00 2016

@author: Krishna
"""
import os
import io
ccount = 0
uncount = 0
count = 0
wcount = 0
a=''
for path, dirs, files in os.walk(r'L:\My Online Documents\MTech\GEO_website\series\newer series'):
    #print 44
    for file in files:
        #print 5
        read_f = io.open(os.path.join(path,file), encoding="utf8")
        #print file
        a=str(file)
        if a=='README.txt':
            break
        # b=a[3:8]
        # b=int(b)
        # if b in range(14881,17721):
            
        output = io.open(os.path.join(r'E:\F DRIVE\M.Tech\for assigning cl\series_imp_info_lll', file + 'imp_info.txt'),'w', encoding="utf8");
        for line in read_f:
            line = line.rstrip()
            if line.startswith('!Series_title'):
                output.write(line);
                output.write('\n');
            if line.startswith('!Series_summary'):
                output.write(line);
                output.write('\n');
            if line.startswith(r'!Series_type'):
                output.write(line);
                output.write('\n');
            if line.startswith('!Sample_organism_ch1'):
                output.write(line);
                output.write('\n');
            if line.startswith('!Series_overall_design'):
                output.write(line);
                output.write('\n');
            if line.startswith('!Sample_title'):
                output.write(line);
                output.write('\n');
            if line.startswith('!Sample_source_name_ch1'):
                output.write(line);
                output.write('\n');
            if line.startswith('!Sample_characteristics_ch1'):
                output.write(line);
                output.write('\n');
            if line.startswith('!Sample_treatment_protocol_ch1'):
                output.write(line);
                output.write('\n');
            if line.startswith('!Sample_description'):
                output.write(line);
                output.write('\n');
            if line == '!series_matrix_table_begin':
                break
        
        output.close()
        read_f.close()
