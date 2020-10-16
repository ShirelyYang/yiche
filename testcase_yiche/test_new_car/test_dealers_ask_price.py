from yiche_android.app import App


class TestDalersAskPrice:
    def test_dalers_ask_price(self):
        btn = App().start().main().goto_search_brand().select_Model().goto_model().goto_dealers_ask_price()
        assert btn == "获取底价"