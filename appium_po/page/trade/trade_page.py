from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.base_page import BasePage


class TradePage(BasePage):
    _a_open=(MobileBy.ACCESSIBILITY_ID, 'A股开户')
    _danjuan_open = (MobileBy.ACCESSIBILITY_ID, '蛋卷基金安全开户')
    _danjuan_menu=(By.ID, "page_type_fund")
    def goto_danjuan(self):

        print(self.driver.find_element(*self._danjuan_menu).text)
        self.driver.find_element(*self._danjuan_menu).click()

    def a_open(self, phone, number):
        WebDriverWait(self.driver, 20, 2).until(
            expected_conditions.visibility_of_element_located(self._a_open))
        self.driver.find_element(*self._a_open).click()

        #todo

    def danjuan_open(self):
        WebDriverWait(self.driver, 20, 2).until(
            expected_conditions.visibility_of_element_located(self._danjuan_open))
        self.driver.find_element(*self._danjuan_open).click()





