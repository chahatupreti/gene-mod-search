import os
output = open('organsims.txt','w');
for path, dirs, files in os.walk('F:\M.Tech\series_imp_info'):
    for file in files:
        read_f = open(os.path.join(path,file),'r');
        for line in read_f:
            line = line.rstrip()
            if line.startswith('!Sample_organism_ch1'):
                splitit = line.split('\t');
                output.write(splitit[1]);
                output.write('\n');
            if line == '!series_matrix_table_begin':
                break
        read_f.close()
output.close()
        
