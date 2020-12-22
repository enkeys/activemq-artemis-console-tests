import pytest

from management_console.pages.hawtio_login import HawtioLogin
from management_console.plugins.artemis import ArtemisPlugin


@pytest.mark.nondestructive
@pytest.mark.webtest
def test_login_valid(base_url, selenium, variables):
    """
    Users can log in
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = HawtioLogin(base_url, selenium)
    hawtio_app = login_page.login(variables['username'], variables['password'])

    # Expected ArtemisPlugin
    assert ArtemisPlugin(base_url, selenium).is_the_current_page

    assert hawtio_app.is_the_current_page
    assert "Current Status" in hawtio_app.heading


@pytest.mark.nondestructive
@pytest.mark.webtest
def test_login_invalid_password(base_url, selenium, variables):
    """
    Users cannot login with wrong password
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = HawtioLogin(base_url, selenium)
    hawtio_app = login_page.login(variables['username'], variables['password'] + 'x')

    # Expected ArtemisPlugin
    assert not ArtemisPlugin(base_url, selenium).is_the_current_page

    assert not hawtio_app.is_the_current_page
    assert login_page.is_forbidden
    assert login_page.is_the_current_page


@pytest.mark.nondestructive
@pytest.mark.webtest
def test_login_invalid_username(base_url, selenium, variables):
    """
    Attempt to log in with an invalid username
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = HawtioLogin(base_url, selenium)
    hawtio_app = login_page.login(variables['username'] + 'x', variables['password'])

    # Expected ArtemisPlugin
    assert not ArtemisPlugin(base_url, selenium).is_the_current_page

    assert not hawtio_app.is_the_current_page
    assert login_page.is_forbidden
    assert login_page.is_the_current_page


@pytest.mark.nondestructive
@pytest.mark.webtest
def test_login_invalid_password_username(base_url, selenium, variables):
    """
    Users cannot login with wrong password
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = HawtioLogin(base_url, selenium)
    hawtio_app = login_page.login(variables['username'] + 'x', variables['password'] + 'x')

    # Expected ArtemisPlugin
    assert not ArtemisPlugin(base_url, selenium).is_the_current_page

    assert not hawtio_app.is_the_current_page
    assert login_page.is_forbidden
    assert login_page.is_the_current_page
