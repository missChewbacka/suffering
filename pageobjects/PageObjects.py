import time
import os
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BotList:

    def __init__(self, driver):
        self.driver = driver

    MyBot = (By.XPATH, "//*[contains(text(),'2023-02-03-bot')]")

    def openBot(self):
        return self.driver.find_element(*BotList.MyBot)


class AppTab:
    def __init__(self, driver):
        self.driver = driver

    AddNewGroup = (By.XPATH, "(//button[@class='icon plus-square'])[1]")
    GroupOption = (By.XPATH, "//dd[@class='new-group']")
    GroupList = (By.XPATH, "//ul[@class='groups']/li/h5")
    Group1 = (By.XPATH, "//ul[@class='groups']/li/h5[contains(text(),'group1')]")
    ActionList = (By.XPATH, "//section[@class='actions']/ul/li/h5")

    AddNewItem = (By.XPATH, "(//button[@class='icon plus-square'])[2]")
    SelectText = (By.XPATH, "//dd[@rt='text']")
    SelectCard = (By.XPATH, "//dd[@rt='card']")
    SelectImageCarousel = (By.XPATH, "//dd[@rt='imagecard']")
    SelectImageMap = (By.XPATH, "//dd[@rt='imagemap']")
    SelectImage = (By.XPATH, "//dd[@rt='image']")
    SelectVideo = (By.XPATH, "//dd[@rt='video']")
    SelectIfCondition = (By.XPATH, "//dd[@rt='logical']")
    SelectFlexMessage = (By.XPATH, "//dd[@rt='flex']")
    SelectSendEmail = (By.XPATH, "//dd[@rt='notice']")

    ButtonsNameInputField = (By.XPATH, "//input[@name='label']")

    ActionNextAction = (By.XPATH, "//input[@value='next']")
    ActionManually = (By.XPATH, "//input[@value='manual']")

    AdvancedSettings = (By.XPATH, "//label[@class='icon cog advanced-button']")
    AutocompleteOptions = (By.XPATH, "//div/div/input[@class='autocomplete']")
    UkeyInputField = (By.XPATH, "//input[@name='ukey']")

    SaveSettings = (By.XPATH, "//button[@class='icon save label']")

    ThreeDots = (By.XPATH, "//a[@class='miniapps icon dots-v']")
    MenuOptions = (By.XPATH, "//section[@class='submenus']/ul/li/a")

    DropdownMatchingTypes = (By.XPATH, "//div[@class='ui-dropdown form-item']")
    MatchingTypes = (By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
    PatternTypes = (By.XPATH, "//ul[@class='ui-dropdown-opts']/li")

    APIDataSource = (By.XPATH, "(//b[@class='icon coding'])[5]")
    APIDataSourceURL = (By.XPATH, "(//p[@class='srcs src-api'])[5]/input")

    ContentDataSourceIcon = (By.XPATH, "(//button[@class='ui-menu'])[12]")
    ContentDataSourceOptions = (By.XPATH, "//article[@id='mask']/ul/li")

    FlexMessageConfirm = (By.XPATH, "//button[@class='a1']")
    FlexMessageTextarea = (By.XPATH, "//textarea[@id='flex-area']")
    FlexMessageSaveButton = (By.XPATH, "//button[@class='icon save']")

    ImageMapImage = (By.XPATH, "//div[@class='imagemap']")
    SaveImapAreaButton = (By.XPATH, "//button[@class='icon save']")

    def addNewGroup(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewGroup)).perform()
        time.sleep(2)
        action.click(self.driver.find_element(*AppTab.GroupOption)).send_keys("group1" + Keys.ENTER).perform()
        time.sleep(2)
        return

    def addTextItem(self, itemname):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewItem)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.SelectText)).send_keys(itemname + Keys.ENTER).perform()
        time.sleep(1)
        return

    def addCardItem(self, itemname):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewItem)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.SelectCard)).send_keys(itemname + Keys.ENTER).perform()
        time.sleep(1)
        return

    def addImageCarouselItem(self, itemname):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewItem)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.SelectImageCarousel)).send_keys(itemname + Keys.ENTER).perform()
        time.sleep(1)
        return

    def addFlexMessageItem(self, itemname):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewItem)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.SelectFlexMessage)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.FlexMessageConfirm)).perform()
        time.sleep(1)
        action.send_keys(Keys.DELETE + itemname + Keys.ENTER).perform()
        time.sleep(1)
        return

    def addImageMapItem(self, itemname):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewItem)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.SelectImageMap)).send_keys(itemname + Keys.ENTER).perform()
        time.sleep(1)
        return

    def addImageItem(self, itemname):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewItem)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.SelectImage)).send_keys(itemname + Keys.ENTER).perform()
        time.sleep(1)
        return

    def addVideoItem(self, itemname):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewItem)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.SelectVideo)).send_keys(itemname + Keys.ENTER).perform()
        time.sleep(1)
        return

    def addConditionItem(self, itemname):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AppTab.AddNewItem)).perform()
        time.sleep(1)
        action.click(self.driver.find_element(*AppTab.SelectIfCondition)).send_keys(itemname + Keys.ENTER).perform()
        time.sleep(1)
        return

    def selectGroup1(self):
        MyGroups = self.driver.find_elements(*AppTab.GroupList)
        for MyGroup in MyGroups:
            if MyGroup.text == "group1":
                MyGroup.click()
                break
        return

    def selectActionItem(self, myactionitem):
        MyActionItems = self.driver.find_elements(*AppTab.ActionList)
        for MyActionItem in MyActionItems:
            if MyActionItem.text == myactionitem:
                MyActionItem.click()
                break
        return

    def enterTextItemsText(self, my_element, my_text):
        return self.driver.find_element(By.XPATH, my_element).send_keys(my_text + Keys.ENTER)

    def clickBigButton(self, my_big_button):
        return self.driver.find_element(By.XPATH, my_big_button).click()

    def clickQuickReactionButton(self, my_quick_reaction_button):
        return self.driver.find_element(By.XPATH, my_quick_reaction_button).click()

    def clickTextHandlerButton(self, my_text_handler_button):
        return self.driver.find_element(By.XPATH, my_text_handler_button).click()

    def selectMatchingType(self, my_type):
        self.driver.find_element(*AppTab.DropdownMatchingTypes).click()
        MyMatchingTypes = self.driver.find_elements(*AppTab.MatchingTypes)
        for MyMatchingType in MyMatchingTypes:
            if MyMatchingType.get_attribute("val") == my_type:
                MyMatchingType.click()
                break
        return

    def selectPatternType(self, my_pattern):
        MyPatternTypes = self.driver.find_elements(*AppTab.PatternTypes)
        for MyPatternType in MyPatternTypes:
            if MyPatternType.get_attribute("val") == my_pattern:
                MyPatternType.click()
                break
        return

    def clickFileHandlerButton(self, my_file_handler_button):
        return self.driver.find_element(By.XPATH, my_file_handler_button).click()

    def enterButtonsName(self, big_button_name):
        self.driver.find_element(*AppTab.ButtonsNameInputField).clear()
        return self.driver.find_element(*AppTab.ButtonsNameInputField).send_keys(big_button_name)

    def selectNextAction(self):
        self.driver.find_element(*AppTab.ActionNextAction).click()

    def selectManually(self):
        self.driver.find_element(*AppTab.ActionManually).click()

    def setNextAction(self, my_next_item):
        self.driver.find_element(*AppTab.AutocompleteOptions).clear()
        return self.driver.find_element(*AppTab.AutocompleteOptions).send_keys(my_next_item + Keys.ENTER)

    def clickAdvancedSettings(self):
        self.driver.find_element(*AppTab.AdvancedSettings).click()

    def enterUserKeyValue(self, myukey):
        self.driver.find_element(*AppTab.UkeyInputField).clear()
        return self.driver.find_element(*AppTab.UkeyInputField).send_keys(myukey)

    def saveSettings(self):
        return self.driver.find_element(*AppTab.SaveSettings).click()

    def selectDataSourceAPI(self, myitemsapidatasource):
        return self.driver.find_element(By.XPATH, myitemsapidatasource).click()

    def enterAPIDataSourceURL(self, myapiurl):
        time.sleep(1)
        self.driver.find_element(*AppTab.APIDataSourceURL).clear()
        return self.driver.find_element(*AppTab.APIDataSourceURL).send_keys(myapiurl + Keys.ENTER)

    def selectDataSourceContent(self, myitemscontentdatasource):
        return self.driver.find_element(By.XPATH, myitemscontentdatasource).click()

    def selectYourContentSource(self, mycontenticon, mysourceen, mysourcejp):
        self.driver.find_element(By.XPATH, mycontenticon).click()
        ContentSourceOptions = self.driver.find_elements(*AppTab.ContentDataSourceOptions)
        for ContentSourceOption in ContentSourceOptions:
            if ContentSourceOption.text == mysourceen or ContentSourceOption.text == mysourcejp:
                ContentSourceOption.click()
                break
        return

    def clickAddFlexMessageContent(self, myflexaddcontent):
        return self.driver.find_element(By.XPATH, myflexaddcontent).click()

    def addFlexMessageContent(self):
        with open('C:\\Users\\Professional\\PycharmProjects\\suffering\\pageobjects\\flex.txt', 'r') as text_file:
            lines = text_file.readlines()
        for line in lines:
            self.driver.find_element(*AppTab.FlexMessageTextarea).send_keys(line)
        return

    def saveFlexMessage(self):
        return self.driver.find_element(*AppTab.FlexMessageSaveButton).click()

    def clickCameraIcon(self, mycameraicon):
        return self.driver.find_element(By.XPATH, mycameraicon).click()

    def clickVideoCameraIcon(self, myvideocameraicon):
        return self.driver.find_element(By.XPATH, myvideocameraicon).click()

    def clickBrushIcon(self, mybrushicon):
        return self.driver.find_element(By.XPATH, mybrushicon).click()

    def clickImageLinkIcon(self, myimagelinkicon):
        return self.driver.find_element(By.XPATH, myimagelinkicon).click()

    def clickVideoLinkIcon(self, myvideolinkicon):
        return self.driver.find_element(By.XPATH, myvideolinkicon).click()

    def uploadImageMapItemImage(self):
        pyautogui.write(r'C:\Users\Professional\PycharmProjects\suffering-upd\uploaddata\image_map.jpg')
        pyautogui.press('enter')
        return

    def uploadImageItemImage(self):
        pyautogui.write(r'C:\Users\Professional\PycharmProjects\suffering-upd\uploaddata\flamingo.jpg')
        pyautogui.press('enter')
        return

    def uploadVideoItemImage(self):
        pyautogui.write(r'C:\Users\Professional\PycharmProjects\suffering-upd\uploaddata\flamingo.jpg')
        pyautogui.press('enter')
        return

    def uploadVideoItemVideo(self):
        pyautogui.write(r'C:\Users\Professional\PycharmProjects\suffering-upd\uploaddata\Flamingo1.mp4')
        pyautogui.press('enter')
        return

    def uploadVideoItemImageByLink(self, myimageinput):
        self.driver.find_element(By.XPATH, myimageinput).click()
        return self.driver.find_element(By.XPATH, myimageinput).send_keys("https://anybot-prerelease.s3.amazonaws.com/588_1673836819_0_newfmt.png" + Keys.ENTER)

    def uploadVideoItemVideoByLink(self, myvideoinput):
        self.driver.find_element(By.XPATH, myvideoinput).click()
        return self.driver.find_element(By.XPATH, myvideoinput).send_keys("https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4" + Keys.ENTER)

    def clickImageMapImage(self):
        return self.driver.find_element(*AppTab.ImageMapImage).click()

    def saveImageImapArea(self):
        return self.driver.find_element(*AppTab.SaveImapAreaButton).click()

    def setImageMapArea1(self):
        element1 = self.driver.find_element(By.XPATH, "//div[@class='imagemap']/b")
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element1, -240, -240).perform()
        resizeable = self.driver.find_element(By.XPATH, "//div[@class='imagemap']/i")

        action = ActionChains(self.driver)
        action.click_and_hold(resizeable).move_by_offset(110, 400).release().perform()
        time.sleep(1)
        return

    def setImageMapArea2(self):
        element2 = self.driver.find_element(By.XPATH, "(//div[@class='imagemap']/b)[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element2, 10, -240).perform()
        time.sleep(0.5)
        resizeable = self.driver.find_element(By.XPATH, "(//div[@class='imagemap']/i)[2]")
        action = ActionChains(self.driver)
        action.click_and_hold(resizeable).move_by_offset(207, 160).release().perform()
        time.sleep(0.5)
        return

    def setImageMapArea3(self):
        element3 = self.driver.find_element(By.XPATH, "(//div[@class='imagemap']/b)[3]")
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element3, 10, 0).perform()
        time.sleep(0.5)
        resizeable = self.driver.find_element(By.XPATH, "(//div[@class='imagemap']/i)[3]")
        action = ActionChains(self.driver)
        action.click_and_hold(resizeable).move_by_offset(207, 160).release().perform()
        time.sleep(0.5)
        return

    def selectIfOption(self, ifoption, ifoptions, myifoption):
        self.driver.find_element(By.XPATH, ifoption).click()
        time.sleep(1)
        MyIfOptions = self.driver.find_elements(By.XPATH, ifoptions)
        for MyIfOption in MyIfOptions:
            if MyIfOption.get_attribute("val") == myifoption:
                MyIfOption.click()
                break
        time.sleep(1)
        return

    def inputConditionOfConditionalItem(self, myconditioninput, mycondition):
        return self.driver.find_element(By.XPATH, myconditioninput).send_keys(mycondition + Keys.ENTER)

    def selectThenAction(self, thenoption, mythenoption):
        return self.driver.find_element(By.XPATH, thenoption).send_keys(mythenoption + Keys.ENTER)

    def selectElseAction(self, elseoption, myelseoption):
        return self.driver.find_element(By.XPATH, elseoption).send_keys(myelseoption + Keys.ENTER)












    def expandMenu(self):
        return self.driver.find_element(*AppTab.ThreeDots)

    def selectMenuOptions(self):
        return self.driver.find_elements(*AppTab.MenuOptions)


