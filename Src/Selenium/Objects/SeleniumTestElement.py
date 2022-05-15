import re
from xml.etree.ElementPath import xpath_tokenizer
from selenium.webdriver.common.by import By

#This class used to track different locators to be used in Expected Condtion Test Validation
class SeleniumTestElement():

    # WebElementObject
    element = None
    # Locator Variables
    xpath = None
    id = None
    hyperlink = None
    tag = None
    _class = None
    cssSelector = None
    by = None

    def __init__(self, element, xpath = None, id = None, hyperlink = None, tag = None,
                    _class = None, cssSelector = None):
        #Set WebElement Object
        self.element = element

        #Set locator variable with By method
        if xpath is not None:
            self.xpath = xpath
            self.by = By.XPATH
        if id is not None:
            self.id = id
            self.by = By.ID
        if hyperlink is not None:
            self.hyperlink = hyperlink
            self.by = By.LINK_TEXT
        if tag is not None:
            self.tag = tag
            self.by = By.TAG_NAME
        if _class is not None:
            self._class = _class
            self.by = By.CLASS_NAME
        if cssSelector is not None:
            self.cssSelector = cssSelector
            self.by = By.CSS_SELECTOR

        #If no locator is specified raise an exception
        if xpath is None and id is None and hyperlink is None and tag is None and _class is None and  cssSelector is None:
            raise Exception("No Locator Specified when initializaing SeleniumTestElement object")

    # Returns the locator to be used in Expected Condition validation
    def GetLocator(self):
        # Note: written in python 3.7 no switch-case statement currently
        if self.by is By.XPATH:
            return self.xpath
        elif self.by is By.ID:
            return self.id
        elif self.by is By.LINK_TEXT:
            return self.hyperlink
        elif self.by is By.TAG_NAME:
            return self.tag
        elif self.by is By.CLASS_NAME:
            return self._class
        elif self.by is By.CSS_SELECTOR:
            return self.cssSelector
        else:
            return None
                






