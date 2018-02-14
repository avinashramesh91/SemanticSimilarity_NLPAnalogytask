from __future__ import division
import sys,json,math
import os
import numpy as np

def load_word2vec(filename):
    # Returns a dict containing a {word: numpy array for a dense word vector} mapping.
    # It loads everything into memory.
    
    w2vec={}
    with open(filename,"r") as f_in:
        for line in f_in:
            line_split=line.replace("\n","").split()
            w=line_split[0]
            vec=np.array([float(x) for x in line_split[1:]])
            w2vec[w]=vec
    return w2vec

def load_contexts(filename):
    # Returns a dict containing a {word: contextcount} mapping.
    # It loads everything into memory.

    data = {}
    for word,ccdict in stream_contexts(filename):
        data[word] = ccdict
    print "file %s has contexts for %s words" % (filename, len(data))
    return data

def stream_contexts(filename):
    # Streams through (word, countextcount) pairs.
    # Does NOT load everything at once.
    # This is a Python generator, not a normal function.
    for line in open(filename):
        word, n, ccdict = line.split("\t")
        n = int(n)
        ccdict = json.loads(ccdict)
        yield word, ccdict

def jaccard_sim_sparse(v1,v2):
    k1 = v1.keys()
    k2 = v2.keys()
    comm = set(k1).intersection(set(k2))
    p= len(comm)
    q=len(k1)
    r=len(k2)
    try:
     val = round(float(p/(p+q+r)),6)
     return val
    except:
     val = 0
     return val





def cossim_sparse(v1,v2):
    # Take two context-count dictionaries as input
    # and return the cosine similarity between the two vectors.
    # Should return a number beween 0 and 1
    ## TODO: delete this line and implement me
    #pass
    k1 = v1.keys()
    k2 = v2.keys()
    comm = set(k1).intersection(set(k2))
    if(len(comm)==0):
        return 0
    #print list(comm)
    vec1 = np.array([v1[k] for k in list(comm)])
    nv1 = np.array([v1[k] for k in k1])
    vec2 = np.array([v2[k] for k in list(comm)])
    nv2 = np.array([v2[k] for k in k2])

    dot= np.dot(vec1,vec2)
    #print dot

    ##normv1 = np.sqrt(abs(vec1.dot(vec1)))
    normv1 = np.sqrt(abs(nv1.dot(nv1)))

    #normv2 = np.sqrt(abs(vec2.dot(vec2)))
    normv2 = np.sqrt(abs(nv2.dot(nv2)))

    if(normv1==0 or normv2==0):
        return 0
    val = round(float(dot/(normv1*normv2)),6)
    #print val
    return val

def cossim_dense(v1,v2):
    # v1 and v2 are numpy arrays
    # Compute the cosine simlarity between them.
    # Should return a number between -1 and 1
    
    ## TODO: delete this line and implement me
    #pass
    dot = np.dot(v1, v2)
    # print dot
    normv1 = np.sqrt(abs(v1.dot(v1)))
    # print normv1
    normv2 = np.sqrt(abs(v2.dot(v2)))
    if (normv1 == 0 or normv2 == 0):
        return 0
    val = round(float(dot / (normv1 * normv2)), 6)
    # print val
    return val




def show_nearest(word_2_vec, w_vec, exclude_w, sim_metric):
    #word_2_vec: a dictionary of word-context vectors. The vector could be a sparse (dictionary) or dense (numpy array).
    #w_vec: the context vector of a particular query word `w`. It could be a sparse vector (dictionary) or dense vector (numpy array).
    #exclude_w: the words you want to exclude in the responses. It is a set in python.
    #sim_metric: the similarity metric you want to use. It is a python function
    # which takes two word vectors as arguments.

    # return: an iterable (e.g. a list) of up to 10 tuples of the form (word, score) where the nth tuple indicates the nth most similar word to the input word and the similarity score of that word and the input word
    # if fewer than 10 words are available the function should return a shorter iterable
    #
    # example:
    #[(cat, 0.827517295965), (university, -0.190753135501)]
    
    ## TODO: delete this line and implement me
    #pass
    exclude_w = list(exclude_w)
    #print exclude_w

    sim ={}
    for k,v in (word_2_vec.items()):
        if(k not in exclude_w):
            #print k
            sim[k] = sim_metric(w_vec,word_2_vec[k])

    tup = []
    for k, v in sorted(sim.items(),key=lambda(k,v):(v,k),reverse=True):
        #print k,v
        tup.append((k,v))

    if(len(tup)>=10):
        return tup[:10]

    #print tup
    return tup

# def main():
#     word_to_ccdict = load_contexts("nytcounts.university_cat_dog")
#     word_to_ccdict['cat']

if __name__ == '__main__':
    word_to_ccdict = load_contexts("nytcounts.university_cat_dog")
    #print word_to_ccdict['cat']
    #print word_to_ccdict['dog']
    #cossim_sparse(word_to_ccdict['cat'],word_to_ccdict['dog'])
    show_nearest(word_to_ccdict, word_to_ccdict['dog'], set(['dog']), cossim_sparse)
