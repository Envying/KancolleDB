class Auth:
    CLIENT_ID = ('236022772111-r1ls58b9ps2vs6q7t1b4g2hr2nqf4jdm'
                 '.apps.googleusercontent.com')
    CLIENT_SECRET = 'gCfyefl41AhZzZK-8ok53efG'
    REDIRECT_URI = 'http://localhost:8080/oAuthcallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']
