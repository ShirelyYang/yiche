from yiche_android.yiche_page.app import App


class TestParamConf:
    def test_param_conf(self):
        param_summary = App().start().main().goto_search_brand().select_Model().goto_paramconf()
        assert param_summary == "参数概述"