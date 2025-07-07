from faker.utils.decorators import lowercase
from playwright.sync_api import Page, expect
from pages.item_page import ItemPage

class ItemsPage:

    def __init__(self, page: Page):
        self.__page = page
        self.__url = "https://www.saucedemo.com/inventory.html"
        self.__add_backpack = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.__add_bike_light = page.locator('[id="add-to-cart-sauce-labs-bike-light"]')
        self.__add_t_shirt = page.locator('[id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        self.__add_jacket = page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
        self.__add_onesie = page.locator('[data-test="add-to-cart-sauce-labs-onesie"]')
        self.__add_red_t_shirt = page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')
        self.__shopping_cart = page.locator('[data-test="shopping-cart-link"]')
        self.__sort = page.locator('[data-test="product-sort-container"]')
        self.__item = ItemPage(page)


    #Methods

    #enter to specific item page.
    def click_details(self, id):
        self.__page.locator(f'[id="item_{id}_title_link"]').click()
        expect(self.__page).to_have_url(f"https://www.saucedemo.com/inventory-item.html?id={id}")
        self.__item.back_to_products()
        expect(self.__page).to_have_url(self.__url)

    #add product by name
    def add_product_by_name(self, name):
        name = name.replace(" ", "-").lower()
        self.__add_product = self.__page.locator(f'[data-test="add-to-cart-{name}"]')
        self.__add_product.click()

    #remove product by name
    def remove_product_by_name(self, name):
        name = name.replace(" ", "-").lower()
        self.__remove_product = self.__page.locator(f'[data-test="remove-{name}"]')
        self.__remove_product.click()

    #click shopping chart
    def click_shopping_cart(self):
        self.__shopping_cart.click()


    # #add to chart
    # def add_backpack(self):
    #     self.__add_backpack.click()
    #
    # def add_bike_light(self):
    #     self.__add_bike_light.click()
    #
    # def add_t_shirt(self):
    #     self.__add_t_shirt.click()
    #
    # def add_jacket(self):
    #     self.__add_jacket.click()
    #
    # def add_onesie(self):
    #     self.__add_onesie.click()
    #
    # def add_red_t_shirt(self):
    #     self.__add_red_t_shirt.click()
    #



    #Assertions

    #sort the products
    def sort_products(self):
        self.__sort.select_option("Price (low to high)")
        expect(self.__sort).to_have_text("Price (low to high)")

    def expect_remove_button(self, name):
        name = name.replace(" ", "-").lower()
        expect(self.__page.locator(f'[id="remove-{name}"]')).to_have_text("Remove")


    def expect_url(self):
        expect(self.__page).to_have_url(self.__url)
