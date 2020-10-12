from yiche_android.yiche_page.app import App


class TestVideo:
    def test_video(self):
        child_title = App().start().main().goto_search_brand().select_Model().goto_video()
        assert child_title == "2021款宝马5系升级了哪些"