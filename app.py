# Name: 		zzClusterEm
# Version:	    1.0
# License:	    MIT
# Author:		Carlo Bisda

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import time

# Read the list of email addresses from a text file
def read_email_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

# Read the email message from a text file
def read_email_message(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Read email configuration from a text file
def read_email_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    return config

# Read the PDF filename from a text file
def read_pdf_filename(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# File paths
email_list_file = 'list.ini'
email_message_file = 'message.ini'
email_config_file = 'config.ini'
pdf_filename_file = 'filename.ini'

# Read data from files
email_list = read_email_list(email_list_file)
email_message = read_email_message(email_message_file)
email_config = read_email_config(email_config_file)
pdf_filename = read_pdf_filename(pdf_filename_file)

# Set the sender address and subject from the config
sender_email = email_config.get('sender_email')
sender_password = email_config.get('sender_password')
subject = email_config.get('subject')
smtp_server = email_config.get('smtp_server')
smtp_port = int(email_config.get('smtp_port'))

# Send the email to each recipient one at a time
for email in email_list:
    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = subject

    # Attach the email message body
    msg.attach(MIMEText(email_message, 'plain'))

    # Attach PDF file if provided
    if pdf_filename and os.path.isfile(pdf_filename):
        with open(pdf_filename, 'rb') as file:
            pdf_part = MIMEApplication(file.read(), Name=os.path.basename(pdf_filename))
        pdf_part['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_filename)}"'
        msg.attach(pdf_part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())
            print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f"Failed to send email to {email}: {str(e)}")

    # Wait for 5 seconds before sending the next email
    print("5sec pause before sending next email")
    time.sleep(5)