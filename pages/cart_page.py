from playwright.sync_api import Page, expect

class CartPage:

    def __init__(self, page: Page):
        self.__page = page
        self.__url = "https://www.saucedemo.com/cart.html"
        self.__your_cart = page.locator('[data-test="title"]')
        self.__continue_shopping = page.locator('[data-test="continue-shopping"]')
        self.__checkout = page.locator('[data-test="checkout"]')


    #Methods

    def click_continue_shopping(self):
        self.__continue_shopping.click()

    def click_checkout(self):
        self.__checkout.click()


    #Assertsions

    def expect_your_cart(self):
        expect(self.__your_cart).to_have_text("Your Cart")

    def expect_url(self):
        expect(self.__page).to_have_url(self.__url)

    def checkout_button_visible(self):
        expect(self.__checkout).to_be_visible()

    def continue_shopping_button_visible(self):
        expect(self.__continue_shopping).to_be_visible()





