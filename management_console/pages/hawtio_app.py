from selenium.webdriver import Remote

from management_console.pages.hawtio_base import HawtioBase
from management_console.plugins.artemis import ArtemisPlugin
from management_console.regions.header import Header
from management_console.regions.navigation import Navigation


class HawtioApp(HawtioBase):
    def __init__(self, base_url, selenium: Remote, open_url=True, **kwargs):
        super().__init__(base_url, selenium, open_url=open_url, **kwargs)
        self.header = Header(base_url, selenium, **kwargs)
        self.nav = Navigation(base_url, selenium, **kwargs)
        self.plugin = HawtioAppPlugins(base_url, selenium, open_url=True)


class HawtioAppPlugins:
    def __init__(self, base_url, selenium: Remote, **kwargs):
        self.selenium = selenium
        self.base_url = base_url
        pass

    @property
    def artemis(self):
        return ArtemisPlugin(self.base_url, self.selenium)
