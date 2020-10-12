from yiche_android.yiche_page.app import App


class TestModelAskPrice:
    def test_model_ask_price(self):
        btn = App().start().main().goto_search_brand().select_Model().goto_model().goto_model_ask_price()
        assert btn == "获取底价"
