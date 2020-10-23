from yiche_android.yiche_page.base_page import BasePage
from yiche_android.yiche_page.my.toolbox.nearby_dealers import NearbyDealers
from yiche_android.yiche_page.my.toolbox.sales_ranking import SalesRanking


class ToolBoxMore(BasePage):
    def goto_sales_ranking(self):
        self.find(by="xpath", locator='//*[@text="销量排行"]').click()
        return SalesRanking(self._driver)

    def goto_nearby_dealers(self):
        self.find(by="xpath", locator='//*[@text="附近经销商"]').click()
        return NearbyDealers(self._driver)
