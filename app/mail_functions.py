import imaplib
import email
from email.header import decode_header
import base64
from bs4 import BeautifulSoup
import re
import os
from dotenv import load_dotenv


def connection_email():
    mail_pass = "ylkp pevn grkh zzuz"
    username = "terremokvasi@gmail.com"
    imap_server = "imap.gmail.com"
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    sts, result = imap.login(username, mail_pass)
    if sts == "OK":
        return imap
    else:
        return False


def fet_topic():
    load_dotenv()
    imap_server = os.getenv("IMAP_SERVER")
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.select("INBOX")
    status, data = imap.search(None, "ALL")
    list_id = data[0].split()
    id_letters = list_id[-1]

    result, data = imap.fetch(id_letters, "(RFC822)")
    message = email.message_from_bytes(data[0][1])

    topic_letter = decode_header(message["Subject"])[0][0].decode()

    print(topic_letter)
