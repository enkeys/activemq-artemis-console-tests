from os import remove
from os.path import dirname, join
from pickle import dump, load

import pytest
from selenium.webdriver import Remote


@pytest.fixture
def selenium(selenium: Remote):
    selenium.implicitly_wait(10)
    return selenium


@pytest.fixture
def get_login(base_url, selenium: Remote, variables):
    """
    Prepare login session
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    from management_console.pages.hawtio_login import HawtioLogin
    login_page = HawtioLogin(base_url, selenium)
    login_page.login(variables['username'], variables['password'])
    # cookies = selenium.get_cookies()
    file = join(dirname(dirname(__file__)), 'cookies.pkl')
    dump(selenium.get_cookies(), open(file, "wb"))


@pytest.fixture
def setup_login(base_url, selenium: Remote):
    selenium.get(base_url)
    selenium.delete_all_cookies()
    file = join(dirname(dirname(__file__)), 'cookies.pkl')
    cookies = load(open(file, "rb"))
    for cookie in cookies:
        selenium.add_cookie(cookie)


@pytest.fixture
def teardown_login():
    file = join(dirname(dirname(__file__)), 'cookies.pkl')
    remove(file)
