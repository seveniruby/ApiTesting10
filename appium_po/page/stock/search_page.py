from selenium.webdriver.remote.webdriver import WebDriver

from appium_po.page.base_page import BasePage


class SearchPage(BasePage):


    def search(self, keyword):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")\
            .send_keys(keyword)
        return self

    def select(self, index):
        self.driver.find_elements_by_id("name")[index].click()
        return self

    def get_price(self, stock_type):
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='"
            + stock_type
            + "']/../../.."
            "//*[contains(@resource-id, 'current_price')]").text)
        return price

    def get_name(self):
        return self.driver.page_source



