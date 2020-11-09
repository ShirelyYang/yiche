from yiche_android.app import App


class TestCommentList:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_comment_list(self):
        type = self.main.start().my().more().goto_sales_ranking().comment_list()
        assert type == "进口/中大型SUV"
