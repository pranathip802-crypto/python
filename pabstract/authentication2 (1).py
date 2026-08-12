from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass


class PasswordAuth(Authentication):
    def login(self):
        print("Login using Password")


class OTPAuth(Authentication):
    def login(self):
        print("Login using OTP")


class GoogleAuth(Authentication):
    def login(self):
        print("Login using Google")


authentications = [
    PasswordAuth(),
    OTPAuth(),
    GoogleAuth()
]

for authentication in authentications:
    authentication.login()