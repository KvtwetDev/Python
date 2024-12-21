import logging
import mysql.connector

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS api_database (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    value TEXT,
    timestamp DATETIME
);
"""

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(CREATE_TABLE_QUERY)
        connection.commit()
        logging.info("Tabela 'api' criada com sucesso")

    except mysql.connector.Error as err:
        logging.error(f"Erro ao criar: {err}")
