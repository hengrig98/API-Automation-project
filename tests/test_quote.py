import requests
import pytest
from configs.config import BASE_URL, API_KEY
from logs.logger import logger

def test_get_quote_without_apikey():
    endpoint = f'{BASE_URL}/quote?symbol=AAPL'
    response = requests.get(endpoint)
    logger.info(f'#### Testing Endpoint {endpoint} ####')
    logger.info(f'Test status code is {response.status_code}')
    assert response.status_code == 401

def test_get_quote():
    endpoint = f'{BASE_URL}/quote?symbol=AAPL{API_KEY}'
    response = requests.get(endpoint)
    data = response.json()
    logger.info(f'#### Testing Endpoint {endpoint} ####')
    logger.info(f'Test status code is {response.status_code}')
    assert (
        response.status_code == 200
        and len(data) == 8
        and response.elapsed.total_seconds() < 1
        )

def test_get_quote_datatypes():
    endpoint = f'{BASE_URL}/quote?symbol=AAPL{API_KEY}'
    response = requests.get(endpoint)
    data = response.json()
    logger.info(f'#### Testing Endpoint {endpoint} ####')
    logger.info(f'Test data type is int/float.')
    for value in data.values():
        assert type(value) in [int, float]

def test_get_quote_keys():
    endpoint = f'{BASE_URL}/quote?symbol=AAPL{API_KEY}'
    response = requests.get(endpoint)
    data = response.json()
    expected_keys = {'c', 'd', 'dp', 'h', 'I', 'o', 'pc'}
    actual_keys = set(data.keys())
    diffs = expected_keys.symmetric_difference(actual_keys)
    logger.info(f'#### Testing Endpoint {endpoint} ####')
    logger.info(f'No differences in test data from expected result.')
    assert len(diffs) == 0

tickers = ['AAPL', 'MSFT', 'TSLA']
@pytest.mark.parametrize("ticker", tickers)
def test_get_several_quotes(ticker):
    endpoint = f'{BASE_URL}/quote?symbol={ticker}{API_KEY}'
    response = requests.get(endpoint)
    logger.info(f'#### Testing Endpoint {endpoint} ####')
    logger.info(f'Test status code is {response.status_code}')
    assert response.status_code == 200