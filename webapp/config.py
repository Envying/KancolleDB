# This is the config file for oauth2, setting variables
class Auth:
    CLIENT_ID = ('236022772111-r1ls58b9ps2vs6q7t1b4g2hr2nqf4jdm'
                 '.apps.googleusercontent.com')
    CLIENT_SECRET = 'gCfyefl41AhZzZK-8ok53efG'
# SLL host
    # REDIRECT_URI = 'https://127.0.0.1:8080/oAuthcallback'
# local host
    # REDIRECT_URI = 'https://localhost:8080/oAuthcallback'
# Google App Engine
    REDIRECT_URI = 'https://kancolledb-project.appspot.com/oAuthcallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']
