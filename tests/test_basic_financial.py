import requests
import pytest
from configs.config import BASE_URL, API_KEY
from logs.logger import logger

def test_basic_financials_without_api():
    endpoint = f'{BASE_URL}/stock/metric?symbol=AAPL&metric=all'
    response = requests.get(endpoint)
    logger.info(f"#### Testing Endpoint {endpoint} ####")
    assert response.status_code == 401
    logger.info(f"Test status code is {response.status_code}")

def test_basic_financials_with_api():
    endpoint = f'{BASE_URL}/stock/metric?symbol=AAPL&metric=all{API_KEY}'
    response = requests.get(endpoint)
    data = response.json()
    logger.info(f"#### Testing Endpoint {endpoint} ####")
    assert (
        response.status_code == 200
        and len(data) == 4
        and response.elapsed.total_seconds() < 1)

def test_basic_financials_keys():
    endpoint = f'{BASE_URL}/stock/metric?symbol=AAPL&metric=all{API_KEY}'
    response = requests.get(endpoint)
    data = response.json()
    expected_keys = {'metric', 'metricType', 'series', 'symbol'}
    actual_keys = set(data.keys())
    diffs = expected_keys.symmetric_difference(actual_keys)
    logger.info(f'#### Testing Endpoint {endpoint} ####')
    assert len(diffs) == 0
    logger.info("No differences in test data from expected result.")
