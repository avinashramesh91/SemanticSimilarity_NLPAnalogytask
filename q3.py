#!/usr/bin/env python
import distsim

# you may have to replace this line if it is too slow 
word_to_ccdict = distsim.load_contexts("nytcounts.4k")


### provide your answer below

###Answer examples
print "name : michael"
ret = distsim.show_nearest(word_to_ccdict, word_to_ccdict['michael'],set(['michael']),distsim.cossim_sparse)
print ret
print "nearest : ",ret[0][0],"\n"

print "common noun : woman"
ret = distsim.show_nearest(word_to_ccdict, word_to_ccdict['she'],set(['she']),distsim.cossim_sparse)
print ret
print "nearest : ",ret[0][0],"\n"

print "adjective : large"
ret = distsim.show_nearest(word_to_ccdict, word_to_ccdict['large'],set(['large']),distsim.cossim_sparse)
print ret
print "nearest : ",ret[0][0],"\n"

print "verb : injured"
ret = distsim.show_nearest(word_to_ccdict, word_to_ccdict['injured'],set(['injured']),distsim.cossim_sparse)
print ret
print "nearest : ",ret[0][0],"\n"
