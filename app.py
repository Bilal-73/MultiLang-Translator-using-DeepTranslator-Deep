from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

LANGUAGES = ["english", "german", "french", "spanish", "italian", "hindi"]

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        text = request.form.get('text')
        src_lang = request.form.get('src_lang')
        tgt_lang = request.form.get('tgt_lang')

        if not text:
            translated_text = "Please enter some text."
        elif src_lang == tgt_lang:
            translated_text = "Source and target languages must be different."
        else:
            try:
                translated_text = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
            except Exception as e:
                translated_text = f"Error during translation: {str(e)}"

    return render_template('index.html', languages=LANGUAGES, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
