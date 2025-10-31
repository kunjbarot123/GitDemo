import json
import os
import sys

import pytest

sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage

datajson_path = "../data/test_e2eframwork.json"
with open(datajson_path) as data_file:
    data = json.load(data_file)
    test_list=data["data"]

@pytest.mark.parametrize("test_item_list",test_list)
def test_e2e(browserInvokation, test_item_list):
    driver = browserInvokation
    print("im kunj")
    print("git testing")

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    print(loginPage.get_title())
    shop_page = loginPage.login(test_item_list["username"], test_item_list["password"])
    print(shop_page.goToCart())

    shop_page.add_to_cart_product(test_item_list["productName"])
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.Checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.velidating_data()






