from sqlalchemy import false
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from Src.Selenium.Objects.SeleniumTestElement import SeleniumTestElement
import time

class ElementInteractionLibrary:

    browser = None
    default_timeout = 30

    def __init__(self, driver):
        self.browser = driver

    #Functions that will return a selenium element object
    def GetElementByXPath(self, xpath):
        element = self.browser.find_element_by_xpath(xpath)
        return SeleniumTestElement(element, xpath = xpath)

    def GetElementByID(self, id):
        element = self.browser.find_element_by_id(id)
        return SeleniumTestElement(element, id = id)

    def GetElementByName(self, name):
        element = self.browser.find_element_by_name(name)
        return SeleniumTestElement(element, name = name)

    def GetElementByHyperlink(self, hyperlink):
        element = self.browser.find_element_by_link_text(hyperlink)
        return SeleniumTestElement(element, hyperlink = hyperlink)

    def GetElementByTag(self, tag):
        element = self.browser.find_element_by_tag_name(tag)
        return SeleniumTestElement(element, tag = tag)

    def GetElementByClass(self, classname):
        element = self.browser.find_element_by_class_name(classname)
        return SeleniumTestElement(element, classname = classname)

    def GetElementByCSSSelector(self, cssSelector):
        element = self.browser.find_element_by_css_selector(cssSelector)
        return SeleniumTestElement(element, cssSelector = cssSelector)

    # Element Validation Functions

    def ElementExists(self, testElement):
        try:
            self.browser.find_element()
            return True
        except NoSuchElementException:
            return false

    # Waits

    def ExplicitWaitUntilElementExists(self, element):
        wait = WebDriverWait(self.browser, self.default_timeout)
        wait.until(EC.presence_of_element_located((element.by, element.GetLocator())))

    def ExplicitWaitUntilElementDisplay(self, element):
        wait = WebDriverWait(self.browser, self.default_timeout)
        wait.until(EC.visibility_of_element_located((element.by, element.GetLocator())))

    def ExplicitWaitUntilElementClickable(self, element):
        wait = WebDriverWait(self.browser, self.default_timeout)
        wait.until(EC.element_to_be_clickable((element.by, element.GetLocator())))

    def ImplicitWait(self, waitTime):
        time.sleep(waitTime)

    #Element Actions

    def Click(self, testElement):
        testElement.element.click()

    def EnterText(self, testElement, text):
        testElement.element.send_keys(text)

    def HitEnterKeyOnElement(self, testElement):
        testElement.element.send_keys(Keys.RETURN)

    def SwitchToIFrame(self, testElement):
        self.browser.switch_to.frame(testElement.element)

    def SwitchOutOfIFrame(self):
        self.browser.switch_to.default_content()

    #Debugging Functions

    def GetHTML(self):
        return self.browser.page_source
    
    def PrintElementAttributes(self, testElement):
        print(self.browser.execute_script("""var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) 
                                            { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value 
                                            }; return items;""", testElement.element))

    # Reporting Functions

    def SaveScreenshot(self, screenshotName):
        self.browser.save_screenshot(screenshotName)
