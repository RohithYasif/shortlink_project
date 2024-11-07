import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/shortlink_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    RATELIMIT_DEFAULT = "100 per minute"
