from appium_po.page.xueqiu_page import XueqiuPage


class TestAds:
    def setup(self):
        self.xueqiu=XueqiuPage()

    def test_ads(self):
        assert self.xueqiu.get_ads() == True