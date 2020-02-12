from ftplib import FTP
filename = ''
folder = 'b6/58f8c7−0d88−424c−96bd−63d97210703c−a408'

ftp = FTP('ftp−private.ebi.ac.uk', user='bsftp', passwd='bsftp1')

ftp.login()
ftp.cwd(folder)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
