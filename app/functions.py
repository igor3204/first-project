import imaplib
import email
from email.header import decode_header
import config


def connection_email():
<<<<<<< HEAD:app/functions.py
    mail_pass = config.mail_pass
    username = config.username
    imap_server = config.imap_server
=======
    mail_pass = 
    username = 
    imap_server = "imap.gmail.com"
>>>>>>> 44d2b81c48e889e3a9b06692b4b24ff9befcfc17:app/mail_functions.py
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    status, result = imap.login(username, mail_pass)
    if status == "OK":
        return imap
    else:
        return False


def get_topic():
    imap_server = config.imap_server
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.select("INBOX")
    status, data = imap.search(None, "ALL")
    list_id = data[0].split()
    id_letters = list_id[-1]

    result, data = imap.fetch(id_letters, "(RFC822)")
    message = email.message_from_bytes(data[0][1])

    topic_letter = decode_header(message["Subject"])[0][0].decode()

    print(topic_letter)
