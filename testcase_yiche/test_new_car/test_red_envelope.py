from yiche_android.app import App


class TestRedEnvelope:
    def test_red_envelope(self):
        content = App().start().main().goto_search_brand().select_Model().goto_red_envelope()
        assert content == "购车红包1000元"
