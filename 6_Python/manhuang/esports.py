# -*- coding: utf-8 -*-

from common import Base, wait_time, BLACK_X

SPORT = (467, 568+ BLACK_X)
SINGLE_SPORT = (69, 762 + BLACK_X) # 69 762
QUN_XIAN = (141, 674 + BLACK_X)
QUICK_MODE = (311,425 + BLACK_X)
KILL_POS = (390,337 +BLACK_X)
OK_POS =(253, 707 + BLACK_X)

# xy
XY_POS = (345, 770 +BLACK_X) 
XY_SEC = (413, 428+BLACK_X)
XY_FIRST = (413, 506+BLACK_X)
XY_REFRESH =(346, 600 + BLACK_X)
XY_OK = (250,721+BLACK_X)
XY_TOP = (410,273 +BLACK_X)

EBLACK_POS=(250, 73+BLACK_X)

# zhan dui
ZD_POS = (276, 790 + BLACK_X)
ZD_ZL = (318,687 +BLACK_X)
ZD_MB = (252, 580+BLACK_X)
ZD_MB_SEC = (239, 672+BLACK_X)

class ESports(Base):
    def __init__(self, driver, waits=1):
        super(ESports, self).__init__(driver, waits=waits)

    def single_sport(self):
        self.main_to_sport()
        self.click_pos(SINGLE_SPORT)
        self.click_pos(QUN_XIAN)
        #self.click_pos(QUICK_MODE)

    def main_to_sport(self):
        self.use_bags()
        self.click_pos(SPORT)        

    def kill_single(self):
        self.click_pos(KILL_POS)
        self.click_pos(OK_POS)

    def main_to_xy(self):
        self.main_to_sport()
        self.click_pos(EBLACK_POS)
        self.click_pos(XY_POS)
        self.xy_kill(XY_SEC)
        self.xy_kill(XY_FIRST)
        self.click_pos(XY_REFRESH)
        self.xy_kill(XY_SEC)
        self.xy_kill(XY_FIRST)
        self.xy_kill(XY_TOP)
        self.click_callback()

    def xy_kill(self, pos):
        self.click_pos(pos)
        wait_time(5)
        #self.click_pos(XY_OK)
        while self.is_exists_image("xy_esport.png")==False:
            wait_time(5)

    def main_to_mobai(self):
        self.main_to_sport()
        wait_time(2)
        self.click_pos(ZD_POS)
        wait_time(2)
        self.click_pos(ZD_MB)
        wait_time(2)
        self.click_pos(ZD_MB_SEC)
        self.click_callback()

    def main_to_single_all(self):
        self.single_sport()
        times = 0
        while self.is_exists_image("quick_mod.png") == False:
            self.click_pos(EBLACK_POS)
            self.click_pos(QUICK_MODE)
            self.click_pos(EBLACK_POS)
        
        while times<10:
            self.kill_single()
            wait_time(2)
            times = times+1
        wait_time()
        self.click_callback()




