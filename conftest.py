import configparser
import json
import os
import sys
import time
from os.path import abspath
from os.path import dirname as d
from os.path import join
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests.auth import HTTPBasicAuth
import pytest
import requests
from selenium import webdriver
from simple_settings import settings

import gettext

#es = gettext.translation('tests', localedir='locale', languages=['es'])
#es.install()

#fr = gettext.translation('tests', localedir='locale', languages=['fr'])
#fr.install()

#de = gettext.translation('tests', localedir='locale', languages=['de'])
#de.install()

#zh = gettext.translation('tests', localedir='locale', languages=['zh'])
#zh.install()


def pytest_configure(config):
    os.environ['SIMPLE_SETTINGS'] = 'settings_stage'
    os.environ['BROWSER'] = 'chrome'
    return config


def pytest_unconfigure(config):
    os.environ['SIMPLE_SETTINGS'] = 'settings_dev'
    os.environ['BROWSER'] = 'chrome'
    return config

# *****************************************************************************
# Context Array to share variables across session and share between methods
# *****************************************************************************
@pytest.fixture(scope='session')
def context():
    return {}

# ********************************************
# Selenium Web Driver Setup
# ********************************************
@pytest.fixture(autouse=True, scope='session')
def driver():
    "Setup for the test"
    if settings.SELENIUM_DRIVER_IS_REMOTE:
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--whitelisted-ips")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        print(settings.SELENIUM_GRID_HUB_HOST)
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        driver = webdriver.Remote(
            command_executor=settings.SELENIUM_GRID_HUB_HOST,
            desired_capabilities=caps,
            options=chrome_options
        )
    else:
        if settings.BROWSER_TYPE == 'chrome':
            # Chrome Options
            chrome_options = webdriver.ChromeOptions()
            #chrome_options.add_argument("--headless")
            #executable_path1 = '/mnt/c/Users/casferna/cimservicesautomation/venv-wsl1/lib/python3.7/site-packages/chromedriver-win.exe'
            # chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=chrome_options)
            #driver = webdriver.Chrome(options=chrome_options, executable_path=executable_path1)
            #driver = webdriver.Chrome(executable_path=executable_path1)
        elif settings.BROWSER_TYPE == 'firefox':
            driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(settings.DRIVER_TIMEOUT)
    base_url = settings.CSH_UI_URI
    verificationErrors = []
    accept_next_alert = True
    yield driver
    driver.quit()

# ********************************************
# Case Routing API Authentication
# ********************************************
@pytest.fixture(autouse=True, scope='session')
def api_auth(context):
    """I am an authenticated user."""
    client_id = settings.ROUTING_CLIENT_ID
    client_secret = settings.ROUTING_CLIENT_SECRET
    AUTH_URI = settings.AUTH_URI
    AUTH_TYPE = settings.AUTH_TYPE
    ROUTING_USERNAME = settings.ROUTING_USERNAME
    ROUTING_PASSWORD = settings.ROUTING_PASSWORD
    context["access_token"] = None

    if "OAUTH2".__eq__(AUTH_TYPE):
        data = {'grant_type': 'client_credentials'}
        access_token_response = requests.post(
            AUTH_URI, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))
        tokens = json.loads(access_token_response.text)
        context['access_token'] = tokens['access_token']
        print(" Pega access token: {}".format(context['access_token']))
    elif "BASIC".__eq__(AUTH_TYPE):
        pass
    else:
        pytest.fail("Auth not supported!")
