from yiche_android.app import App


class TestReset:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_reset(self):
        btn_clear = self.main.start().my().goto_cal().reset()
        assert btn_clear == "清空历史"