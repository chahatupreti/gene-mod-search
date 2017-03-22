import re
a=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\hrr with shortcuts.txt').readlines()
# a=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\etc.txt').readlines()
for line in a:
	a1='%s'
	aa='gene'
	part=''
	
	part = re.sub(re.escape(aa), a1, line, flags=re.I)
	

	if '{space/hyphen}' in part:
		a2='[- ]'
		part = re.sub('{space/hyphen}', a2, part, flags=re.I)

	if '{space/hyphen/nothing}' in part:
		a2='[- ]?'
		part = re.sub('{space/hyphen/nothing}', a2, part, flags=re.I)
	

	UptoN = re.search(r'{\.\.\.upto (\d) words\.\.\.}', part)
	if UptoN:
		# print (part)
		number=UptoN.group(1)
		number=int(number)
		a3='([\w]+\s*){0,%d}'%number
		part = re.sub(UptoN.group(0), a3, part, flags=re.I)


	UptoN_char = re.search(r'{\.\.\.upto (\d) CHARACTERS\.\.\.}', part)
	if UptoN_char:
		# print (3434)
		number=UptoN_char.group(1)
		number=int(number)
		a3='([\w]+\s*){0,%d}'%number
		part = re.sub(UptoN_char.group(0), a3, part, flags=re.I)	
		# print (part)	
	
	
	
	part=part.rstrip()
	# print (part)
	rule=''
	rule='if re.search(r'+'\''+part+'\''+' %gs1, br3, re.I|re.S)' # this is just a string assignment
	print (rule)
	# break