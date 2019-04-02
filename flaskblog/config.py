import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgres://xqjbsdyizfbvgt' \
                              ':12bd5d17f0f3d68b53e33c06575bc783fde655185a8f4a50030db39d95b150de@ec2-184-73-216-48' \
                              '.compute-1.amazonaws.com:5432/dacgf9jlurg0gh '
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
