
# THIS CODE FINDS UNIQUE GENE SYMBOLS FROM A LIST OF SYMBOLS, MANY OF WHICH MAY MAY BE REPEATED
def unique(source):
    sofar = {}
    for val in open(source):
      if not sofar.get(val):
        yield val.strip() # here val.strip creates a list of the words that constitute your match. without strip, yield wouldnt work as it needs to generate
        # a list. however, we use yield here because it works as one-time only, which is good for us.
        sofar[val] = 1
  
for lyne in unique("F:\M.Tech\org segregated\mus musculus\zaq\mouse_keywords123_1.txt"):
    print lyne        
