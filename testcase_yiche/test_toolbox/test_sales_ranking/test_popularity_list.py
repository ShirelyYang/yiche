from yiche_android.app import App


class TestPopularityList:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_popularity_list(self):
        price = self.main.start().my().more().goto_sales_ranking().popularity_list()
        assert price == "142.98-189.88 万"
