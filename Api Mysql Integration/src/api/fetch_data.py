import requests
import logging
from config.api_config import API_URL

def fetch_api_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        logging.info("Dados da API recebidos")
        return response.json()
    except requests.RequestException as err:
        logging.error(f"Erro ao consumir api: {err}")
        return None