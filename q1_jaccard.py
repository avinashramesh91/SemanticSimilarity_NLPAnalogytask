#!/usr/bin/env python
import distsim
word_to_ccdict = distsim.load_contexts("nytcounts.university_cat_dog")
print "Jaccard similarity between cat and dog" ,distsim.jaccard_sim_sparse(word_to_ccdict['cat'],word_to_ccdict['dog'])
print "Jaccard similarity between cat and university" ,distsim.jaccard_sim_sparse(word_to_ccdict['cat'],word_to_ccdict['university'])
print "Jaccard similarity between university and dog" ,distsim.jaccard_sim_sparse(word_to_ccdict['university'],word_to_ccdict['dog'])