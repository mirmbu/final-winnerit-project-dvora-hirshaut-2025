import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.navigate()
    return lp