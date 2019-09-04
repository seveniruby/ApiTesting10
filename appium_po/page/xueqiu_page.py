from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.base_page import BasePage
from appium_po.page.profile.profile_page import ProfilePage
from appium_po.page.stock.search_page import SearchPage
from appium_po.page.trade.trade_page import TradePage


class XueqiuPage(BasePage):

    driver=None
    app="com.xueqiu.android"
    activity=".view.WelcomeActivityAlias"

    _profile_icon = (By.ID, "user_profile_icon")

    def first_start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = self.app
        caps["appActivity"] = self.activity
        caps['autoGrantPermissions'] = True
        #caps['unicodeKeyboard']= True
        #caps['resetKeyboard']= True
        caps['noreset']=True
        caps['automationName']='uiautomator2'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        #等待元素出现
        # WebDriverWait(self.driver, 60).until(
        #     expected_conditions.visibility_of_element_located((By.ID, 'image_cancel'))
        # )
        #
        #
        # def click_cancel(x):
        #     elements=self.driver.find_elements(By.ID, "image_cancel")
        #     if len(elements)>=1:
        #         print("displayed")
        #         elements[0].click()
        #     else:
        #         print("no displayed")
        #
        #     return len(elements) >= 1
        #
        # WebDriverWait(self.driver, 60).until_not(click_cancel)

        XueqiuPage.driver=self.driver

    def __init__(self):
        if XueqiuPage.driver==None:
            self.first_start()
        else:
            print("launch")
            self.driver.start_activity(self.app, self.activity)


        self.find(self._profile_icon)
        # WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.ID, "user_profile_icon")))

    def goto_search(self):
        self.driver.find_element_by_id("home_search").click()
        return SearchPage(self.driver)

    def goto_profile(self):
        self.find(self._profile_icon).click()

        return ProfilePage(self.driver)

    def get_ads(self):
        return False

    def goto_trade(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        return TradePage(self.driver)



