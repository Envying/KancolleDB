from webapp.config import Auth
from requests_oauthlib import OAuth2Session

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
