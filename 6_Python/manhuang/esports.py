# -*- coding: utf-8 -*-

from common import Base, wait_time, BLACK_X, BaseOCR

SPORT = (467, 568+ BLACK_X)
SINGLE_SPORT = (69, 762 + BLACK_X) # 69 762
QUN_XIAN = (141, 674 + BLACK_X)
QUICK_MODE = (311,425 + BLACK_X)
KILL_POS = (390,337 +BLACK_X)
OK_POS =(253, 707 + BLACK_X)

class ESports(Base):
    def __init__(self, driver):
        super(ESports, self).__init__(driver)
        self.ocr_obj = BaseOCR(driver)

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