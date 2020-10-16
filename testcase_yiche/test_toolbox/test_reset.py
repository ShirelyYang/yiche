from yiche_android.app import App


class TestReset:
    def test_reset(self):
        btn_clear = App().start().my().goto_cal().reset()
        assert btn_clear == "清空历史"