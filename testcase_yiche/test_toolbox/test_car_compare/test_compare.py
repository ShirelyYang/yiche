from yiche_android.app import App


class TestCompare:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_compare(self):
        dealer_price = self.main.start().my().goto_model_comparison().start_compare()
        assert dealer_price == "经销商报价"