import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd


# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Port for TLS
smtp_username = 'fb.ffff78@gmail.com'
smtp_password = 'krsk tkst gvzv gekl'

def send_email(recipient_name, recipient_email):
    # Create the email content
    subject = 'Hello, {}!'.format(recipient_name)
    body = 'This is a personalized email to {}.'.format(recipient_name)

    # Create a MIMEText object
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the email body
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()

    # Login to your email account
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(smtp_username, recipient_email, message.as_string())

    # Close the SMTP server
    server.quit()

def excel(path):


    # Read an Excel file
    df = pd.read_excel(path)

    # Convert the DataFrame to a dictionary of dictionaries
    data_dict = df.to_dict(orient='records')

    # Print the resulting dictionary
    return data_dict

print(excel("recipiant.xlsx"))
recipients = [
    {'name': 'Recipient 1', 'email': 'recipient1@example.com'},
    {'name': 'Recipient 2', 'email': 'hehoh97589@chambile.com'},
    # Add more recipients here
]


# for recipient in recipients:
#
#         send_email(recipient['name'], recipient['email'])
#         print(f"Email sent to {recipient['name']} at {recipient['email']}")
