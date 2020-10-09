from yiche_android.yiche_page.base_page import BasePage


class SummaryPage(BasePage):
    def goto_paramconf(self):
        self.find(by="id", locator="com.yiche.price:id/brandtype_parameter_txt").click()
        param_summary = self.find(by="xpath", locator='//*[@text="参数概述"]')
        return param_summary.text