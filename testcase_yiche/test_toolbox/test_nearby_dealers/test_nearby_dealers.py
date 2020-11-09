from yiche_android.yiche_page.app import App


class TestNearbyDealers:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_nearby_dealers(self):
        sales_title = self.main.start().my().more().goto_nearby_dealers().nearby_dealers()
        assert sales_title == "咨询销售顾问"
