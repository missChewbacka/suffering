import pytest
import inspect
import logging
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pageobjects.PageObjects import BotList, AppTab


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogs(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def accessAppTab(self):
        botList = BotList(self.driver)
        botList.openBot().click()
        time.sleep(10)

    def accessCouponsTab(self):
        botList = BotList(self.driver)
        botList.openBot().click()
        appTab = AppTab(self.driver)
        appTab.expandMenu().click()
        submenuOptions = appTab.selectMenuOptions()
        for submenuOption in submenuOptions:
            if submenuOption.get_attribute("name") == "coupon_list_view":
                submenuOption.click()
                break
        time.sleep(2)







