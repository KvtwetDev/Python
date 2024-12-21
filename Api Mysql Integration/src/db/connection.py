import mysql.connector
from config.database_config import DB_CONFIG
import logging

def connect_to_database():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        logging.info("Conexão bem sucedida")
        return connection
    except mysql.connector.Error as err:
        logging.error(f"Erro ao conectar: {err}")
        return None