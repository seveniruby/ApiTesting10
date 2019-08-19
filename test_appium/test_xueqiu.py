# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
import pytest
from hamcrest import *


class TestXueqiu:
    def setup_class(self):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        #等待元素出现
        self.driver.find_element_by_id("user_profile_icon")

    def setup(self):
        pass

    def teardown_class(self):
        sleep(10)
        self.driver.quit()

    def test_profile(self):

        self.driver.find_element_by_id("user_profile_icon").click()

    def test_click(self):
        self.driver.tap()

    def test_sendkeys(self):
        self.driver.keyevent()
    def test_get_attribute(self):
        print(self.driver.find_element_by_id("user_profile_icon").get_attribute("class"))

    def test_source(self):
        print(self.driver.find_element_by_id("user_profile_icon").get_attribute("class"))
        print(self.driver.page_source)

    def test_selected_delete(self):
        pass
        #self.driver.find_element_by_xpath("//*[@text='行情']").click()
        #self.driver.find_element_by_xpath("//*[contains(@text, '新增手势')]").click()
    def test_swipe(self):

        for i in range(5):
            self.driver.swipe(500, 900, 100, 200, 1000)


    @pytest.fixture()
    def search_fixture(self):
        yield
        self.driver.find_element_by_id("action_close").click()

    @pytest.mark.parametrize("keyword, stock_type, expect_price", [
        ('alibaba', 'BABA', 170),
        ('xiaomi', '01810', 8.5)
    ])
    def test_search(self, search_fixture, keyword, stock_type, expect_price):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()
        price=float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='"+ stock_type + "']/../../.."
            "//*[contains(@resource-id, 'current_price')]").text)
        print(price)
        assert price>expect_price
        assert_that(price, close_to(expect_price, expect_price*0.1))

