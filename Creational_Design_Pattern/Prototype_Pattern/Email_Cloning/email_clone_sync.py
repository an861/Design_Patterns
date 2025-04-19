# SYNCHRONOUS

import copy

class Email:
    def __init__(self, sender, recepient, subject, body, attachment: list)->None:
        self.sender = sender
        self.recepient = recepient
        self.subject= subject
        self.body= body
        self.attachments =  []

    def __str__(self)->str:
        return f"From: {self.sender}\nTo: {self.recepient}\nSubject: {self.subject}\nBody: {self.body}\nAttachment:: {self.attachments}\n"
    
    def __repr__(self):
        return f"Email(from={self.sender}, to={self.recepient}, subject={self.subject})\nAttachment:: {self.attachments}"
    
    def to_dict(self)->dict:
        return self.__dict__
    
    def clone(self):
        return copy.deepcopy(self)
    
    def add_attachement(self, attachment: str):
        return self.attachments.append(attachment)
    

email = Email(sender="ankita@gmail.com", recepient="Bhive@workspace.com", subject="Greetings of the day", body="Hi Welcome to bhive", attachment="file.pdf")

email_1 = email.clone()
email_1.add_attachement("Check_file.json")

email_2 = email.clone()
email_2.add_attachement("Email2.pdf")

print(email_1)
print(email_2)

print(id(email_1),   id(email_2))



# OUTPUT
# Email(from=ankita@gmail.com, to=Bhive@workspace.com, subject=Greetings of the day)
# Email(from=ankita@gmail.com, to=Bhive@workspace.com, subject=Greetings of the day)
# 4339592016 4339591632


"""
From: ankita@gmail.com
To: Bhive@workspace.com
Subject: Greetings of the day
Body: Hi Welcome to bhive
Attachment:: ['Check_file.json']

From: ankita@gmail.com
To: Bhive@workspace.com
Subject: Greetings of the day
Body: Hi Welcome to bhive
Attachment:: ['Email2.pdf']

4335954896 4335954512
"""