def count_string_occurrence(org):
    f = open('organisms.txt','r')
    contents = f.read()
    f.close()
    #print  org,
    print contents.count(org)

read_f = open('unique organisms in 5k files.txt','r')
for line in read_f:
    count_string_occurrence(line)
read_f.close()
