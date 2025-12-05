# -*- coding: utf-8 -*-
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
import aircv as ac
import pytesseract as ocr_act
from PIL import Image
from configs import configs
from datetime import datetime
import cv2
import numpy as np

BLACK_POS = (324, 184)
ALL_IMAGE = 'mh_all.png'

def wait_time(secs=10):
    time.sleep(secs)

# BLACK_POS = (324, 184)
BLACK_X = 124
def click_locxy(dr, x, y, left_click=True, waits=0):
    y = y - BLACK_X
    if configs.runtime == 'debug':
        print(f'click_locxy:{x},{y}')
    if waits>0:
        wait_time(waits)    
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    print("clicked at:", x, y)
    ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前
    print("move back to:", -x, -y)

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
def match_img_pos(driver, imgobj, confidencevalue=0.9, is_save=True):
    if is_save:
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

def is_exists_image(driver, imgobj, confidencevalue=0.8, is_save=True):
    if is_save:
        save_all_img(driver)
    result = match_img(ALL_IMAGE, imgobj, confidencevalue)
    if result != None and len(result)>0:
        return True
    return False

def save_all_img(driver):
    driver.save_screenshot(IMG_PREFIX+ALL_IMAGE)
    wait_time(2)

def click_multi(dr,pos,times=1):
    c_times = 0
    while c_times < times:
        click_locxy(dr, pos[0], pos[1])
        wait_time(1)
        c_times = c_times + 1

class Languages(object):
    CHS = 'chi_sim'
    ENG = 'eng'

def get_ocr_txt(image, lang=Languages.CHS):
    result = ''
    content = ocr_act.image_to_string(image, lang)
    for x in content:
        result += x.strip(' ')
    return result

class Base(object):
    def __init__(self, driver, waits=1):
        self.driver = driver
        self.waits = waits

    def click_pos(self, pos, is_check=False):
        try:
            click_locxy(self.driver, pos[0], pos[1])
        except Exception as e:
            print(e)

    def click_by_js(self, x, y):
        try:
            self.driver.execute_script("""
                const event = new MouseEvent('click', {
                    bubbles: true,
                    cancelable: true,
                    view: window,
                    clientX: arguments[0],
                    clientY: arguments[1]
                });
                document.elementFromPoint(arguments[0], arguments[1]).dispatchEvent(event);
            """, x, y)
        except Exception as e:
            print(e)

    def get_pos_byimg(self, img_name, defalut_pos=(0,0), confidence=0.9, screen_shot =True):
        pos = match_img_pos(self.driver, img_name, confidencevalue=confidence, is_save=screen_shot)
        if pos[0] != 0 and pos[1] != 0:
            return pos            
        return defalut_pos

    def get_pos_byimg_region(self, img_name, region,defalut_pos=(0,0), confidence=0.9, screen_shot=True):
        try:
            if screen_shot:
                save_all_img(self.driver)
            
            region_im = self.crop_by_region(IMG_PREFIX+ALL_IMAGE, region)

            if region_im != None:
                region_im.save(IMG_PREFIX+ALL_IMAGE)
                xyt = match_img(ALL_IMAGE, img_name, confidence)    
                if xyt != None and len(xyt) > 0:
                    x = xyt[0]['result'][0]
                    y = xyt[0]['result'][1]
                    return (int(x), int(y) + BLACK_X) # 因为后面点击的方法会减去这个值，所以这里的加一下
        except Exception as e:
            print(e)
        return defalut_pos


    def is_exists_image_by_region(self, img_name, region, confidence=0.8, is_save=True):
        if is_save:
            save_all_img(self.driver)
            
        region_im = self.crop_by_region(IMG_PREFIX+ALL_IMAGE, region, 2)
        if region_im != None:
            region_im.save(IMG_PREFIX+ALL_IMAGE)
            xyt = match_img(ALL_IMAGE, img_name, confidence)    
            return xyt != None and len(xyt) > 0
        return False

    def is_exists_image(self, img_name, confidence = 0.8, is_save_img=True):
        return is_exists_image(self.driver, img_name, confidence, is_save=is_save_img)

    def recognize(self, img):
        img = img.convert('L')
        return get_ocr_txt(img)

    def crop_by_region(self, imgsrc, region, mode=1):
        try:            
            all_img = Image.open(imgsrc)
            if mode == 1:
                return all_img.crop((region[0], region[1], region[0]+region[2], region[1]+region[3]))
            else:
                return all_img.crop((region[0], region[1], region[2], region[3]))
        except Exception as e:
            print(e)
            return None
    
    def is_exists_image_CV2(self, img_name, confidence = 0.8, is_save_img=True):
        if is_save_img:
            save_all_img(self.driver)
        result = self.match_img_CV2(ALL_IMAGE, img_name, confidence)
        if result != None and len(result)>0:
            return True
        return False
    
    def match_img_CV2(self, imgsrc, imgobj, confidencevalue=0.9, is_return_pos= False):
        img_src =  IMG_PREFIX+imgsrc
        img_obj = IMG_PREFIX+imgobj
        try:
            imsrc = cv2.imread(img_src, 0)
            imobj = cv2.imread(img_obj, 0)
            w, h = imobj.shape[::-1]

            res = cv2.matchTemplate(imsrc, imobj, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= confidencevalue)  # 匹配度阈值

            match_result = []

            for pt in zip(*loc[::-1]):  # (x,y)
                x, y = pt
                center_x = x + w / 2
                center_y = y + h / 2

                result = {
                    "result": (center_x, center_y),
                    "rectangle": (
                        (x, y),
                        (x, y + h),
                        (x + w, y),
                        (x + w, y + h)
                    ),
                    "confidence": float(res[y][x])
                }

                match_result.append(result)

            if configs.runtime == 'debug':
                print(f'img_src:{img_src},img_obj:{img_obj}.match_result:{len(match_result)},confdend:{confidencevalue}')  
            #[{'result': (61.0, 135.5), 'rectangle': ((36, 110), (36, 161), (86, 110), (86, 161)), 'confidence': 1.0}]

            if not match_result:
                return None

            # 是否只返回第一个坐标
            if is_return_pos:
                return match_result[0]["result"]

            return match_result
        except Exception as ex:
                print(ex)
        return None
    
    def clear_console():
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print(e)

