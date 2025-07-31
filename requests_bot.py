import requests, os, smtplib          # Import smtplib for the actual sending function
from email.message import EmailMessage      # Import the email modules we'll need


email_subject = 'journpy web app status report'
r = requests.get(os.getenv('JOURNPY_URL'))


def main():
    """ Open the plain text file whose name is in textfile for reading."""
    with open(os.getenv("REPORT_FILE")) as file_object:
        msg = EmailMessage()    # Create a text/plain message
        content = file_object.readlines()   # read the content of the file opened
        if r.status_code == 200:
            msg.set_content(content[0])
        else:
            msg.set_content(content[-1])
    msg['Subject'] = email_subject
    msg['From'] = os.getenv('JOURNPY_EMAIL')
    msg['To'] = os.getenv('JOURNPY_EMAIL')
    s = smtplib.SMTP("smtp.gmail.com", 587)     # creates SMTP session
    s.starttls()                                # start TLS for security
    s.login(os.getenv('JOURNPY_EMAIL'), os.getenv('JOURNPY_CONFIG_PASSWORD'))   # Authentication
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    main()



