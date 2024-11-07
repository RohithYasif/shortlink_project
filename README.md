# ShortLink URL Shortener

ShortLink is a simple URL shortening service built using Flask, PostgreSQL, and Python. It provides API endpoints to shorten URLs and redirect to the original URLs via short codes.

## Features
- Shorten URLs through a POST request
- Redirect to original URL via short code
- Rate limiting for the shorten URL endpoint

## Technologies Used
- Python 3.x
- Flask (Web Framework)
- Flask-SQLAlchemy (Database ORM)
- PostgreSQL (Database)
- Flask-Limiter (Rate Limiting)

### Prerequisites
- Python 3.x
- PostgreSQL
- Virtual Environment (recommended)

### Steps to Run

**1.Clone this repository:**

bash
Copy code
git clone https://github.com/yourusername/shortlink.git
cd shortlink

**2.Create a Virtual Environment:**

Open Command Prompt and navigate to your project folder.

**3.Run the following commands:**

bash
Copy code
python -m venv venv
venv\Scripts\activate

**4.Install required dependencies:**

bash
Copy code
pip install -r requirements.txt

**5.Set up PostgreSQL database:**

Install and start PostgreSQL on your system.
Create a database called shortlink_db (or another name of your choice).
Update the SQLALCHEMY_DATABASE_URI in app/config.py (or in app/__init__.py depending on where it’s configured):
python
Copy code
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/shortlink_db'

**6.Run the application:**

bash
Copy code
python run.py
The app will be available at http://127.0.0.1:5000.

### ACKNOWLEGEMENTS

Flask – Python web framework used for building the app.
SQLAlchemy – ORM used to interact with PostgreSQL.
PostgreSQL – Database used for persistent URL storage.
Flask-Limiter – Rate limiting for the API endpoints.