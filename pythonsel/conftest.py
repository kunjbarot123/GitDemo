import datetime
import os

import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser selection"
    )


@pytest.fixture(scope="function")
def browserInvokation(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,  # disables Chrome password service
        "profile.password_manager_enabled": False,  # disables password manager popup
        "profile.password_manager_leak_detection": False,  # disables leak detection popup
    })
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(5)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)
        driver.implicitly_wait(5)


    yield driver
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)