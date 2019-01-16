from flask import url_for
from flask_mail import Message

from flaskblog import mail


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(subject='Password Reset Request', sender='noreply.simpleflaskblog@gmail.com', body=f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
''', recipients=[user.email])
    mail.send(msg)
