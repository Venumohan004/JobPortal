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
        return True

    except Exception as e:
        print(f"Email Error: {e}")
        return False