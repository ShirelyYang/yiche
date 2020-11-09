from yiche_android.yiche_page.app import App


class TestLoan:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_loan(self):
        contains = self.main.start().my().goto_cal().loan()
        assert contains == "首付比例"