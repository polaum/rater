from flask import Flask, request

from rater_func import User, ConsumptionException

app = Flask(__name__)


@app.route('/create_user', methods=['POST'])
def create_user():
    body = request.json
    user_id = int(body['user_id'])
    try:
        limit = body['limit']
    except:
        limit = None
    User(user_id, limit)
    return 'ok', 201


@app.route('/consume', methods=['POST'])
def consume():
    body = request.json
    user_id = body['user_id']
    add_cons = int(body['added_consumption'])
    user = User(user_id)
    try:
        user.consume(add_cons)
        return 'successfully consumed', 200
    except ConsumptionException:
        return 'User can\' consume that', 400



@app.route('/check_consumption', methods=['GET'])
def check_consumption():
    user_id = int(request.args.get('user_id'))
    user = User(user_id)
    return str(user.consumption), 200


@app.route('/check_limit', methods=['GET'])
def check_limit():
    user_id = int(request.args.get('user_id'))
    user = User(user_id)
    return str(user.limit), 200


if __name__ == '__main__':
    app.run()
