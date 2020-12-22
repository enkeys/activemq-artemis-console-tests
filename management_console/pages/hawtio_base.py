from selenium.webdriver import Remote
from selenium.webdriver.common.by import By

from management_console.page import Page


class HawtioBase(Page):
    def __init__(self, base_url, selenium: Remote, open_url=True, **kwargs):
        super().__init__(base_url, selenium, open_url=open_url, **kwargs)

    @property
    def logged(self):
        """
        Check login state
        @return: bool
        """
        __login_button_locator = (By.CSS_SELECTOR, 'button.btn.btn-success')
        return False if self.is_element_present(__login_button_locator) else True

    @property
    def notification(self):
        """
        Wait for notification and get back text
        @todo Implement model for notifications regions/notifications.py
        @return:
        """
        __message_text_locator = (By.CLASS_NAME, 'toast-message')
        return self.wait_for_element_displayed(*__message_text_locator).text
