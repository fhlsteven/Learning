# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.action_chains import ActionChains
import aircv as ac
import pytesseract as ocr_act
from PIL import Image
from configs import configs

BLACK_POS = (324, 184)
ALL_IMAGE = 'mh_all.png'

def wait_time(secs=10):
    time.sleep(secs)

# BLACK_POS = (324, 184)
BLACK_X = 124
def click_locxy(dr, x, y, left_click=True):
    wait_time(1)
    y = y - BLACK_X
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前

def click_pos_locxy(dr, pos, isleft=True):
    click_locxy(dr, pos[0], pos[1], isleft)

def click_black(dr, times=2):
    c_time = 0 
    while c_time < times:
        click_pos_locxy(dr, BLACK_POS)
        c_time = c_time + 1
        wait_time(1)

QUIT_CLICK = (42, 765)
QUIT_OK =(331, 605)
def quit_scene(dr):
    if is_exists_image(dr, 'quit_left.png'):
        click_pos_locxy(dr, QUIT_CLICK)
    click_pos_locxy(dr, QUIT_OK)

BAG_USE = (375, 781)    
def get_goods(dr):
    while is_exists_image(dr, 'use_btn.png'):
        wait_time(2)
        click_pos_locxy(dr, BAG_USE)

CALLBACK_POS=(450, 916)
def callback_click(dr):
    while is_exists_image(dr, "callback.png"):
        click_pos_locxy(dr, CALLBACK_POS)

IMG_PREFIX = 'imgs/'
def match_img(imgsrc, imgobj, confidencevalue=0.9):  # imgsrc=原始图像，imgobj=待查找的图片   
    img_src =  IMG_PREFIX+imgsrc
    img_obj = IMG_PREFIX+imgobj
    try:
        imsrc = ac.imread(img_src)
        imobj = ac.imread(img_obj)
        match_result = ac.find_all_template(imsrc, imobj, confidencevalue)
        if configs.runtime == 'debug':
            print(f'img_src:{img_src},img_obj:{img_obj}.match_result:{match_result},confdend:{confidencevalue}')  
        #[{'result': (61.0, 135.5), 'rectangle': ((36, 110), (36, 161), (86, 110), (86, 161)), 'confidence': 1.0}]
        return match_result
    except Exception as ex:
        print(ex)
    return None

'''
根据图像匹配坐标，获取第一个
'''
def match_img_pos(driver, imgobj, confidencevalue=0.9):
    save_all_img(driver)
    xyt = match_img(ALL_IMAGE, imgobj, confidencevalue)    
    if xyt != None and len(xyt) > 0:
        x = xyt[0]['result'][0]
        y = xyt[0]['result'][1]
        return (int(x), int(y) + BLACK_X) # 因为后面点击的方法会减去这个值，所以这里的加一下
    return (0,0)

def match_img_pos_all(driver, img_obj, confidence=0.9):
    save_all_img(driver)
    res = []
    xyt = match_img(ALL_IMAGE, img_obj, confidence)
    for re in xyt:
        xy = (int(re['result'][0]), int(re['result'][1]) + BLACK_X) # 同上
        res.append(xy)
    return res

def is_exists_image(driver, imgobj, confidencevalue=0.8):
    save_all_img(driver)
    result = match_img(ALL_IMAGE, imgobj, confidencevalue)
    if result != None and len(result)>0:
        return True
    return False

# 476 526+124
CLOSE_KILL_GO = (476, 650)
def clear_kill_go(driver):
    while is_exists_image(driver, "kill_go.png", confidencevalue=0.7):
        click_pos_locxy(driver, pos)

def save_all_img(driver):
    driver.save_screenshot(IMG_PREFIX+ALL_IMAGE)
    wait_time(2)

BAG_POS=(382, 894)
SMELT_POS=(150, 895)

def open_bag(dr):    
    click_pos_locxy(dr, BAG_POS)

ONEKEY_SMELT_POS = (256,824)
def rong_lian(dr):
    wait_time(1)
    if is_exists_image(dr, "bag.png"):
        open_bag(dr)
        click_pos_locxy(dr, SMELT_POS)
        click_pos_locxy(dr, ONEKEY_SMELT_POS)
        while is_exists_image(dr, "smelt_ok.png") == False:
            wait_time(5)
        click_multi(dr, BLACK_POS, 2)
        wait_time(2)
        callback_click(dr)

def click_multi(dr,pos,times=1):
    c_times = 0
    while c_times < times:
        click_locxy(dr, pos[0], pos[1])
        wait_time(1)
        c_times = c_times + 1

class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def click_pos(self, pos):
        click_pos_locxy(self.driver, pos)

    def get_pos_byimg(self, img_name, defalut_pos=(0,0), confidence=0.9):
        pos = match_img_pos(self.driver, img_name, confidencevalue=confidence)
        if pos[0] != 0 and pos[1] != 0:
            return pos            
        return defalut_pos

    def use_bags(self):
        clear_kill_go(self.driver)
        get_goods(self.driver)

    def is_callback(self):
        return is_exists_image(self.driver, 'callback.png')

    def is_quit(self):
        return is_exists_image(self.driver, 'quit_left.png')
    
    def rong_lian(self):
        rong_lian(self.driver)

    def click_quit(self):
        quit_scene(self.driver)

    def is_exists_image(self, img_name, confidence = 0.8):
        return is_exists_image(self.driver, img_name, confidence)
    
    def click_callback(self):
        callback_click(self.driver)

    def is_exit_loop(self):
        return is_exists_image(self.driver, "chat_box.png") == False


class Languages(object):
    CHS = 'chi_sim'
    ENG = 'eng'

def get_ocr_txt(image, lang=Languages.CHS):
    result = ''
    content = ocr_act.image_to_string(image, lang)
    for x in content:
        result += x.strip(' ')
    return result

class BaseOCR(object):
    def __init__(self, driver):
        self.driver = driver

    def recognize(self, img):
        img = img.convert('L')
        img.save(IMG_PREFIX+'chat_detail.png')
        return get_ocr_txt(img)

    def is_exists_image(self, img_name, confidence = 0.8):
        return is_exists_image(self.driver, img_name, confidence)

    def crop_by_region(self, imgsrc, region):
        try:            
            all_img = Image.open(imgsrc)
            return all_img.crop((region[0], region[1], region[0]+region[2], region[1]+region[3]))            
        except Exception as e:
            print(e)
            return None