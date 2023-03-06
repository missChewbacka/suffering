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

    def addNewApp(self):
        botList = BotList(self.driver)
        botList.addNewApp().click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2")))

    def accessAppTab(self):
        botList = BotList(self.driver)
        botList.openBot().click()
        time.sleep(1)
        WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='header-bot-name']")))

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

    def accessEventsTab(self):
        botList = BotList(self.driver)
        botList.openBot().click()
        appTab = AppTab(self.driver)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='miniapps icon dots-v']")))
        appTab.expandMenu().click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='submenus']")))
        submenuOptions = appTab.selectMenuOptions()
        for submenuOption in submenuOptions:
            if submenuOption.get_attribute("name") == "event_list_view":
                submenuOption.click()
                break
        time.sleep(2)







