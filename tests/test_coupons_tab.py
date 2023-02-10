import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.PageObjects import CouponsTab, CouponPopup
from utilities.BaseClass import BaseClass
from pageobjects.TestData import CouponsTestData


@pytest.mark.usefixtures("setup")
class TestCases(BaseClass):
    def test_coupons_8_1_0(self):
        log = self.getLogs()
        log.info("[8.1] Click the [Coupons] tab.")
        self.accessCouponsTab()

        assert self.driver.find_element(By.XPATH, "//h2").text == "No data to display." or "表示可能なデータは見つかりませんでした。"
        assert self.driver.find_element(By.XPATH, "//input[@type='text']").get_attribute("placeholder") == "Search by coupon code or name"
        assert self.driver.find_element(By.XPATH, "//button[@class='new icon plus-circle']").is_displayed()

    def test_coupons_8_3_0(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        log.info("1. Click the [+ New coupon] button.")
        couponPopup = CouponPopup(self.driver)
        couponPopup.enterCouponName(MyCoupon[0]["coupon-name"])
        couponPopup.enterCouponDiscountValue(MyCoupon[0]["coupon-discount"])
        couponPopup.selectCouponPercentOption()
        couponPopup.enterCouponIssueLimit(MyCoupon[0]["coupon-issued"])
        log.info("2. Enter random data in the coupons fields.")
        couponPopup.saveNewCoupon()
        log.info("3. Click the [Save] button.")
        time.sleep(2)

        assert self.driver.find_element(By.XPATH, "(//td[@class='list-item-title'])[1]").text == "TestCoupon"
        assert self.driver.find_element(By.XPATH, "(//td[@class='list-item-discount'])[1]").text == "15%"

    def test_coupons_8_4_1(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.editCoupon()
        log.info("1. Click the [Edit] icon of the coupon you have just created.")
        couponPopup = CouponPopup(self.driver)
        couponPopup.enterCouponName(MyCoupon[1]["coupon-name"])
        couponPopup.enterCouponDiscountValue(MyCoupon[1]["coupon-discount"])
        couponPopup.selectCouponJPYOption()
        couponPopup.enterCouponIssueLimit(MyCoupon[1]["coupon-issued"])
        couponPopup.enterCouponStartDate(MyCoupon[1]["coupon-start-date"])
        couponPopup.enterCouponEndDate(MyCoupon[1]["coupon-end-date"])
        couponPopup.enterCouponDescription(MyCoupon[1]["coupon-description"])
        log.info("2. Make some changes to the coupons settings.")
        couponPopup.saveNewCoupon()
        log.info("3. Click the [Save] button.")
        time.sleep(2)
        couponsTab.editCoupon()
        log.info("4. Click the [Edit] icon again.")
        time.sleep(2)

        assert self.driver.find_element(By.XPATH,
                                        "//input[@name='title']").get_attribute("data-value") == "EditedTestCoupon"
        assert self.driver.find_element(By.XPATH,
                                        "//input[@name='discount']").get_attribute("data-value") == "55"
        assert self.driver.find_element(By.XPATH,
                                        "//label[@data-value='JPY']").get_attribute("class") == "sel-option radio on"
        assert self.driver.find_element(By.XPATH,
                                        "(//input[@class='dt-picker dt-picker-ipt'])[1]").get_attribute("data-value") == "2022-12-27 12:00"
        assert self.driver.find_element(By.XPATH,
                                        "(//input[@class='dt-picker dt-picker-ipt'])[2]").get_attribute("data-value") == "2022-12-29 12:00"
        assert self.driver.find_element(By.XPATH,
                                        "//input[@name='amount']").get_attribute("data-value") == "17"
        assert self.driver.find_element(By.XPATH,
                                        "//textarea[@name='desc']").get_attribute("data-value") == "This is an edited coupon!"

    def test_coupons_8_4_2(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        log.info("1. Click the [+ New coupon] button.")
        couponPopup = CouponPopup(self.driver)
        couponPopup.saveNewCoupon()
        log.info("2. Click the [Save] button.")
        time.sleep(1)
        couponsTab.editCoupon()
        log.info("3. Click the [Edit] icon again.")

    def test_coupons_8_5_1(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        log.info("1. Click the [+ New coupon] button.")
        couponPopup = CouponPopup(self.driver)
        couponPopup.enterCouponName(MyCoupon[2]["coupon-name"])
        couponPopup.enterCouponDescription(MyCoupon[2]["coupon-description"])
        log.info("2. Do not make any changes.")
        couponPopup.sendNewCoupon()
        time.sleep(3)
        log.info("3. Click the [Send] button in the [New Coupon] popup.")
        couponPopup.sendFromPreviewPopup()
        time.sleep(3)
        log.info("4. Click the [Send] button in the [Preview] popup.")
        assert self.driver.find_element(By.XPATH, "//div[@name='alert']/div/p").text == "Preparing coupon to be sent"
        couponPopup.closeCouponsAlertPopup()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH,
                                        "//tr[@class='broadcasted']/td[@class='list-item-title']").text == "1234567890"
        assert self.driver.find_element(By.XPATH,
                                        "//tr[@class='broadcasted']/td[@class='list-item-broadcast_t list-view-common']").text != "Waiting to be sent"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[1]").get_attribute(
            "class") == "icon noclick"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[2]").get_attribute(
            "class") == "icon noclick"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[3]").get_attribute(
            "class") == "icon trash"

    def test_coupons_8_5_2(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        log.info("1. Click the [+ New coupon] button.")
        couponPopup = CouponPopup(self.driver)
        couponPopup.enterCouponName(MyCoupon[3]["coupon-name"])
        couponPopup.enterCouponDescription(MyCoupon[3]["coupon-description"])
        log.info("2. Do not make any changes.")
        couponPopup.saveNewCoupon()
        time.sleep(2)
        log.info("3. Click the [Save] button in the [New Coupon] popup.")
        couponsTab.sendCoupon()
        time.sleep(2)
        log.info("4. Click the [Send] icon in the operation column the coupon you have just created.")
        couponPopup.sendFromPreviewPopup()
        time.sleep(2)
        log.info("5. Click the [Send] button in the [Preview] popup.")
        assert self.driver.find_element(By.XPATH, "//div[@name='alert']/div/p").text == "Preparing coupon to be sent"
        couponPopup.closeCouponsAlertPopup()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH,
                                        "//tr[@class='broadcasted']/td[@class='list-item-title']").text == "テストクーポン"
        assert self.driver.find_element(By.XPATH,
                                        "//tr[@class='broadcasted']/td[@class='list-item-broadcast_t list-view-common']").text != "Waiting to be sent"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[1]").get_attribute(
            "class") == "icon noclick"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[2]").get_attribute(
            "class") == "icon noclick"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[3]").get_attribute(
            "class") == "icon trash"

    def test_coupons_8_5_3(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        log.info("1. Click the [+ New coupon] button.")
        couponPopup = CouponPopup(self.driver)
        couponPopup.enterCouponName(MyCoupon[4]["coupon-name"])
        couponPopup.enterCouponDiscountValue(MyCoupon[4]["coupon-discount"])
        couponPopup.selectCouponPercentOption()
        couponPopup.enterCouponDescription(MyCoupon[4]["coupon-description"])
        log.info("2. Fill in a random coupon's data.")
        couponPopup.enterCouponIssueLimit(MyCoupon[4]["coupon-issued"])
        log.info("3. Set [Issue] to 1.")
        couponPopup.sendNewCoupon()
        time.sleep(2)
        log.info("4. Click the [Send] button in the [New Coupon] popup.")
        couponPopup.sendFromPreviewPopup()
        time.sleep(3)
        log.info("5. Click the [Send] button in the [Preview] popup.")
        assert self.driver.find_element(By.XPATH, "//div[@name='alert']/div/p").text == "Preparing coupon to be sent"
        couponPopup.closeCouponsAlertPopup()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH,
                                        "//tr[@class='broadcasted']/td[@class='list-item-title']").text == "割引券"
        assert self.driver.find_element(By.XPATH,
                                        "//tr[@class='broadcasted']/td[@class='list-item-discount']").text == "10%"

    def test_coupons_8_5_4(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        log.info("1. Click the [+ New coupon] button.")
        couponPopup = CouponPopup(self.driver)
        couponPopup.enterCouponName(MyCoupon[5]["coupon-name"])
        couponPopup.enterCouponDiscountValue(MyCoupon[5]["coupon-discount"])
        couponPopup.selectCouponPercentOption()
        couponPopup.enterCouponIssueLimit(MyCoupon[5]["coupon-issued"])
        couponPopup.enterCouponDescription(MyCoupon[5]["coupon-description"])
        log.info("2. Fill in a random coupon's data.")
        couponPopup.selectDateRangeOption()
        log.info("3. Set [Period] as [Date range].")
        couponPopup.enterCouponStartDate(MyCoupon[5]["coupon-start-date"])
        couponPopup.enterCouponEndDate(MyCoupon[5]["coupon-end-date"])
        log.info("4. Set [Start date] as [day before], set [End date] as [next day].")
        couponPopup.selectMultipleTimes()
        couponPopup.selectOnceADayOption()
        log.info("5. Set [Conditions] as [Multiple times] > [Once a Day]")
        couponPopup.saveNewCoupon()
        time.sleep(2)
        log.info("6. Save the coupon.")
        """couponPopup.sendNewCoupon()
        time.sleep(2)
        log.info("6. Click the [Send] button in the [New Coupon] popup.")
        couponPopup.sendFromPreviewPopup()
        time.sleep(3)
        log.info("7. Click the [Send] button in the [Preview] popup.")
        assert self.driver.find_element(By.XPATH, "//div[@name='alert']/div/p").text == "Preparing coupon to be sent"
        couponPopup.closeCouponsAlertPopup()
        time.sleep(2)"""
        # add assertion

    def test_coupons_8_5_5(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        log.info("1. Click the [+ New coupon] button.")
        couponPopup = CouponPopup(self.driver)
        couponPopup.enterCouponName(MyCoupon[6]["coupon-name"])
        couponPopup.enterCouponDiscountValue(MyCoupon[6]["coupon-discount"])
        couponPopup.selectCouponPercentOption()
        couponPopup.enterCouponIssueLimit(MyCoupon[6]["coupon-issued"])
        couponPopup.enterCouponDescription(MyCoupon[6]["coupon-description"])
        log.info("2. Fill in a random coupon's data.")
        couponPopup.deselectDateRangeOption()
        couponPopup.selectDaysFromIssueOption()
        log.info("3. Set [Period] as [Days from issue].")
        couponPopup.enterCouponDaysFromIssueValue(MyCoupon[6]["coupon-days-from-issue"])
        log.info("4. Set [From Issue time to] as [2].")
        couponPopup.selectMultipleTimes()
        couponPopup.selectUnlimitedOption()
        log.info("5. Set [Conditions] as [Multiple times] > [Unlimited].")
        couponPopup.saveNewCoupon()
        time.sleep(2)
        log.info("6. Save the coupon.")

        """couponPopup.sendNewCoupon()
        time.sleep(2)
        log.info("6. Click the [Send] button in the [New Coupon] popup.")
        couponPopup.sendFromPreviewPopup()
        time.sleep(3)
        log.info("7. Click the [Send] button in the [Preview] popup.")
        assert self.driver.find_element(By.XPATH, "//div[@name='alert']/div/p").text == "Preparing coupon to be sent"
        couponPopup.closeCouponsAlertPopup()
        time.sleep(2)"""
        #add assertion

    def test_coupons_8_5_6(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        log.info("1. Click the [+ New coupon] button.")
        couponPopup = CouponPopup(self.driver)

        couponPopup.saveNewCoupon()
        time.sleep(2)
        log.info("6. Save the coupon.")
        """couponPopup.sendNewCoupon()
        time.sleep(2)
        log.info("6. Click the [Send] button in the [New Coupon] popup.")
        couponPopup.sendFromPreviewPopup()
        time.sleep(3)
        log.info("7. Click the [Send] button in the [Preview] popup.")
        assert self.driver.find_element(By.XPATH, "//div[@name='alert']/div/p").text == "Preparing coupon to be sent"
        couponPopup.closeCouponsAlertPopup()
        time.sleep(2)"""
        # add assertion
        """Comment"""

    def test_coupons_8_12_1(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        couponPopup = CouponPopup(self.driver)
        couponPopup.enterCouponName(MyCoupon[5]["coupon-name"])
        couponPopup.sendNewCoupon()
        time.sleep(2)
        couponPopup.sendFromPreviewPopup()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, "//div[@name='alert']/div/p").text == "Preparing coupon to be sent"
        couponPopup.closeCouponsAlertPopup()
        time.sleep(1)
        assert self.driver.find_element(By.XPATH,
                                        "//tr[@class='broadcasted']/td[@class='list-item-title']").text == "Coupon-delete-test-1"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[1]").get_attribute(
            "class") == "icon noclick"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[2]").get_attribute(
            "class") == "icon noclick"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[3]").get_attribute(
            "class") == "icon trash"
        couponsTab.deleteCoupon()
        time.sleep(1)
        log.info("1. Click the [Trash] icon in the operation column of the sent coupon's raw.")
        assert self.driver.find_element(By.XPATH,
                                        "//p[@class='popup-text']/div").text == "The coupon has been issued. After deletion, users can still use it. Are you sure you want to delete it?"
        couponPopup.submitDeleteSentCoupon()
        time.sleep(2)
        log.info("2. Click the [OK] button in the sent coupon deleting warning popup.")
        assert self.driver.find_element(By.XPATH,
                                        "//tr[@class='broadcasted']/td[@class='list-item-title']").text != "Coupon-delete-test-1"

        """A reusable function to iterate through the list of all coupons should be added"""

    def test_coupons_8_12_2(self):
        log = self.getLogs()
        MyCoupon = CouponsTestData.myCoupon
        self.accessCouponsTab()
        couponsTab = CouponsTab(self.driver)
        couponsTab.addNewCoupon()
        couponPopup = CouponPopup(self.driver)
        couponPopup.enterCouponName(MyCoupon[6]["coupon-name"])
        couponPopup.saveNewCoupon()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH,
                                        "(//tr/td[@class='list-item-title'])[1]").text == "Coupon-delete-test-2"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[1]").get_attribute(
            "class") == "icon edit"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[2]").get_attribute(
            "class") == "icon send"
        assert self.driver.find_element(By.XPATH,
                                        "(//td[@class = 'list-item-undefined buttons']/i)[3]").get_attribute(
            "class") == "icon trash"
        couponsTab.deleteCoupon()
        time.sleep(2)
        log.info("1. Click the [Trash] icon in the operation column of the unsent coupon's raw.")
        assert self.driver.find_element(By.XPATH,
                                        "//p[@class='popup-text']/div").text == "Are you sure you want to REMOVE this coupon?"
        couponPopup.submitDeleteUnsentCoupon()
        time.sleep(2)
        log.info("2. Click the [OK] button in the unsent coupon deleting warning popup.")
        assert self.driver.find_element(By.XPATH,
                                        "(//tr/td[@class='list-item-title'])[1]").text != "Coupon-delete-test-2"

        """A reusable function to iterate through the list of all coupons should be added"""










































