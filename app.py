from flask import Flask, render_template

app = Flask(__name__)

@app.route("/About_me")
def home():
    return render_template("index.html", title="Hello")

@app.route("/education_and_certification")
def education():
        return render_template("education.html", title= "Education and Certs!")

@app.route("/work_history")
def work_history():
      return render_template("work_history.html", title = "Work History!")