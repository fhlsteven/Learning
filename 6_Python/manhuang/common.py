# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.action_chains import ActionChains
import aircv as ac

BLACK_POS = (324, 184)
ALL_IMAGE = 'mh-all.png'

def wait_time(secs=10):
    time.sleep(secs)

# BLACK_POS = (324, 184)
BLACK_X = 124
def click_locxy(dr, x, y, left_click=True):
    wait_time(1)
    y = y - BLACK_X
    #print(f'click_locxy,x:{x},y:{y}')
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前

def clcik_pos_locxy(dr, pos, isleft=True):
    click_locxy(dr, pos[0], pos[1], isleft)

def click_black(dr, times=2):
    c_time = 0 
    while c_time < times:
        clcik_pos_locxy(dr, BLACK_POS)
        c_time = c_time + 1
        wait_time(1)

QUIT_CLICK = (42, 765)
QUIT_OK =(331, 605)
def quit_scene(dr):
    wait_time(3)
    clcik_pos_locxy(dr, QUIT_CLICK)
    wait_time(2)
    clcik_pos_locxy(dr, QUIT_OK)

BAG_USE = (375, 781)    
def get_goods(dr):
    while is_exists_image(dr, 'use_btn.png'):
        wait_time(3)
        clcik_pos_locxy(dr, BAG_USE)
        wait_time(1)

CALLBACK_POS=(451, 916)
def callback_click(dr):
    clcik_pos_locxy(dr, CALLBACK_POS)

IMG_PREFIX = 'imgs/'
def match_img(imgsrc, imgobj, confidencevalue=0.9):  # imgsrc=原始图像，imgobj=待查找的图片    
    imsrc = ac.imread(IMG_PREFIX+imgsrc)
    imobj = ac.imread(IMG_PREFIX+imgobj)
    match_result = ac.find_all_template(imsrc, imobj, confidencevalue)  
    #[{'result': (61.0, 135.5), 'rectangle': ((36, 110), (36, 161), (86, 110), (86, 161)), 'confidence': 1.0}]
    return match_result

def match_img_pos(driver, imgobj, confidencevalue=0.9):
    driver.save_screenshot(IMG_PREFIX+ALL_IMAGE)
    xyt = match_img(ALL_IMAGE, imgobj, confidencevalue)[0]
    if xyt != None:
        x = xyt['result'][0]
        y = xyt['result'][1]
        return (int(x), int(y))
    return (0,0)

def is_exists_image(driver, imgobj, confidencevalue=0.9):
    driver.save_screenshot(IMG_PREFIX+ALL_IMAGE)
    result = match_img(ALL_IMAGE, imgobj, confidencevalue)
    if result != None and len(result)>0:
        return True
    return False

