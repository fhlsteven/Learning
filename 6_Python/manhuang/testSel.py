# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

from DailyActivities import DailyActivities
from housejobs import HouseJob
from bosses import Boss
from instancezones import InstanceZone
from topprocess import TopProcess
from teams import Teams
from common import *

from configs import configs
from monitor import Monitors
# html node name
ACCOUNT_KEY = "account"
PWD_KEY = "password"
LOGIN_BTN_KEY ="#gowan-ui>div>div.popbox.show.account-login>div>div>div.gowan-btns>div"
# frame
FIRST_FRAME="game-iframe"
SECOND_FRAME="gameFrame"

# Position
BROWSER_POS=(0,0)

# 放到根目录（MicrosoftWebDriver.exe）
# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
def get_driver(url="https://baidu.com"):
    if configs.browser_type == "chrome":
        c_op = webdriver.ChromeOptions()
        c_op.add_argument("--mute-audio")
        driver = webdriver.Chrome(chrome_options=c_op)
    else:
        e_op = webdriver.EdgeOptions()
        e_op.add_argument("--mute-audio")
        e_op.add_argument("--disable-features=msHubApps")
        driver = webdriver.Edge(options=e_op)

    driver.set_window_size(500,950)
    driver.set_window_position(BROWSER_POS[0], BROWSER_POS[1])
    driver.get(url)
    return driver

def login(driver):
    wait_time(2)
    acct_text = driver.find_element(by=By.NAME, value=ACCOUNT_KEY)
    acct_text.send_keys(configs.login.user_name)
    wait_time(1)
    pwd_text = driver.find_element(by=By.NAME, value=PWD_KEY)
    pwd_text.send_keys(configs.login.pwd)

    wait_time(1)
    driver.implicitly_wait(1)
    login_btn = driver.find_element(by=By.CSS_SELECTOR, value=LOGIN_BTN_KEY)
    login_btn.click()

    wait_time(2)
    driver.implicitly_wait(2)
    # click black
    click_locxy(driver, 100, 30 + BLACK_X)
   
    switch_frame(driver)
    select_server(driver)
    wait_time(20) # wait loading
    to_main(driver)  # clcik black

def select_server(driver):
    # check term    
    wait_time(2)  
    chk_term = driver.find_element(by=By.CSS_SELECTOR, value=configs.check_term)
    chk_term.click()

    wait_time(2)
    start_btn = driver.find_element(by=By.CSS_SELECTOR, value=configs.start_button)
    start_btn.click()
    
def switch_frame(driver):
    driver.switch_to.frame(FIRST_FRAME)
    driver.switch_to.frame(SECOND_FRAME)

def to_main(driver):
    wait_time(3)
    click_multi(driver, BLACK_POS, 4)

def test_eight_components():
    driver = get_driver(configs.login.url) 
    
    #隐式等待 设置隐士等待的目的是为了找元素的时候动态等待页面加载，参数是最大等待时间，单位为秒
    driver.implicitly_wait(3) 
    login(driver)    
    # waiting loading

    #Teams(driver).auto_receive()
    # monitor
    get_goods(driver)
    #Boss(driver).main_to_three_realms()

    #InstanceZone(driver).main_to_everyday_fb()
    #TopProcess(driver).get_welfare()
    
    #wait_time()
    #callback_click(driver)
    #DailyActivities(driver).monitor()
    Monitors(driver).quick_mode()
    # HouseJob(driver).rechallenge_pets()
    driver.quit()

def main_loop():
    driver = get_driver(configs.login.url) 
    
    #隐式等待 设置隐士等待的目的是为了找元素的时候动态等待页面加载，参数是最大等待时间，单位为秒
    driver.implicitly_wait(3) 
    login(driver)    
    # waiting loading
    get_goods(driver)
    rong_lian(driver)

    while True:
        times=0
        pre_time = datetime(2015, 4, 7, 4, 30, 3, 628556) 
        while True:   
            if times < 10 and get_date_minutes(pre_time, datetime.now()) > 11:     
                pre_time = datetime.now()
                HouseJob(driver).house_to_pettravel()
                times = times +1            
            wait_time(10)
            self.click_pos(CHALLENGE_POS)
            wait_time(100)

if __name__ == "__main__":
    try:
        test_eight_components()
    except Exception as e:
        print(f'ex:{e}')