from pages.locators import LandingPageLocators
from pages.landing_page import LandingPage
import time


def test_click_sun_icon(browser):
    """Test 'Join' button in HEADER. [9] test from check-list"""
    page = LandingPage(browser, LandingPageLocators.LINK)
    page.open()

    page.browser.find_element(*LandingPageLocators.SUN_ICON_HEADER_BUTTON).click()
    
    time.sleep(10)

