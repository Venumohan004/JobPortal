from flask_mail import Mail, Message

mail = Mail()

def send_email(subject, recipients, body):
    try:
        msg = Message(
            subject=subject,
            recipients=recipients,
            body=body
        )
        mail.send(msg)
        print("Email sent successfully")
    except Exception as e:
        print("========== EMAIL ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        print("================================")
        raise