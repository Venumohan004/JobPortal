from flask_mail import Mail, Message
import traceback

mail = Mail()

def send_email(subject, recipients, body):
    try:
        msg = Message(
            subject=subject,
            recipients=recipients,
            body=body
        )

        mail.send(msg)
        print("✅ Email sent successfully!")

    except Exception as e:
        print("\n========== EMAIL ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        traceback.print_exc()
        print("=================================\n")
        raise