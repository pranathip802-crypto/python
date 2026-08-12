
from abc import ABC, abstractmethod

class CloudStorage(ABC):

    @abstractmethod
    def upload(self, file):
        pass


class GoogleDrive(CloudStorage):

    def upload(self, file):
        print(file, "uploaded to Google Drive")


class AWSStorage(CloudStorage):

    def upload(self, file):
        print(file, "uploaded to AWS")


class AzureStorage(CloudStorage):

    def upload(self, file):
        print(file, "uploaded to Azure")


storages = [GoogleDrive(), AWSStorage(), AzureStorage()]

for storage in storages:
    storage.upload("document.pdf")