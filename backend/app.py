from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import CORS
import os
import uuid

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Enable CORS for the frontend origin
# Enable CORS for all routes and allow the frontend origin
CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "methods": ["OPTIONS", "GET", "POST"]}})


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    full_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Store plain password
    session_token = db.Column(db.String(128), unique=True, nullable=True)

@app.route('/api/signup', methods=['POST', 'OPTIONS'])
def signup():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'CORS preflight successful'}), 200
    try:
        data = request.get_json()
        print(f"Received data: {data}")
        if not data:
            print("No data received")
            return jsonify({'message': 'No data received'}), 400

        username = data.get('username')
        full_name = data.get('fullName')
        email = data.get('email')
        password = data.get('password')

        if not username or not full_name or not email or not password:
            print("Missing fields")
            return jsonify({'message': 'Missing fields'}), 400

        if User.query.filter_by(email=email).first():
            print("User already exists print from backend")
            return jsonify({'message': 'User already exists'}), 400

        user = User(username=username, full_name=full_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        print("User created successfully print from backend")
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Internal server error'}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        print(f"Received data: {data}")
        if not data:
            print("No data received")
            return jsonify({'message': 'No data received'}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            print("Missing fields")
            return jsonify({'message': 'Missing fields'}), 400

        user = User.query.filter_by(email=email).first()

        if user is None or user.password != password:
            print("Invalid email or password")
            return jsonify({'message': 'Invalid email or password'}), 400

        # Generate a session token
        session_token = str(uuid.uuid4())
        user.session_token = session_token
        db.session.commit()

        print("Login successful")
        return jsonify({'message': 'Login successful', 'token': session_token}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Internal server error'}), 500

if __name__ == '__main__':
    print("Starting Flask app now!")
    app.run(debug=True, host='0.0.0.0', port=5005)

