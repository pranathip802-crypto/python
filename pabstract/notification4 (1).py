
from abc import ABC, abstractmethod

class Notification(ABC):

    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self):
        pass

    def display_message(self):
        print("Message:", self.message)


class Email(Notification):

    def send(self):
        print("Email sent")


email = Email("Welcome!")

email.send()
email.display_message()