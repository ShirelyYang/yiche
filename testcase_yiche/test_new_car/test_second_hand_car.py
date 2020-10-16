from yiche_android.app import App


class TestSecondHandCar:
    def test_second_hand_car(self):
        res_title = App().start().main().goto_search_brand().select_Model().goto_second_hand_car()
        assert res_title == "宝马5系 2018款 改款 530Li 尊享版 M运动套装"