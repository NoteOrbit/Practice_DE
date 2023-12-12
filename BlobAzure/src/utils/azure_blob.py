from azure.storage.blob import BlobServiceClient, ContentSettings
from dotenv import load_dotenv
import os

class AzureBlob:
    
    def __init__(self):


        load_dotenv()
        self.storage_account_url = os.getenv("STORAGEACCOUNTURL")
        self.container_name = os.getenv("CONTAINERNAME")
        self.sas_token = os.getenv("SAS_TOKEN")

        self.blob_service_client = BlobServiceClient(account_url=self.storage_account_url, credential=self.sas_token)
        
        self.container_client = self.blob_service_client.get_container_client(self.container_name)


    def upload_blob(self, blob_name, data, content_settings=None):
        try:
            self.container_client.upload_blob(name=blob_name, data=data, content_settings=content_settings)
            print(f"Blob '{blob_name}' uploaded to container '{self.container_name}'")
            return True
        except Exception as e:
            print(f"Error uploading blob '{blob_name}': {str(e)}")


    def download_blob(self, blob_name):
        try:
            blob_client = self.container_client.get_blob_client(blob_name)
            blob_data = blob_client.download_blob()
            return blob_data.readall()
        except Exception as e:
            print(f"Error downloading blob '{blob_name}': {str(e)}")
            return None


    def list_blobs(self):
        try:
            blob_list = self.container_client.list_blobs()
            return [blob.name for blob in blob_list]
        except Exception as e:
            print(f"Error listing blobs: {str(e)}")
            return []


    def copy_blob(self, blob_name, source_blob_url):
        try:
            copied_blob = self.blob_service_client.get_blob_client(self.container_name, blob_name)
            copied_blob.start_copy_from_url(source_blob_url)
            return True
        except Exception as e:
            print(f"Error copying blob '{blob_name}': {str(e)}")
            return False
        

    def delete_blob(self, blob_name):
        try:
            self.container_client.delete_blob(blob_name)
            return True
        except Exception as e:
            print(f"Error deleting blob '{blob_name}': {str(e)}")
            return False
        
    
    