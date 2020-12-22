from selenium.webdriver.common.by import By

from management_console import Region


class Header(Region):
    # Menu
    __menu_locator = (By.CSS_SELECTOR, 'i.icon-user.fixme')  # @todo open issue for ID

    # Menu items
    __preferences_locator = (By.CSS_SELECTOR, 'i.icon-cogs.fixme')
    __logout_locator = (By.CSS_SELECTOR, 'i.icon-signout.fixme')
    __about_locator = (By.CSS_SELECTOR, 'i.icon-info')
    __menu_locator1 = (By.XPATH, "//div[@id='main-nav']/div/div/div[2]/ul/li[4]/a/span")
    __logout_locator1 = (By.XPATH, "//div[@id='main-nav']/div/div/div[2]/ul/li[4]/ul/li[2]/a")
    __yes_locator = (By.XPATH, "//input[@value='Yes']")
    __yes_locator1 = (By.CSS_SELECTOR, "input.btn.btn-success")
    __menu_locator2 = (By.LINK_TEXT, "Log out")

    def click_menu(self):
        self.selenium.find_element(*self.__menu_locator1)

    def click_logout(self):
        self.click_menu()
        self.selenium.find_element(*self.__logout_locator1).click()
        self.selenium.find_element(*self.__yes_locator).click()
        from pages.login import LoginPage
        return LoginPage(self.base_url, self.selenium, open_url=False)

    def click_preferences(self):
        self.click_menu()
        self.is_element_visible(*Base.Menu.__preferences_locator).click()

    def click_about(self):
        self.click_menu()
        self.is_element_visible(*Base.Menu.__about_locator).click()
