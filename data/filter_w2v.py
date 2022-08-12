from gensim.models import Word2Vec, KeyedVectors
import os
#Read each line in one file and print the number of lines in it

webster_word_path = "out.csv" #not actually a csv, but a text file with one word per line
w2v_path = "../../GoogleNews-vectors-negative300.bin"

with open(webster_word_path, "r") as f:
    r = f.readlines()

r_set = set([x.strip().lower() for x in r])

def webster_filter_func(w):
    key_gen = list(w.key_to_index.keys())
    for key in key_gen:
        if not key.lower() in r_set:
            del w.key_to_index[key]

def webster_or_100k_filter_func(w):
    key_gen = list(w.key_to_index.keys())
    count = 0
    for key in key_gen:
        count += 1
        #Top 100k words get a pass
        if count < 100000:
            continue
        if not key.lower() in r_set:
            del w.key_to_index[key]

def process_w2v(filename, w_filter_func):
    #Load full w2v
    w = KeyedVectors.load_word2vec_format(w2v_path, binary=True)
    
    #delete vecs we don't care about
    w_filter_func(w)

    #save it to text
    w.save_word2vec_format(filename + ".txt", binary=False)

    #Fix the incorrect line number in text
    with open(filename + ".txt", "r") as f:
        n_l = len(f.readlines())

    f = open(filename + ".txt", "r")
    first_line, remainder = f.readline(), f.read()
    f.close()
    t = open(filename + ".txt.fixed","w")
    t.write(str(n_l - 1) + " 300" + "\n")
    t.write(remainder)
    t.close()

    #Read the fixed model
    w = KeyedVectors.load_word2vec_format(filename + ".txt.fixed", binary=False)

    #Save it as a binary model
    w.save_word2vec_format(filename + ".bin", binary=True)

    #Remove intermediate files
    os.remove(filename + ".txt")
    os.remove(filename + ".txt.fixed")

process_w2v("webster_filtered_w2v", webster_filter_func)
process_w2v("webster_or_100k_filtered_w2v", webster_or_100k_filter_func)

#w.save_word2vec_format("webster_or_100k_filtered_w2v.txt", binary=False)

#read text file and count number of lines


#read text file and count number of lines
#with open("webster_or_100k_filtered_w2v.txt", "r") as f:
#    n_l = len(f.readlines())
#print(n_l)

#Now - you need to open the text file and change the number of lines to the following:



