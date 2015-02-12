import smtplib

fromaddr = 'hevongordon.com'

toaddr = 'hevongordon.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""

fromname="hevongordon"
fromaddr="hevongordon@gmail.com"
toname="hevongordon"
toaddr="hevongordon@gmail.com"
subject="stuff"
msg="this is a message from me to me"

messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = 'hevongordon@gmail.com'

password = 'kzleowzlnezoomdy'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()