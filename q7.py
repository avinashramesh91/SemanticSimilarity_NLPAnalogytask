#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")

groups = {}
with open("word-test.v3.txt",'r') as f:
 f.readline()
 analogies = []
 count = 0
 grp = ""
 for line in f:
  line=line.strip()
  if line != "":
      if line.startswith(":"):
          if(len(analogies)>0):
              groups[grp] = analogies
          grp = line.split()[1]
          analogies = []
          #print grp
      else:
          analogies.append(line)
 groups[grp] = analogies

best = {}
for g in groups.keys():
    #print g
    #print groups
    best1 = 0
    best5 = 0
    best10 = 0
    N=len(groups[g])
    for line in groups[g]:
        words = line.split()
        #print words[0]+":"+words[1]+"::"+words[2]+":"+words[3]
        expected = words[2]
        w1 = word_to_vec_dict[words[0]]
        w2 = word_to_vec_dict[words[1]]
        w4 = word_to_vec_dict[words[3]]
        ret = distsim.show_nearest(word_to_vec_dict,
                                   w1 - w2 + w4,
                                   set([words[0], words[1], words[3]]),
                                   distsim.cossim_dense)
        #print "-------"
        for i in range(0,10):
            try:
             #print ret[i][0]
             if(ret[i][0]==expected):
                 #print ret[i][0]+" @ position "+str(i)
                 if(i==0):
                     best1+=1
                     best5+=1
                     best10+=1
                 if(i>0 and i<5):
                     best5+=1
                     best10+=1
                 if(i>=5 and i<=9):
                     best10+=1

             if(ret[0][0]==expected):
                 print "correct-"," group: ",g
                 print(" {} : {} :: {} : {}".format(words[0],words[1],ret[0][0],words[3]))

            except:
                print "10 elements not present"
        #print "-------"

    b1 = round(float(best1)/float(N),5)
    b2 = round(float(best5)/float(N),5)
    b3 = round(float(best10)/float(N),5)
    best[g] = [b1,b2,b3]


for x in best:
 print x,"\t",best[x]

    #print(" {} : {} :: {} : {}".format(words[0],words[1],ret[0][0],words[3]))


