from flask import Flask, request
import numpy as np
import pandas as pd
import os

from transformers import AutoTokenizer
from transformers import pipeline
from transformers import TFAutoModelForQuestionAnswering

summarizer_model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=summarizer_model_name)

question_answering_model_name = "deepset/roberta-base-squad2"

qa_model = TFAutoModelForQuestionAnswering.from_pretrained(question_answering_model_name)
tokenizer = AutoTokenizer.from_pretrained(question_answering_model_name)

qa = pipeline("question-answering", model=qa_model, tokenizer=tokenizer)
app = Flask(__name__)

guidesfile = pd.read_excel('./data/Flower_and_Plant_Care_Data.xlsx')

guides = guidesfile['CareGuide'].to_list()

for i, g in enumerate(guides):
    guides[i] = guides[i].replace('\n', ' ')

guidesfile['CareGuide'] = guides

@app.get('/api/summarize')
def summarize():

    print("Summarizing...")
    args = request.args

    plant_name = args.get('plant_name')

    if not guidesfile['Name'].str.contains(plant_name.lower()).any():
        return 'plant not found ', 404

    row = guidesfile.loc[guidesfile['Name'] == plant_name]

    summarization = summarizer(str(row['CareGuide'].values), max_length=300, min_length=200, do_sample=False)[0].get('summary_text')
    
    return summarization

@app.get('/api/question')
def question():
    args = request.args
    plant_name = args.get('plant_name')
    question = args.get('question')

    if len(question) < 0:
        return 'no question', 400


    if not guidesfile['Name'].str.contains(plant_name.lower()).any():
        return 'plant not found ', 404

    row = guidesfile.loc[guidesfile['Name'] == plant_name]


    question_input = {
        "question": question,
        "context": str(row['CareGuide'].values)
    }

    response = qa(question_input)


    return response['answer'], 200

if __name__ == '__main__':
    app.run()