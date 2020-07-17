import flask
from flask import Flask, g
from flask_oidc import OpenIDConnect

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': 'a12ecbf6-b954-4059-95d3-24a8a4909995',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_VALID_ISSUERS': ['http://keycloak:8080/auth/realms/flask-demo'],
    'OIDC_OPENID_REALM': 'http://keycloak:5000/oidc_callback'
})
oidc = OpenIDConnect(app)


@app.route('/')
def hello_world():
    if oidc.user_loggedin:
        return ('Hello, %s, <a href="/private">See private</a> '
                '<a href="/logout">Log out</a>') % \
            oidc.user_getfield('email')
    else:
        return 'Welcome anonymous, <a href="/private">Log in</a>'


@app.route('/private')
@oidc.require_login
def hello_me():
    info = oidc.user_getinfo(['email', 'openid_id'])
    return ('Hello, %s (%s)! <a href="/">Return</a>' %
            (info.get('email'), info.get('openid_id')))


@app.route('/api/user/info')
@oidc.accept_token(True, ['email', 'profile'])
def user_info():
    return flask.jsonify(g.oidc_token_info)


@app.route('/logout')
def logout():
    oidc.logout()
    return 'Hi, you have been logged out! <a href="/">Return</a>'


if __name__ == '__main__':
    app.run('localhost', port=5000)
