import pytest

from yiche_android.yiche_page.base_page import BasePage


class ModelComparison(BasePage):
    def model_comparison(self):
        pass

    # 添加车款
    def add_model(self, value):
        # self._params["value"] = value
        # self.steps("../../../yiche_yaml/add_model.yaml")
        self.find(by="xpath", locator='//*(@text="添加车款")').click()
        self.find(by="id", locator="searchEdtTxt").send_keys("奔驰GLC")
        self.find(by="xpath", locator='//*[@text="奔驰GLC"]').click()
        self.find(by="xpath", locator='//*[contains(@text, "动感型")]').click()

        self.find(by="xpath", locator='//*(@text="添加车款")').click()
        self.find(by="id", locator="searchEdtTxt").send_keys("路虎")
        self.find(by="xpath", locator='//*[@text="揽胜极光"]').click()
        self.find(by="xpath", locator='//*[contains(@text, "动感型")]').click()
        btn_compare_start = self.find(by="id", locator="compare_start_txt")
        if btn_compare_start.is_clickable() == True:
            return