import pytest
from app import app, workouts

@pytest.fixture
def client():
    """
    Sets up a test client for the Flask application.
    The 'yield' statement ensures that the client is available
    for testing and the teardown code runs after the test is complete.
    """
    # Use app.test_client() to simulate requests to the app
    with app.test_client() as client:
         # Clear the workouts list before each test to ensure a clean state
         workouts.clear()
         yield client
         # Clear the workouts list after each test
         workouts.clear()

def test_index_page(client):
    """
    Tests that the main index page loads correctly.
    It should return a 200 OK status code.
    """
    response = client.get('/')
    assert response.status_code == 200

def test_get_workouts_initial(client):
    """
    Tests the GET /api/workouts endpoint.
    Initially, the in-memory 'workouts' list should be empty.
    """
    response = client.get('/api/workouts')
    data = response.get_json()
    assert response.status_code == 200
    assert data == []

def test_post_workout_success(client):
    """
    Tests adding a new workout with a valid POST request.
    Verifies the status code, response message, and that the workout was added.
    """
    # Define a valid workout to send in the request body
    valid_workout = {
        'workout': 'Running',
        'duration': 30,
        'date': '2023-10-27'
    }
    response = client.post('/api/workouts', json=valid_workout)
    data = response.get_json()
    assert response.status_code == 201
    assert data['message'] == 'Workout added successfully'
    
    # Check if the workout was actually added to the in-memory list
    assert len(workouts) == 1
    assert workouts[0] == valid_workout
    
def test_post_workout_missing_fields(client):
    """
    Tests a POST request with missing required fields.
    It should return a 400 Bad Request error.
    """
    # Test case with missing 'date' field
    invalid_workout_1 = {
        'workout': 'Yoga',
        'duration': 60
    }
    response = client.post('/api/workouts', json=invalid_workout_1)
    data = response.get_json()
    assert response.status_code == 400
    assert data['message'] == 'Missing fields: workout, duration, date'

    # Test case with missing 'duration' field
    invalid_workout_2 = {
        'workout': 'Swimming',
        'date': '2023-10-30'
    }
    response = client.post('/api/workouts', json=invalid_workout_2)
    data = response.get_json()
    assert response.status_code == 400
    assert data['message'] == 'Missing fields: workout, duration, date'

def test_post_workout_invalid_json(client):
    """
    Tests a POST request with an invalid JSON payload.
    It should return a 415 Bad Request error.
    """
    # Send a non-JSON payload
    response = client.post('/api/workouts', data="this is not json")
    data = response.get_json()
    assert response.status_code == 415
    assert data == None
