from yiche_android.app import App


class TestCommentList:
    def test_comment_list(self):
        price = App().start().my().more().goto_sales_ranking().comment_list()
        assert price == "79.62-161.74 万"
