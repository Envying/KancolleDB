from requests_oauthlib import OAuth2Session

# This is the config file for oauth2, setting variables
class Auth:
    CLIENT_ID = ('236022772111-r1ls58b9ps2vs6q7t1b4g2hr2nqf4jdm'
                 '.apps.googleusercontent.com')
    CLIENT_SECRET = 'gCfyefl41AhZzZK-8ok53efG'
# SLL host
    REDIRECT_URI = 'https://127.0.0.1:8080/oAuthcallback'
# local host
    # REDIRECT_URI = 'https://localhost:8080/oAuthcallback'
# Google App Engine
    # REDIRECT_URI = 'https://kancolledb-project.appspot.com/oAuthcallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']


# Defining a method, and setting tokens and states
def get_google_auth(state=None, token=None):
    if token:
        return OAuth2Session(Auth.CLIENT_ID, token=token)
    if state:
        return OAuth2Session(
            Auth.CLIENT_ID,
            state=state,
            redirect_uri=Auth.REDIRECT_URI)
    oauth = OAuth2Session(
        Auth.CLIENT_ID,
        redirect_uri=Auth.REDIRECT_URI,
        scope=Auth.SCOPE)
    return oauth

from webapp import login_manager
from webapp.models import User

# Loading the users id oject to check if user is autheticated
@login_manager.user_loader
def get_user(id):
    return User.query.get(id)
