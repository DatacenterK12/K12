import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DATA = {
    "smtp_server": os.getenv("SMTP_SERVER"),
    "email_fl": os.getenv("EMAIL_FL"),
    "email_noc": os.getenv("EMAIL_NOC"),
    "password": os.getenv("PASSWORD"),
}

smpObj = smtplib.SMTP(
    DATA["smtp_server"],
    587,
)
smpObj.starttls()
smpObj.login(DATA["email_fl"], DATA["password"])


def send_mail(phone):
    SUBJECT = "Заказ обратного звонка!"
    TEXT = f"Номер {phone}"
    msg = MIMEText(TEXT)
    msg["Subject"] = SUBJECT
    smpObj.sendmail(
        DATA["email_fl"],
        DATA["email_noc"],
        msg.as_string(),
    )


def main():
    phone = "тестовый номер"
    return (send_mail(phone))


if __name__ == "__main__":
    main()