from yiche_android.app import App


class TestThreeStepCarSelection:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_three_step_car_selection(self):
        btn = self.main.start().my().goto_four_step_car_selection().three_step()
        assert "确定意向车款" in btn
