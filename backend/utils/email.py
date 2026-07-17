from flask_mail import Mail, Message
from flask import current_app
import traceback


mail = Mail()


def send_email(subject, recipients, body):

    print("================ EMAIL DEBUG START ================")

    try:
        print("MAIL SERVER:",
              current_app.config.get("MAIL_SERVER"))

        print("MAIL PORT:",
              current_app.config.get("MAIL_PORT"))

        print("MAIL USER:",
              current_app.config.get("MAIL_USERNAME"))

        print("MAIL TLS:",
              current_app.config.get("MAIL_USE_TLS"))

        print("SENDER:",
              current_app.config.get("MAIL_DEFAULT_SENDER"))

        print("RECIPIENTS:",
              recipients)


        msg = Message(
            subject=subject,
            sender=current_app.config["MAIL_DEFAULT_SENDER"],
            recipients=recipients,
            body=body
        )


        print("Message created")

        mail.send(msg)

        print("========== EMAIL SENT SUCCESS ==========")


    except Exception as e:

        print("========== EMAIL FAILED ==========")

        print("ERROR TYPE:", type(e).__name__)

        print("ERROR MESSAGE:", str(e))

        traceback.print_exc()

        raise 