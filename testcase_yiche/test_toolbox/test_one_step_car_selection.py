from yiche_android.app import App


class TestFourStepCarSelection:
    def test_four_step_car_selection(self):
        ask_price_btn = App().start().my().goto_four_step_car_selection().one_step()
        assert "符合要求" in ask_price_btn