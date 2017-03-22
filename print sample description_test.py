import os
fname = "output_file2.txt"
output = open(fname, 'w')
ccount = 0
uncount = 0
for path, dirs, files in os.walk('F:\M.Tech\output'):
    for file in files:
        read_f = open(os.path.join(path,file),'r')
        for line in read_f:
            line = line.rstrip()
            if line.startswith('!Series_geo_accession'):
           # if 'Series_geo_accession' in line:
                series = line;
            if line.startswith('!Sample_geo_accession'):
            #if 'Sample_geo_accession' in line:
                samples = line;
            if line.startswith('!Sample_description'):
           # if 'Sample_description' in line:
                descri = line;
            if line == '!series_matrix_table_begin':
                break
        read_f.close()
        split_series = series.split("\t");
        split_samples = samples.split("\t");
        split_descri = descri.split("\t");
        if 'control' in descri:
            ccount = ccount + 1
        if 'untreated' in descri:
            uncount = uncount + 1
        n = 1
        while n < len(split_samples):
            output.write(split_series[1]);
            output.write('\t');
            output.write(split_samples[n]);
            output.write('\t');
            output.write(split_descri[n]);
            output.write('\n');
            n = n + 1;
output.close()
print 'control count is %d and untreated count is %d' % (ccount, uncount);
