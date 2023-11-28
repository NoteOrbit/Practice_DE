from BlobAzure.src.Services.logic import ETLService

def main():
    a = ETLService()
    a.run_etl()

if __name__ == "__main__":
    main()
