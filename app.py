from flask import Flask, escape, request
from sensible.loginit import logger

app = Flask(__name__)
log = logger(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__": # pragma: no cover
    log.info("START Flask")
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    log.info("SHUTDOWN Flask")
    