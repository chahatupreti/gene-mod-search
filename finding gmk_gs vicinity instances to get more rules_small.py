import os
import re
import time
start_time = time.time()
q=open('C:\Users\Krishna\Desktop\up down analysis for orgs\gmk_gs vicinity_small.txt','w')
a = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1
#print a
keywords = open('F:\M.Tech\mouse_gs_small_simple.txt','r').readlines()  # this has the down keywords
#gmk = 'knockout'
c=0
for path, dirs, files in os.walk('F:\M.Tech\org segregated\mus musculus'):
    for file in files:

        sentences = open(os.path.join(path,file),'r').readlines();
        c = c+1
        r=0
        print c # one value printed for each file
        #print file
        print("--- %s seconds ---" % (time.time() - start_time))
                
        k=0
        hg=0
        for gmk in a:
            gmk = gmk.rstrip() #to remove the lagging \n in many GMKs
            #print gmk
            for s in sentences:
                s = s.rstrip()
                if s.startswith('!Series_title'):
                    if gmk in s:  # checking if gmk is in the line
                        l = re.split(';|,|-| ', s) # split the line by comma, semicolon and space to check for gmks and gs
                        for key2 in keywords: # gene symbols
                            key2 = key2.rstrip()     #remove lagging whitespace characters                   
                            #print key2
                            #re.compile(key2)
                            #print hg=hg+1
                            if key2 in s: # search for GS in line. using 'key2 in s' led to a lot of partial word matches
                                #print key2, 'reret', s                             
                                if ((key2 in l) and (gmk in l)): # ensure both are in the list. sometimes, they are not because of some attached delimiters                                                                                                     
#                                    index = s.find(key2) #find index of the GS in the line
#                                    if (s[index-1].isalpha() or s[index+len(key2)+1].isalpha())==False: #see if the 2 characters preceding and succeeding the GS are not alphabets. this is imp because if they are, then we dont want it, cause it means the GS is within a word
                                                                 
                                    r = abs(l.index(key2) - l.index(gmk)) # find distance between first character of key2 and gmk
                                    if r<=6:
                                        q.write(file)
                                        q.write('\n')
                                        q.write(key2)
                                        q.write('\n')
                                        q.write('Found %s in %s' % (gmk,s.strip()))
                                        q.write('\n')
                                       
                if s.startswith('!Series_summary'):
                    if gmk in s:
                        l = re.split(r'[;, ]', s)
                        for key2 in keywords:
                            key2 = key2.rstrip()
                            if key2 in s:
                                #print key2
                                if ((key2 in l) and (gmk in l)):
                                    #index = s.find(key2)
                                    #if (s[index-1].isalpha() or s[index+len(key2)+1].isalpha())==False:
                                   
                                    r = abs(l.index(key2) - l.index(gmk))
                                    if r<=6:
                                        q.write(file) 
                                        q.write('\n')
                                        q.write(key2)
                                        q.write('\n')
                                        q.write('Found %s in %s' % (gmk,s.strip()))
                                        q.write('\n')
                if s.startswith('!Series_overall_design'):
                    if gmk in s:
                        l = re.split(r'[;, ]', s)
                        for key2 in keywords:
                            key2 = key2.rstrip()
                            if key2 in s:
                                if ((key2 in l) and (gmk in l)): 
                                    #index = s.find(key2)
                                    #if (s[index-1].isalpha() or s[index+len(key2)+1].isalpha())==False:
                                   
                                    r = abs(l.index(key2) - l.index(gmk))
                                    if r<=6:
                                        q.write(file)
                                        q.write('\n')
                                        q.write(key2)
                                        q.write('\n')
                                        q.write('Found %s in %s' % (gmk,s.strip()))
                                        q.write('\n')
q.close()
print("--- %s seconds ---" % (time.time() - start_time))         
#        for s in sentences:
#            s = s.rstrip()
#            if s.startswith('!Series_title'):
#                if gmk in s:
#                    s = ' '.join(re.findall(r'\b(\w+)\b', s.lower())) #convert line to lower case
#                    for keyword in keywords:
#                        key2 = re.escape(keyword.rstrip()) # GS
#                        indexes = sorted((s.find(x), len(x)) for x in [gmk, key2]) #sort the strings based on length
#                 
#                        if all(i[0] != -1 for i in indexes) and len(s[indexes[0][0] + indexes[0][1] : indexes[-1][0]].split()) <= 5: # for details, see http://goo.gl/Y8PdTs
#                            print gmk, key2                            
#                            q.write('Found %s' % (s.strip()))
#                            q.write('\n')
#                                   
#            if s.startswith('!Series_summary'):
#                if gmk in s:
#                    s = ' '.join(re.findall(r'\b(\w+)\b', s.lower()))
#                    for keyword in keywords:
#                        key2 = re.escape(keyword.rstrip())
#                        indexes = sorted((s.find(x), len(x)) for x in [gmk, key2])
#               
#                        if all(i[0] != -1 for i in indexes) and len(s[indexes[0][0] + indexes[0][1] : indexes[-1][0]].split()) <= 5:
#                            print gmk, key2                            
#                            q.write('Found %s' % (s.strip()))
#                            q.write('\n')
#                        
#            if s.startswith('!Series_overall_design'):
#                if gmk in s:
#                    s = ' '.join(re.findall(r'\b(\w+)\b', s.lower()))
#                    for keyword in keywords:
#                        key2 = re.escape(keyword.rstrip())
#                        indexes = sorted((s.find(x), len(x)) for x in [gmk, key2])
#                    #    print key2
#                        if all(i[0] != -1 for i in indexes) and len(s[indexes[0][0] + indexes[0][1] : indexes[-1][0]].split()) <= 5:
#                            q.write('Found %s' % (s.strip()))
#                            q.write('\n')
q.close()
          
      
          
    
