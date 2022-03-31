from flask import Flask, jsonify, request  # import objects from the Flask model
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
app = Flask(__name__)  # define app using Flask

history = [{'content': 'i am feeling good about CoachAI', 'date': '03-30-2022', 'id': '1'},
          {'content': 'doing flask and its pretty cool', 'date': '03-30-2022', 'id': '2'}]


# NO PYTORCH
tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english")

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english")

pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)


@app.route('/', methods=['GET'])
def test():
    content = request.json['content']

    hasil = pipe(content)
    print(hasil[0]['label'])
    return jsonify({'message': content, 'sentiment': hasil[0]['label']})


@app.route('/history', methods=['GET'])
def returnAll():
    return jsonify({'history': history})


@app.route('/save', methods=['POST'])
def createTweet():
    content = request.json['content']
    hasil = pipe(content)

    message = {'content': content,
             'date': request.json['date'], 'id': request.json['id'], 'sentiment': hasil[0]['label']}

    history.append(message)
    return jsonify({'data': history})

if __name__ == '__main__':
    app.run(debug=True, port=8080)  # run app on port 8080 in debug mode
