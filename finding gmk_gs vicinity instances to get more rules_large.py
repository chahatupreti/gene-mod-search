import os
import re
import time
start_time = time.time()
q=open('C:\Users\Krishna\Desktop\up down analysis for orgs\gmk_gs vicinity_large_new.txt','w')
a = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1
#print a
keywords = open('F:\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large gs's
#gmk = 'knockout'
def find_matches(s, gmk):
    r=0
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        filter(None, l)       # remove empty elements in the list                  
        for gs in keywords: # gene symbols
            #q.write(gs)
            #q.write('\n')            
            gs = gs.rstrip()     #remove lagging whitespace characters                   
            #q.write(gs)            
            #print gs
            #re.compile(gs)
            #print hg=hg+1
            if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches
                #print 'title'
                #print gs, gmk
                gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                gs1=filter(None, gs1)
                gs11=gs1[0]
                gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                gmk1=filter(None, gmk1)
                gmk11=gmk1[0]
                #print 'gmk is %s' % gmk
                #print 'l is %s' % l
                #print gs, gmk, l, s
                if any(l[i:i+len(gs1)]==gs1 for i in xrange(len(l)-len(gs1)+1)) and (any(l[i:i+len(gmk1)]==gmk1 for i in xrange(len(l)-len(gmk1)+1))): # this ensures that both gs and gmk are in l, as a unit(i.e. and in order) otherwise it was detecting things like 'beta c' from beta cells
                #if (gs1 in l) and (gmk1 in l):
                #if (gmk in s): # ensure both are in the list. sometimes, they are not because of some attached delimiters                                                                                                     
#                                    index = s.find(gs) #find index of the GS in the line
#                                    if (s[index-1].isalpha() or s[index+len(gs)+1].isalpha())==False: #see if the 2 characters preceding and succeeding the GS are not alphabets. this is imp because if they are, then we dont want it, cause it means the GS is within a word
                    r = abs(l.index(gs11) - l.index(gmk11)) # find distance between first character of gs and gmk
                    #print 'title %d' % r                                     
                    if r<=8:
                        q.write(file)
                        q.write('\n')
                        q.write(gs)
                        q.write (' r is %d ' % r)
                        q.write('\n')
                        q.write('Found %s in %s' % (gmk,s.strip()))
                        q.write('\n')
    
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
                    find_matches(s, gmk)                   
                if s.startswith('!Series_summary'):
                    find_matches(s, gmk)
                if s.startswith('!Series_overall_design'):
                    find_matches(s, gmk)
q.close()
print("--- %s seconds ---" % (time.time() - start_time))         
#        for s in sentences:
#            s = s.rstrip()
#            if s.startswith('!Series_title'):
#                if gmk in s:
#                    s = ' '.join(re.findall(r'\b(\w+)\b', s.lower())) #convert line to lower case
#                    for keyword in keywords:
#                        gs = re.escape(keyword.rstrip()) # GS
#                        indexes = sorted((s.find(x), len(x)) for x in [gmk, gs]) #sort the strings based on length
#                 
#                        if all(i[0] != -1 for i in indexes) and len(s[indexes[0][0] + indexes[0][1] : indexes[-1][0]].split()) <= 5: # for details, see http://goo.gl/Y8PdTs
#                            print gmk, gs                            
#                            q.write('Found %s' % (s.strip()))
#                            q.write('\n')
#                                   
#            if s.startswith('!Series_summary'):
#                if gmk in s:
#                    s = ' '.join(re.findall(r'\b(\w+)\b', s.lower()))
#                    for keyword in keywords:
#                        gs = re.escape(keyword.rstrip())
#                        indexes = sorted((s.find(x), len(x)) for x in [gmk, gs])
#               
#                        if all(i[0] != -1 for i in indexes) and len(s[indexes[0][0] + indexes[0][1] : indexes[-1][0]].split()) <= 5:
#                            print gmk, gs                            
#                            q.write('Found %s' % (s.strip()))
#                            q.write('\n')
#                        
#            if s.startswith('!Series_overall_design'):
#                if gmk in s:
#                    s = ' '.join(re.findall(r'\b(\w+)\b', s.lower()))
#                    for keyword in keywords:
#                        gs = re.escape(keyword.rstrip())
#                        indexes = sorted((s.find(x), len(x)) for x in [gmk, gs])
#                    #    print gs
#                        if all(i[0] != -1 for i in indexes) and len(s[indexes[0][0] + indexes[0][1] : indexes[-1][0]].split()) <= 5:
#                            q.write('Found %s' % (s.strip()))
#                            q.write('\n')

          
      
          
    
