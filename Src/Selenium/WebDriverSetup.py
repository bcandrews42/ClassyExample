import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverSetup(unittest.TestCase):

    driver = None
    isHeadless = False

    def setUp(self, isHeadless = False):
        #TODO: get isHeadless from appsettings
        self.isHeadless = isHeadless
        print("Spinning Up Webdriver")
        #Only launch on Chrome for now, can add a switch-case to spin up driver with other browsers
        self.LaunchChromeDriver()

    def tearDown(self):
         if (self.driver != None):
            print("Tearing Down Webdriver")
            self.driver.close()
            self.driver.quit()

    #Other Webdriver functions
    def NavigateTo(self, url):
        self.driver.get(url)

    #Private functions
    def LaunchChromeDriver(self):
        options = Options()
        if(self.isHeadless):
            options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
