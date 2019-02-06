#!compute-api/bin/python
from flask import Flask, jsonify, make_response, request
from arithmetic import Arithmetic

app = Flask(__name__)

@app.route('/')
def index():
	return make_response(jsonify({
			'status': 'success',
			'message': 'Welcome to compute API'
		}), 200)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({ 
			'status': 'error',
			'message': 'Not found' 
		}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({ 
    		'status': 'error',
    		'message': 'Bad request' 
    	} ), 400)

class Arithmetic():
	@app.route('/compute/arithmetic/add', methods = ['POST'])
	def add():
		if not request.json: abort(400)
		return jsonify({
			'status': 'success',
			'result': request.json['a'] + request.json['b']
		}), 200

if __name__ == '__main__':
	app.run(debug = True)