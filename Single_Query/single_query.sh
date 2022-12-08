#!/bin/bash

model_path="./saved_model/best_model.model"
question=$1

cd preprocess

python3 ./single_query.py --question="${question}"

cd ..

python3 ./one.py

python3 ./src/eval.py --dataset ./data --vocab ./data/vocab.bin \
--beam_size 5 \
--model $model_path \
--batch_size 1 \
--sentence_features \

python3 sem2SQL.py --data_path "./data" --input_path "./lf_predict.json" --output_path output.txt
