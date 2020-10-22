from appium import webdriver

from yiche_android.yiche_page.base_page import BasePage
from yiche_android.yiche_page.my.my import My
from yiche_android.yiche_page.new.brand_list import BrandList
from time import sleep


class App(BasePage):
    def start(self):
        # _package = 'com.yiche_android.price'
        _package = 'com.yiche.price'
        _activity = '.MainActivity'
        if self._driver is None:
            sleep(10)
            caps = {}
            caps["platformName"] = "Android"
            # MUMU模拟器
            # caps["deviceName"] = "127.0.0.1:7555"
            # caps["deviceName"] = "emulator-5554"
            # OPPO手机
            caps["deviceName"] = "c0926ab9"
            caps["platformVersion"] = "7.1.1"
            # caps["platformVersion"] = "6.0"
            caps['automationName'] = 'UiAutomator2'
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["unicodeKeyBoard"] = "true"
            caps["resetKeyBoard"] = "true"
            caps["autoGrantPermissions"] = True
            caps["noReset"] = True
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self._driver.implicitly_wait(20)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return BrandList(self._driver)

    def my(self):
        self.find(by="id", locator="bottom_button05").click()
        return My(self._driver)

    # def quit(self):
    #     return self._driver.quit()
