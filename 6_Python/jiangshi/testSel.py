# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from common import *
from configs import configs
from datetime import datetime
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os
import platform

# html node name
ACCOUNT_KEY = "account"
PWD_KEY = "password"
LOGIN_BTN_KEY ="#gowan-ui>div>div.popbox.show.account-login>div>div>div.gowan-btns>div"
# frame
FIRST_FRAME="game-iframe"
SECOND_FRAME="gameFrame"

# Position
BROWSER_POS=(configs.browser_pos.x, configs.browser_pos.y)

# 放到根目录（MicrosoftWebDriver.exe）
# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
def get_driver(url="https://baidu.com"):
    if configs.browser_type == "chrome":
        c_op = webdriver.ChromeOptions()
        c_op.add_argument("--mute-audio")
        driver = webdriver.Chrome(options=c_op)
    elif configs.browser_type == "edge":
        e_op = webdriver.EdgeOptions()
        e_op.add_argument("--mute-audio")
        e_op.add_argument("--disable-features=msHubApps")
        e_op.add_argument("--remote-allow-origins=*")
        driver = webdriver.Edge(options=e_op)
    else:
        f_binary = FirefoxBinary("C:\Program Files\Mozilla Firefox\\firefox.exe")
        f_op = webdriver.FirefoxOptions()
        f_op.add_argument("--mute-audio")
        driver = webdriver.Firefox(firefox_binary=f_binary,options=f_op)

    driver.set_window_size(1140,1202) # witdth 1140, height 1202
    driver.set_window_position(BROWSER_POS[0], BROWSER_POS[1])
    driver.get(url)
    return driver
