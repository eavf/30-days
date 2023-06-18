import imaplib
import email
from operator import truediv

# environment variables
host = 'imap.gmail.com'
from _kluce import *



def get_inbox():
    i=0
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')

    my_messages = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        #print(data[0])
        _,b = data[0]
        email_message = email.message_from_bytes(b)
        #email_message = email.message_from_string(b)
        #print (email_message)
        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
            
        for part in email_message.walk():
            if part.get_content_type() == "text/plain" :
                i += 1
                body = part.get_payload(decode = True)
                #print(body.decode())
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                i += 1
                html_body = part.get_payload(decode = True)
                #print(html_body.decode())
                email_data['html_body'] = html_body.decode()
        my_messages.append(email_data)
        if i>10:
            return my_messages
    return my_messages

if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)