# -*- coding: utf-8 -*-
import re
#rg7=open('/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/new rule occurence/gs_start.txt','w')
#rg8=open('/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/new rule occurence/effect_on.txt','w')
#rg9=open('/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/new rule occurence/in_wildtype.txt','w')
#rg10=open('/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/new rule occurence/here_we.txt','w')
#rg11=open('/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/new rule occurence/overall_with.txt','w')
#rg12=open('/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/new rule occurence/overall_with_others.txt','w')

#rg7=open(r'E:\F DRIVE\M.Tech\for assigning cl\new rule occurence\gs_start.txt','w')
#rg7_1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new rule occurence\gs_start1.txt','w')
#rg8=open(r'E:\F DRIVE\M.Tech\for assigning cl\new rule occurence\effect_on.txt','w')
#rg9=open(r'E:\F DRIVE\M.Tech\for assigning cl\new rule occurence\in_wildtype.txt','w')
#rg9_1=open(r'E:\F DRIVE\M.Tech\for assigning cl\new rule occurence\in_wildtype_summ.txt','w')
rg10=open(r'E:\F DRIVE\M.Tech\for assigning cl\new rule occurence\here_we.txt','w')
#rg11=open(r'E:\F DRIVE\M.Tech\for assigning cl\new rule occurence\overall_with.txt','w')
#rg12=open(r'E:\F DRIVE\M.Tech\for assigning cl\new rule occurence\overall_with_others.txt','w')

def cl(s1, gmk1, gs1, gs_list1, data1, file):
#    print s1
    gs11=gs1
#    br0=''
#    br3=''
#    br=''
    gs_list1.remove(gs1) # AS WE WANT TO USE THIS LIST FOR GETTING THE GS'S THAT ARE APART FROM THE CURRENT GS        
    s1 = re.sub(r'(\b(%s)\b)' % (gs1), r'_8MILLION8_', s1, flags=re.I) # inserts the token wherever there is GS. The \b before & after ensures this doesnt happen in between words
     
    gs1='_8MILLION8_'
#    l = s1.split()  # i switched from the complex split above to just space split to ensure that the splitters can be part of a rule 
#    for ii in range(0,len(data1)):
#        a = data1[ii]
#        lo = min(a[1], a[2])
#        hi = max(a[1], a[2])
#        brr = l[max(0, lo-6):hi+6]
#        br= " ".join(brr) 
#        br00 = l[max(0, lo):hi+1]  # we dont need the 8 words here and there as the fullstop is between gmk1 and gs1
#        br0= ' '.join(br00)
#        br33 = l[max(0, lo-3):hi+3] 
#        br3= ' '.join(br33)                    
#    print br3
    
#    if re.search(r'(^\W*(?:\w+\W+){0,6}%s\b)' %gs1, s1, re.I|re.S):
##        print 33
#        rg7.write(file)
#        rg7.write('\n')
#        rg7.write(gs11)
#        rg7.write('\n')
#        rg7.write('Found %s in %s' % (gs1,s1.strip()))
#        rg7.write('\n')
#        
#    s2=s1.split()
#    if gs1 in s2[:7]:
##        print 33
#        rg7_1.write(file)
#        rg7_1.write('\n')
#        rg7_1.write(gs11)
#        rg7_1.write('\n')
#        rg7_1.write('Found %s in %s' % (gs1,s1.strip()))
#        rg7_1.write('\n')
##        
#    if re.search(r'(effect of %s [^\.]*?on)' %gs1, s1):
#        rg8.write(file)
#        rg8.write('\n')
#        rg8.write(gs11)
#        rg8.write('\n')
#        rg8.write('Found %s in %s' % (gs1,s1.strip()))
#        rg8.write('\n')
#        
#    if re.search(r'(in wild([- ])?type (and|or) %s)' %gs1, s1) and (s1.startswith('!series_title') or s1.startswith('!series_overall_design')): # the ([- ])? between wild and type means it can match either 'wildtype' or 'wild type' or 'wild-type'. EXPLANATION -> ()? means whatever is inside is optional. the [- ] means the character can either be ' ' or '-'
##        print s1, gs1
##        print (2343423423)
#        rg9.write(file)
#        rg9.write('\n')
#        rg9.write(gs11)
#        rg9.write('\n')
#        rg9.write('Found %s in %s' % (gs1,s1.strip()))
#        rg9.write('\n')
#        
#    if re.search(r'(in wild([- ])?type (and|or) %s)' %gs1, s1) and not (s1.startswith('!series_title') or s1.startswith('!series_overall_design')):
##        print 34
#        rg9_1.write(file)
#        rg9_1.write('\n')
#        rg9_1.write(gs11)
#        rg9_1.write('\n')
#        rg9_1.write('Found %s in %s' % (gs1,s1.strip()))
#        rg9_1.write('\n')
#
    if re.search(r'([\.] here(,)? we[^\.]*?( |\()%s)' %gs1, s1) : # starts with a fullstop b/c the 'Here we' line should be a new one. the (,)? means the comma is optional so it can match both 'here we' and 'here, we'. the [^\.] means any character other than fullstop, b/c we want the GS in the same sentence. also the ( |\() is for allowing both space and '(' to occur before the GS because just space misses cases like (GS..)
#        print 34
        rg10.write(file)
        rg10.write('\n')
        rg10.write(gs11)
        rg10.write('\n')
        rg10.write('Found %s in %s' % (gs1,s1.strip()))
        rg10.write('\n')
#        
#    if re.search(r'(with (or|and) without %s)' %gs1, s1) and (s1.startswith('!series_overall_design')): # the or|and means it will match either of them
#        rg11.write(file)
#        rg11.write('\n')
#        rg11.write(gs11)
#        rg11.write('\n')
#        rg11.write('Found %s in %s' % (gs1,s1.strip()))
#        rg11.write('\n')
#
#    if re.search(r'(with (or|and) without %s)' %gs1, s1) and not (s1.startswith('!series_overall_design')):
#        rg12.write(file)
#        rg12.write('\n')
#        rg12.write(gs11)
#        rg12.write('\n')
#        rg12.write('Found %s in %s' % (gs1,s1.strip()))
#        rg12.write('\n')

def closedd():        
#    rg7.close()
#    rg7_1.close()
#    rg8.close()
#    rg9.close()
#    rg9_1.close()
    rg10.close()
#    rg11.close()
#    rg12.close()