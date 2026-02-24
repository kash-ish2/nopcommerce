import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


# Add command line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, edge"
    )


# Setup driver fixture
@pytest.fixture()
def setup(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError("Browser not supported")

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()


# Add metadata to HTML report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = "nopCommerce"
    config.stash[metadata_key]['Module Name'] = "Admin Login"
    config.stash[metadata_key]['Tester'] = "Kashish Tiwari"


# Remove unwanted metadata
@pytest.mark.optionalhooks
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
