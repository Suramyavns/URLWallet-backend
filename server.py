'''
This is the main module for this server backend
'''
import os
from dotenv import load_dotenv
from flask import Flask,render_template,redirect,jsonify,request
from crud import add_url,get_url
from flask_cors import CORS
import argparse
from database import *

argparser = argparse.ArgumentParser()
load_dotenv()
apiKey = os.getenv('apiKey')
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET','POST'])
def root():
    '''
    This will return a simple html page showing no content here
    '''
    return render_template('no-content.html')

@app.route('/get_url',methods=['GET','POST'])
def fetch_url():
    '''
    This is fetch the URL from given id in request data if method is POST.
    Returns bad-request page for GET request on this API
    '''
    if request.headers.get('x-api-key')!=apiKey:
        return render_template('unauthorized.html')
    method = request.method
    if method=='POST':
        try:
            uuid = request.get_json()['uuid']
        except:
            return jsonify({'message':'Provide correct uuid!'}),400
        url = get_url(uuid)
        if url:
            return jsonify({'url':url}),201
        return jsonify({'message':'Invalid uuid!'}),400
    return render_template('bad-request.html')
@app.route('/add_url',methods=['GET','POST'])
def insert_url():
    '''
    This is add the given URL in request body if method is POST.
    Returns bad-request page for GET request on this API
    '''
    if request.headers.get('x-api-key')!=apiKey:
        return render_template('unauthorized.html')
    method = request.method
    if method=='POST':
        data = request.get_json()
        uuid = add_url(str(data['url']))
        if uuid:
            return jsonify({'uuid':uuid}),201
        return jsonify({"message":'Invalid url!'}),400
    return render_template('bad-request.html')

@app.route('/<string:uuid>',methods=['GET','POST'])
def go_to(uuid):
    '''
    This function will redirect the user to the correct URL
    '''
    url = get_url(uuid)
    if url:
        return redirect(url)
    return render_template('not-found.html')

if __name__=='__main__':
    init_db()
    argparser.add_argument("--debug",help='Run the app in debug mode',action='store_true')
    args = argparser.parse_args()
    app.run(debug=args.debug)
