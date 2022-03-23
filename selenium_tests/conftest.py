# -*- coding: utf-8 -*-

import os.path
import pathlib
from typing import Final
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


IMPLICITLY_WAIT: Final[int] = 30
CHROMDERIVER_PATH: Final[str] = os.path.join(pathlib.Path(__file__).parent.absolute(), "chromedriver")


def pytest_addoption(parser):
    """
    If we use the '--remote' flag, tests will try to be run against a Docker container on port 4444
    :param parser:
    :return:
    """
    parser.addoption(
        "--remote", action="store_true", default=False,
        help="Set this flag if the driver you are using is not on the local system"
    )
    parser.addoption(
        "--rmt-host", action="store", default="localhost", type=str,
        help="Set the host name or the host IP of the system who contains the web driver. By default 'localhost'"
    )
    parser.addoption(
        "--rmt-port", action="store", default=4444, type=int,
        help="Set the port where the host who has the driver is listening. By default '4444'"
    )


def get_driver(request) -> WebDriver:
    """
    Generate the Selenium driver that will be used by the tests
    :param request:
    :return: a callable that generates the driverSelenium WebDriver instance
    """
    driver: WebDriver
    if request.config.getoption("--remote"):
        driver = webdriver.Remote(
            "http://{host}:{port}/wd/hub".format(
                host=request.config.getoption("--rmt-host"), port=request.config.getoption("--rmt-port")
            ), DesiredCapabilities.CHROME
        )
    else:
        driver = webdriver.CHROME(executable_path=CHROMDERIVER_PATH)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    driver.set_window_size(width=1400, height=1024)
    yield driver
    driver.close()
