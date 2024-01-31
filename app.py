from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

if __name__ == "__main__":
      app.run(debug=True)

@app.route("/")
def home():
    return render_template("index.html", title="Hello")

@app.route("/education_and_certification")
def education():
        return render_template("education.html", title= "Education and Certs!")

@app.route("/work_history")
def work_history():
      return render_template("work_history.html", title = "Work History!")