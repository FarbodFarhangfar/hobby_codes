import imaplib
import email
from email.header import decode_header

# Gmail IMAP settings
imap_server = "imap.gmail.com"
email_address = "fb.ffff78@gmail.com"
password = "fyps rycb byzl sbtt"

# Connect to the Gmail IMAP server
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(email_address, password)

# Select the mailbox (e.g., "INBOX")
mailbox = "INBOX"
mail.select(mailbox)

# Search for emails (in this example, searching for unread emails)
status, email_ids = mail.search(None, "UNSEEN")

# Get the list of email IDs
email_id_list = email_ids[0].split()

# Loop through the email IDs
for email_id in email_id_list:
    # Fetch the email by its ID
    status, msg_data = mail.fetch(email_id, "(RFC822)")

    # Parse the email message
    raw_email = msg_data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Extract email details
    subject, encoding = decode_header(email_message["Subject"])[0]
    if encoding:
        subject = subject.decode(encoding)
    else:
        subject = subject

    from_address = email_message.get("From")
    date_sent = email_message.get("Date")

    # Print email details
    print(f"Subject: {subject}")
    print(f"From: {from_address}")
    print(f"Date Sent: {date_sent}")

    # Print email content (plain text part)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode("utf-8")
            print("Email Content:")
            print(body)

    print("\n")

# Logout and close the connection
mail.logout()
