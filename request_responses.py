from flask import jsonify

#=== Request Responses ===#


RESPONSE_OK={"response":"OK"}
RESPONSE_NOK={"response":"NOK"}

#=== JSON Getters ===#

def get_RESPONSE_OK():
    return jsonify(RESPONSE_OK)

def get_RESPONSE_NOK():
    return jsonify(RESPONSE_NOK)

def is_RESPONSE_OK(response):
    return response==jsonify(RESPONSE_OK)

def is_RESPONSE_NOK(response):
    return response==jsonify(RESPONSE_NOK)

def get_response_from_Exception(Exception):
    return jsonify({"response":str(Exception)})