from selenium.webdriver import Remote

from management_console.region import Region


class Plugin(Region):
    name = None

    def __init__(self, base_url, selenium: Remote, root=None, open_url=False, **kwargs):
        super().__init__(base_url, selenium, open_url=open_url, **kwargs)
