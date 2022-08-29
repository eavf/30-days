from pipes import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from buildm import Mail_b
from sendm import Send_m


"""
Toto je trieda na zostavenie mailovej správy komplet.......
"""

class Mailer():
    subject = "Hellp world"
    context = {}
    to_emails = []
    from_email = 'E&VF <eavfeavf@gmail.com>'
    has_html = False
    test_send = False
    template_name = None
    template_html = None
    
    def __init__(self, subject="", template_name=None, context={}, template_html=None, to_emails=None, test_send = False):
        if template_name == None and template_html == None:
            raise Exception("You must set a template")
        assert isinstance(to_emails, list)
        self.to_emails = to_emails
        if subject != "":
            self.subject = subject
        if template_html != None:
            self.has_html = True
            self.template_html = template_html
        self.template_name = template_name
        self.context = context
        self.test_send = test_send
        
    def send_mesg(self):
        msg_obj = Mail_b(subject = self.subject, template_name=self.template_name, context=self.context, template_html=self.template_html, to_emails=self.to_emails)
        msg_list = msg_obj.format_msg()
        srv = Send_m(msg_str=msg_list, to_emails=self.to_emails, test_send=self.test_send)
        resul = srv.send_mail()
        print(resul)
        return  resul