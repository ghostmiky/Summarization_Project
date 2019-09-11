# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:41:19 2019

@author: Malinda
"""

import run as sm
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

def verify_summarization_data(receivedData):
    if ('text' not in receivedData):
        return 300
    else:
        return 200


class summarize_api(Resource):
    def post(self):
        receivedData = request.get_json() # Receieve data
        status_code = verify_summarization_data(receivedData) # Verify data
        if (status_code != 200):
            returnJson = {
            	'msg': 'Invalid data',
                'status': 200
            }
            return jsonify(returnJson)
        text = receivedData['text']
       	text = f"""{text}"""
        text_tobe_summarized = text  
        try:
            bs = sm.base_summarize()
            res =bs.summarize(text_tobe_summarized)
        	#res =  run.base_summarize.summarize(text_tobe_summarized)# Summarize
            returnJson = {
            	'result': res,
            	'status': 200 
	        }
            return jsonify(returnJson) 
        except Exception as e:
        	returnJson = {
            	'msg': e,
            	'status': 500
        	}
        	return jsonify(returnJson)
        #return {'data':run.base_summarize.summarize(summarize_text)}

api.add_resource(summarize_api,'/summarize/')

if __name__ == '__main__':
    app.run()
    
# Home route
@app.route('/api')
def welcome():
    return 'Text Summarization & Grammar Checking API'