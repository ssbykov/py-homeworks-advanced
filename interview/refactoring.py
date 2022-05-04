import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:

    def __init__(self, gmail_smtp, gmail_imap, login, password):
        self.gmail_smtp = gmail_smtp
        self.gmail_imap = gmail_imap
        self.login = login
        self.password = password

    def send_message(self, subject, message, recipients):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        ms = smtplib.SMTP(self.gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, recipients, msg.as_string())
        ms.quit()

    def recive_message(self, header = None):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        if not data[0]:
            print('There are no letters with current header')
            return
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = str(data[0][1])
        email_message = email.message_from_string(raw_email)
        return email_message
        mail.logout()

if __name__ == '__main__':
    gmail = Mail('smtp.gmail.com', 'imap.gmail.com', 'login@gmail.com', 'pass')
