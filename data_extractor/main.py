import en_core_web_sm
from flask import Flask
from flask import render_template
from flask import request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if 'jsondata' not in request.form:
        return jsonify({'result': 'NaN'})

    source_text = request.form['jsondata']
    content = source_text.strip()
    content = ' '.join(content.splitlines())

    nlp = en_core_web_sm.load()
    doc = nlp(content)
    result_entities = [(x.text, x.label_) for x in doc.ents]
    print(result_entities)
    result = {}
    for data, label in result_entities:
        if label not in result:
            result[label] = set()
        result[label].add(data)
    for label, data in result.items():
        result[label] = list(data)
    result['SOURCE'] = source_text

    return jsonify(result)
