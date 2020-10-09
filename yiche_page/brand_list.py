from appium.webdriver.common.touch_action import TouchAction

from yiche_android.yiche_page.base_page import BasePage


class BradList(BasePage):
    def goto_search(self):
        action = TouchAction(self._driver)
        # 获取当前屏幕的尺寸
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