class CouponsTab:
    def __init__(self, driver):
        self.driver = driver

    EmptyPageH2 = (By.XPATH, "//h2")
    SearchField = (By.XPATH, "//input[@type='text']")
    NewCoupon = (By.XPATH, "//button[@class='new icon plus-circle']")

    RunningOption = (By.XPATH, "(//dl[@class='owners ui-tab-menu']/dd)[1]")
    AllOption = (By.XPATH, "(//dl[@class='owners ui-tab-menu']/dd)[2]")

    EditCouponIcon = (By.XPATH, "(//i[@class='icon edit'])[1]")
    SendCouponIcon = (By.XPATH, "(//i[@class='icon send'])[1]")
    DeleteCouponIcon = (By.XPATH, "(//i[@class='icon trash'])[1]")

    def getCouponsEmptyPageHeader(self):
        return self.driver.find_elements(*CouponsTab.EmptyPageH2)

    def couponsSearchField(self):
        return self.driver.find_elements(*CouponsTab.SearchField)

    def clickAllOption(self):
        return self.driver.find_element(*CouponsTab.AllOption).click()

    def clickRunningOption(self):
        return self.driver.find_element(*CouponsTab.RunningOption).click()

    def addNewCoupon(self):
        return self.driver.find_element(*CouponsTab.NewCoupon).click()

    def editCoupon(self):
        return self.driver.find_element(*CouponsTab.EditCouponIcon).click()

    def sendCoupon(self):
        return self.driver.find_element(*CouponsTab.SendCouponIcon).click()

    def deleteCoupon(self):
        return self.driver.find_element(*CouponsTab.DeleteCouponIcon).click()



