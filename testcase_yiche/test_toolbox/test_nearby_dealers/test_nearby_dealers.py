from yiche_android.app import App


class TestNearbyDealers:
    def test_nearby_dealers(self):
        sales_title = App().start().my().more().goto_nearby_dealers().nearby_dealers()
        assert sales_title == "咨询销售顾问"
