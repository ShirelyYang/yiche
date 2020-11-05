from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from yiche_android.yiche_page.base_page import BasePage


class NearbyDealers(BasePage):
    def nearby_dealers(self):
        self.find(by="xpath", locator='//*[@text="宝马"]').click()
        self.find(by="xpath", locator='//*[@text="4S-泉州晋宝宝马"]').click()
        sales_list = self.find(by="id", locator="sales_tv")
        return sales_list.text

    def map(self):
        self.find(by="id", locator="tv_head_location").click()
        self.find(by="xpath", locator='//*[contains(@text, "福建")]').click()
        self.find(by="xpath", locator='//*[@text="泉州"]').click()
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
                self.find(by="xpath", locator='//*[contains(@text, "泉州大众汽车")]/..//*[@resource-id="com.yiche.price:id/iv_gps"]').click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        sleep(3)
        address = self.find(by="xpath", locator='//*[@text="泉州展览城"]')
        return address.text

    def switch_position(self):
        self.find(by="id", locator="tv_head_location").click()
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
                self.find(by="xpath", locator='//*[contains(@text, "广东")]').click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1
        self.find(by="xpath", locator='//*[@text="深圳"]').click()
        addr = self.find(by="xpath", locator='//*[contains(@text, "深圳东通大众")]/..'
                                              '/*[@resource-id="com.yiche.price:id/dealer_address"]')
        return addr.text
