from yiche_android.app import App


class TestTwoStepCarSelection:
    def test_two_step_car_selection(self):
        btn = App().start().my().goto_four_step_car_selection().two_step()
        assert "初步确定意向" in btn
