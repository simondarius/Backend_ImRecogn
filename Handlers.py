from flask import jsonify
import request_responses
import os 
IMAGE_ID=0
UPLOAD_FOLDER='/image_recognition_model/tmp'
def upload_handler(request,app):
    if(request.method=='POST'):
        if request.headers['Content-Type'].startswith('multipart/form-data'):
            
            
            photo = request.files['photo']
            
            if photo:
               if photo.filename == "":
                   raise Exception('ContentError: No selected photo, filename is null!')
 
               print('PHOTO DEBUG:')
               print(photo)
               try:
                   filename = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_photo{IMAGE_ID}.jpg')
                   IMAGE_ID+=1
                   print('SAVING TO '+filename)
                   photo.save(filename)
                   return request_responses.get_RESPONSE_OK()
               except Exception as e:
                    print(str(e))
                    return request_responses.get_RESPONSE_NOK() 
            else: raise Exception('ContentError: Invalid photo!')     
        else: raise Exception('ContentError: Wrong request content type in upload handler, should be \' multipart/form-data \' recieved \' '+request.headers['Content-Type']+'\' !')
    else: raise Exception('RequestError: Wrong request method in upload handler!')

def preflight_handler():
    
    response = jsonify({'message': 'Preflight request successful'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    return response         