import logging
import mysql.connector
from datetime import datetime

INSERT_QUERY = "INSERT INTO api_database (name, value, timestamp) VALUES (%s, %s, %s)"

def insert_data(connection, data):
    try:
        cursor = connection.cursor()
        for item in data:
            name = item['name']
            value = item['email'][:255]
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            cursor.execute(INSERT_QUERY, (name, value, timestamp))

        connection.commit()
        logging.info(f"{cursor.rowcount} registros inseridos")
    except mysql.connector.Error as err:
        logging.error(f"Erro ao inserir os dados: {err}")
    finally:
        cursor.close()

