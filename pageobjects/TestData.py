class Group1TestData:
    def __init__(self, driver):
        self.driver = driver

    MyGroup1Items = [
        {
            "item_option": "//dd[@rt='text']",
            "item_name": "textitem1",
            "item_content": "text1",
            "item_xpath": "(//textarea[@class='msg with-emoticon'])[1]",
            "item_big_button": "(//li[@tp='items'])[1]",
            "item_big_button_name": "text1 button"
        },
        {
            "item_option": "//dd[@rt='text']",
            "item_name": "textitem2",
            "item_content": "text2",
            "item_xpath": "(//textarea[@class='msg with-emoticon'])[2]",
            "item_big_button": "(//li[@tp='items'])[2]",
            "item_quick_reaction_button": "(//label[@class='new'])[2]"
        },
        {
            "item_option": "//dd[@rt='text']",
            "item_name": "textitem3",
            "item_content": "text3",
            "item_xpath": "(//textarea[@class='msg with-emoticon'])[3]",
            "item_big_button": "(//li[@tp='items'])[3]",
            "item_text_handler_button": "(//div[@class='react-ipts-new']/span)[3]",
            "item_matching_type": "pattern",
            "item_matching_pattern": "len:1"
        },
        {
            "item_option": "//dd[@rt='text']",
            "item_name": "textitem4",
            "item_content": "text4",
            "item_xpath": "(//textarea[@class='msg with-emoticon'])[4]",
            "item_big_button": "(//li[@tp='items'])[4]",
            "item_file-handler": "(//div[@class='react-fhs-new']/span)[4]"
        },
        {
            "item_option": "//dd[@rt='card']",
            "item_name": "carousel1",
            "item_api_data_source": "(//b[@class='icon coding'])[5]",
            "item_content_pre": "https://pre.bonp.me/api/service/recipes/?format=list",
            "item_content_prod": "https://anybot.me/api/service/recipes/?format=list",
            "item_big_button": "(//li[@tp='items'])[12]",
            "item_big_button_name": "Next"
        },
        {
            "item_option": "//dd[@rt='card']",
            "item_name": "carousel2",
            "item_big_button": "(//li[@class='item new'])[17]",
            "item_big_button_name1": "save",
            "item_big_button_name2": "reserve",
            "item_content_data_source": "(//b[@class='icon double-right'])[2]",
            "item_content_icon": "(//button[@class='ui-menu'])[12]",
            "item_quick_reaction_button": "(//label[@class='new'])[6]",
            "item_quick_reaction_button_name": "Next",
            "item_source_en": "Events",
            "item_source_jp": "????????????"
        },
        {
            "item_option": "//dd[@rt='imagecard']",
            "item_name": "image_carousel",
            "item_content_data_source": "(//b[@class='icon double-right'])[3]",
            "item_content_icon": "(//button[@class='ui-menu'])[14]",
            "item_big_button": "(//li[@class='row-imagecard src-content on']/div/div/ol/li[@class='item new'])[1]",
            "item_big_button_name": "Next",
            "item_source_en": "Events",
            "item_source_jp": "????????????"
        },
        {
            "item_option": "//dd[@rt='flex']",
            "item_name": "flex_message",
            "item_add_content": "//ol[@class='card imagecard new flex']",
            "item_content": "",
            "item_quick_reaction_button": "(//label[@class='new'])[8]",
            "item_quick_reaction_button_name": "Next"
        },
        {
            "item_option": "//dd[@rt='imagemap']",
            "item_name": "image_map",
            "item_camera_icon": "(//ol[@class='card imagecard seq-0']/i[@class='icon camera large upload-btn'])[17]",
            "item_brush_icon": "(//i[@class='icon brush large upload-btn'])[17]",
            "item_link_icon": "(//i[@class='icon link large upload-btn'])[17]",
            "item_image_link": "https://anybot-prerelease.s3.amazonaws.com/618_1674651478_0_newfmt.jpg",
            "item_area1_button": "(//div/div/input[@class='autocomplete'])[11]",
            "item_area2_button": "(//div/div/input[@class='autocomplete'])[11]",
            "item_area3_button": "(//div/div/input[@class='autocomplete'])[11]",
        },
        {
            "item_option": "//dd[@rt='image']",
            "item_name": "image1",
            "item_camera_icon": "(//ol[@class='card imagecard seq-0']/i[@class='icon camera large upload-btn'])[18]",
            "item_brush_icon": "(//i[@class='icon brush large upload-btn'])[18]",
            "item_link_icon": "(//i[@class='icon link large upload-btn'])[18]",
            "item_quick_reaction_button": "(//label[@class='new'])[10]",
            "item_quick_reaction_button_name": "Next",
        },
        {
            "item_option": "//dd[@rt='video']",
            "item_name": "video1",
            "item_camera_icon": "//ol/i[@class='icon camera large upload-btn left_t']",
            "item_video_camera_icon": "//ol/i[@class='icon video large upload-btn left_b']",
            "item_image_link_icon": "//ol/i[@class='icon link large upload-btn right_t']",
            "item_video_link_icon": "(//ol/i[@class='icon link large upload-btn'])[19]",
            "item_quick_reaction_button": "(//label[@class='new'])[11]",
            "item_quick_reaction_button_name": "Next",
        },
        {
            "item_option": "//dd[@rt='video']",
            "item_name": "video2",
            "item_camera_icon": "(//ol/i[@class='icon camera large upload-btn left_t'])[2]",
            "item_video_camera_icon": "(//ol/i[@class='icon video large upload-btn left_b'])[2]",
            "item_image_link_icon": "(//ol/i[@class='icon link large upload-btn right_t'])[2]",
            "item_video_link_icon": "(//ol/i[@class='icon link large upload-btn'])[20]",
            "item_image_link_input": "(//i[@class='icon link large upload-btn right_t'])[2]/input",
            "item_video_link_input": "(//i[@class='icon link large upload-btn'])[20]/input",
            "item_quick_reaction_button": "(//label[@class='new'])[12]",
            "item_quick_reaction_button_name": "Next",
        },
        {
            "item_option": "//dd[@rt='logical']",
            "item_name": "conditional",
            "item_if_field": "//div[@class='fbox']/div[@class='ui-dropdown']",
            "item_field_options": "//ul[@class='ui-dropdown-opts']/li",
            "item_if_option_val": "ukey",
            "item_condition_field": "//input[@name='condition']",
            "item_condition_option": "{{user.choice}}=choice1",
            "item_then_field": "//input[@target_name='then']",
            "item_then_option": "1:textitem1",
            "item_else_field": "//input[@target_name='else']",
            "item_else_option": "6:carousel2",
        },
        {
            "item_option": "//dd[@rt='flex']",
            "item_name": "another_flex_message",
            "item_add_content": "(//ol[@class='card imagecard new flex'])[2]",
            "item_content": ""
        },

    ]

    """"for i in range(len(myData)):
        print(myData[i]["item_name"])
        print(myData[i]["item_xpath"])
        print(myData[i]["item_content"])"""
    # print(len(myData))


