import json

webster_word_path = "out.csv" #not actually a csv, but a text file with one word per line
webster_path = "../../WebsterParser/output/dict.json"

with open(webster_path, "r") as f:
    data = json.load(f)

#Write keys of data dictionary to a csv
with open(webster_word_path, "w") as f:
    for key in data:
        f.write(key + "\n")