from flask import Flask, request, render_template, flash, request, url_for, redirect, session
import queue
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:testing123@localhost:3306/MYFIRSTDATABASE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "thesecretness"

class Case:
    def __init__(self, case_id, case_name, case_type, staff_id,case_status,case_team):
        self.caseid = case_id
        self.casename = case_name
        self.casetype = case_type
        self.staffid = staff_id
        self.status = case_status
        self.team = case_team

id = 0
# ***---*** trying SQLAlchemy
db = SQLAlchemy(app)

class sers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

# ***---*** trying SQLAlchemy
@app.route('/register/', methods=['GET','POST'])
def register():
    try:
        if not request.json or not 'username' in request.json:
            return "Errors 400"

        user = request.json['username']
        session["user"] = user
        newser = sers(user , "")
        db.session.add(newser)
        db.session.commit()

        return "entry received "
        # input_id = request.json['id']
        # return "Success! recieved id: {}".format(input_id)

    except Exception as e:
        return str(e)


@app.route('/homeuser/', methods=['GET', 'POST'])
def homeuser():
    try:
        if "user" in session:
            user = session["user"]
            print (user + "from home user page")
            # return "<div>{{user}}</div>"
        else:
            return render_template("home.html")
    except Exception as e:
        return str(e)





@app.route('/')
def homepage():
    try:
        return render_template('home.html')
    except Exception as e:
        return str(e)


@app.route('/get', methods=['GET'])
def test_get():
    try:
        return "Success!"
    except Exception as e:
        return str(e)


@app.route('/post', methods=['POST'])
def test_post():
    try:
        global id
        id = id + 1
        if not request.json or not 'id' in request.json :
            return "Error 400"
        input_id = request.json['id']
        return "Success! recieved id: {}".format(input_id)
    except Exception as e:
        return str(e)


@app.route('/casecreation/', methods=['POST'])
def tes_post():
    try:
        global id
        id = id + 1
        if not request.json or not 'id' in request.json or not 'name' in request.json or not 'type' in request.json or not 'staff' in request.json:
            return "Error 400"
        newcase = Case(str(id), request.json['name'], request.json['type'], request.json['staff'], "c", "c")
        if request.json['type'] == 'hardware':
            newcase.team = 'hardware'
        elif request.json['type'] == 'software':
            newcase.team = 'sofware'
        else:
            return "the case type isn't valid"
        return ("your case has been created under the the number: " + str(newcase.caseid) + " by " + str(
            newcase.staffid) + ", and been asssigned to " + str(newcase.team) + " team.")
    except Exception as e:
        return str(e)

def caseidcounter():
    global id
    return id
    id = id + 1


#
if __name__ == "__main__":
    db.create_all
    app.run()

