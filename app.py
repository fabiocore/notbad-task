from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def notbad():
    if request.method == 'POST' and bool(request.headers.get("NotBad")):
            message = "ReallyNotBad"
            return message
    else:
        return "<h1>hmmm... not bad but, try setting a magical header and use post method. :)</h1>"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5080))
    app.run(debug=True, host='0.0.0.0', port=port)
