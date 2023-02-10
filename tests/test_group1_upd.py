import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        appTab.selectActionItem(Group1[0]["item_name"])
        log.info("2. Select [textitem1] in the [group1] actions list.")
        appTab.enterTextItemsText(Group1[0]["item_xpath"], Group1[0]["item_content"])
        log.info("3. Enter [text1] in the text field of the [textitem1] and press [Enter].")
        appTab.selectActionItem(Group1[1]["item_name"])
        log.info("4. Select [textitem2] in the [group1] actions list.")
        appTab.enterTextItemsText(Group1[1]["item_xpath"], Group1[1]["item_content"])
        log.info("5. Enter [text2] in the text field of the [textitem2] and press [Enter].")
        appTab.selectActionItem(Group1[2]["item_name"])
        log.info("6. Select [textitem3] in the [group1] actions list.")
        appTab.enterTextItemsText(Group1[2]["item_xpath"], Group1[2]["item_content"])
        log.info("7. Enter [text3] in the text field of the [textitem3] and press [Enter].")
        appTab.selectActionItem(Group1[3]["item_name"])
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
        appTab.selectActionItem(Group1[0]["item_name"])
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
        appTab.selectActionItem(Group1[1]["item_name"])
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
        appTab.selectActionItem(Group1[2]["item_name"])
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
        appTab.selectActionItem(Group1[3]["item_name"])
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
        appTab.selectActionItem(Group1[4]["item_name"])
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
        appTab.selectActionItem(Group1[4]["item_name"])
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
        appTab.selectActionItem(Group1[5]["item_name"])
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
        appTab.selectActionItem(Group1[5]["item_name"])
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
        appTab.selectActionItem(Group1[6]["item_name"])
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
        appTab.selectActionItem(Group1[6]["item_name"])
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
        appTab.selectActionItem(Group1[7]["item_name"])
        log.info("1. Select [flex_message] chatflow item in [group1].")
        time.sleep(2)
        appTab.clickAddFlexMessageContent(Group1[7]["item_add_content"])
        time.sleep(1)
        log.info("2. Click the [Add content of Flex message] link.")
        appTab.addFlexMessageContent()
        log.info("3. Enter a valid JSON-code in the [Flex Editor] textarea.")
        appTab.saveFlexMessage()
        log.info("4. Save the [flex_message] content.")
        time.sleep(2)

    def test_adding_quick_reaction_buttons_for_flex_message(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[7]["item_name"])
        log.info("1. Select [flex_message] chatflow item in [group1].")
        appTab.clickQuickReactionButton(Group1[7]["item_quick_reaction_button"])
        log.info("2. Click the [Quick reaction] option of [carousel2] chatflow item.")
        appTab.enterButtonsName(Group1[7]["item_quick_reaction_button_name"])
        appTab.saveSettings()
        log.info("3. Enter the new [Quick reaction] button's name and save.")
        time.sleep(1)

    def test_adding_image_map_item(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [Group1] in the groups list.")
        appTab.addImageMapItem(Group1[8]["item_name"])
        log.info("2. Click the [Image Map] option, enter image map's item name and save.")

    def test_selecting_image_map_item_image(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[8]["item_name"])
        log.info("1. Select [image_map] chatflow item in [group1].")
        time.sleep(2)
        appTab.clickCameraIcon(Group1[8]["item_camera_icon"])
        time.sleep(1)
        log.info("2. Click the camera icon of the [image_map] chatflow item.")
        appTab.uploadImageMapItemImage()
        time.sleep(3)
        log.info("3. Select and upload an image for your image map.")

    def test_setting_up_imagemap(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[8]["item_name"])
        log.info("1. Select [image_map] chatflow item in [group1].")
        appTab.clickBrushIcon(Group1[8]["item_brush_icon"])
        time.sleep(1)
        log.info("2. Click on the edit button (brush)")
        appTab.clickImageMapImage()
        log.info("3. Click the image map image you have uploaded in the opened popup.")
        appTab.setImageMapArea1()
        log.info("4. Set [image_map] [Area 1].")
        appTab.clickImageMapImage()
        appTab.setImageMapArea2()
        log.info("5. Set [image_map] [Area 2].")
        appTab.clickImageMapImage()
        appTab.setImageMapArea3()
        log.info("6. Set [image_map] [Area 3].")
        appTab.saveImageImapArea()
        log.info("7. Save the settings.")
        time.sleep(2)

    def test_setting_transitions_for_imagemap_areas(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[8]["item_name"])
        log.info("1. Select [image_map] chatflow item in [group1].")
        ###########Add area's settings

    def test_adding_image_item(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [Group1] in the groups list.")
        appTab.addImageItem(Group1[9]["item_name"])
        log.info("2. Click the [Image] option, enter image's item name and save.")

    def test_selecting_image_item_image(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[9]["item_name"])
        log.info("1. Select [image1] chatflow item in [group1].")
        time.sleep(2)
        appTab.clickCameraIcon(Group1[9]["item_camera_icon"])
        time.sleep(1)
        log.info("2. Click the camera icon of the [image1] chatflow item.")
        appTab.uploadImageItemImage()
        time.sleep(5)
        log.info("3. Select and upload an image for your image item.")

    def test_adding_reaction_button_image_item(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[9]["item_name"])
        log.info("1. Select [image1] chatflow item in [group1].")
        appTab.clickQuickReactionButton(Group1[9]["item_quick_reaction_button"])
        log.info("2. Click the [Quick reaction] option of [image1] chatflow item.")
        appTab.enterButtonsName(Group1[9]["item_quick_reaction_button_name"])
        appTab.saveSettings()
        log.info("3. Enter the new [Quick reaction] button's name and save.")
        time.sleep(1)

    def test_adding_video_item1(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [Group1] in the groups list.")
        appTab.addVideoItem(Group1[10]["item_name"])
        log.info("2. Click the [Video] option, enter video's item name and save.")

    def test_selecting_image_and_video_for_video_using_upload(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[10]["item_name"])
        log.info("1. Select [video1] chatflow item in [group1].")
        appTab.clickCameraIcon(Group1[10]["item_camera_icon"])
        time.sleep(2)
        log.info("2. Click the [camera] icon of [video1] chatflow action.")
        appTab.uploadVideoItemImage()
        time.sleep(4)
        log.info("3. Upload a thumbnail image for [video1] chatflow action.")
        appTab.clickVideoCameraIcon(Group1[10]["item_video_camera_icon"])
        time.sleep(2)
        log.info("4. Click the [video camera] icon of [video1] chatflow action.")
        appTab.uploadVideoItemVideo()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//li/video")))
        log.info("5. Upload a video for [video1] chatflow action.")

    def test_adding_reaction_button_video_item1(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[10]["item_name"])
        log.info("1. Select [video1] chatflow item in [group1].")
        appTab.clickQuickReactionButton(Group1[10]["item_quick_reaction_button"])
        log.info("2. Click the [Quick reaction] option of [video1] chatflow item.")
        appTab.enterButtonsName(Group1[10]["item_quick_reaction_button_name"])
        appTab.saveSettings()
        time.sleep(1)
        log.info("3. Enter the new [Quick reaction] button's name and save.")

    def test_adding_video_item2(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [Group1] in the groups list.")
        appTab.addVideoItem(Group1[11]["item_name"])
        log.info("2. Click the [Video] option, enter video's item name and save.")

    def test_selecting_image_and_video_for_video_using_link(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[11]["item_name"])
        time.sleep(2)
        log.info("1. Select [video2] chatflow item in [group1].")
        appTab.clickImageLinkIcon(Group1[11]["item_image_link_icon"])
        time.sleep(1)
        log.info("2. Click the [image link] icon of [video2] chatflow action.")
        appTab.uploadVideoItemImageByLink(Group1[11]["item_image_link_input"])
        log.info("3. Paste image link for [video2] chatflow action.")
        time.sleep(4)
        appTab.clickVideoLinkIcon(Group1[11]["item_video_link_icon"])
        time.sleep(1)
        log.info("4. Click the [video link] icon of [video2] chatflow action.")
        appTab.uploadVideoItemVideoByLink(Group1[11]["item_image_link_input"])
        log.info("5. Paste video link for [video2] chatflow action.")
        time.sleep(20)

    def test_adding_reaction_button_video_item2(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[11]["item_name"])
        log.info("1. Select [video2] chatflow item in [group1].")
        appTab.clickQuickReactionButton(Group1[11]["item_quick_reaction_button"])
        log.info("2. Click the [Quick reaction] option of [video2] chatflow item.")
        appTab.enterButtonsName(Group1[11]["item_quick_reaction_button_name"])
        appTab.saveSettings()
        log.info("3. Enter the new [Quick reaction] button's name and save.")
        time.sleep(1)

    def test_adding_conditional_item(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        log.info("1. Select [Group1] in the groups list.")
        appTab.addConditionItem(Group1[12]["item_name"])
        log.info("2. Click the [Condition] option, enter condition's item name and save.")

    def test_setting_up_conditional_item(self):
        log = self.getLogs()
        self.accessAppTab()
        Group1 = Group1TestData.MyGroup1Items
        appTab = AppTab(self.driver)
        appTab.selectGroup1()
        appTab.selectActionItem(Group1[12]["item_name"])
        log.info("1. Select [conditional] chatflow item in [group1].")
        appTab.selectIfOption(Group1[12]["item_if_field"], Group1[12]["item_field_options"], Group1[12]["item_if_option_val"])
        log.info("2. Select [conditional] chatflow item in [group1].")
        appTab.inputConditionOfConditionalItem(Group1[12]["item_condition_field"], Group1[12]["item_condition_option"])
        log.info("3. Select [conditional] chatflow item in [group1].")
        appTab.selectThenAction(Group1[12]["item_then_field"], Group1[12]["item_then_option"])
        log.info("4. Select [conditional] chatflow item in [group1].")
        appTab.selectThenAction(Group1[12]["item_else_field"], Group1[12]["item_else_option"])
        log.info("4. Select [conditional] chatflow item in [group1].")




















