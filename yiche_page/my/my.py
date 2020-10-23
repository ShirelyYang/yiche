from appium.webdriver.common.touch_action import TouchAction

from yiche_android.yiche_page.base_page import BasePage
from yiche_android.yiche_page.my.toolbox.cal import Calculator
from yiche_android.yiche_page.my.toolbox.four_step_car_selection import FourStepCarSelection
from yiche_android.yiche_page.my.toolbox.model_comparison import ModelComparison
from yiche_android.yiche_page.my.toolbox.toolbox_more import ToolBoxMore


class My(BasePage):
    def goto_cal(self):
        self.find(by="xpath", locator='//*[@text="购车计算器"]').click()
        return Calculator(self._driver)

    def goto_model_comparison(self):
        self.find(by="xpath", locator="//*[@text='车型对比']").click()
        return ModelComparison(self._driver)

    def goto_four_step_car_selection(self):
        self.find(by="xpath", locator='//*[@text="四步选车"]').click()
        return FourStepCarSelection(self._driver)

    def more(self):
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
                self.find(by="xpath", locator='//*[@text="更多"]').click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        return ToolBoxMore(self._driver)
