from appium.webdriver.common.touch_action import TouchAction

from yiche_android.yiche_page.base_page import BasePage
from yiche_android.yiche_page.summary_page import SummaryPage


class SubBrandPage(BasePage):
    def select_Model(self):
        action = TouchAction(self._driver)
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = width * 0.5
        y1 = height * 0.9
        y2 = height * 0.2
        i = 0
        while i < 10:
            try:
                self.find(by="xpath", locator='//*[@text="宝马5系"]').click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        return SummaryPage(self._driver)