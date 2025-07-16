import pytest
from pages.login_page import LoginPage
from utils.config_reader import read_config
from utils.logger import get_logger

log = get_logger()
config = read_config()

@pytest.mark.login
def test_login(driver):
    login = LoginPage(driver)
    login.load(config['base_url'])
    login.login(config['username'], config['password'])

    assert "inventory" in driver.current_url
    log.info("Login test passed")
