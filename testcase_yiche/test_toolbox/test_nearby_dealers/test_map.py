from yiche_android.app import App


class TestMap:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_map(self):
        addr = self.main.start().my().more().goto_nearby_dealers().map()
        # 模拟器
        # assert addr == "泉州展览城-东门"
        # OPPO
        assert addr == "泉州展览城"
