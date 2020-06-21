import flask


app = flask.Flask(__name__)
@app.route("/node/index")
def index():
    return  "test nginx88"