def unique(source):
    sofar = {}
    for val in open(source):
      if not sofar.get(val):
        yield val.strip() # here val.strip creates a list of the words that constitute your match. without strip, yield wouldnt work as it needs to generate
        # a list. however, we use yield here because it works as one-time only, which is good for us.
        sofar[val] = 1
  
for lyne in unique("D:\M.Tech work\qfilter_output matches.txt"):
    print lyne        
