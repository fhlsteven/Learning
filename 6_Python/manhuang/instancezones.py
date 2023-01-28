# -*- coding:utf-8 -*-

from common import wait_time, Base

MAIN_FB_POS =(477, 610)

SINGLE_FB_POS = (75, 893)
EVERYDAY_POS = (260, 804)
FB_START_POS = (398, 549)
OK_POS = (263, 806)
# 宝塔 pagoda
PAGODA_POS = (148,798)
PAGODA_ZF_CLICK = (255, 707)

#
ZF_POS = (367, 805)

class InstanceZone(Base):
    def __init__(self, driver):
        super(InstanceZone, self).__init__(driver)

    def signle_everyday_fb(self):
        c_times=0
        while 7 > c_times:
            self.click_pos(FB_START_POS)
            wait_time()
            self.click_pos(OK_POS)
            wait_time(2)
            c_times = c_times + 1 
        
        c_times = 0
        while 7 > c_times:
            self.click_pos(FB_START_POS)
            wait_time(3)
            c_times = c_times + 1
    
    def da_huang_pagoda(self):
        self.click_pos(PAGODA_POS)
        self.click_pos(PAGODA_ZF_CLICK)

    def main_to_everyday_fb(self):
        self.rong_lian()
        self.main_to_fb()
        self.click_pos(SINGLE_FB_POS)
        self.click_pos(EVERYDAY_POS)
        self.signle_everyday_fb()
        self.click_callback()

    def main_to_fb(self):
        self.click_pos(MAIN_FB_POS)