from yiche_android.yiche_page.base_page import BasePage
from yiche_android.yiche_page.my.toolbox.cal import Calculator
from yiche_android.yiche_page.my.toolbox.model_comparison import ModelComparison


class My(BasePage):
    def goto_cal(self):
        self.find(by="xpath", locator='//*[@text="购车计算器"]').click()
        return Calculator(self._driver)

    def goto_model_comparison(self):
        self.find(by="xpath", locator="//*[@text='车型对比']").click()
        return ModelComparison(self._driver)