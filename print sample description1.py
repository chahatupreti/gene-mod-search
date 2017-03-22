import os
fname = "output_file3.txt"
output = open(fname, 'w')
ccount = 0
uncount = 0
count = 0
wcount = 0
for path, dirs, files in os.walk('F:\M.Tech\series files'):
    for file in files:
        read_f = open(os.path.join(path,file),'r')
        for line in read_f:
            line = line.rstrip()
            if line.startswith('!Series_geo_accession'):
                series = line;
            if line.startswith('!Sample_geo_accession'):
                samples = line;
            if line.startswith('!Sample_description'):
                descri = line;
            if line == '!series_matrix_table_begin':
                break
        read_f.close()
        split_series = series.split("\t");
        split_samples = samples.split("\t");
        split_descri = descri.split("\t");
        if 'control' in descri:
            ccount = ccount + 1
        if 'wild-type' in descri:
            wcount = wcount + 1
        if 'untreated' in descri:
            uncount = uncount + 1
        print 'control count is %d and untreated count is %d and wild-type count is %d' % (ccount, uncount, wcount);
        count = count + 1;
        print 'series is %s and count is %d' % (series, count);
        n = 1
##        while n < len(split_samples):
##            output.write(split_series[1]);
##            output.write('\t');
##            output.write(split_samples[n]);
##            output.write('\t');
##            output.write(split_descri[n]);
##            output.write('\n');
##            n = n + 1;
output.close()
#print 'control count is %d and untreated count is %d' % (ccount, uncount);
