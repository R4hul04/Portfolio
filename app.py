from flask import Flask, render_template, request, jsonify
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDGRID_SENDER = os.getenv('SENDGRID_SENDER')
SENDGRID_RECIPIENT = os.getenv('SENDGRID_RECIPIENT')

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
        # Create the email
        email_message = Mail(
            from_email=SENDGRID_SENDER,
            to_emails=SENDGRID_RECIPIENT,
            subject='New Contact Form Submission',
            plain_text_content=f"Name: {name}\nEmail: {email}\nMessage: {message}"
        )

        # Send the email
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(email_message)

        if response.status_code == 202:
            return jsonify({'success': 'Form submitted successfully!'})
        else:
            return jsonify({'error': 'Failed to send message. Please try again later.'}), 500

    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'error': 'Failed to send message. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
