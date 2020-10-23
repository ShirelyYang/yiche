from yiche_android.app import App


class TestMap:
    def test_map(self):
        addr = App().start().my().more().goto_nearby_dealers().map()
        assert addr == "泉州展览城"
