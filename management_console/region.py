from selenium.webdriver import Remote

from management_console import Page


class Region(Page):
    _root_locator = None

    def __init__(self, base_url, selenium: Remote, open_url=False, root=None, **kwargs):
        super().__init__(base_url, selenium, open_url=open_url, **kwargs)
        self.root_element = root

    @property
    def root(self):
        if self.root_element is None and self._root_locator is not None:
            self.root_element = self.selenium.find_element(*self._root_locator)
        return self.root_element
