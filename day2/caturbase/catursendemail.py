import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#configurasi
email_user = "fayyadarsynandi2@gmail.com"
email_pass = "ixuzqbuwoetqdnsg"

#atachment
attachment = "tugascatur_fayyad.xlsx"

#dstination email
to_email = "fayyad.nandi@berca.co.id,fayyadnandi@gmail.com"
cc = "fayyadarsy@gmail.com"

#create email message
subject = "Tugas Python Day 2 - Fayyad Arsy Nandi"
body = "Saya, Fayyad Arsy Nandi bermaksud untuk mengirimkan hasil pengerjaan tugas python day 2 saya. Berikut saya melampirkan hasil pengerjaan saya. Demikian email ini saya buat, atas perhatian kakak saya ucapkan terima kasih"

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = to_email
msg['Cc'] = cc
msg['Subject'] = subject
rcpt = cc.split(",") + [to_email]
msg.attach(MIMEText(body, 'plain'))

part = MIMEBase('application', "octet-stream")
part.set_payload(open(attachment, "rb").read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment', filename=attachment)

msg.attach(part)

#initial koneksi ke server email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

#login gmail
server.login(email_user, email_pass)

#send email
server.send_message(msg)

#close connection
server.quit()

print("email telah dikirim")

