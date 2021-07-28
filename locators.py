"""
Locators for our elements that are used in page.py
"""
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME_TEXTBOX = (By.ID, 'txtUserID')
    PASSWORD_TEXTBOX = (By.ID, 'txtPassword')
    LOGIN_BUTTON = (By.ID, "sub")
    
class DesinerStudioLocators(object):
    COMMERCIAL_TO_RESIDENTIAL = (By.XPATH, '/html/body/div[4]/header/div/div/div[1]/div/div/div[3]')
    SWITCH_APP = (By.XPATH, '//*[@id="menu-item-$PpyNavigation1623247002130$ppyElements$l1$ppyElements$l9"]/a/span/span')
    RESIDENTIAL = (By.XPATH, '//*[@id="$PpyNavigation1623247002130$ppyElements$l1$ppyElements$l9"]/li[3]/a')
    LAUNCH_BUTTON = (By.XPATH, '//*[@id="RULE_KEY"]/div[1]/div/div/div[4]')
    ADMIN_PORTAL = (By.XPATH, '//*[@id="pyNavigation1623247002166"]/li[2]/a')

class AdminPortalLocators(object):
    SEARCH_POLICY_BOX = (By.ID, 'pySearchText')
    RENEWED = (By.XPATH, '//a[starts-with(@name, "pyCaseSummary_pyWorkPage_")][contains(@data-test-id, "201908191427580876580858")]')
    RENEWED_2 = (By.XPATH, '//a[starts-with(@name, "pyCaseSummary_pyWorkPage_")][contains(@data-test-id, "201908191427580876579912")]')
    RENEWED_CHECK_BOX = (By.XPATH, '//div[contains(@data-ui-meta, "NonRenewable")]//span[contains(@data-test-id, "201908120909080652595220")]//img[contains(@alt, "true")]')
    ACTIONS_DROP_MENU = (By.XPATH, '//button[contains(@title, "Actions")]')
    UPDATE_SHELL = (By.XPATH,  '//a[contains(@data-click, "UpdateShell")]')
    HO_DF_BOX = (By.ID, 'InsuranceCarrier')
    HOME_POLICY_NUM = (By.ID, 'HomeOwnersNumber')
    HO_DF_BOX_CHECK = (By.XPATH, '//div[starts-with(@class, "field-item dataValueRead")]//span[contains(@data-test-id, "20200117132915002082777")]')
    HOME_POLICY_NUM_CHECK = (By.XPATH, '//div[starts-with(@class, "field-item dataValueRead")]//span[contains(@data-test-id, "20200117132915002083817")]')
    AGENT_CODE = (By.XPATH, '//div[starts-with(@class, "field-item dataValueRead")]//span[contains(@data-test-id, "20180308135434014591765")]')
    AGENT_CHECK = (By.XPATH, '//div[contains(@class, "content-item content-field item-2 flex")]//div[starts-with(@class, "field-item dataValueRead")]//span[starts-with(@data-test-id, "20180308135434014591765")]')
    AGENCY_NAME = (By.ID, 'SeachLocations')
    TEMP_TOGGLE_NAME = (By.XPATH, '//tr[contains(@data-gargs, "John MacDonald")]')
    AGENT_ON_RECORD = (By.ID, 'ContactId')
    SUBMIT = (By.XPATH, '//button[contains(@data-test-id, "2014121801251706289770")]')
    OTHER_BUTTON = (By.XPATH, '//div[contains(@class, "cellIn")]//span[contains(@class, "match-highlight")]')
    CANCEL_BUTTON = (By.XPATH, '/html/body/div[3]/form/div[3]/div/section/div/span/div/span[3]/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/span/div/span[2]/div/span/div/div/div/div[2]/div/div/div[1]/span/div/button')
    CLOSE = (By.XPATH, '//a[contains(@data-click, "doClose")]')
       
