#place this file in preprocess folder

import json
import subprocess
import argparse

#question = input("Enter your question: ")
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--question', default="")
args = arg_parser.parse_args()
question = args.question
print(question)
question_toks = question.split()

with open("./question.json","r+") as question_file:
    data = json.load(question_file)
    data = data[0]
    data['question'] = question
    data['question_toks'] = question_toks
    question_file.seek(0)
    question_file.truncate(0)
    json.dump([data], question_file, indent=4)

subprocess.call("./run.sh")
