from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from yiche_android.yiche_page.base_page import BasePage
from time import sleep

from yiche_android.yiche_page.new.summary.model import Model


class SummaryPage(BasePage):
    # 配置
    def goto_paramconf(self):
        # sleep(3)
        self.find(by="xpath", locator='//*[@text="参数配置"]').click()
        param_summary = self.find(by="xpath", locator='//*[@text="参数概述"]')
        power = self.find(by="xpath", locator='//*[@text="动力"]')
        return param_summary.text, power.text

    # 视频说明书
    def goto_video(self):
        # sleep(3)
        # # locator = (self.find(by="xpath", locator='//*[@text="视频说明书"]'))
        # locator = (MobileBy.XPATH, '//*[@text="视频说明书"]')
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.find(by="xpath", locator='//*[@text="视频说明书"]').click()
        child_title = self.find(by="id", locator='child_title')
        return child_title.text

    # 二手车
    def goto_second_hand_car(self):
        sleep(3)
        self.find(by="xpath", locator='//*[@text="二手车"]').click()
        res_title = self.find(by="xpath", locator='//*[contains(@text, "尊享版 M运动套装")]')
        return res_title.text

    # 小视频
    def goto_small_video(self):
        # sleep(3)
        self.find(by="id", locator="brandtype_style_b_smallvideo_title_txt").click()
        title = self.find(by="xpath", locator='//*[@text="小视频"]')
        content_title = self.find(by="xpath", locator='//*[contains(@text, "15年宝马")]')
        return title.text, content_title.text

    # 分期购车
    def goto_Install_car(self):
        # sleep(3)
        self.find(by="xpath", locator='//*[@text="分期购车"]').click()
        title = self.find(by="id", locator="ildTvTitle")
        return title.text

    # 本地最新成交价
    def goto_latest_trans_price(self):
        # sleep(3)
        self.find(by="id", locator="owner_title").click()
        price_label = self.find(by="id", locator="owner_price_label")
        price_value = self.find(by="id", locator="owner_price_value")
        return price_label.text, price_value.text

    # 红包
    def goto_red_envelope(self):
        self.find(by="id", locator="chg_title").click()
        content = self.find(by="accessibility id", locator="购车红包1000元")
        return content.get_attribute(name="content-desc")

    # 前往车款列表页
    def goto_model(self):
        self.find(by="xpath", locator='//*[@text="车型"]').click()
        return Model(self._driver)