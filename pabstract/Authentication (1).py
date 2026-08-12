
from abc import ABC, abstractmethod

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


class PasswordAuth(Authentication):

    def login(self):
        print("Login using Password")

    def logout(self):
        print("Logged out from Password Authentication")


class OTPAuth(Authentication):

    def login(self):
        print("Login using OTP")

    def logout(self):
        print("Logged out from OTP Authentication")


password = PasswordAuth()
otp = OTPAuth()

password.login()
password.logout()

otp.login()
otp.logout()