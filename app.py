from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Simple in-memory data store for the workouts.
# This will be reset every time the server restarts.
# In a real-world application, you would use a database.
workouts = []

# To persist data between server restarts, you can uncomment the following
# and comment out the simple in-memory list above.
# Define a file to store the workouts
DATA_FILE = 'workouts.json'
# # Load data from file on startup
if os.path.exists(DATA_FILE):
 with open(DATA_FILE, 'r') as f:
     try:
        workouts = json.load(f)
     except json.JSONDecodeError:
        workouts = []


#     """Saves the current workouts list to a JSON file."""
def save_data():
    try:
        with open(DATA_FILE, 'w') as f:
             json.dump(workouts, f)
    except IOError as e:
        print(f"Error saving data to file: {e}")


@app.route('/')
def index():
    """Renders the main dashboard page."""
    return render_template('index.html')


@app.route('/api/workouts', methods=['GET', 'POST'])
def handle_workouts():
    """
    Handles GET and POST requests for workout data.
    - GET: Returns the list of all workouts.
    - POST: Adds a new workout to the list.
    """
    if request.method == 'POST':
        # Get the new workout data from the request body
        new_workout = request.get_json()
        if not new_workout:
            return jsonify({'message': 'Invalid JSON data received'}), 415

        # Validate required fields
        if not all(k in new_workout for k in ['workout', 'duration', 'date']):
            return jsonify({'message': 'Missing fields: workout, duration, date'}), 400
        # Data type validation
        if not isinstance(new_workout['workout'], str):
            return jsonify({'message': 'Invalid data type for workout'}), 400
        if not isinstance(new_workout['duration'], int):
            return jsonify({'message': 'Invalid data type for duration'}), 400
        try:
            datetime.strptime(new_workout['date'], '%Y-%m-%d')
        except ValueError:
            return jsonify({'message': 'Invalid date format. Use YYYY-MM-DD'}), 400

        # Append the new workout to our list
        workouts.append(new_workout)

        # Uncomment to save data to file
        save_data()

        # Return a success message
        return jsonify({'message': 'Workout added successfully'}), 201

    elif request.method == 'GET':
        # Return the list of all workouts as JSON
        return jsonify(workouts)

if __name__ == '__main__':
    # You can change the port and debug settings as needed
    app.run(debug=True, port=5000)
    