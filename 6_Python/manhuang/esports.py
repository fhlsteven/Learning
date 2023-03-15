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

class ESports(Base):
    def __init__(self, driver):
        super(ESports, self).__init__(driver)

    def single_sport(self):
        self.main_to_sport()
        self.click_pos(SINGLE_SPORT)
        self.click_pos(QUN_XIAN)
        self.click_pos(QUICK_MODE)

    def main_to_sport(self):
        self.click_pos(SPORT)        

    def kill_single(self):
        self.click_pos(KILL_POS)
        self.click_pos(OK_POS)

    def main_to_xy(self):
        self.main_to_sport()
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
        self.click_pos(XY_OK)
        while self.is_exists_image("xy_esport.png")==False:
            wait_time(5)


