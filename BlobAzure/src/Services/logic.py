from BlobAzure.src.utils.db import init_db
from BlobAzure.src.utils.common.etl_utils import create_dataframe, show_dataframe
from BlobAzure.src.Services.load_sample_data import Load_data

class ETLService:

    def run_etl(self):
        self.transforms_load()

    def transforms_load(self):
        
        db_session, transaction_repository,employee_repository = init_db()

        try:
            extracted_data = Load_data()

            for item in extracted_data:
                if item['file_name'] == 'sales_data.csv':
                    df = create_dataframe(item['file_data'], item['tag'])
                    df2 = df.copy()
                    df2['Total_price'] = df2['Sales_Amount']
                    show_dataframe(item['tag'], item['file_name'], df2)
                    
            
                    transactions = df2.to_dict(orient='records')
                    for transaction_data in transactions:
                        transaction_repository.create_transaction(transaction_data)

                else:
                    df = create_dataframe(item['file_data'], item['tag'])
                    show_dataframe(item['tag'], item['file_name'], df)
                    transactions = df.to_dict(orient='records')
                    for transaction_data in transactions:
                        employee_repository.create_transaction(transaction_data)

            # all_transactions = transaction_repository.get_all_transactions()
            # employee_repository_transactions = employee_repository.get_all_transactions()



            # print("All Transactions:")
            # for transaction in all_transactions:
            #     print(transaction.__dict__)


        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            
            db_session.close()

        # return extracted_data
    

    
        
