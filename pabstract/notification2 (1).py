from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def schedule(self):
        pass


class Email(Notification):

    def send(self):
        print("Email notification sent")

    def schedule(self):
        print("Email notification scheduled")


class SMS(Notification):

    def send(self):
        print("SMS notification sent")

    def schedule(self):
        print("SMS notification scheduled")


class WhatsApp(Notification):

    def send(self):
        print("WhatsApp notification sent")

    def schedule(self):
        print("WhatsApp notification scheduled")


email = Email()
sms = SMS()
whatsapp = WhatsApp()

email.send()
email.schedule()

sms.send()
sms.schedule()

whatsapp.send()
whatsapp.schedule()