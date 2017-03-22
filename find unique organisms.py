def unique(source):
    sofar = {}
    for val in open(source):
      if not sofar.get(val):
        yield val.strip()
        sofar[val] = 1
  
for lyne in unique("organsims.txt"):
    print lyne        
