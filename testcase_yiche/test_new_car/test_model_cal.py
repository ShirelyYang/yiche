from yiche_android.app import App


class TestModelCal:
    def test_model_cal(self):
        result = App().start().main().goto_search_brand().select_Model().goto_model().goto_model_cal()
        assert result == "北京成交价格"

