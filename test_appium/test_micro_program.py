from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestMicroProgram:

    def setup_class(self):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = ".ui.LauncherUI"
        caps["noReset"]=True

        #caps['autoGrantPermissions'] = True
        #todo： 使用path变量更可靠
        #caps["chromedriverExecutableDir"] = '/Users/seveniruby/projects/chromedriver/2.20/'
        #caps["chromedriverUseSystemExecutable"]=True
        caps["chromedriverExecutable"] = '/Users/seveniruby/projects/chromedriver/2.30/chromedriver'


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)


    #todo：小程序发生变化
    def test_xueqiu(self):
        self.driver.find_element(By.XPATH, "//*[@text='文件传输助手']").click()
        self.driver.find_element(By.XPATH, "//*[@text='雪球股票']").click()


        for i in range(30):
            sleep(2)
            print("=======")
            print(i)
            print(self.driver.contexts)
            print(self.driver.page_source)
            if "WEBVIEW_com.tencent.mm:appbrand0" in self.driver.contexts:
                print("brand0")
                self.driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand0")
                print(self.driver.page_source)
                break



        self.driver.find_element(By.XPATH, "//*[@class='android.widget.Image']").click()
        self.driver.find_element(By.XPATH, "//*[@class='android.widget.EditText']").send_keys("alibaba")
        self.driver.find_element(By.XPATH, "//*[@text='阿里巴巴']").click()


    # def test_fat(self):
    #     # coding=utf-8
    #     from fastAutoTest.core.wx.wxEngine import WxDriver
    #     import os
    #
    #     # 进入企鹅医典小程序
    #     wxDriver = WxDriver()
    #     wxDriver.initDriver()
    #     # 点击全部疾病
    #     wxDriver.clickElementByXpath('/html/body/div[1]/div/div[3]/p')
    #     wxDriver.clickFirstElementByText('白内障')
    #     wxDriver.returnLastPage()
    #     wxDriver.returnLastPage()
    #     # 截图
    #     dirPath = os.path.split(os.path.realpath(__file__))[0]
    #     PIC_SRC = os.path.join(dirPath, 'pic.png')
    #     wxDriver.d.screenshot(PIC_SRC)
    #     wxDriver.close()

