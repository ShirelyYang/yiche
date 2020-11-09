from yiche_android.app import App


class TestSalesList:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_sales_list(self):
        type = self.main.start().my().more().goto_sales_ranking().sales_list()
        assert type == "国产/中大型SUV"
