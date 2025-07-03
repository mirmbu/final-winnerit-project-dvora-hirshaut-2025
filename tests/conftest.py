import pytest
from pages.cart_page import CartPage
from pages.item_page import ItemPage
from pages.items_page import ItemsPage
from pages.login_page import LoginPage
from playwright.sync_api import Page
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def login(page: Page):
    lp = LoginPage(page)
    lp.navigate()
    return lp

@pytest.fixture
def items(page: Page):
    items = ItemsPage(page)
    return items

@pytest.fixture
def cart(page: Page):
    cart = CartPage(page)
    return cart

@pytest.fixture
def base_reqres_url():
    return "https://reqres.in/"


@pytest.fixture
def headers():
    return {"x-api-key": os.getenv("X_API_KEY")}
