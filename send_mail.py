import os
import smtplib

HOST = 'smtp.gmail.com'
USER_NAME = 'anuj.nits2@gmail.com'
PASSWORD = 'wzgpcyhchhcdoret'


def send_mail(to_, msg_):
    with smtplib.SMTP(host=HOST, port=587) as conn:
        conn.starttls()
        conn.login(user=USER_NAME, password=PASSWORD)
        conn.sendmail(from_addr=USER_NAME, to_addrs=to_, msg=msg_)
