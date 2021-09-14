import flask, time

app = flask.Flask(__name__)


@app.route("/")
def index():
    name = "SPM Rejects"

    return "Welcome!!! " + name + " ",time.localtime
