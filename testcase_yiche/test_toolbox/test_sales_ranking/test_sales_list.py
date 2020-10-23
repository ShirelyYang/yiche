from yiche_android.app import App


class TestSalesList:
    def test_sales_list(self):
        price = App().start().my().more().goto_sales_ranking().sales_list()
        assert price == "29.80-39.80 万"
