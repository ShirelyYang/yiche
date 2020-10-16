from yiche_android.app import App


class TestLatestTransPrice:
    def test_latest_trans_price(self):
        info = App().start().main().goto_search_brand().select_Model().goto_latest_trans_price()
        assert info == ("本地最新成交价", "4*.59万")