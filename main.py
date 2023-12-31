from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from Posts import Projects



app = Flask(__name__)

all_projects = Projects


#print(all_projects)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=all_projects)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/show_project/<int:index>")
def show_project(index):
    requested_project = None
    for proj in all_projects:
        if proj["id"] == index:
            requested_project = proj
    return render_template("show_project.html", project=requested_project)



if __name__ == "__main__":
    app.run(debug=True)

