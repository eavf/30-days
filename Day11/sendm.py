
import smtplib


"""
Toto je trieda na odosielanie mailu iba
"""


# environment variables
username = 'eavfeavf@gmail.com'
password = 'aafnjdioifpzvyzq'   # heslo pre aplikácie v google


class Send_m():
    to_emails = []
    from_email = 'E&VF <eavfeavf@gmail.com>'
    test_send = False
    msg_str = ""
    
    def __init__(self, msg_str = "", to_emails =None, test_send = False):
        if msg_str == None :
            raise Exception("You must set a template")
        else:
            self.msg_str = msg_str
        assert isinstance(to_emails, list)
        self.to_emails = to_emails
        self.test_send = test_send

    def send_mail(self):
        msg = self.msg_str
        # Login to smtp server

        did_send = False
        if not self.test_send:
            with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as server:
                server.ehlo()
                server.starttls()
                server.login(username, password)
                try:
                    server.sendmail(self.from_email, self.to_emails, msg)
                    did_send = True
                except:
                    did_send = False
        return did_send