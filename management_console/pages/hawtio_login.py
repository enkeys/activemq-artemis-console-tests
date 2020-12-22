from selenium.webdriver.common.by import By

from management_console.pages.hawtio_app import HawtioApp
from management_console.pages.hawtio_base import HawtioBase


class HawtioLogin(HawtioBase):
    """HawtIO login page"""
    _url = '{base_url}/auth/login'

    __username_locator = (
        By.XPATH,
        "//input[@name='username']"
    )
    __password_locator = (
        By.XPATH,
        "//input[@name='password']"
    )

    __login_button_locator = (By.XPATH, "//button[@type='submit']")

    __forbidden_msg = 'Failed to log in, Forbidden'

    def __init__(self, base_url, selenium, open_url=True):
        """Creates a new instance of the class and gets the page ready for testing."""
        HawtioBase.__init__(self, base_url, selenium, open_url)

    def __click_login(self):
        self.wait_for_element_displayed(*self.__login_button_locator).click()

    def __type_username(self, username):
        self.wait_for_element_displayed(*self.__username_locator).send_keys(username)

    def __type_password(self, password):
        self.wait_for_element_displayed(*self.__password_locator).send_keys(password)

    def login(self, username, password, remember=False):
        """
        Login to console with username and password
        @param username: Used username for login
        @param password: Used password for login
        @param remember: Check remember
        @return:
        """
        self.__type_username(username)
        self.__type_password(password)
        self.__click_login()

        hawtio_app = HawtioApp(self.base_url, self.selenium)
        artemis_plugin = hawtio_app.plugin.artemis

        if artemis_plugin.is_the_current_page:
            return artemis_plugin

        else:
            return self

    @property
    def is_forbidden(self):
        """
        Check if login was forbidden
        @return: Boolean
        """
        return True if self.__forbidden_msg in self.notification else False
