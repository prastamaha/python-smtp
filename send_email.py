import smtplib
from getpass import getpass

print('pastikan akun google sudah less secure')

# server and port
server = 'smtp.gmail.com'
port = 587

conn = smtplib.SMTP(server, port)
conn.ehlo()  # untuk mengkoneksikan ke server
conn.starttls()  # mengkoneksikan menggunakan starttls

# user email account
usr = input('Masukan Email: ')
pwd = getpass('Masukan Password: ')
mailto = input('Email tujuan: ')

# message
print()
sub = input('Subject: ')
message = input()

try:
    conn.login(usr, pwd)
    conn.sendmail(usr, mailto, 'Subject: ' + sub + '\n\n' + message)
    conn.quit()
    print()
    print('Pesan Berhasil Terkirim')
except:
    print()
    print('Pesan Gagal terkirim')
