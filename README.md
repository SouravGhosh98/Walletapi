# Walletapi
A Django-based API for wallet transactions with JWT authentication and multiple apps. Simplify wallet management and secure transactions.input is withdrawal account number and paid account no and output is transaction I'd and message.
# Wallet Web Application

The Wallet Web Application is a Django-based project that provides a simple API for wallet transactions. It uses JWT (JSON Web Tokens) for authentication and includes two apps: `wallet_api` and `wallerapp`.

## Features

- **JWT Authentication**: Secure API endpoints using JSON Web Tokens for user authentication.
- **Wallet Transactions**: Allows users to perform wallet transactions, including deposits and withdrawals.
- **Multiple Apps**: Demonstrates a Django project with multiple apps.
- **Custom Models**: Defines custom models for user wallets and transactions.
- **API Endpoints**: Provides API endpoints for interacting with wallets and transactions.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/SouravGhosh98/wallet-web-app.git
   cd walletapi
## Create a virtual environment and activate it:
   python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

## Install project dependencies:
pip install -r requirements.txt
## Set up the database:
python manage.py migrate
## Create a superuser for admin access (optional):
python manage.py createsuperuser
## Start the development server:
bash
python manage.py runserver
## Access the API at http://127.0.0.1:8000/ and the admin panel (if you created a superuser) at http://127.0.0.1:8000/admin/.
## Usage:-
Use the API endpoints to interact with wallet transactions.
Ensure you include a valid JWT token in your requests for authenticated access.
Modify the apps, models, and views to suit your specific project requirements.
## Configuration
Set your secret key, database settings, and other configuration options in the settings.py file.
## License
This project is licensed under the MIT License. See the LICENSE file for details.
