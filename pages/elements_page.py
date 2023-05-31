import time

from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators
class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('sdf')
        self.element_is_visible(self.locators.EMAIL).send_keys('sdf@sd.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('dsf')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('sdf')
        self.element_is_visible(self.locators.SUBMIT).click()
