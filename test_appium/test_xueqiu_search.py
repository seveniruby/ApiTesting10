# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
import pytest
from hamcrest import *
from selenium.webdriver.common.by import By


class TestXueqiu:
    def setup_class(self):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True
        #caps['unicodeKeyboard']= True
        #caps['resetKeyboard']= True
        caps['automationName']='uiautomator2'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        #等待元素出现
        print(self.driver.find_element(By.ID, "image_cancel").location)
        self.driver.find_element(By.ID, "image_cancel").click()
        self.driver.find_element_by_id("user_profile_icon")

    def setup(self):
        pass

    def teardown(self):
        self.driver.find_element_by_id("action_close").click()

    def teardown_class(self):
        sleep(10)
        self.driver.quit()

    @pytest.mark.parametrize("keyword, stock_type, expect_price", [
        ('alibaba', 'BABA', 170),
        ('xiaomi', '01810', 8.5)
    ])
    def test_search(self, keyword, stock_type, expect_price):
        self.driver.find_element_by_id("home_search").click()

        #self.driver.find_element_by_id("search_input_text").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        sleep(1)
        print(self.driver.page_source)
        self.driver.find_element_by_id("name").click()
        price=float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='"+ stock_type + "']/../../.."
            "//*[contains(@resource-id, 'current_price')]").text)
        print(price)
        assert price>expect_price
        assert_that(price, close_to(expect_price, expect_price*0.1))




