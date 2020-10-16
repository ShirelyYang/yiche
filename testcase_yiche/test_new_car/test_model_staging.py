from yiche_android.app import App


class TestModelStaging:
    def test_model_staging(self):
        btn = App().start().main().goto_search_brand().select_Model().goto_model().goto_model_staging()
        assert btn == "申请贷款"