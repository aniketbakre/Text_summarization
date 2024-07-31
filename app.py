from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import pipeline, BartForConditionalGeneration, BartTokenizer

app = Flask(__name__)
CORS(app)

# Load the tokenizer and model
model_dir = r"C:\Users\anikbakr\Desktop\Project\Text_Summarization\model\checkpoint-2760"

tokenizer = BartTokenizer.from_pretrained(r"C:\Users\anikbakr\Desktop\Project\Text_Summarization\model")
model = BartForConditionalGeneration.from_pretrained(r"C:\Users\anikbakr\Desktop\Project\Text_Summarization\model")

# Load the summarization pipeline
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return jsonify(summary[0]['summary_text'])

@app.route('/keywords', methods=['POST'])
def keywords():
    data = request.json
    text = data.get('text', '')
    # Implement keyword extraction logic here
    # For simplicity, let's return dummy keywords
    keywords = ["keyword1", "keyword2", "keyword3"]
    return jsonify(keywords)

if __name__ == '__main__':
    app.run(debug=True)
