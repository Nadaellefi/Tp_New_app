from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = [{"id": 1, "name": "Nada", "course": "Cloud Computing"}]
next_id = 2


@app.route("/")
def home():
    return render_template("index.html", students=students)


@app.route("/student")
def student():
    return render_template("student.html")


@app.route("/add", methods=["POST"])
def add():
    global next_id
    name = request.form.get("name", "").strip()
    course = request.form.get("course", "").strip()
    if name and course:
        students.append({"id": next_id, "name": name, "course": course})
        next_id += 1
    return redirect(url_for("home"))


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete(student_id):
    students[:] = [s for s in students if s["id"] != student_id]
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
