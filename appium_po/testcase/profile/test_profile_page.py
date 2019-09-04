from unittest import TestCase

from appium_po.page.xueqiu_page import XueqiuPage


class TestProfile:
    def setup(self):
        self.xueqiu=XueqiuPage()
        self.profile=self.xueqiu.goto_profile()

    def test_login_by_phone(self):
        source=self.profile.login_by_phone("15600534761", "1234").get_msg()
        print(source)
        assert '验证码已过期' in source

    def test_login_by_wechat(self):
        self.profile.login_by_wechat()
        print(self.profile.get_toast())
        assert "请先安装微信" in self.profile.get_toast()

    def test_login_by_weibo(self):
        self.fail()

    def test_login_by_qq(self):
        self.fail()
