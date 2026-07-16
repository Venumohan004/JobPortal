from flask_mail import Mail, Message
from flask import current_app
import traceback

mail = Mail()

def send_email(subject, recipients, body):
    try:
        msg = Message(
            subject=subject,
            sender=current_app.config["MAIL_DEFAULT_SENDER"],
            recipients=recipients,
            body=body
        )

        mail.send(msg)
        print("✅ Email sent successfully")

    except Exception as e:
        print("========== EMAIL ERROR ==========")
        traceback.print_exc()
        print(e)
        raise