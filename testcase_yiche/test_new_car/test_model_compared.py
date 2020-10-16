from yiche_android.app import App


class TestModelCompared:
    def test_model_compared(self):
        result = App().start().main().goto_search_brand().select_Model().goto_model().goto_model_compared()
        assert result == "已加"