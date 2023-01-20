# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import time

import pyautogui as pa

from DailyActivities import DailyActivities
from housejobs import HouseJob
from bosses import Boss
from instancezones import InstanceZone
from topprocess import TopProcess

from common import *

from configs import configs

class Languages(object):
    CHS = 'chi_sim'
    ENG = 'eng'

# html node name
ACCOUNT_KEY = "account"
PWD_KEY = "password"
LOGIN_BTN_KEY ="#gowan-ui>div>div.popbox.show.account-login>div>div>div.gowan-btns>div"
# frame
FIRST_FRAME="game-iframe"
SECOND_FRAME="gameFrame"

# Position
BROWSER_POS=(0,0)

BAG_POS=(382, 894)
SMELT_POS=(150, 895)

def get_driver(url="https://baidu.com"):
    driver = webdriver.Chrome()
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

def click_multi(dr,pos,times=1):
    c_times = 0
    while c_times < times:
        #click_pos(BLACK_POS)
        #click_locxy(dr, pos[0]+BROWSER_POS[0],pos[1]+BROWSER_POS[1])
        click_locxy(dr, pos[0], pos[1])
        wait_time(1)
        c_times = c_times + 1

def click_pos(pos):
    pa.moveTo(pos[0]+BROWSER_POS[0],pos[1]+BROWSER_POS[1], duration=0.5)
    pa.click(pos[0]+BROWSER_POS[0],pos[1]+BROWSER_POS[1])

# common methods start
def open_bag(dr):
    clcik_pos_locxy(dr, BAG_POS)

# common methods end

ONEKEY_SMELT_POS = (256,824)
def rong_lian(dr):
    wait_time(2)
    open_bag(dr)
    clcik_pos_locxy(dr, SMELT_POS)
    clcik_pos_locxy(dr, ONEKEY_SMELT_POS)
    wait_time(10)
    click_multi(dr, BLACK_POS, 2)
    callback_click(dr)

def to_main(driver):
    wait_time(3)
    click_multi(driver, BLACK_POS, 4)

def test_eight_components():
    driver = get_driver("https://h5game.gowan8.com/?yisdk_param=mZpuX9Lm2M_S&ext_param=ZJ1raKOp") 
    
    #隐式等待 设置隐士等待的目的是为了找元素的时候动态等待页面加载，参数是最大等待时间，单位为秒
    driver.implicitly_wait(3) 
    login(driver)    
    # waiting loading
    
    # monitor
    driver.save_screenshot('all_test.png')
    #rong_lian(driver)
    #Boss(driver).main_to_single_boss()
    #callback_click(driver)
    #InstanceZone(driver).main_to_everyday_fb()
    TopProcess(driver).get_welfare()
    
    #wait_time()
    #callback_click(driver)
    # DailyActivities(driver).monitor()
    # HouseJob(driver).rechallenge_pets()

    time.sleep(60*60*2)
    driver.quit()

if __name__ == "__main__":
    try:
        test_eight_components()
    except Exception as e:
        print(f'ex:{e}')