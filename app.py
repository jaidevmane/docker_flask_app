from flask import Flask,render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.sqlite3'
app.config['SECRET_KEY'] = "dlaks83jfal29rnf"
db = SQLAlchemy(app)

class student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)


@app.route('/')
def show_all():
    return render_template('show_all.html', student = student.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['email'] or not request.form['address']:
            flash('Please enter all the fields', 'error')
        else:
         
            db.session.add(student(name=request.form['name'], email=request.form['email'], address=request.form['address']))
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
            
    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug = True)