from yiche_android.app import App


class TestPopularityList:
    def test_popularity_list(self):
        price = App().start().my().more().goto_sales_ranking().popularity_list()
        assert price == "142.98-189.88 万"
