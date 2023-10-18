import pandas as pd
import zipfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def fill_chessboard():
    n = 8  # Ukuran papan catur
    x = 1
    chessboard = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(f"{x}")
            x = x * 2
        chessboard.append(row)

    for i, row in enumerate(chessboard):
        row_total = sum(map(int, row))
        row.append(str(row_total))
        chessboard[i] = row
    column_totals = [sum(int(row[i]) for row in chessboard) for i in range(n)]

    # Menambahkan baris terakhir dengan total per kolom
    last_row = [str(total) for total in column_totals]
    chessboard.append(last_row)


    return chessboard

chessboard_data = fill_chessboard()

chessboard_df = pd.DataFrame(chessboard_data)
chessboard_df = chessboard_df.rename({chessboard_df.index[-1]: 'Total'})
chessboard_df.rename(columns={chessboard_df.columns[-1]: 'Total'}, inplace=True)
# print(chessboard_df)

chessboard_df.to_excel("tugascatur_fayyad.xlsx")
print("Berhasil: Membuat Excel")

#membuat zip
zip_filename = "Tugas_Fayyad.zip"

files_to_zip = ["tugascatur_fayyad.xlsx","catur_email.py"]

with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in files_to_zip:
        zipf.write(file)
print("Berhasil: Membuat Zip")
#configurasi
email_user = "fayyadarsynandi2@gmail.com"
email_pass = "ixuzqbuwoetqdnsg"

#atachment
attachment = "tugascatur_fayyad.xlsx"

#dstination email
to_email = "andre.kautsar@berca.co.id,fatchurrachman.yudha@berca.co.id"
cc = "rifqi.muhammad@berca.co.id,fayyad.nandi@berca.co.id"

#create email message
subject = "Tugas Python Day 2 - Fayyad Arsy Nandi"
body =  """
<!DOCTYPE html>
<html>
<head>
</head>
<body>
    <p><strong>Kepada Yth.</strong></p>
    <p>Bapak Andre Kautsar & Bapak Fatchurrachman Purna Yudha</p>
    <p>PT. Berca Hardayaperkasa</p>
    <p>Jakarta, Indonesia</p>
    
    
    
    <p>Selamat sore, Kak Andre dan Kak Fatur.</p>
    <p>Perkenalkan saya Fayyad Arsy Nandi dari Bootcamp Developer Berca batch 4. Saya mengirimkan email ini untuk mengumpulkan jawaban tugas python hari ke-2,</p>
    <p>Berikut file python sudah saya lampirkan melalu link google drive, dikarenakan batasan oleh server email Berca.</p>
    <p>https://drive.google.com/drive/folders/17COwpg5h0PC6SDvTLOZB1ZgOpgF_tOD0?usp=drive_link</p>
    <p>(Email ini dikirim dengan automasi)</p>
    <p> Demikian email ini saya buat, atas perhatian kakak saya ucapkan terima kasih.</p>
    
    
    
    <p><em>Hormat Saya,</em></p>
    <p><strong>Fayyad Arsy Nandi</strong></p>
</body>
</html>
"""

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = to_email
msg['Cc'] = cc
msg['Subject'] = subject
rcpt = cc.split(",") + [to_email]
msg.attach(MIMEText(body, 'html'))

part = MIMEBase('application', "octet-stream")
part.set_payload(open(attachment, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % attachment)

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

print("Berhasil: Mengirim Email")
