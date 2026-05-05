<<<<<<< HEAD
from flask import Flask, render_template, request
=======
from flask import Flask, render_template
>>>>>>> 4ceb07c (clean flask portfolio setup)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

<<<<<<< HEAD
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    sent = False

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print(f"{name} - {email}: {message}")
        sent = True

    return render_template("contact.html", sent=sent)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
=======
if __name__ == "__main__":
    app.run()
>>>>>>> 4ceb07c (clean flask portfolio setup)
