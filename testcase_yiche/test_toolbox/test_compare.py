from yiche_android.app import App


class TestCompare:
    def test_compare(self):
        dealer_price = App().start().my().goto_model_comparison().start_compare()
        assert dealer_price == "经销商报价"