"""    {
            "item_option": "//dd[@rt='card']",
            "item_name": "carousel1",
        },"""


class EventsTestData:
    def __init__(self, driver):
        self.driver = driver

    myEvent = [
        {"event-url": "https://www.udemy.com/",
         "event-title": "Test Event1",
         "event-desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae arcu turpis. Morbi quis dignissim nunc, nec luctus nibh. In luctus porttitor posuere. Quisque.",
         "event-seats": "1",
        },
        {"event-url": "https://www.netflix.com/",
         "event-title": "Test Event2",
         "event-desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae arcu turpis. Morbi quis dignissim nunc, nec luctus nibh. In luctus porttitor posuere. Quisque.",
         "event-seats": "1",
         },
        {"event-url": "https://soundcloud.com/",
         "event-title": "Test Event3",
         "event-desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae arcu turpis. Morbi quis dignissim nunc, nec luctus nibh. In luctus porttitor posuere. Quisque.",
         "event-seats": "1",
         },
    ]

class StoreTestData:
    def __init__(self, driver):
        self.driver = driver
    myStore = [
        {
            "store-url": "https://jerryspringertv.com/",
            "store-name": "store1",
            "store-description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis non ornare ante, non vestibulum elit. Vivamus a erat dictum, porttitor ante in, commodo risus. Vivamus lacinia velit ut purus pulvinar ultricies. Sed hendrerit scelerisque quam, ac volutpat sem mattis eget. Nulla viverra leo eget dui pretium, at condimentum libero ullamcorper.",
            "store-category": "TestCategory",
            "store-country": "Japan",
            "store-address": "15-1 Udagawacho, Shibuya City, Tokyo 150-0042",
            "store-latitude": "35.6621425",
            "store-longitude": "139.6984964",
            "store-weekdays-start-time": "11",
            "store-weekdays-end-time": "17",
            "store-break-time": "13:00-14:00",

        },
    ]


