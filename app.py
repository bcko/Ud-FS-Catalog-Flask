import flask
from flask_dance.contrib.google import make_google_blueprint, google

''' how to run
export FLASK_APP=app.py
export FLASK_DEBUG = 1
flask run
'''

app = flask.Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?SX'
blueprint = make_google_blueprint(
    client_id="11010107052-vbclk01pda9beneni62dnj1556t3av24.apps.googleusercontent.com",
    client_secret="PjKlVpFymjkO1tt7w9viv9a9",
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")







@app.route("/")
def index():
    if not google.authorized:
        return flask.redirect(flask.url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["email"])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        flask.session['username'] = flask.request.form['username']
        return flask.redirect(flask.url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    flask.session.pop('username', None)
    return flask.redirect(flask.url_for('index'))



@app.errorhandler(404)
def not_found(error):
	return "page not found"