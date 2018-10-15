from webapp import app

# Run without the SSL (GAE)
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8080, debug=True)

# Run with a SSL (Locally)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, ssl_context=('./ssl.crt', './ssl.key'))
