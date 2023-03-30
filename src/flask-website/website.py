from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start(): 
    return render_template('start.html')
    
@app.route("/authentification")
def auth(): 
    return render_template('authentification.html')

@app.route("/list")
def liste():
    return render_template('list_server.html')

@app.route("/ajout")
def ajout():
    return render_template('ajout_server.html')

@app.route("/suppression")
def sup():
    return render_template('suppression_server.html')

@app.route("/list_users")
def liste_users():
    return render_template('list_users.html')


