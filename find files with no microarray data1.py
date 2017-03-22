import os
lk=0
print 22
q=open(r'I:\My Online Documents\MTech\GEO_website\series\tdg4.txt','w')
print 22
for path, dirs, files in os.walk(r'I:\My Online Documents\MTech\GEO_website\series\series files\fg'):
    print 22
    for file in files:
        lk += 1
        print lk
        count=0
        readf = open(os.path.join(path,file),'r').readlines()
        for i in range(0, len(readf)):
            readf[i]=readf[i].rstrip()
            
        #print type(readf)
        #output = open(os.path.join('I:\My Online Documents\MTech\series_imp_info', file + 'imp_info.txt'),'w');
        for i, line in enumerate(readf):
            if "series_matrix_table_begin" in line:
                k=i
            if 'series_matrix_table_end' in line:
                k1=i
                break
    

        count=k1-k
        if count<10:       
            q.write(file)
            q.write('\n')                
            q.write('count is %d' %count)
            q.write('\n')

        
