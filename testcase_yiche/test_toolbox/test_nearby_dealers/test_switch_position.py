from yiche_android.yiche_page.app import App


class TestSwitchPosition:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_switch_position(self):
        addr = self.main.start().my().more().goto_nearby_dealers().switch_position()
        assert "深圳" in addr