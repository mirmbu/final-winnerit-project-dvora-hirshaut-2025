from playwright.sync_api import Page, expect

class CheckoutComplete:

    def __init__(self, page: Page):
        self.__page = page
        self.__url = "https://www.saucedemo.com/checkout-complete.html"
        self.__title = page.locator('[data-test="title"]')
        self.__thank_you = page.locator('[data-test="complete-header"]')
        self.__back_home = page.locator('[data-test="back-to-products"]')


    #Methods
    def click_back_home(self):
        self.__back_home.click()

    #Assertions
    def expect_url(self):
        expect(self.__page).to_have_url(self.__url)

    def expect_thank_you(self):
        expect(self.__thank_you).to_contain_text("Thank you for your order!")