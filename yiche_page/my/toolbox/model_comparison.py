import pytest
from appium.webdriver.common.mobileby import MobileBy

from yiche_android.yiche_page.base_page import BasePage


class ModelComparison(BasePage):
    # _btn_compare_start = BasePage().find(by="id", locator="compare_start_txt")
    # 添加车款
    def add_model(self):
        # self._params["value"] = value
        # self.steps("../../../yiche_yaml/add_model.yaml")
        # self.find(by="xpath", locator='//*[@text="添加车款"]').click()
        lis = self._driver.find_elements(MobileBy.ID, "compare_ll")
        btn_start_compare = self.find(by="id", locator="compare_start_txt")
        n = 0
        if len(lis) < 2:
            self.find(by="id", locator="compare_addcar_txt").click()
            self.find(by="id", locator="searchEdtTxt").send_keys("奔驰GLC")
            self.find(by="xpath", locator='//*[@text="奔驰GLC"]').click()
            self.find(by="xpath", locator='//*[contains(@text, "动感型")]').click()

            self.find(by="xpath", locator='//*(@text="添加车款")').click()
            self.find(by="id", locator="searchEdtTxt").send_keys("路虎")
            self.find(by="xpath", locator='//*[@text="揽胜极光"]').click()
            self.find(by="xpath", locator='//*[contains(@text, "动感型")]').click()
        else:
            radios = self._driver.find_elements(MobileBy.ID, "compare_sel_iv")
            for i in range(len(radios)):
                if "2" in btn_start_compare.text:
                    n += 1
                else:
                    radios[i].click()
                    n += 1
                if n > 2:
                    return True

    # 开始对比
    def start_compare(self):
        if self.add_model() is not True:
            self.add_model()
        self.find(by="id", locator="compare_start_txt").click()
        self.find(by="xpath", locator='//*[@text="综合对比"]').click()
        dealer_price = self.find(by="xpath", locator='//*[@text="经销商报价"]')
        return dealer_price.text