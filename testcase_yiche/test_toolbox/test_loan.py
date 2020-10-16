from yiche_android.app import App


class TestLoan:
    def test_loan(self):
        contains = App().start().my().goto_cal().loan()
        assert contains == "首付比例"