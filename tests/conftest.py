import pytest
from pages.cart_page import CartPage
from pages.checkout_complete import CheckoutComplete
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview import CheckoutOverview
from pages.product_page import ProductPage
from pages.products_page import ProductsPage
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
def products(page: Page):
    products = ProductsPage(page)
    return products

@pytest.fixture
def cart(page: Page):
    cart = CartPage(page)
    return cart

@pytest.fixture
def checkout_information(page: Page):
    information = CheckoutInformationPage(page)
    return information

@pytest.fixture
def checkout_overview(page: Page):
    overview = CheckoutOverview(page)
    return overview

@pytest.fixture
def checkout_complete(page: Page):
    complete = CheckoutComplete(page)
    return complete

@pytest.fixture
def base_reqres_url():
    return "https://reqres.in/"


@pytest.fixture
def headers():
    return {"x-api-key": os.getenv("X_API_KEY")}
