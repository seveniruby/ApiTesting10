# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup_class(self):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #caps['autoGrantPermissions'] = True
        #caps["avd"]="Pixel_2_API_27"
        #caps["networkSpeed"]="gsm"
        #caps["dontStopAppOnReset"]="true"
        caps["noReset"]="true"

        #fast
        # caps["skipUnlock"]=True
        # caps["skipLogcatCapture"]=True
        # caps["disableAndroidWatchers"]=True
        # caps["ignoreUnimportantViews"]=True
        # caps["skipServerInstallation"]=True
        # caps["systemPort"]=6790

        #todo： 使用path变量更可靠
        #caps["chromedriverExecutableDir"] = '/Users/seveniruby/projects/chromedriver/2.20/'
        #caps["chromedriverUseSystemExecutable"]=True
        caps["chromedriverExecutable"] = '/Users/seveniruby/projects/chromedriver/2.20/chromedriver'
        caps['showChromedriverLog']=True


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        #等待元素出现

        def click_cancel(x):
            size=len(self.driver.find_elements(By.ID, "image_cancel"))
            if size>=1:
                print("displayed")
                self.driver.find_element(By.ID, "image_cancel").click()
            else:
                print("no displayed")

            return size >= 1

        #WebDriverWait(self.driver, 10, 1, ignored_exceptions=[TimeoutException]).until(expected_conditions.visibility_of_element_located((By.ID, 'image_cancel')))
        #WebDriverWait(self.driver, 5, 1, ignored_exceptions=[TimeoutException]).until_not(click_cancel)

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

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        #返回的是不带webview的组件，默认是找不到webview内的元素，除非设置了等待
        print(self.driver.page_source)
        #原生定位
        self.driver.find_element(MobileBy.ID, 'page_type_fund').click()

        WebDriverWait(self.driver, 20, 1).until(lambda x: "WEBVIEW_com.xueqiu.android" in self.driver.contexts)
        print("=======webview load")
        #返回的是带有webview组件树，此时可以使用原生定位去定位webview内的元素
        print(self.driver.page_source)
        #使用原生定位方式定位webview控件
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "蛋卷基金安全开户").click()

        self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
        print("======webview enter")
        #返回的是html，此次可以使用selenium的css定位
        print(self.driver.page_source)
        self.driver.find_element(By.NAME, "tel").send_keys("15600534760")
        self.driver.find_element(By.NAME, "captcha").send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR, ".dj-button").click()


    def test_webview_2(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        #返回的是不带webview的组件，默认是找不到webview内的元素，除非设置了等待
        print(self.driver.page_source)
        #原生定位


        WebDriverWait(self.driver, 20, 1).until(lambda x: "WEBVIEW_com.xueqiu.android" in self.driver.contexts)
        print("=======webview load")
        #返回的是带有webview组件树，此时可以使用原生定位去定位webview内的元素
        print(self.driver.page_source)
        self.driver.find_element(By.CSS_SELECTOR, '')


    def test_screenshot(self):
        print(self.driver.start_recording_screen())
        self.driver.save_screenshot("1.png")
        trade=self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']")
        trade.screenshot("2.png")
        trade.click()
        #self.driver.orientation
        sleep(3)
        self.driver.stop_recording_screen()


    def test_log(self):
        print(self.driver.log_types)
        print(self.driver.get_log("logcat"))


    def test_network(self):
        self.driver.send_sms("15600534760", "hello veryone, from hogwarts")
        sleep(2)
        self.driver.make_gsm_call("15600534760", "call")

    def test_perf(self):
        print(self.driver.get_performance_data_types())
        sleep(20)

        for p in self.driver.get_performance_data_types():
            print(self.driver.get_performance_data("com.xueqiu.android", p))

    def test_notification(self):
        self.driver.open_notifications()
        sleep(3)
        print(self.driver.page_source)
        self.driver.keyevent(4)
        self.driver.launch_app()
