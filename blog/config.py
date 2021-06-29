import os
from blog.Key import SECRET_KEY
class Config():
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TSL = True
    MAIL_USERNAME = os.environ.get('LIVE_MAIL_USER')
    MAIL_PASSWORD = os.environ.get('LIVE_MAIL_PASS')