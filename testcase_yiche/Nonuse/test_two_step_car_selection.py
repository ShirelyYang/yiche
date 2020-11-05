from yiche_android.app import App


class TestTwoStepCarSelection:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_two_step_car_selection(self):
        btn = self.main.start().my().goto_four_step_car_selection().two_step()
        assert "初步确定意向" in btn
