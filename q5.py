#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
###Provide your answer below

###Answer examples
print "name : michael"
ret = distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['michael'],set(['michael']),distsim.cossim_dense)
print ret
print "nearest : ",ret[0][0],"\n"

print "common noun : woman"
ret = distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['she'],set(['she']),distsim.cossim_dense)
print ret
print "nearest : ",ret[0][0],"\n"

print "adjective : large"
ret = distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['large'],set(['large']),distsim.cossim_dense)
print ret
print "nearest : ",ret[0][0],"\n"

print "verb : injured"
ret = distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['injured'],set(['injured']),distsim.cossim_dense)
print ret
print "nearest : ",ret[0][0],"\n"

