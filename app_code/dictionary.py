from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open('./static/dictionary.json') as f:
    dictionary_data = json.load(f)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/search")
def search_form():
    return render_template('search_form.html')

@app.route("/meaning")
def meaning():

    word = request.args.get('word')
    word = word.lower()
    if word in dictionary_data:
        meaning = dictionary_data[word]

        return render_template('meaning.html',
                           word = word,
                           meaning = meaning)
    else:
        return render_template('meaning_not_found.html',
                               word=word)

@app.errorhandler(404)
def page_nt_found(e):
    return render_template('404.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
