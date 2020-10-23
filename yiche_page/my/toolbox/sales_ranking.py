import pytest
from appium.webdriver.common.touch_action import TouchAction

from yiche_android.yiche_page.base_page import BasePage


class SalesRanking(BasePage):
    # @pytest.mark.parametrize('car', ['北京BJ80', "揽胜运动版"])
    def window_scroll(self, car):
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
                self.find(by="xpath", locator=f'//*[@text="{car}"]').click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1

    def sales_list(self):
        self.find(by="id", locator="car_suv_tv").click()
        self.find(by="xpath", locator='//*[@text="中大型SUV"]').click()
        self.window_scroll(car="北京BJ80")
        price = self.find(by="id", locator="brandtype_dealerprice_txt")
        return price.text

    def comment_list(self):
        self.find(by="id", locator="rank_comment_tv").click()
        self.find(by="id", locator="car_suv_ll").click()
        self.find(by="xpath", locator='//*[@text="中大型SUV"]').click()
        self.window_scroll(car="揽胜运动版")
        price = self.find(by="id", locator="brandtype_dealerprice_txt")
        return price.text

    def popularity_list(self):
        self.find(by="id", locator="rank_popularity_tv").click()
        self.find(by="id", locator="car_suv_tv").click()
        self.find(by="xpath", locator='//*[@text="中大型SUV"]').click()
        self.window_scroll(car="奔驰G级")
        price = self.find(by="id", locator="brandtype_dealerprice_txt")
        return price.text
