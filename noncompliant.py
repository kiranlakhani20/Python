from requests_oauthlib.oauth2_session import OAuth2Session
from flask import Flask

from flask import Flask, request, send_from_directory

from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)

@app.route('/example')
def log():
    data = request.args.get("data")
    app.logger.critical("%s", data)  # Noncompliant
    return 'Logged: ' + data

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


app = Flask('example')

@app.route('/example')
def example():
    my_file = request.args['my_file']
    return send_file("static/%s" % my_file, as_attachment=True) # Noncompliant
    

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "secretkey"  # Noncompliant

scope = ['https://www.api.example.com/auth/example.data']

oauth = OAuth2Session(
    'example_client_id',
    redirect_uri='https://callback.example.com/uri',
    scope=scope)

token = oauth.fetch_token(
        'https://api.example.com/o/oauth2/token',
        client_secret='example_Password') # Noncompliant


import xml.sax

parser = xml.sax.make_parser()
myHandler = MyHandler()
parser.setContentHandler(myHandler)
parser.setFeature(feature_external_ges, True) # Noncompliant
parser.parse('xxe.xml')
