from yiche_android.yiche_page.app import App


class TestPopularityList:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_popularity_list(self):
        type = self.main.start().my().more().goto_sales_ranking().popularity_list()
        assert type == "进口/中大型SUV"
