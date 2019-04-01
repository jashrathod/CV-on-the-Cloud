# from flask import Flask,request,make_response,render_template
# import digit
# import os
#
# app = Flask(__name__)
#
#
# @app.route('/test')
# def hello():
#     return "Hello World!"
#
# @app.route('/rec')
# def recogize():
#     filename =  request.args['file']
#     imFile = digit.deploy(filename)
#     response = "<image src='/static/output1.png' />"
# #     print("Res:",res)
#     return response
#
#
# @app.route('/')
# def home():
#     return render_template('frontPage.html')
#
# @app.route('/api', methods=['POST'])
# def api():
#     file = request.files['file']
#
# #     r = request
#     # convert string of image data to uint8
# #     nparr = np.fromstring(r.data, np.uint8)
#     # decode image
# #     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     print("Input Received:",file)
#     imFile = digit.deployImg(file)
#     response = "<image src='/static/output1.png' />"
# #     print("Res:",res)
#     return response
#     # do some fancy processing here....
#
#     # build a response dict to send back to client
# #     response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
# #                 }
#     # encode response using jsonpickle
# #     response_pickled = jsonpickle.encode(response)
#
# #     return Response(response=response_pickled, status=200, mimetype="application/json")
# #     return "File Read"
#
# if __name__ == '__main__':
#     app.debug = True
#     app.run(host = '0.0.0.0', port = 5015)
#     # app.run()
#
# # from shutil import copyfile
# # copyfile("output.png","static/outputx.png")
#



from flask import Flask, request, make_response, render_template
# import import_ipynb
import digit
import os
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)


@app.route('/test')
def hello():
    return "Hello World!"

@app.route('/rec')
def recogize():
    filename =  request.args['file']
    imFile = digit.deploy(filename)
    response = "<image src='/static/output1.png' />"
#     print("Res:",res)
    return response


@app.route('/')
def home():
    return render_template('frontPage.html')

@app.route('/api', methods=['POST'])
def api():
    file = request.files['file']

#     r = request
    # convert string of image data to uint8
#     nparr = np.fromstring(r.data, np.uint8)
    # decode image
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print("Input Received:",file)
    imFile = digit.deployImg(file)
    response = "<image src='/static/output1.png' />"
#     print("Res:",res)
    return response
    # do some fancy processing here....

    # build a response dict to send back to client
#     response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
#                 }
    # encode response using jsonpickle
#     response_pickled = jsonpickle.encode(response)

#     return Response(response=response_pickled, status=200, mimetype="application/json")
#     return "File Read"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port = "1000")
    # app.run()