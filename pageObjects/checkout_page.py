from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class checkout_Confirmation():

    def __init__(self, driver):
        self.driver = driver
        self.checkout_button =(By.XPATH, "//button[@class='btn btn-success']")
        self.country =(By.ID, "country")
        self.country_name_text = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")

    def Checkout(self):
        self.driver.find_element(*self.checkout_button).click()


    def enter_delivery_address(self,countryname):

        self.driver.find_element(*self.country).send_keys(countryname)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_name_text))
        self.driver.find_element(*self.country_name_text).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()


    def velidating_data(self):
        successText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in successText