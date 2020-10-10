from appium.webdriver.common.touch_action import TouchAction

from yiche_android.yiche_page.base_page import BasePage
from yiche_android.yiche_page.sub_brand_page import SubBrandPage


class BrandList(BasePage):
    def goto_search_brand(self):
        action = TouchAction(self._driver)
        # 获取当前屏幕的尺寸
        window_rect = self._driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = width * 0.5
        # mac下
        # y1 = height * 0.8
        # Windows下
        y1 = height * 0.6
        # y2 = height * 0.2
        # Windows下
        y2 = height * 0.4
        i = 0
        while i < 100:
            try:
                # self.find(by="xpath", locator='//*[@text="宝马"]').click()
                self.steps("../yiche_yaml/brand_list.yaml")
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(50).move_to(x=x1, y=y2).release().perform()
                i += 1
        return SubBrandPage(self._driver)






