import flask
from flask import request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route('/status')
def status():
    return flask.jsonify({'msg': 'app running'})


@app.route('/public/hostname')
def public_hostname():
    with open('/etc/hostname') as fp:
        hostname = fp.readline()[:-1]
    return flask.jsonify({'hostname': hostname})


@app.route('/private/hostname')
def private_hostname():

    auth_header = request.headers.get('Authorization')
    if auth_header:
        pass
    else:
        return flask.jsonify({'msg': 'Authorization header not present'}), 401

    with open('/etc/hostname') as fp:
        hostname = fp.readline()[:-1]
    return flask.jsonify({'hostname': hostname})


# @app.route('/user/info')
# @oidc.accept_token(True, ['email', 'profile'])
# def user_info():
#     return flask.jsonify(g.oidc_token_info)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
