from flask_mail import Mail, Message
from flask import current_app

mail = Mail()


def send_email(subject, recipients, body):
    msg = Message(
        subject=subject,
        sender=current_app.config["MAIL_DEFAULT_SENDER"],
        recipients=recipients,
        body=body
    )

    mail.send(msg)