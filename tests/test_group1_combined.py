import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pageobjects.PageObjects import AppTab, EventsTab, ReservationManageTab
from utilities.BaseClass import BaseClass
from pageobjects.TestData import Group1TestData, StoreTestData, EventsTestData



@pytest.mark.usefixtures("setup")
class TestCasesGroup1Combined(BaseClass):

    def test_group1_combined(self):
        '''create new bot
        self.addNewApp()'''
        appTab = AppTab(self.driver)
        eventsTab = EventsTab(self.driver)
        reservationTab = ReservationManageTab(self.driver)
        Group1 = Group1TestData.MyGroup1Items
        EventData = EventsTestData.myEvent
        StoreData = StoreTestData.myStore
        '''appTab.enterNewAppName("Sasha_bot") #enter new bots name, change this variable content
        appTab.selectAllBotModules()
        appTab.selectProPlan()
        #appTab.selectAPI10() #uncomment this line if api version is supposed to be API1.0
        appTab.selectEvolanyCompany() #change this function if the company is different
        appTab.saveNewApp()
        self.driver.refresh()'''
        appTab.openNewBot()
        self.accessEventsTab()
        #add dummy event1
        eventsTab.clickNewEventButton()
        eventsTab.enterEventsURL(EventData[0]["event-url"])
        eventsTab.uploadEvents1Image()
        eventsTab.enterEventsTitle(EventData[0]["event-title"])
        eventsTab.enterEventsDescription(EventData[0]["event-desc"])
        eventsTab.enterEventsSeats(EventData[0]["event-seats"])
        eventsTab.saveEventSettings()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='new icon plus-square']")))
        # add dummy event2
        eventsTab.clickNewEventButton()
        eventsTab.enterEventsURL(EventData[1]["event-url"])
        eventsTab.uploadEvents2Image()
        eventsTab.enterEventsTitle(EventData[1]["event-title"])
        eventsTab.enterEventsDescription(EventData[1]["event-desc"])
        eventsTab.enterEventsSeats(EventData[1]["event-seats"])
        eventsTab.saveEventSettings()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='new icon plus-square']")))
        # add dummy event3
        eventsTab.clickNewEventButton()
        eventsTab.enterEventsURL(EventData[2]["event-url"])
        eventsTab.uploadEvents3Image()
        eventsTab.enterEventsTitle(EventData[2]["event-title"])
        eventsTab.enterEventsDescription(EventData[2]["event-desc"])
        eventsTab.enterEventsSeats(EventData[2]["event-seats"])
        eventsTab.saveEventSettings()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='new icon plus-square']")))
        reservationTab.accessReservationManageTab()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='new icon plus-square']")))
        reservationTab.selectStoreMenuTab()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='new icon plus-square']")))
        reservationTab.addNewStore()
        reservationTab.enterStoreURL(StoreData[0]["store-url"])
        reservationTab.enterStoreName(StoreData[0]["store-name"])
        reservationTab.uploadStoreImage()
        reservationTab.enterStoreDescription(StoreData[0]["store-description"])
        reservationTab.enterStoreCategory(StoreData[0]["store-category"])
        reservationTab.enterStoreCountry(StoreData[0]["store-country"])
        reservationTab.enterStoreAddress(StoreData[0]["store-address"])
        reservationTab.enterStoreLatitude(StoreData[0]["store-latitude"])
        reservationTab.enterStoreLongitude(StoreData[0]["store-longitude"])
        reservationTab.selectWeekendStartTime()
        reservationTab.selectWeekendEndTime()
        reservationTab.turnOnStoreCapacitySwitch()
        reservationTab.selectStoreRMSCapacity()
        reservationTab.enterStoreBreakTime(StoreData[0]["store-break-time"])
        reservationTab.saveStoreSetting()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='new icon plus-square']")))
        reservationTab.accessAppTab()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='icon plus-square'])[1]")))
        appTab.addNewGroup("group1")
        time.sleep(2)
        appTab.selectGroup1()
        appTab.addGroup1Item(Group1[0]["item_option"], Group1[0]["item_name"])
        appTab.addGroup1Item(Group1[1]["item_option"], Group1[1]["item_name"])
        appTab.addGroup1Item(Group1[2]["item_option"], Group1[2]["item_name"])
        appTab.addGroup1Item(Group1[3]["item_option"], Group1[3]["item_name"])
        appTab.selectActionItem(Group1[0]["item_name"])
        appTab.enterTextItemsText(Group1[0]["item_xpath"], Group1[0]["item_content"])
        appTab.selectActionItem(Group1[1]["item_name"])
        appTab.enterTextItemsText(Group1[1]["item_xpath"], Group1[1]["item_content"])
        appTab.selectActionItem(Group1[2]["item_name"])
        appTab.enterTextItemsText(Group1[2]["item_xpath"], Group1[2]["item_content"])
        appTab.selectActionItem(Group1[3]["item_name"])
        appTab.enterTextItemsText(Group1[3]["item_xpath"], Group1[3]["item_content"])
        # setting reaction for textitem1
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[0]["item_name"])
        appTab.clickBigButton(Group1[0]["item_big_button"])
        appTab.enterButtonsName(Group1[0]["item_big_button_name"])
        if self.driver.find_element(*AppTab.ActionNextAction).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionNextAction).click()
        appTab.saveSettings()
        #setting reaction for textitem2
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[1]["item_name"])
        appTab.clickQuickReactionButton(Group1[1]["item_quick_reaction_button"])
        appTab.enterButtonsName("choice1")
        if self.driver.find_element(*AppTab.ActionManually).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionManually).click()
        appTab.setNextAction("3:textitem3")
        appTab.clickAdvancedSettings()
        appTab.enterUserKeyValue("choice")
        appTab.saveSettings()
        appTab.clickQuickReactionButton(Group1[1]["item_quick_reaction_button"])
        appTab.enterButtonsName("choice2")
        if self.driver.find_element(*AppTab.ActionManually).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionManually).click()
        appTab.setNextAction("3:textitem3")
        appTab.clickAdvancedSettings()
        appTab.enterUserKeyValue("choice")
        appTab.saveSettings()
        # setting reaction for textitem3
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[2]["item_name"])
        appTab.clickTextHandlerButton(Group1[2]["item_text_handler_button"])
        appTab.selectMatchingType(Group1[2]["item_matching_type"])
        appTab.selectPatternType(Group1[2]["item_matching_pattern"])
        if self.driver.find_element(*AppTab.ActionManually).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionManually).click()
        time.sleep(1)
        appTab.setNextAction("4:textitem4")
        appTab.saveSettings()
        # setting reaction for textitem4
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[3]["item_name"])
        appTab.clickFileHandlerButton(Group1[3]["item_file-handler"])
        appTab.saveSettings()
        #adding carousel items
        appTab.selectGroup1()
        appTab.addGroup1Item(Group1[4]["item_option"], Group1[4]["item_name"])
        appTab.addGroup1Item(Group1[5]["item_option"], Group1[5]["item_name"])
        #setting api data source for carousel1
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[4]["item_name"])
        time.sleep(3)
        appTab.selectDataSourceAPI(Group1[4]["item_api_data_source"])
        time.sleep(1)
        appTab.enterAPIDataSourceURL(Group1[4]["item_content_pre"])
        time.sleep(8)
        #adding big button to carousel1
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[4]["item_name"])
        time.sleep(3)
        appTab.clickBigButton(Group1[4]["item_big_button"])
        appTab.enterButtonsName(Group1[4]["item_big_button_name"])
        time.sleep(1)
        appTab.saveSettings()
        #setting content data source for carousel2
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[5]["item_name"])
        time.sleep(3)
        appTab.selectDataSourceContent(Group1[5]["item_content_data_source"])
        appTab.selectYourContentSource(Group1[5]["item_content_icon"], Group1[5]["item_source_en"],
                                       Group1[5]["item_source_jp"])
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//p[@class='srcs src-content']/button[@value='5'])[1]")))
        #adding quick reaction button fro carousel2
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[5]["item_name"])
        time.sleep(3)
        appTab.clickQuickReactionButton(Group1[5]["item_quick_reaction_button"])
        appTab.enterButtonsName(Group1[5]["item_quick_reaction_button_name"])
        appTab.saveSettings()
        time.sleep(1)
        #adding image carousel item
        appTab.selectGroup1()
        appTab.addGroup1Item(Group1[6]["item_option"], Group1[6]["item_name"])
        #setting content data source for image carousel item
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[6]["item_name"])
        time.sleep(3)
        appTab.selectDataSourceContent(Group1[6]["item_content_data_source"])
        appTab.selectYourContentSource(Group1[6]["item_content_icon"], Group1[6]["item_source_en"],
                                       Group1[6]["item_source_jp"])
        time.sleep(8)
        #adding a big button for image carousel item
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[6]["item_name"])
        appTab.clickBigButton(Group1[6]["item_big_button"])
        appTab.enterButtonsName(Group1[6]["item_big_button_name"])
        appTab.saveSettings()
        #adding flex message
        appTab.selectGroup1()
        appTab.addFlexMessageItem(Group1[7]["item_name"])
        #adding conten to a flex message item
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[7]["item_name"])
        time.sleep(2)
        appTab.clickAddFlexMessageContent(Group1[7]["item_add_content"])
        time.sleep(1)
        appTab.addFlexMessageContent()
        appTab.saveFlexMessage()
        time.sleep(2)
        #adding reaction to a flex message item
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[7]["item_name"])
        appTab.clickQuickReactionButton(Group1[7]["item_quick_reaction_button"])
        appTab.enterButtonsName(Group1[7]["item_quick_reaction_button_name"])
        appTab.saveSettings()
        #adding image map item
        appTab.selectGroup1()
        appTab.addGroup1Item(Group1[8]["item_option"], Group1[8]["item_name"])
        #upload image map image
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[8]["item_name"])
        appTab.clickCameraIcon(Group1[8]["item_camera_icon"])
        time.sleep(2)
        appTab.uploadImageMapItemImage()
        time.sleep(15)
        #setting up image map
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[8]["item_name"])
        appTab.clickBrushIcon(Group1[8]["item_brush_icon"])
        time.sleep(1)
        appTab.clickImageMapImage()
        appTab.setImageMapArea1()
        appTab.clickImageMapImage()
        appTab.setImageMapArea2()
        appTab.clickImageMapImage()
        appTab.setImageMapArea3()
        appTab.saveImageImapArea()
        time.sleep(2)
        #setting up image map areas
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[8]["item_name"])
        # Add area 1 settings
        appTab.selectImagemapAreaButton("Area 1")
        time.sleep(1)
        if self.driver.find_element(*AppTab.ActionManually).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionManually).click()
        time.sleep(1)
        appTab.setImagemapAreaNextAction("1:textitem1", Group1[8]["item_area1_button"])
        time.sleep(1)
        appTab.saveSettings()
        time.sleep(1)
        # Add area 2 settings
        time.sleep(1)
        appTab.selectImagemapAreaButton("Area 2")
        time.sleep(1)
        if self.driver.find_element(*AppTab.ActionManually).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionManually).click()
        time.sleep(1)
        appTab.setImagemapAreaNextAction("5:carousel1", Group1[8]["item_area2_button"])
        time.sleep(1)
        appTab.saveSettings()
        time.sleep(1)
        # Add area 3 settings
        appTab.selectImagemapAreaButton("Area 3")
        time.sleep(1)
        if self.driver.find_element(*AppTab.ActionNextAction).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionNextAction).click()
        time.sleep(1)
        appTab.saveSettings()
        time.sleep(1)


























        '''appTab = AppTab(self.driver)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewGroup)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.GroupOption)).send_keys("group1" + Keys.ENTER).perform()
        time.sleep(1)'''







