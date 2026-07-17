from flask_mail import Mail, Message
from flask import current_app
import traceback

mail = Mail()


def send_email(subject, recipients, body):

    print("================ EMAIL DEBUG START ================")

    print("MAIL SERVER:",
          current_app.config.get("MAIL_SERVER"))

    print("MAIL PORT:",
          current_app.config.get("MAIL_PORT"))

    print("MAIL USER:",
          current_app.config.get("MAIL_USERNAME"))

    print("MAIL TLS:",
          current_app.config.get("MAIL_USE_TLS"))

    try:

        msg = Message(
            subject=subject,
            sender=current_app.config["MAIL_DEFAULT_SENDER"],
            recipients=recipients,
            body=body
        )

        print("Message created")

        mail.send(msg)

        print("EMAIL SENT SUCCESSFULLY")

    except Exception as e:

        print("================ EMAIL FAILED ================")
        traceback.print_exc()

        raise e