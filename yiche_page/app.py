from appium import webdriver

from yiche_android.yiche_page.base_page import BasePage


class App(BasePage):
    def start(self):
        def start(self):
            _package = 'com.yiche.price'
            _activity = '.commonlib.component.ArouterRootFragmentActivity'
            if self._driver is None:
                caps = {}
                caps["platformName"] = "Android"
                caps["deviceName"] = "emulator-5554"
                caps["appPackage"] = _package
                caps["appActivity"] = _activity
                caps["autoGrantPermissions"] = True
                caps["noReset"] = True
                self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
                self._driver.implicitly_wait(10)
            else:
                self._driver.start_activity(_package, _activity)
            return self

        def main(self):
            return BrandList(self._driver)
