from yiche_android.yiche_page.app import App


class TestSmallVideo:
    def test_small_video(self):
        info = App().start().main().goto_search_brand().select_Model().goto_small_video()
        assert info == ("小视频", "15年宝马535Li  3.0T 爆改M5套件")