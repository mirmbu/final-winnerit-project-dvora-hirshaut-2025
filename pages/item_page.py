from playwright.sync_api import Page, expect

class ItemPage:

    def __init__(self, page: Page):
        self.__add_to_cart = page.get_by_role("button", name="Add to cart")
        self.__back_to_products = page.get_by_role("button", name="Back to products")



    def back_to_products(self):
        self.__back_to_products.click()

    def add_to_cart(self):
        self.__add_to_cart.click()

