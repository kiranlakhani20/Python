from requests_oauthlib.oauth2_session import OAuth2Session
from flask import Flask

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
