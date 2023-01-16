from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
import time

import pyautogui as pa

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
# frame gameFrame
CHECK_TERM ="#serverCon>img:nth-child(7)"
START_BTN = "#serverCon>img:nth-child(3)"
# user info 
LOGIN_NAME="fhl1993"
LOGIN_PWD = "fhl19930321"

# Position
BROWSER_POS=(0,0)
BLACK_POS = (324, 184)

BAG_POS=(382, 894)
SMELT_POS=(150, 895)

def wait_time(secs=10):
    time.sleep(secs)

def get_driver(url="https://baidu.com"):
    driver = webdriver.Chrome()
    driver.set_window_size(500,950)
    driver.set_window_position(BROWSER_POS[0], BROWSER_POS[1])
    driver.get(url)
    return driver

def login(driver):
    wait_time(2)
    acct_text = driver.find_element(by=By.NAME, value=ACCOUNT_KEY)
    acct_text.send_keys(LOGIN_NAME)
    wait_time(1)
    pwd_text = driver.find_element(by=By.NAME, value=PWD_KEY)
    pwd_text.send_keys(LOGIN_PWD)

    wait_time(1)
    driver.implicitly_wait(1)
    login_btn = driver.find_element(by=By.CSS_SELECTOR, value=LOGIN_BTN_KEY)
    login_btn.click()

    wait_time(2)
    driver.implicitly_wait(2)
    # click black
    click_locxy(driver, 100, 30 + BLACK_X)

def select_server(driver):
    # check term    
    wait_time(2)    
    chk_term = driver.find_element(by=By.CSS_SELECTOR, value=CHECK_TERM)
    chk_term.click()

    wait_time(2)
    start_btn = driver.find_element(by=By.CSS_SELECTOR, value=START_BTN)
    start_btn.click()
    
def switch_frame(driver):
    driver.switch_to.frame(FIRST_FRAME)
    driver.switch_to.frame(SECOND_FRAME)

# BLACK_POS = (324, 184)
BLACK_X = 124
def click_locxy(dr, x, y, left_click=True):
    wait_time(1)
    y = y - BLACK_X
    print(f'click_locxy,x:{x},y:{y}')
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前

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

def clcik_pos_locxy(dr, pos, isleft=True):
    click_locxy(dr, pos[0], pos[1], isleft)

# common methods start
def open_bag(dr):
    clcik_pos_locxy(dr, BAG_POS)

BAG_USE = (1819, 834)    
def get_goods(driver):
    wait_time(3)
    clcik_pos_locxy(driver, BAG_USE)
    wait_time(3)

def click_black(dr, times=2):
    c_time = 0 
    while c_time < times:
        clcik_pos_locxy(dr, BLACK_POS)
        c_time = c_time + 1
        wait_time(1)
# common methods end

ONEKEY_SMELT_POS = (256,824)
def rong_lian(dr):
    wait_time(2)
    open_bag(dr)
    clcik_pos_locxy(dr, SMELT_POS)
    clcik_pos_locxy(dr, ONEKEY_SMELT_POS)

def to_main(driver):
    wait_time(3)
    click_multi(driver, BLACK_POS, 4)

# process hd start
HD_POS = (1669,674)  
HD_POS_START = (376, 282)
XF_GOODS_POS =(1710,801)
HD_CLOSE = (468, 199)

def start_hd(driver):
    clcik_pos_locxy(driver, HD_POS)
    wait_time(2)
    clcik_pos_locxy(driver, HD_POS_START)
    wait_time(3)

def close_hd(dr):
    clcik_pos_locxy(dr,HD_CLOSE)
    wait_time(1)

def hd_monitor(driver):
    while True:
        hd_process(driver)

def hd_process(driver):
    d_now = datetime.now()
    d_wkday = d_now.weekday()
    try:
        god_treasure(driver)
        bath(driver)
        if d_wkday != 6:
            tianti(driver)
    except Exception as e:
        print(f'exception:{e}')
    wait_time()

# down 
def god_treasure(dr):
    if is_between((11,30),(11,37)) or is_between((18,30),(18,37)):
        print("god_treasure start")
        start_hd(dr)
        clcik_pos_locxy(dr, XF_GOODS_POS)
        wait_time(480)
        print(f"god_treasure end.{datetime.now()}")
        close_hd(dr)
        get_goods(dr)

# bath
def bath(dr):
    if is_between((19,1), (19,16)):
        print("bath start")
        start_hd(dr)
        wait_time(17*60)
        close_hd(dr)
        print("bath end")
        get_goods(dr)

TT_MATCH = (1771,692)
def tianti(dr):    
    if is_between((19,30),(19,43)):
        print("tian ti start")
        start_hd(dr)
        wait_time(4)
        click_position(TT_MATCH)
        wait_time(13 * 60)
        close_hd(dr)
        print("tian ti end")
# process hd end

def test_eight_components():
    driver = get_driver("https://h5game.gowan8.com/?yisdk_param=mZpuX9Lm2M_S&ext_param=ZJ1raKOp") 
    
    #隐式等待 设置隐士等待的目的是为了找元素的时候动态等待页面加载，参数是最大等待时间，单位为秒
    driver.implicitly_wait(3) 
    login(driver)
    switch_frame(driver)
    select_server(driver)
    # waiting loading
    wait_time(20)
    to_main(driver)  

    rong_lian(driver)

    time.sleep(1800)
    driver.quit()

if __name__ == "__main__":
    try:
        test_eight_components()
    except Exception as e:
        print(f'ex:{e}')