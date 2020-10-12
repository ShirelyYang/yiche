from yiche_android.yiche_page.app import App


class TestInstallCar:
    def test_install_car(self):
        title = App().start().main().goto_search_brand().select_Model().goto_Install_car()
        assert title == "金融分期"