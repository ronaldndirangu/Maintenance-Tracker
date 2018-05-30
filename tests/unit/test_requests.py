api_prefix = "/api/v1/"

def test_all_user_requests_page(test_client):
    response = test_client.get(api_prefix+'/users/requests/')
    assert response.status_code == 200
    response = test_client.post(api_prefix+'/users/requests/')
    assert response.status_code == 201
    assert b"date" in response.data
    assert b"title" in response.data
    assert b"location" in response.data
    assert b"priority" in response.data
    assert b"description" in response.data    

def test_a_user_request_page(test_client):
    response = test_client.get(api_prefix+'/users/requests//')
    assert response.status_code == 200
    response = test_client.post(api_prefix+'/users/requests//')
    assert response.status_code == 201
    assert b"date" in response.data
    assert b"title" in response.data
    assert b"location" in response.data
    assert b"priority" in response.data
    assert b"description" in response.data