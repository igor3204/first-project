import imaplib
import email
from email.header import decode_header
import config


def connection_email():
    mail_pass = config.mail_pass
    username = config.username
    imap_server = config.imap_server
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
