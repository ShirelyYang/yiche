from yiche_android.app import App


class TestModelChange:
    def test_model_change(self):
        result = App().start().main().goto_search_brand().select_Model().goto_model().goto_model_change()
        assert result == "2018款 525Li 豪华设计套装"