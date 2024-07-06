from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# AWS SES Configuration
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
SES_SENDER = os.getenv('SES_SENDER')
SES_RECIPIENT = os.getenv('SES_RECIPIENT')

ses_client = boto3.client(
    'ses',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

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
        # Send the email
        response = ses_client.send_email(
            Source=SES_SENDER,
            Destination={
                'ToAddresses': [SES_RECIPIENT]
            },
            Message={
                'Subject': {
                    'Data': 'New Contact Form Submission',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': f"Name: {name}\nEmail: {email}\nMessage: {message}",
                        'Charset': 'UTF-8'
                    }
                }
            }
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return jsonify({'success': 'Form submitted successfully!'})
        else:
            return jsonify({'error': 'Failed to send message. Please try again later.'}), 500

    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Credentials error: {e}")
        return jsonify({'error': 'Failed to send message. Invalid AWS credentials.'}), 500
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'error': 'Failed to send message. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
