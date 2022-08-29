from pipes import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from templates import Template


"""
Toto je trieda na zostavenie mailovej správy komplet.......
"""

class Mail_b():
    subject = "Hello world"
    context = {}
    to_emails = []
    from_email = 'E&VF <eavfeavf@gmail.com>'
    has_html = False
    template_name = None
    template_html = None
    
    def __init__(self, subject="", template_name=None, context={}, template_html=None, to_emails=None):
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
        
        
    def format_msg(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ", ".join(self.to_emails)
        msg['Subject'] = self.subject
        
        if self.template_name != None:
            tmpl_str = Template(template_name=self.template_name, context=self.context)
            txt_part = MIMEText(tmpl_str.render(),'plain')
            print(txt_part)
            msg.attach(txt_part)

        if self.template_html != None:
            tmpl_str = Template(template_name=self.template_html, context=self.context)
            html_part = MIMEText(tmpl_str.render(),'html')
            print(html_part)
            msg.attach(html_part)
        
        msg_str = msg.as_string()
        return msg_str