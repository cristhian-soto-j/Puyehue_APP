from flask import current_app
from flask_mail import Message
from app import mail
from flask import render_template
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(
        target=send_async_email,
        args=(current_app._get_current_object(), msg)).start()

def contact_email(form):
    recipient = ['ing.puyehue@gmail.com', 'cristhian.soto.j@gmail.com']
    send_email('[Puyehue APP] Formulario de Contacto',
        sender = current_app.config['ADMINS'][0],
        recipients = recipient,
        text_body = render_template('email/contact_email.txt', form=form),
        html_body = render_template('email/contact_email.html', form=form))
  