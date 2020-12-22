from selenium.webdriver import Remote
from selenium.webdriver.common.by import By

from management_console.regions.tree import Tree


class ArtemisTree(Tree):
    """
    Data model for items in logging console
    """

    _root_locator = (By.CSS_SELECTOR, "artemis[class='ng-scope ng-isolate-scope']")

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
