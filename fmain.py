from flask import Flask,request,jsonify
from flask_cors import CORS

# ======= Config =======
app=Flask(__name__)




CORS(app, resources={r"/*": {"origins": "*","allow_headers":"*","methods":"*"}})


# ===== Back-end request handler =====

@app.route('/upload_image',methods=['POST','OPTIONS'])
def upload_request():
    print('ALIVE')
    # ==== Handle image post request ====
    if request.method=='OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        print('responeded to OPTIONS method')
        return response
    elif request.method=='POST':
        if request.is_json:
           login_data=request.json

           print('INCOMING POST METHOD!')
           
           return jsonify({'response':True})
        else :
           return jsonify({'response':'REQUEST NOT IN JSON FORMAT!'})
    else: return jsonify({'response':'Invalid method, cannot respond to method of type '+request.method+' !'})       


# ======= Main =======
if __name__=="__main__":
    app.run(debug=True)
    