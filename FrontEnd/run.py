import tamil
from PyPDF2 import PdfFileReader
from flask import Flask, flash, render_template, request, redirect
from flask_bootstrap import Bootstrap
import processFile, os
from FrontEnd import crf_impl

app= Flask(__name__)
Bootstrap(app)

app.config["FILE_UPLOADS"] = "C:\\Users\ASUS\PycharmProjects\QuestionAnswerGeneration\FrontEnd\\files"
app.config["TXT_CONVERSION_FILE_PATH"] = "C:\\Users\ASUS\PycharmProjects\QuestionAnswerGeneration\FrontEnd\\files\pdftotxtconversion.txt"
app.config["ALLOWED_FILE_EXTENSIONS"] = ["pdf", "doc", "txt", "docx"]
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['QUESTION_ANSWER_FILE_PATH'] = "C:\\Users\ASUS\PycharmProjects\QuestionAnswerGeneration\FrontEnd\\files\questionanswers.txt"
app.config["MAX_IMAGE_FILESIZE"] = 10 * 1024 * 1024

def allowed_files(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]
    if ext.lower() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

def readpdffile(file):
    pdf = PdfFileReader(file)
    with open(app.config['TXT_CONVERSION_FILE_PATH'], 'w', encoding="utf-8") as f:
        for page_num in range(pdf.numPages):
            # print('Page: {0}'.format(page_num))
            pageObj = pdf.getPage(page_num)

            try:
                txt = pageObj.extractText()
                print(''.center(100, '-'))
            except:
                pass
            else:
                f.write('Page {0}\n'.format(page_num + 1))
                f.write(''.center(100, '-'))
                f.write(txt)
        f.close()

def readtxtfile(filename):
    with open(os.path.join(app.config["FILE_UPLOADS"], filename), encoding="utf-8") as f:
        file_content = f.read()
        flash('File uploaded successfully. Please review content before generating Q&A.', 'success')
        return file_content

@app.route("/", methods=["GET", "POST"])
def view_qa_generation_page():
    file_content = ""
    generatedQAs = ""
    if request.method == "POST":
        if request.form['submitBtn'] == 'uploadFile':
            crf_impl.trainandtest()
            if request.files:
                file = request.files["upload-file"]
                if allowed_files(file.filename):
                    ext = file.filename.rsplit(".", 1)[1].lower()
                    file.save(os.path.join(app.config["FILE_UPLOADS"], file.filename))
                    if ext == 'pdf':
                        readpdffile(file)
                        file_content = readtxtfile('pdftotxtconversion.txt')
                        file_content = tamil.txt2unicode.auto2unicode(file_content)
                    else:
                        file_content = readtxtfile(file.filename)

                else:
                    flash('The file uploaded is not supported by the application.', 'danger')

        elif request.form['submitBtn'] == 'generateQA':
            file_content = request.form['textContent']
            processFile.processfile(file_content, app.config['QUESTION_ANSWER_FILE_PATH'])
            with open(app.config["QUESTION_ANSWER_FILE_PATH"], encoding="utf-8") as f:
                generatedQAs = f.read()

    return render_template("questionAnswerGenerator.html", content=file_content, questionAnswers=generatedQAs)

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