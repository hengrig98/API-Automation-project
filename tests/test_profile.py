import requests
import pytest
from configs.config import BASE_URL, API_KEY
from logs.logger import logger

def test_get_company_profile_without_apikey():
    endpoint = f'{BASE_URL}/stock/profile2?symbol=AAPL'
    response = requests.get(endpoint)
    logger.info(f'#### Testing Endpoint {endpoint} ####')
    logger.info(f'Test status code is {response.status_code}')
    assert response.status_code == 401


def test_get_company_profile_data():
    endpoint = f'{BASE_URL}/stock/profile2?symbol=AAPL{API_KEY}'
    response = requests.get(endpoint)
    data = response.json()
    logger.info(f'#### Testing Endpoint {endpoint} ####')
    logger.info(f'Test data matches')
    assert (
        data.get('country') == "US"
        and data.get('currency') == "USD"
        and data.get('ipo') == "1980-12-12"
        and data.get('ticker') == "AAPL"
    )


