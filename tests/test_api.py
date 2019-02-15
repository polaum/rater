import requests


# @pytest.fixture(scope='session')
# def start_api():
#     p = Process(target=app.run)
#     p.start()
#     yield  # run tests
#     p.kill()


def test_api_create_valid_user_with_limit():
    response = requests.post('http://localhost:5000/create_user', json={'user_id': 1, 'limit': 5})
    assert response.status_code == 201
    assert response.text == 'ok'


def test_api_create_valid_user_without_limit():
    response = requests.post('http://localhost:5000/create_user', json={'user_id': 2})
    assert response.status_code == 201
    assert response.text == 'ok'


def test_api_check_consumption():
    response = requests.get('http://localhost:5000/check_consumption', params={'user_id': 1})
    assert response.status_code == 200
    assert response.text == '0'


def test_api_check_limit():
    response = requests.get('http://localhost:5000/check_limit', params={'user_id': 1})
    assert response.text == '5'


def test_api_check_without_limit():
    response = requests.get('http://localhost:5000/check_limit', params={'user_id': 2})
    assert response.text == 'None'


def test_api_create_same_user():
    requests.post('http://localhost:5000/create_user', json={'user_id': 1, 'limit': 10})
    response = requests.get('http://localhost:5000/check_limit', params={'user_id': 1})
    assert response.status_code == 200
    assert response.text == '5'


def test_api_create_same_user_without_limit():
    requests.post('http://localhost:5000/create_user', json={'user_id': 2, 'limit': 10})
    response = requests.get('http://localhost:5000/check_limit', params={'user_id': 2})
    assert response.status_code == 200
    assert response.text == 'None'


def test_api_consume():
    response = requests.post('http://localhost:5000/consume', json={'user_id': 1, 'added_consumption': 4})
    assert response.status_code == 200
    response2 = requests.get('http://localhost:5000/check_consumption', params={'user_id': 1})
    assert response2.text == '4'
    response3 = requests.post('http://localhost:5000/consume', json={'user_id': 1, 'added_consumption': 2})
    assert response3.status_code == 400
    assert response3.text == 'User can\'t consume that'
    response4 = requests.get('http://localhost:5000/check_consumption', params={'user_id': 1})
    assert response4.text == '4'
    response5 = requests.post('http://localhost:5000/consume', json={'user_id': 1, 'added_consumption': 1})
    assert response5.status_code == 200
    response6 = requests.get('http://localhost:5000/check_consumption', params={'user_id': 1})
    assert response6.text == '5'
