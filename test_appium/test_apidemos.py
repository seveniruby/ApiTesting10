# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu:
    def setup(self):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps['autoGrantPermissions'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def test_swipe(self):

        self.driver.swipe(500, 900, 100, 200, 1000)
        self.driver.find_element_by_accessibility_id("Views").click()

        for i in range(5):
            self.driver.swipe(500, 900, 100, 200, 1000)

    def test_swipe_percent(self):

        size=self.driver.get_window_size()
        print(size)
        width=size['width']
        height=size['height']

        self.driver.swipe(width*0.8, height*0.8, width*0.2, height*0.2, 1000)
        self.driver.find_element_by_accessibility_id("Views").click()

        for i in range(5):
            self.driver.swipe(width*0.8, height*0.8, width*0.2, height*0.2, 1000)

    def test_uiautomator(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().scrollable(true).instance(0))'
                                                        '.scrollIntoView('
                                                        'new UiSelector().text("Views").instance(0));').click()

        print("""
        new UiScrollable(
            new UiSelector().scrollable(true).instance(0)
        ).scrollIntoView(
            new UiSelector().text("Views").instance(0)
        );
        """)

        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().scrollable(true).instance(0))'
                                                        '.scrollIntoView('
                                                        'new UiSelector().text("Tabs").instance(0));').click()



    def teardown(self):
        sleep(10)
        self.driver.quit()