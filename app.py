from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import requests

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
SUPABASE_TABLE = 'contact_form'

# Define the Supabase API URL for interacting with the database
SUPABASE_API_URL = f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('fullname')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        return jsonify({'error': 'All form fields are required.'}), 400

    try:
        # Save to Supabase
        response = requests.post(
            SUPABASE_API_URL,
            headers={
                'Authorization': f'Bearer {SUPABASE_KEY}',
                'Content-Type': 'application/json',
                'apikey': SUPABASE_KEY
            },
            json={
                'fullname': name,
                'email': email,
                'message': message
            }
        )

        if response.status_code == 201:
            return jsonify({'success': 'Form submitted successfully!'})
        else:
            return jsonify({'error': 'Failed to send message. Please try again later.'}), 500

    except Exception as e:
        print(f"Error sending message: {e}")
        return jsonify({'error': 'Failed to send message. Please try again later.'}), 500

if __name__ == '__main__':
    app.run()
