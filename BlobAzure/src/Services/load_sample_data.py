from BlobAzure.src.utils.azure_blob import AzureBlob
from dotenv import load_dotenv
import re


load_dotenv()

def Load_data():
    
    
    service = AzureBlob()
    list_blob = service.list_blobs()

    data = []

    for blob_path in list_blob:


        file_name = blob_path.split("/")[-1]


        file_data = service.download_blob(blob_path)


        if blob_path.lower().endswith('.xml'):
            pass


        else:
            if blob_path.lower().endswith(('.xlsx', '.xls')):

                tag = 'Excel'
                data.append({'file_data': file_data, 'tag': tag, 'file_name': file_name}) 

            elif blob_path.lower().endswith('.csv'):
                if file_name == 'sales_data.csv':
                    tag = 'CSV'
                    data.append({'file_data': file_data, 'tag': tag, 'file_name': file_name})        

    return data



