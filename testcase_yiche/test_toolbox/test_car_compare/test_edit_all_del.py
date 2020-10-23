from yiche_android.app import App


class TestEditAllDel:
    def test_edit_all_del(self):
        empty_info = App().start().my().goto_model_comparison().edit_all_del()
        return empty_info == "暂无车款信息！快去添加车型对比吧"
