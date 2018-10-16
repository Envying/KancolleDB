import os
from webapp import app

# For Developers only
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Run without the SSL (GAE)
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

# Run with a SSL (Locally)
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8080, debug=True, ssl_context=('./ssl.crt', './ssl.key'))
