from appium.webdriver.common.touch_action import TouchAction
from yiche_android.yiche_page.base_page import BasePage
from time import sleep


class Calculator(BasePage):
    def cal(self):
        self.find(by="id", locator="carNameTxt").click()
        sleep(3)
        # action = TouchAction(self._driver)
        # window_rect = self._driver.get_window_rect()
        # width = window_rect['width']
        # height = window_rect['height']
        # x1 = width * 0.5
        # y1 = height * 0.6
        # y2 = height * 0.4
        # i = 0
        # while i < 10:
        #     try:
        #         self.find(by="xpath", locator='//*[@text="奔驰"]').click()
        #         break
        #     except Exception as e:
        #         action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
        #         i += 1
        self.find(by="id", locator="searchEdtTxt").click()
        self.find(by="id", locator="searchEt").send_keys("奔驰GLC")
        # self.find(by="xpath", locator='//*[@text="奔驰GLC"]').click()
        self.find(by="id", locator="txtView").click()
        self.find(by="xpath", locator="//*[@text='奔驰GLC']").click()
        # price = self.find(by="xpath", locator='//*[@text="35.38万起"]').text
        self.find(by="xpath", locator="//*[contains(@text, '豪华型')]").click()
        calculateBtn = self.find(by="id", locator="carcalculate_byfy_title_txt")
        return calculateBtn.text

    # 贷款页面
    def loan(self):
        if self.cal() is None:
            self.cal()
        self.find(by="id", locator="loanBtn").click()
        contains = self.find(by="xpath", locator='//*[@text="首付比例"]')
        return contains.text

    # 重置
    def reset(self):
        if self.cal() is None:
            self.cal()
        self.find(by="id", locator="title_right_btn").click()
        btn_clear = self.find(by="id", locator="calculate_history_clear")
        return btn_clear.text