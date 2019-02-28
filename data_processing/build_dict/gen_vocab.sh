#!/usr/bin/env bash
#Bulid Dictionary
python ./build_dict/build_dictionary.py ./data
trg_vocab_size=1000000
python ./build_dict/generate_vocab_from_json.py ./data.json ${trg_vocab_size} > ./vocab
rm -r ./data.json