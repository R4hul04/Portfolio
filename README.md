# Portfolio Website

This repository contains the code for a personal portfolio website built with Flask and deployed on Vercel. The site includes a contact form that stores user inputs in a Supabase database and integrates Vercel's web analytics for tracking user interactions.

## Table of Contents

- [Portfolio Website](#portfolio-website)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [Clone the Repository](#clone-the-repository)
    - [Set up the Environment](#set-up-the-environment)
    - [Install Dependencies](#install-dependencies)
    - [Configure Supabase](#configure-supabase)
    - [Run the Application](#run-the-application)
  - [Deploying to Vercel](#deploying-to-vercel)
  - [Deploy](#deploy)
  - [License](#license)

## Features

- Personal portfolio showcasing projects and skills
- Contact form to receive messages from visitors
- Store form submissions in a Supabase database
- Integrated with Vercel Analytics for tracking
- Deployed on Vercel for easy scalability and management

## Requirements

- Python 3.7 or higher
- Node.js and npm (for Vercel Analytics)
- A Supabase account
- A Vercel account

## Setup

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/portfolio-website.git
cd portfolio-website
```

## Set Up the Environment
Create a .env file in the root of the project and add your Supabase and Vercel Analytics credentials:

```bash
touch .env
```

Add the following to your .env file:

```bash
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
```

## Install Dependencies
Install the necessary Python packages:

```bash 
pip install -r requirements.txt
```

## Configure Supabase
Ensure your Supabase project is set up and create a table named contact_form with columns fullname, email, and message.

## Run the Application
Run the Flask application locally:

```bash
python app.py
```

Open your browser and navigate to http://127.0.0.1:5000 to see your portfolio website.

## Deploying to Vercel

- Connect to GitHub
- Push your local repository to GitHub
- Log in to Vercel and create a new project, importing your GitHub repository
- Configure Environment Variables
- In your Vercel project dashboard, go to Settings > Environment Variables and add the following:
```bash
SUPABASE_URL
SUPABASE_KEY
```

## Deploy
Once the environment variables are set, deploy your project. Vercel will provide you with a URL to access your live site.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

