from itertools import count
maxsubstr = s[0:0]
for start in range(len(s)):
    for end in count(start + len(maxsubstr) + 1):
        substr = s[start:end]
        if len(substr) != (end - start): 
            break
        if sorted(substr) == list(substr):
            maxsubstr = substr
print 'Longest substring in alphabetical order is: ' + maxsubstr