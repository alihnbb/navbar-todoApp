from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
#from flask_mysqldb import MySQL
#from wtforms import Form,StringField,PasswordField,validators
#from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/alihn/Desktop/Python/ToDoApp/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos =Todo.query.all()
    return render_template("index.html", todos=todos)
@app.route("/archieve",methods=["POST","GET"])
def archieve():
    todos =Todo.query.all()
    return render_template("archieve.html", todos=todos)
@app.route("/complete/<string:id>")
def CompleteTodo(id):
    todo= Todo.query.filter_by(id = id).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/back/<string:id>")
def BackTodo(id):
    todo= Todo.query.filter_by(id = id).first()
    todo.complete =False
    db.session.commit()

    return redirect(url_for("index"))
@app.route("/delete/<string:id>")
def Delete(id):
    todo= Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))
@app.route("/archieve/<string:id>")
def Archieve1(id):
    todo= Todo.query.filter_by(id=id).first()
    todo.archieve = True
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/geri/<string:id>")
def Geri(id):
    todo= Todo.query.filter_by(id = id).first()
    todo.archieve = False
    db.session.commit()
    return redirect(url_for("archieve"))

@app.route("/add",methods=["POST"])
def addTodo():
    title = request.form.get("title")
    newTodo = Todo(title=title,complete=False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)
    archieve = db.Column(db.Boolean, default=False)
@app.route("/about")
def about():
    return render_template("about.html",ali=5)



if __name__ == "__main__":
    app.run(debug=True)

