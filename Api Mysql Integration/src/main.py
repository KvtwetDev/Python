import logging
from db.connection import connect_to_database
from db.table import create_table
from db.insert import insert_data
from api.fetch_data import fetch_api_data

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    setup_logger()

    connection = connect_to_database()
    if not connection:
        logging.error("Não foi possivel conectar")
        return
    
    create_table(connection)

    data = fetch_api_data()
    if not data:
        logging.error("Não foi possivel obter os dados")
        return
    
    insert_data(connection, data)

    connection.close()
    logging.info("Conexão com banco de dados fechada")

if __name__ == "__main__":
    main();

