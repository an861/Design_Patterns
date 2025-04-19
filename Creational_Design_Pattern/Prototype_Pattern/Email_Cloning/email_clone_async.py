# ASYNCHRONOUS

import asyncio
import copy

class AsyncEmail:
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
    
    async def send_emails(self):
        await asyncio.sleep(1)
        return f"Sent Email to {self.recepient} - Subject: {self.subject}"
    


async def main():
    email = AsyncEmail(sender="ankita@gmail.com", recepient="Bhive@workspace.com", subject="Promo Offer!", body="Hello, check out our new offer!", attachment="file.pdf")

    email_1 = email.clone()
    email_1.add_attachement("Joke.txt")
    email_1.recepient = "Bhive@alts.com"

    email_2 = email.clone()
    email_2.add_attachement("Change.json")
    email_2.add_attachement("Kite.pdf")

    await asyncio.gather(email_1.send_emails(), email_2.send_emails())
    print(email_1)
    print(email_2)
    print(email_1 is email_2)
    print(await email_1.send_emails())
    print(await email_2.send_emails())

asyncio.run(main())


# OUTPUT
"""
From: ankita@gmail.com
To: Bhive@alts.com
Subject: Promo Offer!
Body: Hello, check out our new offer!
Attachment:: ['Joke.txt']

From: ankita@gmail.com
To: Bhive@workspace.com
Subject: Promo Offer!
Body: Hello, check out our new offer!
Attachment:: ['Change.json', 'Kite.pdf']

False
Sent Email to Bhive@alts.com - Subject: Promo Offer!
Sent Email to Bhive@workspace.com - Subject: Promo Offer!
"""
