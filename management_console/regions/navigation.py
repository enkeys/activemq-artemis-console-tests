from selenium.webdriver.common.by import By

from management_console import Region


class Navigation(Region):
    """
    Navigation where is viewed activated plugins
    """
    # Menu
    _root_locator = ''
    __artemis_locator = (By.CSS_SELECTOR, 'a:contains("Artemis")')
    __connect_locator = (By.LINK_TEXT, 'Connect')
    __dashboard_locator = (By.LINK_TEXT, 'Dashboard')
    __jmx_locator = (By.LINK_TEXT, 'JMX')

    def click_artemis(self):
        self.is_element_visible(*self.__artemis_locator).click()

    def click_connect(self):
        self.is_element_visible(*self.__connect_locator).click()

    def click_dashboard(self):
        self.is_element_visible(*self.__dashboard_locator).click()

    def click_jmx(self):
        self.is_element_visible(*self.__jmx_locator).click()
