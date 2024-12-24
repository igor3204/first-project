import imaplib
import email
from email.header import decode_header
import base64
from bs4 import BeautifulSoup
import re


mail_pass = 
username = 
imap_server = 
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)

imap.select("INBOX")

status, data = imap.search(None, "ALL")
list_id = data[0].split()
id_letters = list_id[-1]

result, data = imap.fetch(id_letters, "(RFC822)")
message = email.message_from_bytes(data[0][1])

topic_letter = decode_header(message["Subject"])

print(topic_letter)

