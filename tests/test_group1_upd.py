import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pageobjects.PageObjects import AppTab
from utilities.BaseClass import BaseClass
from pageobjects.TestData import Group1TestData


@pytest.mark.usefixtures("setup")
class TestCasesGroup1(BaseClass):

    def test_create_new_group(self):
        log = self.getLogs()
        self.accessAppTab()
        log.info("1. Go to the [App] tab.")
        appTab = AppTab(self.driver)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewGroup)).perform()
        time.sleep(1)
        log.info("2. Hover over [+Add new group] button.")
        action.click(self.driver.find_element(*AppTab.GroupOption)).send_keys("group1" + Keys.ENTER).perform()
        time.sleep(1)
        log.info("3. Click the [Group] option.")

        groups = self.driver.find_elements(By.XPATH, "//ul[@class='groups']/li/h5")
        for group in groups:
            if group.text == "group1":
                assert True
                break

    def test_create_text_items(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [Group1] in the groups list.")
        appTab.addTextItem(Group1[0]["item_name"])
        log.info("2. Click the [Text] option, enter 1st text item's name and save.")
        appTab.addTextItem(Group1[1]["item_name"])
        log.info("3. Click the [Text] option, enter 2nd text item's name and save.")
        appTab.addTextItem(Group1[2]["item_name"])
        log.info("4. Click the [Text] option, enter 3rd text item's name and save.")
        appTab.addTextItem(Group1[3]["item_name"])
        log.info("5. Click the [Text] option, enter 4th text item's name and save.")
        time.sleep(1)
        #add assertion

    def test_enter_text_in_the_textfield(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [group1] in the groups list.")
        appTab.selectTextitem1()
        log.info("2. Select [textitem1] in the [group1] actions list.")
        appTab.enterTextItemsText(Group1[0]["item_xpath"], Group1[0]["item_content"])
        log.info("3. Enter [text1] in the text field of the [textitem1] and press [Enter].")
        appTab.selectTextitem2()
        log.info("4. Select [textitem2] in the [group1] actions list.")
        appTab.enterTextItemsText(Group1[1]["item_xpath"], Group1[1]["item_content"])
        log.info("5. Enter [text2] in the text field of the [textitem2] and press [Enter].")
        appTab.selectTextitem3()
        log.info("6. Select [textitem3] in the [group1] actions list.")
        appTab.enterTextItemsText(Group1[2]["item_xpath"], Group1[2]["item_content"])
        log.info("7. Enter [text3] in the text field of the [textitem3] and press [Enter].")
        appTab.selectTextitem4()
        log.info("8. Select [textitem4] in the [group1] actions list.")
        appTab.enterTextItemsText(Group1[3]["item_xpath"], Group1[3]["item_content"])
        log.info("9. Enter [text4] in the text field of the [textitem4] and press [Enter].")
        time.sleep(1)

        #add assertion

    def test_adding_big_button_for_textitem1(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectTextitem1()
        appTab.clickBigButton(Group1[0]["item_big_button"])
        log.info("1. Click the [+ Add new button] option.")
        appTab.enterButtonsName(Group1[0]["item_big_button_name"])
        log.info("2. Enter [text1 button] as the button's name.")
        if self.driver.find_element(*AppTab.ActionNextAction).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionNextAction).click()
        log.info("3. Leave [Action] set as [Next action].")
        appTab.saveSettings()
        log.info("4. Click the [Save] button.")
        time.sleep(1)

    def test_adding_quick_reaction_buttons_for_textitem2(self):
        log = self.getLogs()
        self.accessAppTab()
        time.sleep(1)
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectTextitem2()
        appTab.clickQuickReactionButton(Group1[1]["item_quick_reaction_button"])
        log.info("1. Click the [Quick reply] button of [textitem2].")
        appTab.enterButtonsName("choice1")
        log.info("2. Set the buttons name as [choice1]")
        if self.driver.find_element(*AppTab.ActionManually).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionManually).click()
        log.info("3. Set [Action] as [Manually]")
        appTab.setNextAction("3:textitem3")
        log.info("4. Select [textitem3] as a destination chatflow item.")
        appTab.clickAdvancedSettings()
        log.info("5. Click the [Advanced] settings option.")
        appTab.enterUserKeyValue("choice")
        log.info("6. Set [Save user data] as [choice].")
        appTab.saveSettings()
        log.info("7. Save the [Quick reply] button's settings")
        time.sleep(1)
        appTab.clickQuickReactionButton(Group1[1]["item_quick_reaction_button"])
        log.info("8. Click the [Quick reply] button of [textitem2].")
        appTab.enterButtonsName("choice2")
        log.info("9. Set the buttons name as [choice2]")
        if self.driver.find_element(*AppTab.ActionManually).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionManually).click()
        log.info("10. Set [Action] as [Manually]")
        appTab.setNextAction("3:textitem3")
        log.info("11. Select [textitem3] as a destination chatflow item.")
        appTab.clickAdvancedSettings()
        log.info("12. Click the [Advanced] settings option.")
        appTab.enterUserKeyValue("choice")
        log.info("13. Set [Save user data] as [choice].")
        appTab.saveSettings()
        log.info("14. Save the [Quick reply] button's settings")
        time.sleep(1)

    def test_adding_text_handler_for_textitem3(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectTextitem3()
        appTab.clickTextHandlerButton(Group1[2]["item_text_handler_button"])
        log.info("1. Click the [Text handler] button of [textitem3].")
        appTab.selectMatchingType(Group1[2]["item_matching_type"])
        time.sleep(1)
        log.info("2. Set [Matching type] as [Match pattern of].")
        appTab.selectPatternType(Group1[2]["item_matching_pattern"])
        time.sleep(1)
        log.info("3. Set [Pattern type] as [Match all patterns].")
        if self.driver.find_element(*AppTab.ActionManually).get_attribute("checked") != "true":
            self.driver.find_element(*AppTab.ActionManually).click()
        time.sleep(1)
        log.info("4. Set [Action] as [Manually]")
        appTab.setNextAction("4:textitem4")
        log.info("5. Select [textitem4] as a destination chatflow item.")
        appTab.saveSettings()
        log.info("6. Save the [Text handler] button's settings")

    def test_adding_file_handler_for_textitem4(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectTextitem4()
        appTab.clickFileHandlerButton(Group1[3]["item_file-handler"])
        log.info("1. Click the [File handler] button of [textitem3].")
        appTab.saveSettings()
        log.info("2. Save the [File handler] button's settings")

    def test_adding_carousel_items(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [Group1] in the groups list.")
        appTab.addCardItem(Group1[4]["item_name"])
        log.info("2. Click the [Card] option, enter 1st carousel item's name and save.")
        appTab.addCardItem(Group1[5]["item_name"])
        log.info("3. Click the [Card] option, enter 2nd carousel item's name and save.")

    def test_setting_api_data_source_carousel1(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectCarousel1()
        log.info("1. Select [carousel1] chatflow item in [group1].")
        appTab.selectDataSourceAPI(Group1[4]["item_api_data_source"])
        time.sleep(1)
        log.info("2. Select [API] data source option.")
        appTab.enterAPIDataSourceURL(Group1[4]["item_content_pre"])
        time.sleep(8)
        log.info("3. Set [https://pre.bonp.me/api/service/recipes/?format=list] as the API URL and press Enter.")


    def test_adding_big_button_carousel1(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectCarousel1()
        log.info("1. Select [carousel1] chatflow item in [group1].")
        appTab.clickBigButton(Group1[4]["item_big_button"])
        log.info("2. Click the [+ Add new button] option of [carousel1] chatflow item.")
        appTab.enterButtonsName(Group1[4]["item_big_button_name"])
        time.sleep(1)
        appTab.saveSettings()
        log.info("3. Enter [Next] as the button's name and save.")

    def test_setting_content_data_source_carousel2(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectCarousel2()
        log.info("1. Select [carousel2] chatflow item in [group1].")
        appTab.selectDataSourceContent(Group1[5]["item_content_data_source"])
        log.info("2. Select [Content] data source option.")
        appTab.selectYourContentSource(Group1[5]["item_content_icon"], Group1[5]["item_source_en"], Group1[5]["item_source_jp"])
        log.info("3. Select the [Content] data source you have prepared (Events) for [carousel2].")
        time.sleep(2)

    def test_adding_quick_reaction_buttons_for_carousel2(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectCarousel2()
        log.info("1. Select [carousel2] chatflow item in [group1].")
        appTab.clickQuickReactionButton(Group1[5]["item_quick_reaction_button"])
        log.info("2. Click the [Quick reaction] option of [carousel2] chatflow item.")
        appTab.enterButtonsName(Group1[5]["item_quick_reaction_button_name"])
        appTab.saveSettings()
        log.info("3. Enter the new [Quick reaction] button's name and save.")
        time.sleep(1)

    def test_adding_image_carousel_item(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [Group1] in the groups list.")
        appTab.addImageCarouselItem(Group1[6]["item_name"])
        log.info("2. Click the [Image Carousel] option, enter image carousel item's name and save.")

    def test_setting_content_data_source_image_carousel(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectImageCarousel()
        log.info("1. Select [image_carousel] chatflow item in [group1].")
        appTab.selectDataSourceContent(Group1[6]["item_content_data_source"])
        log.info("2. Select [Content] data source option.")
        appTab.selectYourContentSource(Group1[6]["item_content_icon"], Group1[6]["item_source_en"], Group1[6]["item_source_jp"])
        log.info("3. Select the [Content] data source you have prepared (Events) for [image_carousel].")
        time.sleep(2)

    def test_adding_big_button_image_carousel(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectImageCarousel()
        log.info("1. Select [carousel2] chatflow item in [group1].")
        appTab.clickBigButton(Group1[6]["item_big_button"])
        log.info("2. Click the [+ Add new button] option of [carousel1] chatflow item.")
        appTab.enterButtonsName(Group1[6]["item_big_button_name"])
        appTab.saveSettings()
        log.info("3. Enter [Next] as the button's name and save.")

    def test_adding_flex_message_item(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [Group1] in the groups list.")
        appTab.addFlexMessageItem(Group1[7]["item_name"])
        log.info("2. Click the [Flex Message] option, enter flex message item's name and save.")

    def test_adding_flex_message_content(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectFlexMessage()
        time.sleep(2)
        appTab.clickAddFlexMessageContent(Group1[7]["item_add_content"])
        time.sleep(1)
        appTab.addFlexMessageContent()
        appTab.saveFlexMessage()
        time.sleep(3)

    def test_adding_quick_reaction_buttons_for_flex_message(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectFlexMessage()
        log.info("1. Select [flex_message] chatflow item in [group1].")
        appTab.clickQuickReactionButton(Group1[7]["item_quick_reaction_button"])
        log.info("2. Click the [Quick reaction] option of [carousel2] chatflow item.")
        appTab.enterButtonsName(Group1[7]["item_quick_reaction_button_name"])
        appTab.saveSettings()
        log.info("3. Enter the new [Quick reaction] button's name and save.")
        time.sleep(1)

    def test_adding_image_map_item(self):
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.addImageMapItem(Group1[8]["item_name"])