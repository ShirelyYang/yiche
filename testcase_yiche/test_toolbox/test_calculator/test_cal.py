from yiche_android.app import App


class TestCalculator:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_calculator(self):
        btn = self.main.start().my().goto_cal().cal()
        assert btn == "必要花费"





