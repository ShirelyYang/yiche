from yiche_android.yiche_page.base_page import BasePage
from yiche_android.yiche_page.my.toolbox.cal import Calculator
from yiche_android.yiche_page.my.toolbox.four_step_car_selection import FourStepCarSelection
from yiche_android.yiche_page.my.toolbox.model_comparison import ModelComparison


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