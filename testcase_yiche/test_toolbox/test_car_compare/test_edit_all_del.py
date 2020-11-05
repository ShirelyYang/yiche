from yiche_android.app import App


class TestEditAllDel:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_edit_all_del(self):
        empty_info = self.main.start().my().goto_model_comparison().edit_all_del()
        return empty_info == "暂无车款信息！快去添加车型对比吧"
