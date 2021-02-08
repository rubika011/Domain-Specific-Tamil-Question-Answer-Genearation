from flask import Flask, flash, render_template, request, redirect
from flask_bootstrap import Bootstrap
import processFile
import os

app= Flask(__name__)
Bootstrap(app)

app.config["FILE_UPLOADS"] = "C:\\Users\ASUS\PycharmProjects\QuestionAnswerGeneration\FrontEnd\\files"
app.config["ALLOWED_FILE_EXTENSIONS"] = ["PDF", "DOC", "TXT", "DOCX"]

def allowed_files(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/", methods=["GET", "POST"])
def view_qa_generation_page():
    if request.method == "POST":
        if request.files:
            file = request.files["file"]
            if allowed_files(file.filename):
                file.save(os.path.join(app.config["FILE_UPLOADS"], file.filename))

                with open(os.path.join(app.config["FILE_UPLOADS"], file.filename), encoding="utf-8") as f:
                    file_content = f.read()
                    processFile.processFile(file_content)
                return redirect(request.url)
            else:
                flash("The file uploaded is not supported by the application.")

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