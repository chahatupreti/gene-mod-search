import os
fname = "F:\M.Tech\gene list\mus musculus genes.txt"
d = 0
output = open(os.path.join('F:\M.Tech', 'mus musculus_other_designation_only.txt'),'w')
with open(fname) as f:
    next(f)    ## this helps us skip the first line which was like header, it said what was in the file
    for line in f:
        line = line.rstrip()
        split_the_line = line.split("\t");
      #  split_the_line = filter(None, split_the_line)
      #  print split_the_line;
        n = 0
        print d
        d = d+1
        
        #             SYMBOLS

        #output.write(split_the_line[5]);
        #output.write('\n');

               #     ALIASES
        
        # if split_the_line[6]:
        #     c = split_the_line[6].split(',');
     
        #     while n< len(c):

        #         output.write(c[n]);
        #         output.write('\n');
        #         n= n + 1;

                #	  DESCRIPTION	

        # if split_the_line[7] != None:	

        #    output.write(split_the_line[7]);
        #    output.write('\n');

				#  OTHER_DESIGNATION

        n = 0
        if (len(split_the_line) > 8) and (split_the_line[8]):
         
            other_desc_split = split_the_line[8].split('|');
       
            while n < len(other_desc_split):
                output.write(other_desc_split[n]);
              
                n = n + 1;
                output.write('\n');
##        
fname.close()
output.close()