class CouponPopup:
    def __init__(self, driver):
        self.driver = driver

    CouponName = (By.XPATH, "//input[@name='title']")

    CouponImage = (By.XPATH, "//div[@class='form-item-file']")

    CouponDiscountValue = (By.XPATH, "//input[@name='discount']")

    DiscountPercent = (By.XPATH, "//label[@data-value='%']")
    DiscountJPY = (By.XPATH, "//label[@data-value='JPY']")

    CouponDiscountPER = (By.XPATH, "//input[@value='%']")
    CouponDiscountJPY = (By.XPATH, "//input[@value='JPY']")

    CouponIssueLImit = (By.XPATH, "//input[@name='amount']")

    #add period options here
    DateRange = (By.XPATH, "//div[@class='form-type-checkbox']/label[@data-value='1']")
    DaysFromIssue = (By.XPATH, "//div[@class='form-type-checkbox']/label[@data-value='2']")

    CouponDateRange = (By.XPATH, "//input[@name='exp_type' and @value='1']")

    CouponDateRangeStartDate = (By.XPATH, "(//input[@class='dt-picker dt-picker-ipt'])[1]")
    CouponDateRangeEndDate = (By.XPATH, "(//input[@class='dt-picker dt-picker-ipt'])[2]")

    CouponDaysFromIssue = (By.XPATH, "//input[@name='exp_type' and @value='2']")

    CouponDaysFromIssueValue = (By.XPATH, "//input[@name='span']")

    CouponSegment = (By.XPATH, "//input[@class='autocomplete']")

    #add conditions options here
    OneTimeOnly = (By.XPATH, "//dd[@name='times']/div/label[@data-value='1']")
    OptionOneTimeOnly = (By.XPATH, "//input[@name='times' and @value='1']")

    OncePerCoupon = (By.XPATH, "//li[@name='mul_times_1']/div/label[@data-value='1']")
    OptionOncePerCoupon = (By.XPATH, "//input[@name='mul_times_1' and @value='1']")

    OncePerCouponTicket = (By.XPATH, "//li[@name='mul_times_1']/div/label[@data-value='2']")
    OptionOncePerCouponTicket = (By.XPATH, "//input[@name='mul_times_1' and @value='2']")

    MultipleTimes = (By.XPATH, "//dd[@name='times']/div/label[@data-value='2']")
    OptionMultipleTimes = (By.XPATH, "//input[@name='times' and @value='2']")

    OnceADay = (By.XPATH, "//li[@name='mul_times_2']/div/label[@data-value='1']")
    OptionOnceADay = (By.XPATH, "//input[@name='mul_times_2' and @value='1']")

    Unlimited = (By.XPATH, "//li[@name='mul_times_2']/div/label[@data-value='2']")
    OptionUnlimited = (By.XPATH, "//input[@name='mul_times_2' and @value='2']")

    CouponLinkTo = (By.XPATH, "//input[@name='linkto']")

    CouponDescription = (By.XPATH, "//textarea[@name='desc']")

    CouponSaveButton = (By.XPATH, "//button[@class='icon save']")
    CouponSendButton = (By.XPATH, "//button[@class='icon send']")
    CouponCancelButton = (By.XPATH, "//button[@class='icon cancel']")

    CouponCloseIcon = (By.XPATH, "//i[@class='icon close']")

    #Preview popup page objects
    PreviewSendButton = (By.XPATH, "//button[@class='icon send']")

    #Coupons alert popup
    AlertCloseIcon = (By.XPATH, "//i[@class='icon close']")

    #Sent and unsent coupons delete alert popup
    DeleteCouponOKButton = (By.XPATH, "//button[@class='a1']")

    def enterCouponName(self, name):
        self.driver.find_element(*CouponPopup.CouponName).clear()
        return self.driver.find_element(*CouponPopup.CouponName).send_keys(name)

    #image upload here

    def enterCouponDiscountValue(self, dis_val):
        self.driver.find_element(*CouponPopup.CouponDiscountValue).clear()
        return self.driver.find_element(*CouponPopup.CouponDiscountValue).send_keys(dis_val)

    def selectCouponPercentOption(self):
        if self.driver.find_element(*CouponPopup.DiscountPercent).get_attribute("class") == "sel-option radio on":
            return self.driver.find_element(*CouponPopup.CouponDiscountPER)
        else:
            return self.driver.find_element(*CouponPopup.CouponDiscountPER).click()

    def selectCouponJPYOption(self):
        if self.driver.find_element(*CouponPopup.DiscountJPY).get_attribute("class") == "sel-option radio on":
            return self.driver.find_element(*CouponPopup.CouponDiscountJPY)
        else:
            return self.driver.find_element(*CouponPopup.CouponDiscountJPY).click()

    def enterCouponIssueLimit(self, issue_val):
        self.driver.find_element(*CouponPopup.CouponIssueLImit).clear()
        return self.driver.find_element(*CouponPopup.CouponIssueLImit).send_keys(issue_val)

    #add period verification/selection options here
    def selectDateRangeOption(self):
        if self.driver.find_element(*CouponPopup.DateRange).get_attribute("class") == "sel-option checkbox on":
            return self.driver.find_element(*CouponPopup.CouponDateRange)
        else:
            return self.driver.find_element(*CouponPopup.CouponDateRange).click()

    def deselectDateRangeOption(self):
        if self.driver.find_element(*CouponPopup.DateRange).get_attribute("class") == "sel-option checkbox on":
            return self.driver.find_element(*CouponPopup.CouponDateRange).click()
        else:
            return self.driver.find_element(*CouponPopup.CouponDateRange)

    def selectDaysFromIssueOption(self):
        if self.driver.find_element(*CouponPopup.DaysFromIssue).get_attribute("class") == "sel-option checkbox on":
            return self.driver.find_element(*CouponPopup.CouponDaysFromIssue)
        else:
            return self.driver.find_element(*CouponPopup.CouponDaysFromIssue).click()

    def deselectDaysFromIssueOption(self):
        if self.driver.find_element(*CouponPopup.DaysFromIssue).get_attribute("class") == "sel-option checkbox on":
            return self.driver.find_element(*CouponPopup.CouponDaysFromIssue).click()
        else:
            return self.driver.find_element(*CouponPopup.CouponDaysFromIssue)

    def enterCouponDaysFromIssueValue(self, issue_value):
        self.driver.find_element(*CouponPopup.CouponDaysFromIssueValue).clear()
        return self.driver.find_element(*CouponPopup.CouponDaysFromIssueValue).send_keys(issue_value)

    def enterCouponStartDate(self, start_date):
        self.driver.find_element(*CouponPopup.CouponDateRangeStartDate).clear()
        return self.driver.find_element(*CouponPopup.CouponDateRangeStartDate).send_keys(start_date)

    def enterCouponEndDate(self, end_date):
        self.driver.find_element(*CouponPopup.CouponDateRangeEndDate).clear()
        return self.driver.find_element(*CouponPopup.CouponDateRangeEndDate).send_keys(end_date)

    def enterCouponSegment(self):
        return self.driver.find_element(*CouponPopup.CouponSegment)

    #add conditions options here
    def selectOneTimeOnly(self):
        if self.driver.find_element(*CouponPopup.OneTimeOnly).get_attribute("class") == "sel-option radio on":
            return self.driver.find_element(*CouponPopup.OptionOneTimeOnly)
        else:
            return self.driver.find_element(*CouponPopup.OptionOneTimeOnly).click()

    def selectOncePerCouponOption(self):
        if self.driver.find_element(*CouponPopup.OncePerCoupon).get_attribute("class") == "sel-option radio on":
            return self.driver.find_element(*CouponPopup.OptionOncePerCoupon)
        else:
            return self.driver.find_element(*CouponPopup.OptionOncePerCoupon).click()

    def selectOncePerCouponTicketOption(self):
        if self.driver.find_element(*CouponPopup.OncePerCouponTicket).get_attribute("class") == "sel-option radio on":
            return self.driver.find_element(*CouponPopup.OptionOncePerCouponTicket)
        else:
            return self.driver.find_element(*CouponPopup.OptionOncePerCouponTicket).click()

    def selectMultipleTimes(self):
        if self.driver.find_element(*CouponPopup.MultipleTimes).get_attribute("class") == "sel-option radio on":
            return self.driver.find_element(*CouponPopup.OptionMultipleTimes)
        else:
            return self.driver.find_element(*CouponPopup.OptionMultipleTimes).click()

    def selectOnceADayOption(self):
        if self.driver.find_element(*CouponPopup.OnceADay).get_attribute("class") == "sel-option radio on":
            return self.driver.find_element(*CouponPopup.OptionOnceADay)
        else:
            return self.driver.find_element(*CouponPopup.OptionOnceADay).click()

    def selectUnlimitedOption(self):
        if self.driver.find_element(*CouponPopup.Unlimited).get_attribute("class") == "sel-option radio on":
            return self.driver.find_element(*CouponPopup.OptionUnlimited)
        else:
            return self.driver.find_element(*CouponPopup.OptionUnlimited).click()

    def enterCouponLinkTo(self, link):
        self.driver.find_element(*CouponPopup.CouponLinkTo).clear()
        return self.driver.find_element(*CouponPopup.CouponLinkTo).send_keys(link)

    def enterCouponDescription(self, desc):
        self.driver.find_element(*CouponPopup.CouponDescription).clear()
        return self.driver.find_element(*CouponPopup.CouponDescription).send_keys(desc)

    def saveNewCoupon(self):
        return self.driver.find_element(*CouponPopup.CouponSaveButton).click()

    def sendNewCoupon(self):
        return self.driver.find_element(*CouponPopup.CouponSendButton).click()

    def cancelNewCoupon(self):
        return self.driver.find_element(*CouponPopup.CouponCancelButton)

    def closeIcon(self):
        return self.driver.find_element(*CouponPopup.CouponCloseIcon)

    def sendFromPreviewPopup(self):
        return self.driver.find_element(*CouponPopup.PreviewSendButton).click()

    def closeCouponsAlertPopup(self):
        return self.driver.find_element(*CouponPopup.AlertCloseIcon).click()

    def submitDeleteSentCoupon(self):
        return self.driver.find_element(*CouponPopup.DeleteCouponOKButton).click()

    def submitDeleteUnsentCoupon(self):
        return self.driver.find_element(*CouponPopup.DeleteCouponOKButton).click()

















