# ASYNCHRONOUS + IMMUTABLE
import asyncio

class AsyncEmail:
    def __init__(self, sender: str = None, subject: str = None, body: str = None, recepients: list = None, attachments: list = None)->None:
        self.sender = sender
        self.subject = subject
        self.body = body
        self.recepients = recepients or []
        self.attachments = attachments or []

    def __repr__(self)->str:
        return f"Email(from={self.sender}, to={self.recepients}, subject={self.subject})"
    
    def to_dict(self)->dict:
        return self.__dict__
    

class AsyncEmailBuilder:
    def __init__(self)->None:
        self._sender = None
        self._subject = None
        self._body = None
        self._recepients = []
        self._attachments = []

    def _clone_with(self, **kwargs: dict):
        new_builder = AsyncEmailBuilder()
        new_builder._sender = kwargs.get("sender", self._sender)
        new_builder._subject = kwargs.get("subject", self._subject)
        new_builder._body = kwargs.get("body", self._body)
        new_builder._recepients = kwargs.get("recepients", self._recepients)
        new_builder._attachments = kwargs.get("attachments", self._attachments)
        return new_builder
    
    async def set_sender(self, sender: str):
        return self._clone_with(sender=sender)
    
    async def set_subject(self, subject: str):
        return self._clone_with(subject=subject)
    
    async def set_body(self, body):
        return self._clone_with(body=body)
    
    async def set_recepients(self, recepients: list):
        return self._clone_with(recepients=recepients)
    
    async def set_attachment(self, attachment):
        return self._clone_with(attachment = self._attachments+[attachment])

    async def build(self):
        return AsyncEmail(self._sender, self._subject, self._body, self._recepients, self._attachments)
    

async def main():
    async_email_builder = AsyncEmailBuilder()
    email = (await (await (await (await (await (await async_email_builder.set_sender("ankita@gmail.com"))
                                          .set_recepients("saha@bhive.com"))
                                          .set_subject("Async Email"))
                                          .set_body("This is an optimized async email"))
                                          .set_attachment("file.pdf"))
                                          .build())
    print(email)

asyncio.run(main())


# OUTPUT
# Email(from=admin@example.com, to=user@example.com, subject=Async Email)

