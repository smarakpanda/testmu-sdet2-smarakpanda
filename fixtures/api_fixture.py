import pytest

from config.config import get_value_from_config
from utils.api_client import APIClient
from api.account_client import AccountClient
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def api_client(playwright):
    request_context = playwright.request.new_context()
    base_url = get_value_from_config("api_base_url")
    return APIClient(base_url, request_context)


@pytest.fixture(scope="session")
def account_client(api_client):
    return AccountClient(api_client)