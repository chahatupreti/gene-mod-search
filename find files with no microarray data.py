import os
lk=0
q=open(r'I:\My Online Documents\MTech\GEO_website\series\tdg.txt','w')
for path, dirs, files in os.walk('I:\My Online Documents\MTech\GEO_website\series\series files\fg'):
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
            
            
for path, dirs, files in os.walk('I:\My Online Documents\MTech\GEO_website\series\old series files'):
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
   
        #read_f.close()
        #output.close()
        
