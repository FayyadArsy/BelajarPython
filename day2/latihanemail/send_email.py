import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#configurasi
email_user = "fayyadarsynandi2@gmail.com"
email_pass = "ixuzqbuwoetqdnsg"

#dstination email
to_email = "fayyad.nandi@berca.co.id"

#create email message
subject = "Test Email"
body = "Test body email"

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

#initial koneksi ke server email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

#login gmail
server.login(email_user, email_pass)

#send email
server.sendmail(email_user, to_email, msg.as_string())

#close connection
server.quit()

print("email telah dikirim")

