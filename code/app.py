from flask import Flask, redirect, render_template, request,url_for 
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] =

db = SQLAlchemy(app) # create SQLALchemy object

@app.route("/") # The first page people will see on my project
def index():
    return render_template("index.html")

@app.route("/current_projects") # A list of ongoing 3d Prints
def current_projects():
    projects = project.query.all()
    tasks = task.query.all()
    connect = jointable.query.all()
    return render_template("current_projects.html", **locals())
    #projects = projects, tasks=tasks,connect=connect)

@app.route("/add_project", methods =["GET","POST"]) # Add a new 3d print
def add_project():
    error = ""
    form = projadd()
    if request.method == "POST":
        Task = form.name.data
        desc = form.description.data 
        if len(Task) == 0 :
            error = "Please supply a Project"
        else:
            nproj = project(name=Task,description = desc, staatus = False)
            db.session.add(nproj)
            db.session.commit()
            return redirect(url_for('current_projects'))
    return render_template("add_project.html", form = form, message = error)
@app.route("/deleteproj/<int:projid>")
def deletep(projid):
    todel = project.query.get(projid)
    db.session.delete(todel)
    db.session.commit()
    projarray = jointable.query.filter_by(project_id =projid).all()
    for proj in projarray:
        db.session.delete(proj)
        db.session.commit()
    return redirect( url_for('current_projects'))
@app.route("/deletetask/<int:taskid>")
def deletet(taskid):
    todel = task.query.get(taskid)
    db.session.delete(todel)
    db.session.commit()
    taskarray = jointable.query.filter_by(task_id =taskid).all()
    for ta in taskarray:
        db.session.delete(ta)
        db.session.commit()
    return redirect(url_for("current_tasks"))
@app.route("/current_tasks")
def current_tasks():
    projects = project.query.all()
    tasks = task.query.all()
    connect = jointable.query.all()
    return render_template("current_tasks.html", **locals())
@app.route("/add_new_task/<int:projid>", methods = ["GET","POST"]) # Add a new task for a print / several prints
def add_task(projid):
    error = ""
    form = taskadd()
    if request.method == "POST":
        Task = form.name.data
        details = form.details.data 
        if len(Task) == 0 :
            error = "Please supply a task"
        else:
            ntask = task(name=Task,details = details)
            db.session.add(ntask)
            db.session.commit()
            taskyidy = task.query.filter_by(name=Task).first()
            connect = jointable(project_id = projid, task_id = taskyidy.id )
            db.session.add(connect)
            db.session.commit()
            return redirect(url_for('current_projects'))
    return render_template("add_task.html", form = form, message = error)
@app.route("/update_project/<int:projid>", methods = ["GET","POST"]) # Update existing prints
def up_project(projid):
    error = ""
    form = projadd()
    entry = project.query.get(projid)
    if request.method == "POST":
        Task = form.name.data
        details = form.description.data
        if len(Task) == 0 :
            error = "Please supply a task"
        else:
            entry.name = Task
            entry.description = details
            db.session.commit()
            return redirect(url_for('current_projects'))
    return render_template('update_project.html', form=form, message=error)
@app.route("/projectincomplete/<int:projid>" , methods = ["GET","POST"])
def project_incomplete(projid):
    tasky = project.query.get(projid)
    tasky.staatus = False
    db.session.commit()
    return redirect(url_for("current_projects"))
@app.route("/projectcomplete/<int:projid>" , methods = ["GET","POST"])
def project_complete(projid):
    projecty = project.query.get(projid)
    projecty.staatus = True
    db.session.commit()
    return redirect(url_for("current_projects"))
@app.route("/update_task/<int:taskid>", methods =["GET","POST"]) # Update existing tasks
def up_task(taskid):
    error = ""
    form = taskadd()
    entry = task.query.get(taskid)
    if request.method == "POST":
        Task = form.name.data
        details = form.details.data
        progress = form.progress.data
        if len(Task) == 0 :
            error = "Please supply a task"
        else:
            entry.name = Task
            entry.details = details
            entry.progress = progress
            db.session.commit()
            return redirect(url_for('current_tasks'))
    return render_template('update_task.html', form=form, message=error)
@app.route("/taskincomplete/<int:taskid>", methods =["GET","POST"])
def task_incomplete(taskid):
    tasky = task.query.get(taskid)
    tasky.complete = False
    db.session.commit()
    return redirect(url_for("current_tasks"))

@app.route("/taskcomplete/<int:taskid>", methods = ["GET", "POST"])
def task_complete(taskid):
    projecty = task.query.get(taskid)
    projecty.complete = True
    db.session.commit()
    return redirect(url_for("current_tasks"))

@app.route("/gluetables/<int:projectid>/<int:taskid>", methods = ["GET","POST"])
def glue(projectid,taskid):
    joint = jointable(project_id = projectid, task_id = taskid)
    db.session.add(joint)
    db.session.commit()
    return redirect(url_for("current_tasks"))


# My Tables

class project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(60), nullable = True)
    staatus = db.Column(db.Boolean, nullable=False, default=False)
    connect = db.relationship('jointable', backref = 'projects')

class task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    details = db.Column(db.String(60), nullable = True)
    progress = db.Column(db.String(30), nullable = True, default = "Not Started") # Turn into drop down options?
    complete = db.Column(db.Boolean, nullable=False, default=False)
    connect = db.relationship('jointable', backref = "tasks")

class jointable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
    task_id = db.Column('task_id',db.Integer,db.ForeignKey('task.id'))

class projadd(FlaskForm):
    name = StringField("Project Name")
    description = StringField("Project Description ( optional)")
    submit = SubmitField("Submit")

class taskadd(FlaskForm):
    name = StringField("Task")
    details = StringField("Task Details ( optional)")
    progress = StringField("Task Progress ")
    submit = SubmitField("Submit")

if __name__=='__main__':
    app.run(debug=True)
