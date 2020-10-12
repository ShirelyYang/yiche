from appium.webdriver.common.touch_action import TouchAction

from yiche_android.yiche_page.base_page import BasePage


class Model(BasePage):
    # 车款列表页
    # 车型 由2021款切换至 2018款
    def goto_model_change(self):
        self.find(by="xpath", locator='//*[@text="2018款"]').click()
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
                self.find(by="id", locator="brandname").is_displayed()
                # result = self.find(by="xpath", locator='//*[contains(@text, "豪华设计")]')
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        result = self.find(by="id", locator="brandname")
        return result.text

    # 车款列表页-对比
    def goto_model_compared(self):
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
                self.find(by="id", locator="brandtype_model_compare_btn").click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        result = self.find(by="id", locator="brandtype_model_compare_btn")
        return result.text

    # 车款列表页-计算
    def goto_model_cal(self):
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
                self.find(by="id", locator="brandtype_car_calculate_btn").click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        result = self.find(by="id", locator="chezhu_price_txt")
        return result.text

    # 车款列表页-分期
    def goto_model_staging(self):
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
                self.find(by="id", locator="brandtype_car_gongneng_btn").click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        btn = self.find(by="id", locator="askprice_txt_bottom")
        return btn.text

    # 车款列表页-询底价
    def goto_model_ask_price(self):
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
                self.find(by="id", locator="brandtype_ask_price_btn").click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        btn = self.find(by="id", locator="askprice_txt_bottom")
        return btn.text