from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import digit
import bcrypt
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'db'
app.config['MONGO_URI'] = 'mongodb://0.0.0.0:27017/db'

mongo = PyMongo(app)


@app.route('/redirect_to_homepage', methods=['POST'])
def homepage():
    return render_template('index.html')


@app.route('/')
def index():
    if 'username' in session:
        return render_template('frontPage.html')  # 'You are logged in as ' + session['username']

    return render_template('index.html')


@app.route('/rec')
def recogize():
    filename = request.args['file']
    imFile = digit.deploy(filename)
    response = "<image src='/static/output1.png' />"
    return response


# @app.route('/')
# def home():
#     return render_template('frontPage.html')


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.CV_Cloud_login
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.CV_Cloud_login
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')


@app.route('/api', methods=['POST'])
def api():
    file = request.files['file']
    print("Input Received:", file)
    imFile = digit.deployImg(file)
    response = "<image src='/static/output1.png' />"
    return response


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')


@app.route('/delete', methods=['GET', 'POST'])  # function to delete existing account
def delete_item():
    users = mongo.db.CV_Cloud_login
    users.remove({'name': session['username']})
    return render_template('redirect_homepage.html')


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.debug = True
    app.run(host='0.0.0.0', port="1000")
    # app.run()