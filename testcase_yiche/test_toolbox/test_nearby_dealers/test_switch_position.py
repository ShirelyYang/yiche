from yiche_android.app import App


class TestSwitchPosition:
    def test_switch_position(self):
        addr = App().start().my().more().goto_nearby_dealers().switch_position()
        assert "深圳" in addr