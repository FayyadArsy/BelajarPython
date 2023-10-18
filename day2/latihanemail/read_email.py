import imaplib
import email
from email.header import decode_header

#configurasi
email_user = "fayyadarsynandi2@gmail.com"
email_pass = "ixuzqbuwoetqdnsg"

#Initial
mail = imaplib.IMAP4_SSL("imap.gmail.com")

#login gmail
mail.login(email_user, email_pass)

mail.select("inbox")

# status, email_ids = mail.search(None, 'FROM "sdjsdjas@gmail.com"')
status, email_ids = mail.search(None, "ALL")
# print(f"status {status}")
# print("email_ids {email_ids}")

email_id_list = email_ids[0].split()
# print(f"email_id_lost {email_id_list}")

status, msg_data = mail.fetch(email_id_list[len(email_id_list) -1], "(RFC822)")
# print(f"status {status}")
# print(f"msg_data {msg_data}")

raw_email = msg_data[0][1]
msg = email.message_from_bytes(raw_email)
# print(f"msg {msg}")
body = ""
if msg.is_multipart():
    for part in msg.walk():
        content_type = part.get_content_type()
        if "text/plain" in content_type:
            body = part.get_payload(decode=True).decode()
            print(f"body : {body}")

subject, encoding = decode_header(msg["Subject"])[0]
if isinstance(subject, bytes):
    subject = subject.decode(encoding or "utf-8")

from_ = msg.get("From")
print(f"From: {from_}")
print(f"Subject: {subject}")