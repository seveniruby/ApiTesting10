from appium_po.page.xueqiu_page import XueqiuPage


class TestTrade:
    def setup_class(self):
        self.xueqiu=XueqiuPage()
        self.trade = self.xueqiu.goto_trade()
        self.trade.goto_danjuan()
    def test_a_open(self):
        self.trade.a_open("15600534760", '1234')


    def test_danjuan_open(self):
        self.trade.danjuan_open()



