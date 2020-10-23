from yiche_android.app import App


class TestThreeStepCarSelection:
    def test_three_step_car_selection(self):
        btn = App().start().my().goto_four_step_car_selection().three_step()
        assert "确定意向车款" in btn
