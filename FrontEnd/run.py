from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app= Flask(__name__)
Bootstrap(app)

@app.route("/")
def view_qa_generation_page():
    return render_template("questionAnswerGenerator.html", title="Q&A Generator")

@app.route("/named-entity-recognition")
def view_ner_page():
    return render_template("ner.html", title="Named Entity Recognition")

@app.route("/manual-tagging")
def view_manual_tagging_page():
    return render_template("manualTagging.html", title="Manual Tagging")

@app.route("/gazeteers")
def view_gazetteers_page():
    return render_template("gazetteers.html", title="Gazetteers")

if __name__ =='__main__':
    app.run(debug=True)