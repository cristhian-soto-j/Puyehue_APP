import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # App settings
    APP_NAME = 'Puyehue APP'
    APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"
    
    # Generate a safe one with:
    # >$ python -c "import uuid; print(uuid.uuid4().hex)"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "it_is_a_secret"
    
    # SQLAlchemy setting
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'puyehue.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Flask-Mail settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # export MAIL_SERVER=smtp.gmail.com
    # export MAIL_PORT=587
    # export MAIL_USE_SSL = False
    # export MAIL_USE_TLS= True
    # export MAIL_USERNAME=<your-gmail-username>
    # export MAIL_PASSWORD=<your-gmail-password>
    # export MAIL_DEFAULT_SENDER = '"PuyehueAPP" <noreply@gmail.com>'

    ADMINS = [
        #'"Puyehue APP" <contacto@ingpueyehue.cl>',
        '"Puyehue APP 2" <ing.puyehue@gmail.com>' 
    ]

    
