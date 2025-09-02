import pytest
from Webapp import Webapp  # Assuming your Flask app is in a file named 'app.py'

@pytest.fixture
def client():
    """
    Creates a test client for the Flask app.
    This fixture is used by all the tests to make requests.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_main_page_status_code(client):
    """
    Test to ensure the main route ('/') returns a successful status code (200).
    This validates that the application is running and the main page is accessible.
    """
    response = client.get('/')
    assert response.status_code == 200

def test_api_get_request(client):
    """
    Test the GET request on the '/api/data' endpoint.
    It checks that the response status code is 200 and the content type is JSON.
    """
    response = client.get('/api/data')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    # Assuming an empty list is returned initially
    assert response.json == []

def test_api_post_valid_data(client):
    """
    Test a valid POST request to '/api/data'.
    It simulates sending correct JSON data and verifies the response status code and message.
    """
    data_to_send = {"item": "Test Item", "value": 123}
    response = client.post('/api/data', json=data_to_send)
    assert response.status_code == 201  # HTTP 201 Created
    assert response.json['message'] == 'Data added successfully'
    
    # Optional: Test if the data was actually stored (e.g., check with a subsequent GET)
    get_response = client.get('/api/data')
    assert get_response.json == [data_to_send]

def test_api_post_invalid_data_missing_field(client):
    """
    Test a POST request with missing required data.
    The test ensures the application correctly handles the invalid input and returns a 400 status code.
    """
    invalid_data = {"item": "Invalid Data"}  # 'value' field is missing
    response = client.post('/api/data', json=invalid_data)
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Missing required fields: item, value'

def test_api_post_invalid_data_wrong_type(client):
    """
    Test a POST request with an incorrect data type.
    The test checks that the application provides a meaningful error message for type validation.
    """
    invalid_data = {"item": "Test Item", "value": "not_a_number"}
    response = client.post('/api/data', json=invalid_data)
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid value type for field: value'

def test_api_post_empty_json(client):
    """
    Test a POST request with an empty JSON payload.
    This validates the application's handling of empty requests.
    """
    response = client.post('/api/data', json={})
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Missing required fields: item, value'