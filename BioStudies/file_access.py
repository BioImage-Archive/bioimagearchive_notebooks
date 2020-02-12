from ftplib import FTP
filename = ''
folder = #Secret key

ftp = FTP('ftp−private.ebi.ac.uk', user='bsftp', passwd='bsftp1')

ftp.login()
ftp.cwd(folder)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
