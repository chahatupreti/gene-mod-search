import os
ccount = 0
uncount = 0
count = 0
wcount = 0
for path, dirs, files in os.walk('I:\My Online Documents\MTech\GEO_website\series\series files'):
    for file in files:
        read_f = open(os.path.join(path,file),'r')
        output = open(os.path.join('I:\My Online Documents\MTech\series_imp_info', file + 'imp_info.txt'),'w');
        for line in read_f:
            line = line.rstrip()
            if line.startswith('!Series_title'):
                output.write(line);
                output.write('\n');
            if line.startswith('!Series_summary'):
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
        read_f.close()
        output.close()
        
