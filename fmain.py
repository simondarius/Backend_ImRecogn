from flask import Flask,request
from flask_cors import CORS
from request_responses import get_response_from_Exception
from Handlers import upload_handler,preflight_handler
# ======= Config =======
app=Flask(__name__)




CORS(app, resources={r"/*": {"origins": "*","allow_headers":"*","methods":"*"}})


# ===== Back-end request handler =====

@app.route('/upload_image',methods=['POST','OPTIONS'])
def upload_request():
    if request.method=='OPTIONS':
        return preflight_handler()
    else:
        try:
            return upload_handler(request,app)
        except Exception as e:
            return get_response_from_Exception(e) 


# ======= Main =======
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
    