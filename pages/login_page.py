from playwright.sync_api import Page, expect

class LoginPage:

    def __init__(self, page: Page):
        self.__page = page
        self.__username = page.locator('[name="user-name"]')
        self.__password = page.locator('[name="password"]')
        self.__login_button = page.locator('[name="login-button"]')
        self.__error_message = page.locator('[data-test="error"]')
        self.__credentials = page.locator('[data-test="login-credentials"]')
        self.__url = "https://www.saucedemo.com/"
        self.__products = page.locator('[data-test="title"]')


    #Methods

    def navigate(self):
        self.__page.goto(self.__url)

    def type_username(self, username):
        self.__username.press_sequentially(username, delay=100)

    def type_password(self, password):
        self.__password.fill(password)

    def click_login_button(self):
        self.__login_button.click()


    #Assertions

    def expect_error_message(self, message):
        expect(self.__error_message).to_have_text(message)

    def expect_credentials(self):
        expect(self.__credentials).to_be_visible()

    def expect_products_page(self):
        expect(self.__page).to_have_url(f"{self.__url}inventory.html")
        expect(self.__products).to_have_text("Products")



