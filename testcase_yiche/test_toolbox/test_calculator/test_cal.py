from yiche_android.app import App


class TestCalculator:
    def test_calculator(self):
        btn = App().start().my().goto_cal().cal()
        assert btn == "必要花费"