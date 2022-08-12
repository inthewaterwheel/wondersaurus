from flask import Flask, jsonify, request
from gensim.models import KeyedVectors
import json

app = Flask(__name__, static_folder='static')
app.debug = True

path_to_model = "../data/webster_or_100k_filtered_w2v.bin"
w = KeyedVectors.load_word2vec_format(path_to_model, binary=True)

# You can probably comment out both the path_to_thesaurus and path_to_dictionary sections
# They're not being used rn!

path_to_thesaurus = "../data/out.csv"
with open(path_to_thesaurus, "r") as f:
    r_set = set(f.readlines())

path_to_dictionary = "../data/dict_plain.json"
with open(path_to_dictionary, "r") as f:
    dictionary = json.load(f)

dictionary = {x.lower():y for x, y in dictionary.items()}

def in_thesaurus(word):
    return word.lower() in w.vocab

@app.route("/dict/<word>")
def get_word_definition(word):
    return dictionary[word.lower()].replace("\n", "<br>")

@app.route("/neighbors", methods=['POST'])
def neighbors():
    #read request body json
    json_data = request.get_json()

    #read weighted_words and construct w2v array
    pos_array = []
    pos_words = json_data['pos_words']
    for key in pos_words:
        pos_array.append((key, pos_words[key]))

    neg_array = []
    neg_words = json_data['neg_words']
    for key in neg_words:
        neg_array.append((key, neg_words[key]))

    #get results
    similar_words = w.most_similar(positive=pos_array, negative=neg_array, topn=500)

    #let's convert this to a nicer output
    output = []
    for word in similar_words:
        output.append({'word': word[0], 'score': word[1], 'thesaurus': true})
    
    #jsonify output and return
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
    print(app.instance_path)