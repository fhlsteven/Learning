# -*- coding: utf-8 -*-

from common import Base, BLACK_X, wait_time, click_black
from datetime import datetime

ROLE_POS = (126, 769 + BLACK_X) # 126 769 + 124

CUR_ROLE = (66, 769 + BLACK_X)
ELIXIR_POS = (250 , 597 + BLACK_X)
EAT_ELIXIR = (251, 682 + BLACK_X)

FIRST_ELIXIR = (112, 143 + BLACK_X)
ELIXIR_X = 90
ELIXIR_Y = 75

# first down: 112 215
# last: 379 213

BLACK_POS = (250, 59+BLACK_X)

MORE_POS = (454,666+BLACK_X)
XINA_YUAN = (278, 603+BLACK_X)
YI_JIE = (141, 770+BLACK_X)
XY_FB = (416, 350 +BLACK_X)
XY_FB_START = (250,628 +BLACK_X)
# login

class Roles(Base):
    def __init__(self, driver, waits=1):
        super(Roles, self).__init__(driver, waits=waits)

    def main_to_role(self):
        self.click_pos(ROLE_POS)

    def main_to_eat_Elixir(self):
        self.main_to_role()
        self.click_pos(CUR_ROLE)
        self.click_pos(ELIXIR_POS)
        self.eat_Elixir()
        self.click_callback()
    
    def eat_Elixir(self):
        times = 0
        while times < 8:
            x = FIRST_ELIXIR[0] + (times%4) * ELIXIR_X
            y = FIRST_ELIXIR[1] + int(times/4) * ELIXIR_Y
            self.click_pos((x, y))
            self.click_pos(EAT_ELIXIR)
            self.click_pos(BLACK_POS)
            times = times + 1
        wait_time(2)

    def main_to_xianyuan(self):
        self.click_pos(MORE_POS)
        self.click_pos(XINA_YUAN)

    def main_to_xianyuan_fb(self):
        self.main_to_xianyuan()
        self.xianyuan_fb()

    def xianyuan_fb(self):
        self.click_pos(YI_JIE)
        times = 0
        while times < 2:  
            times = times + 1           
            self.click_pos(XY_FB)
            self.click_pos(XY_FB_START)
            wait_time(3*60+2)            
            click_black(self.driver, times=1)
            c_times = 0
            while self.is_exists_image("xy_fb.png") == False and c_times<20:
                wait_time(5)
                c_times = c_times +1

        self.use_bags()
        self.click_callback()

    def check_login(self, check_more=True):
        if check_more:
            self.use_bags()
            click_black(self.driver, times=5)
            self.log_by_img()
        pos = self.get_pos_byimg("ok.png")
        if pos[0]>0:
            self.click_pos(pos)
            wait_time()
            while self.is_exists_image("login_bg.png"):
                wait_time()
            click_black(self.driver, 5)
        if check_more:
            self.log_by_img()
        pos = self.get_pos_byimg("ok_sec.png")
        if pos[0]>0:
            self.relogin() 

    def relogin(self):
        self.driver.refresh()
        while True:
            wait_time()
            if self.is_exists_image("login.png"):
                break            
        pos = self.get_pos_byimg("login.png", False)
        if pos[0]>0:
            self.click_pos(pos)
            wait_time()
            while self.is_exists_image("login_bg.png"):
                wait_time()
            click_black(self.driver, 5)
        
    def log_by_img(self):
        self.driver.save_screenshot("temp/clog_"+ str(datetime.now()).replace(':','_')+'.png')
            


        
    
    