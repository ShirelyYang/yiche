from yiche_android.yiche_page.app import App


class TestParamConf:
    def test_param_conf(self):
        info = App().start().main().goto_search_brand().select_Model().goto_paramconf()
        assert info == ("参数概述", "动力")