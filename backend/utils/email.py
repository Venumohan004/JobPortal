from flask_mail import Mail, Message
from flask import current_app
import traceback

mail = Mail()

def send_email(subject, recipients, body):
    print("===== EMAIL START =====")
    print("Sender:", current_app.config.get("MAIL_DEFAULT_SENDER"))
    print("Recipients:", recipients)

    try:
        msg = Message(
            subject=subject,
            sender=current_app.config["MAIL_DEFAULT_SENDER"],
            recipients=recipients,
            body=body
        )

        mail.send(msg)
        print("✅ Email sent successfully")

    except Exception:
        print("===== EMAIL FAILED =====")
        traceback.print_exc()
        raise