class CouponsTestData:
    def __init__(self, driver):
        self.driver = driver
    myCoupon = [
        {"coupon-name": "TestCoupon",
         "coupon-image": "",
         "coupon-discount": "15",
         "coupon-issued": "10",
         "coupon-start-date": "",
         "coupon-end-date": "",
         "coupon-days-from-issue": "",
         "coupon-link": "",
         "coupon-description": "",
         },
        {"coupon-name": "EditedTestCoupon",
         "coupon-image": "",
         "coupon-discount": "55",
         "coupon-issued": "17",
         "coupon-start-date": "2022-12-27 12:00",
         "coupon-end-date": "2022-12-29 12:00",
         "coupon-days-from-issue": "0",
         "coupon-link": "",
         "coupon-description": "This is an edited coupon!",
         },
        {"coupon-name": "1234567890",
         "coupon-image": "",
         "coupon-discount": "",
         "coupon-issued": "",
         "coupon-start-date": "",
         "coupon-end-date": "",
         "coupon-days-from-issue": "",
         "coupon-link": "",
         "coupon-description": "This coupon is sent directly from the [New Coupon] popup. Did you get it?",
         },
        {"coupon-name": "?????????????????????",
         "coupon-image": "",
         "coupon-discount": "",
         "coupon-issued": "",
         "coupon-start-date": "",
         "coupon-end-date": "",
         "coupon-days-from-issue": "",
         "coupon-link": "",
         "coupon-description": "This is a saved coupon sent from the coupons list. Did you get it?",
         },
        {"coupon-name": "?????????",
         "coupon-image": "",
         "coupon-discount": "10",
         "coupon-issued": "1",
         "coupon-start-date": "",
         "coupon-end-date": "",
         "coupon-days-from-issue": "",
         "coupon-link": "",
         "coupon-description": "This coupon should verify the issue field. The user with the lowest ID should get it",
         },
        {"coupon-name": "Date Range: multiple times + once a day",
         "coupon-image": "",
         "coupon-discount": "15",
         "coupon-issued": "20",
         "coupon-start-date": "2023-01-06 10:00",
         "coupon-end-date": "2023-01-07 12:00", #!!!!!!!!!!!!!!!Edit end-date before each regression test.
         "coupon-days-from-issue": "",
         "coupon-link": "",
         "coupon-description": "This coupon can be used once a day during selected period. This coupon can be used again tomorrow, till 12:00.",
         },
        {"coupon-name": "Days from issue: multiple times + unlimited",
         "coupon-image": "",
         "coupon-discount": "20",
         "coupon-issued": "20",
         "coupon-start-date": "",
         "coupon-end-date": "",
         "coupon-days-from-issue": "2",
         "coupon-link": "",
         "coupon-description": "This coupon can be used multiple times during selected period. This coupon can be used for the next 48hours after dleivery.",
         },
        {"coupon-name": "Date Range + Days from issue: multiple times + unlimited",
         "coupon-image": "",
         "coupon-discount": "25",
         "coupon-issued": "20",
         "coupon-start-date": "",
         "coupon-end-date": "",
         "coupon-days-from-issue": "1",
         "coupon-link": "",
         "coupon-description": "This coupon can be used multiple times during selected period. This coupon can be used for the next 48hours after dleivery.",
         },
        {"coupon-name": "Coupon-delete-test-1",
         "coupon-image": "",
         "coupon-discount": "",
         "coupon-issued": "",
         "coupon-start-date": "",
         "coupon-end-date": "",
         "coupon-days-from-issue": "",
         "coupon-link": "",
         "coupon-description": "",
         },
        {"coupon-name": "Coupon-delete-test-2",
         "coupon-image": "",
         "coupon-discount": "",
         "coupon-issued": "",
         "coupon-start-date": "",
         "coupon-end-date": "",
         "coupon-days-from-issue": "",
         "coupon-link": "",
         "coupon-description": "",
         },
    ]


print(CouponsTestData.myCoupon[0]["coupon-name"])
