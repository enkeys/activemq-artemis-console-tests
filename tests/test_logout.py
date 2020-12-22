import pytest

from management_console.pages.hawtio_login import HawtioLogin


@pytest.mark.nondestructive
@pytest.mark.webtest
def test_logout(base_url, selenium, variables):
    """
    Users can logout
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = HawtioLogin(base_url, selenium)
    app_page = login_page.login(variables['username'], variables['password'])
    assert app_page.is_the_current_page
    logout = app_page.menu.click_logout()
    assert logout.is_the_current_page
