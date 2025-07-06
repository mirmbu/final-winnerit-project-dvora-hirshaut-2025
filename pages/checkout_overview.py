from playwright.sync_api import Page, expect
from assertpy import assert_that

class CheckoutOverview:

    def __init__(self, page: Page):
        self.__page = page
        self.__url = "https://www.saucedemo.com/checkout-step-two.html"
        self.__title = page.locator('[data-test="title"]')
        self.__price = page.locator('[data-test="inventory-item-price"]')
        self.__total = page.locator('[data-test="subtotal-label"]')
        self.__finish = page.locator('[data-test="finish"]')

    #Methods
    def click_finish_button(self):
        self.__finish.click()

    #Assertions

    def expect_url(self):
        expect(self.__page).to_have_url(self.__url)

    def expect_title(self):
        expect(self.__title).to_contain_text("Overview")

    def expect_price(self):
        prices = [float(self.__price.nth(p).inner_text().replace('$','')) for p in range(self.__price.count())]
        total = (self.__total.text_content()).replace("Item total: $", '')
        assert_that(sum(prices)).is_equal_to(float(total))

