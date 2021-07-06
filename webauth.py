from flask import Flask, request, redirect
import os
from pymongo import MongoClient as MC

D = os.environ.get('DB_URL')
BOT = os.environ.get('BOT_NAME')
c = MC(D)['anibot']
AUTH_USERS = c.get_collection('AUTH_USERS')
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "API is working fine"


@app.route('/anilist')
def add_auth():
    k = AUTH_USERS.insert_one({'code': request.args['code'], 'id': 'pending'})
    return redirect(f'https://telegram.me/{BOT}?start=code_{str(k.inserted_id)}', code=302)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))