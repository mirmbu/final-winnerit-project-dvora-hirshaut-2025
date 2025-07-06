from playwright.sync_api import Page, expect

class CheckoutInformationPage:

    def __init__(self, page: Page):
        self.__page = page
        self.__url = "https://www.saucedemo.com/checkout-step-one.html"
        self.__title = page.locator('[data-test="title"]')
        self.__firstName = page.locator('[data-test="firstName"]')
        self.__lastName = page.locator('[data-test="lastName"]')
        self.__zip = page.locator('[data-test="postalCode"]')
        self.__continue = page.locator('[data-test="continue"]')
        self.__cancel = page.locator('[data-test="cancel"]')


    #Methods

    def type_first_name(self, first_name):
        self.__firstName.press_sequentially(first_name, delay=100)

    def type_last_name(self, last_name):
        self.__lastName.press_sequentially(last_name, delay=100)

    def type_zip_code(self, zip):
        self.__zip.fill(zip)

    def click_continue_button(self):
        self.__continue.click()


    def click_cancel_button(self):
        self.__cancel.click()


    #Assertions

    def expect_checkout_information_url(self):
        expect(self.__page).to_have_url(self.__url)

    def expect_checkout_your_information(self):
        expect(self.__title).to_contain_text("Your Information")

