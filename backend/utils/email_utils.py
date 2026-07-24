from flask import current_app
from flask_mail import Message

from extensions import mail


def send_email(subject, recipients, body):
    """
    Generic email sender.
    """
    try:
        msg = Message(
            subject=subject,
            recipients=recipients,
            body=body
        )

        mail.send(msg)

        current_app.logger.info(
            f"Email sent successfully to {recipients}"
        )

        return True

    except Exception as e:
        current_app.logger.error(str(e))
        return False


def send_interview_email(candidate_email, candidate_name, interview_data):
    """
    Send interview schedule notification email.
    """

    subject = f"Interview Scheduled - {interview_data['job_title']}"

    body = f"""
Dear {candidate_name},

Congratulations! Your interview has been scheduled.

Job Title: {interview_data['job_title']}
Company: {interview_data['company_name']}

Interview Details
-----------------------------
Date: {interview_data['interview_date']}
Time: {interview_data['interview_time']}
Mode: {interview_data['mode']}
"""

    if interview_data["mode"].lower() == "online":
        body += f"\nMeeting Link: {interview_data.get('meeting_link', 'Will be shared later')}"
    else:
        body += f"\nLocation: {interview_data.get('location', 'Office address will be shared later')}"

    body += """

Please be available 10 minutes before the interview.

Best Regards,
Recruitment Team
"""

    return send_email(
        subject=subject,
        recipients=[candidate_email],
        body=body
    )