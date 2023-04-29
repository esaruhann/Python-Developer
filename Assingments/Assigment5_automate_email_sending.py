''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
import schedule
import time
import logging

sender_email = "edanursaruhan@gmail.com"
password = input("Type your password and press enter:")
# configure log file
logging.basicConfig(filename='email_log.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
# add a stream handler to print logs to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logging.getLogger('').addHandler(console_handler)

def send_emails():

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    
    

    #########################################

    
    filename = "document.pdf"  # In same directory as script
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    # Open PDF file in binary mode
    with open(filepath, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    
    # Add HTML/plain-text parts to MIMEMultipart message

    
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    
    import csv
    
    with open("contacts_file.csv") as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip header row
        for row in reader:
            try:
                name, email = row
                # Create the plain-text and HTML version of your message
                text = """\
                Hi {},
                How are you?
                Real Python has many great tutorials:
                www.realpython.com""".format(name)
                html = """\
                <html>
                  <body>
                    <p>Hi {},<br>
                       How are you?<br>
                    </p>
                  </body>
                </html>
                """.format(name)
            


            except ValueError:
                logging.error(f"Skipping row {row}, not enough values")
                continue
            
            logging.info('Email sending process started')
            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)
            # Send email here
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(
                        sender_email, email, message.as_string()
                    )
                logging.info(f"Email sent to {name} at {email}")
            except ValueError:
                logging.error(f"Skipping row {row}, not enough values")
# schedule the script to run every day at 8:00 AM
schedule.every().day.at("10:51").do(send_emails)
# loop through the scheduled jobs

while True:
    # Check if there are any pending scheduled jobs
    if schedule.idle_seconds() == 0:
        print("All jobs have been completed. Exiting...")
        break
    
    # Run any pending scheduled jobs
    schedule.run_pending()
    
    # Wait a short amount of time to avoid using too much CPU
    time.sleep(1)

    