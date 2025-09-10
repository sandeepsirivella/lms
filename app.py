from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory "database"
courses = ["Math", "Science", "History"]
enrolled = []

@app.route("/")
def home():
    return render_template("index.html", courses=courses, enrolled=enrolled)

@app.route("/add", methods=["POST"])
def add_course():
    name = request.form.get("course")
    if name and name not in courses:
        courses.append(name)
    return redirect(url_for("home"))

@app.route("/enroll/<course>")
def enroll(course):
    if course not in enrolled:
        enrolled.append(course)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
