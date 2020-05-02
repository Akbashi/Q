from flask import Flask, render_template, flash, request, url_for, redirect, session
import queue

app = Flask(__name__)
@app.route('/')

def homepage():

    try:

        return render_template("home.html")

    except Exception as e:
        return str(e)





if __name__ == "__main__":
    app.run()