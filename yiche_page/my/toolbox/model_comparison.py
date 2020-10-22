import pytest
from appium.webdriver.common.mobileby import MobileBy

from yiche_android.yiche_page.base_page import BasePage


class ModelComparison(BasePage):
    # _btn_compare_start = BasePage().find(by="id", locator="compare_start_txt")
    # 查找车款
    def search_car(self):
        self.find(by="id", locator="searchEdtTxt").click()
        self.find(by="id", locator="searchEt").send_keys("奔驰GLC")
        self.find(by="xpath", locator='//*[@resource-id="com.yiche.price:id/txtView" and @text="奔驰GLC"]').click()
        self.find(by="xpath", locator='//*[@text="奔驰GLC"]').click()
        self.find(by="xpath", locator='//*[contains(@text, "动感型")]').click()

        self.find(by="xpath", locator='//*(@text="添加车款")').click()
        self.find(by="id", locator="searchEdtTxt").send_keys("路虎")
        self.find(by="xpath", locator='//*[@resourceid="txtView" and @text="揽胜极光"]').click()
        self.find(by="xpath", locator='//*[@text="揽胜极光"]').click()
        self.find(by="xpath", locator='//*[contains(@text, "动感型")]').click()

    # 添加车款
    def add_model(self):
        # self._params["value"] = value
        # self.steps("../../../yiche_yaml/add_model.yaml")
        # self.find(by="xpath", locator='//*[@text="添加车款"]').click()
        try:
            lis = self._driver.find_elements(MobileBy.ID, "compare_ll")
            btn_start_compare = self.find(by="id", locator="compare_start_txt")
            n = 0
            if len(lis) < 2:
                self.find(by="id", locator="compare_addcar_txt").click()
                self.search_car()
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
        except Exception as e:
            self.find(by="id", locator="compare_empty_tv2").click()
            self.search_car()

    # 开始对比
    def start_compare(self):
        if self.add_model() is not True:
            self.add_model()
        self.find(by="id", locator="compare_start_txt").click()
        self.find(by="xpath", locator='//*[@text="综合对比"]').click()
        dealer_price = self.find(by="xpath", locator='//*[@text="经销商报价"]')
        return dealer_price.text

    # 编辑-全选-删除
    def edit_all_del(self):
        try:
            empty_info = self.find(by="id", locator="compare_empty_tip1")
            if empty_info.text == "暂无车款信息！快去添加车型对比吧":
                self.add_model()
        except Exception as e:
            self.find(by="id", locator="title_right_btn").click()
            self.find(by="id", locator="compare_selectall_txt").click()
            self.find(by="id", locator="compare_delete_txt").click()
            return empty_info.text