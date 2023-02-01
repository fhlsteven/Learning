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

# 249 631
# 211 775
ISLAND = (211, 899)
ISLAND_INFINITE = (127, 808) # 127 684+124
ISLAND_KILL = (249, 755)
ISLAND_SEC = (368, 807) # 368 683
ISLAND_SEC_FENG = (92, 444) # 92, 320 +124
ISLAND_SEC_LONG = (254, 484) # 254 360

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
        self.main_to_fb()
        self.click_pos(SINGLE_FB_POS)
        self.click_pos(EVERYDAY_POS)
        self.signle_everyday_fb()
        self.click_callback()

    def main_to_fb(self):
        self.click_pos(MAIN_FB_POS)

    def main_to_shenbeast_island(self):
        self.main_to_fb()
        self.shenbeast_island_infinite()
        self.shenbesat_island_feng()
        self.click_callback()

    def shenbeast_island_infinite(self):
        self.click_pos(ISLAND)
        self.click_pos(ISLAND_INFINITE)
        self.click_pos(ISLAND_KILL)
        wait_time(10)
        while self.is_exists_image("boss_small.png", 0.65):
            wait_time(20)
        self.click_quit()  
    
    def shenbesat_island_feng(self):
        self.click_pos(ISLAND_SEC)
        self.click_pos(ISLAND_SEC_FENG)
        self.click_pos(ISLAND_KILL)
        wait_time(15*21)
        self.click_quit()

    def shenbesat_island_long(self):
        self.click_pos(ISLAND_SEC)
        self.click_pos(ISLAND_SEC_LONG)
        self.click_pos(ISLAND_KILL)
        wait_time(50)
        self.click_quit() 

        
