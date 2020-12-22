from selenium.webdriver import Remote
from selenium.webdriver.common.by import By

from management_console import Region


class Tree(Region):
    """
    Data model for items in logging console
    """

    _root_locator = ''

    __expand_all_locator = (By.CSS_SELECTOR, "i[ng-click='$ctrl.expandAll()']")
    __collapse_all_locator = (By.CSS_SELECTOR, "i[ng-click='$ctrl.contractAll()']")
    __search = (By.CSS_SELECTOR, "input[ng-model='$ctrl.filter']")

    __status_items = (By.CSS_SELECTOR, "[ng-repeat='item in $ctrl.status.info track by $index']")

    def __init__(self, base_url, selenium: Remote, root=None, **kwargs):
        super().__init__(base_url, selenium, **kwargs)
        self.root_element = root

    @property
    def status_version(self):
        return True

    @property
    def heading(self):
        __artemis_status_heading = (By.CSS_SELECTOR, 'artemis-status h1')
        return self.wait_for_element_displayed(*__artemis_status_heading).text

    @property
    def expand(self):
        return self.wait_for_element_displayed("a[ng-switch-when='next']").click()
