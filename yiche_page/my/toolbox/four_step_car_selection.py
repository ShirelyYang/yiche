from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from yiche_android.yiche_page.base_page import BasePage


class FourStepCarSelection(BasePage):
    def one_step(self):
        self.find(by="xpath", locator='//*[@text="女"]').click()
        self.find(by="xpath", locator='//*[@text="90后"]').click()
        action = TouchAction(self._driver)
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = width * 0.5
        y1 = height * 0.6
        y2 = height * 0.4
        i = 0
        while i < 100:
            try:
                self.find(by="xpath", locator='//*[@text="新手上路"]').click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        self.find(by="id", locator="tv_choose_car_commit").click()
        self.find(by="xpath", locator='//*[@text="暂不考虑"]').click()
        self.find(by="id", locator="tv_choose_car_commit").click()
        self.find(by="xpath", locator='//*[@text="大块头suv"]').click()
        sleep(5)
        btn = self.find(by="id", locator="tv_choose_car_commit")
        btn.click()
        return btn.text

    def two_step(self):
        action = TouchAction(self._driver)
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = width * 0.5
        y1 = height * 0.6
        y2 = height * 0.4
        i = 0
        while i < 100:
            try:
                self.find(by="xpath", locator='//*[@text="宝马X7"]').click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        self.find(by="id", locator="tv_choose_car_commit").click()

    def three_step(self):
        action = TouchAction(self._driver)
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = width * 0.8
        y1 = height * 0.7
        x2 = height * 0.3
        i = 0
        while i < 100:
            try:
                self.find(by="xpath", locator='//*[@text="xDrive40i 行政型 M运动套装"]').click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x2, y=y1).release().perform()
                i += 1
        self.find(by="id", locator="tv_intelligent3_car_commit").click()

    def four_step(self):
        self.find(by="id", locator="promotion_focus_askprice").click()
        ask_price_btn = self.find(by="id", locator="askprice_txt_bottom")
        return ask_price_btn.text
