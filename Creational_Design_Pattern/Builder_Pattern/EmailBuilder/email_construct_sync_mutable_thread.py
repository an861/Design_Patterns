# SYNCHRONOUS MUTABLE WITH THREAD LOCK
import threading

class SyncEmail:
    def __init__(self, sender, recepients, subject, body, attachments)->None:
        self.sender = sender
        self.recepients = recepients or []
        self.subject= subject
        self.body = body
        self.attachments = attachments or []

    def __str__(self)->str:
        return f"Email(from={self.sender}, to={self.recepients}, subject={self.subject})"
    
    def to_dict(self):
        return self.__dict__
    


class EmailBuilder:
    _lock = threading.Lock()

    def __init__(self)->None:
       self._reset()

    def _reset(self):
        self.sender = None
        self.recepients = []
        self.subject= None
        self.body = None
        self.attachments = []

    def set_sender(self, sender):
        with self._lock:
            self.sender= sender
        return self
    
    def set_recepients(self, recepient):
        with self._lock:
            self.recepients.append(recepient)
        return self
    
    def set_subject(self, subject):
        with self._lock:
            self.subject = subject
        return self
    
    def set_body(self, body):
        with self._lock:
            self.body = body
        return self
    
    def set_attachments(self, attachment):
        with self._lock:
            self.attachments.append(attachment)
        return self

    def build(self):
        """Creates final Email object and resets builder for next use"""
        with self._lock:
            email = SyncEmail(self.sender, self.recepients, self.subject, self.body, self.attachments)
            self._reset()
            return email
    

# sync_builder = EmailBuilder()
# email_sync = (sync_builder.set_sender("ankita@gmail.com")
#                           .set_recepients("bhive@workspace.com")
#                           .set_subject("Sync Email")
#                           .set_body("This is a test email")
#                           .set_attachments("file.pdf")
#                           .build()
#                           )


# OUTPUT
# Email(from=ankita@gmail.com, to=['bhive@workspace.com'], subject=Sync Email)



email_sync = (EmailBuilder()
         .set_sender("ankita@gmail.com")
         .set_recepients("bhive@workspace.com")
         .set_subject("Greetings Bhive")
         .set_body("This is an automated email.")
         .set_attachments("file.pdf")
         .build()
        )

print(email_sync)


# OUTPUT
# Email(from=ankita@gmail.com, to=['bhive@workspace.com'], subject=Greetings Bhive)


