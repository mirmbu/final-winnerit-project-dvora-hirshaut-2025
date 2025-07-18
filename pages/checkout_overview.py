from playwright.sync_api import Page, expect
from assertpy import assert_that
from pages.product_page import ProductPage


class CheckoutOverview:

    def __init__(self, page: Page):
        self.__page = page
        self.__url = "https://www.saucedemo.com/checkout-step-two.html"
        self.__title = page.locator('[data-test="title"]')
        self.__price = page.locator('[data-test="inventory-item-price"]')
        self.__total_price = page.locator('[data-test="subtotal-label"]')
        self.__finish = page.locator('[data-test="finish"]')
        self.__cancel = page.locator('[data-test="cancel"]')
        self.__product = ProductPage(page)

    #Methods
    def click_finish_button(self):
        self.__finish.click()

    #click to see the details of a product
    def click_details(self, id: int):
        self.__page.locator(f'[id="item_{id}_title_link"]').click()
        expect(self.__page).to_have_url(f"https://www.saucedemo.com/inventory-item.html?id={id}")
        self.__product.back_to_products()

    def click_cancel(self):
        self.__cancel.click()


    #Assertions
    def expect_url(self):
        expect(self.__page).to_have_url(self.__url)

    def expect_title(self):
        expect(self.__title).to_contain_text("Overview")

    #assert of the prices of all the product is same to the total price.
    def expect_price(self):
        prices = [float(self.__price.nth(p).inner_text().replace('$','')) for p in range(self.__price.count())]
        total = (self.__total_price.text_content()).replace("Item total: $", '')
        assert_that(sum(prices)).is_equal_to(float(total))

