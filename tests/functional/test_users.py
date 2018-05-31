api_prefix = "/api/v1/"

def test_login_page(test_client):
    response = test_client.get(api_prefix+'/login')
    assert response.status_code == 200
    response = test_client.post(api_prefix+'/login')
    assert response.status_code == 201
    assert b"email" in response.data
    assert b"password" in response.data

def test_valid_signup_page(test_client):
    response = test_client.get(api_prefix+'/signup')
    assert response.status_code == 200
    response = test_client.post(api_prefix+'/signup')
    assert response.status_code == 201
    assert b"firstname" in response.data
    assert b"lastname" in response.data
    assert b"email" in response.data
    assert b"password" in response.data

    