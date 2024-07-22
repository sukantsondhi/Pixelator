## Only uncomment if needed
# import os
# os.environ['FLASK_APP'] = 'app.py'
# os.environ['FLASK_ENV'] = 'development'


from flask import Flask, render_template
from flask_restx import Api, Resource  

app = Flask(__name__)

## Uncomment to turn this into an API
# api = Api(app, version='1.0', title='Pixelator API',
#           description='A simple Pixelator API')

# ns = api.namespace('api', description='Pixelator operations')

@app.route('/')
def home():
    """"Server Home Page"""

    return "<h1>Welcome to the Pixelator App!</h1><p>This is the home page.</p>"

@app.route('/hello')
class HelloResource(Resource): 

    def get(self):
        """Returns a greeting"""
        return {"message": "Hello Pixelator App!"}

@app.route('/goodbye')
class GoodByeResource(Resource):
    def get(self):
        """"Returns a goodbye"""
        return {"message": "Bye Pixelator"}

if __name__ == '__main__':
    app.run(debug=True)