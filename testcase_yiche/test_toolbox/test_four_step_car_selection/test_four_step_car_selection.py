from yiche_android.app import App


class TestFourStepCarSelection:
    def test_four_step_car_selection(self):
        ask_price_btn = App().start().my().goto_four_step_car_selection().four_step()
        assert ask_price_btn == "获取底价"