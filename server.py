from flask import Flask, request, render_template
import digit
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route('/test')
def hello():
    return "Hello World!"

@app.route('/rec')
def recogize():
    filename = request.args['file']
    imFile = digit.deploy(filename)
    response = "<image src='/static/output1.png' />"
    return response


@app.route('/')
def home():
    return render_template('frontPage.html')

@app.route('/api', methods=['POST'])
def api():
    file = request.files['file']
    print("Input Received:",file)
    imFile = digit.deployImg(file)
    response = "<image src='/static/output1.png' />"
    return response

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port="1000")
    # app.run()