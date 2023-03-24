# -*- coding:utf-8 -*-

from common import wait_time, Base, BLACK_X
from configs import configs
from teams import Teams

MAIN_FB_POS =(477, 610)

SINGLE_FB_POS = (75, 893)
EVERYDAY_POS = (260, 804)
FB_START_POS = (398, 549)
FB_FIRST_POS = (390, 279) # 155+124
OK_POS = (263, 806) # 806 - 124 = 682
OK_POS_SEC = (253, 759)# 253 635 + 124
# 宝塔 pagoda
PAGODA_POS = (148,798)
PAGODA_ZF_CLICK = (255, 707)

#
YGFZ_POS = (367, 805) # 357 678 + 124 


# 
MULTI_POS = (138, 900) # 138 766+124

# 249 631
# 211 775
ISLAND = (211, 899)
ISLAND_INFINITE = (127, 808) # 127 684+124
ISLAND_KILL = (249, 755)
ISLAND_SEC = (368, 808) # 368 683
ISLAND_SEC_FENG = (92, 444) # 92, 320 +124
ISLAND_SEC_LONG = (254, 484) # 254 360


QUICK_MATCH = (251, 615 + BLACK_X)

class InstanceZone(Base):
    def __init__(self, driver):
        super(InstanceZone, self).__init__(driver)

    def single_fb_time_kill(self):
        self.click_pos(FB_FIRST_POS)
        wait_time(100)
        self.click_pos(OK_POS_SEC)
        wait_time(1)

    def single_fb_kill(self):
        self.click_pos(FB_START_POS)
        wait_time(7)
        self.click_pos(OK_POS)
        wait_time(2)

    def signle_everyday_fb(self):
        c_times=0
        while 7 > c_times:            
            self.single_fb_kill()
            c_times = c_times + 1 
        
        # money and reki
        self.single_fb_time_kill()
        self.single_fb_time_kill()

        # 补救
        self.single_fb_kill()
        self.single_fb_kill()

        quick_times = 10
        c_times = 0
        if configs.svip_level > 0:
            quick_times = 45
        
        while c_times < quick_times:
            self.click_pos(FB_FIRST_POS)
            wait_time(2)
            c_times = c_times + 1
        
        while self.is_exists_image("fb_quick_kill.png", 0.95):
            self.click_pos(FB_FIRST_POS)
            wait_time(2)
    
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
        self.use_bags()
        self.click_pos(MAIN_FB_POS)

    def main_to_shenbeast_island(self, is_feng=True):
        self.main_to_fb()
        self.shenbeast_island_infinite()
        wait_time(3)
        if is_feng:
            self.shenbesat_island_feng()
            wait_time(3)
        self.click_callback()

    def shenbeast_island_infinite(self):
        self.click_pos(ISLAND)
        self.click_pos(ISLAND_INFINITE)
        self.click_pos(ISLAND_KILL)
        wait_time(10)
        while self.is_exists_image("boss_small.png", 0.65):
            wait_time(20)
        self.click_quit(False)
    
    def shenbesat_island_feng(self):
        wait_time(2)
        self.click_pos(ISLAND_SEC)
        wait_time(1)
        self.click_pos(ISLAND_SEC_FENG)
        self.click_pos(ISLAND_KILL)
        wait_time(15*21)
        self.use_bags()
        self.click_quit(False)
       

    def shenbesat_island_long(self):
        self.click_pos(ISLAND_SEC)
        self.click_pos(ISLAND_SEC_LONG)
        self.click_pos(ISLAND_KILL)
        wait_time(50)
        self.use_bags()
        self.click_quit(False)

    def go_you_ming(self):
        self.click_pos(QUICK_MATCH)
        wait_time(180-5)
        self.click_quit()
