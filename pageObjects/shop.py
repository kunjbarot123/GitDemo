from tabnanny import check
from time import sleep

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By

from pageObjects.checkout_page import checkout_Confirmation
from pageObjects.login import LoginPage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.shop_click=(By.CSS_SELECTOR, " a[href*='shop']")
        self.products_onpage = (By.XPATH, "//div[@class='card h-100']")
        self.checkoutbutton = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_to_cart_product(self, productName):
        self.driver.find_element(*self.shop_click).click()
        products = self.driver.find_elements(*self.products_onpage )

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == productName:
                product.find_element(By.XPATH, "div/button").click()



    def goToCart(self):
        self.driver.find_element(*self.checkoutbutton).click()
        checkout_confirmation = checkout_Confirmation (self.driver)
        return checkout_confirmation