from selenium.webdriver.common.by import By

from management_console.plugin import Plugin
from management_console.plugins.artemis.artemis_tree import ArtemisTree


class ArtemisPlugin(Plugin):
    __root_locator = (By.CSS_SELECTOR, "artemis[class='ng-scope ng-isolate-scope']")
    _url = '{base_url}/artemis/artemisStatus'

    def __init__(self, base_url, selenium, open_url=False):
        super().__init__(base_url, selenium, open_url=open_url)
        self.tree = ArtemisTree(base_url, selenium)
        self.content = None
