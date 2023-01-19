# -*- coding:utf-8 -*-

from common import wait_time, clcik_pos_locxy


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


class InstanceZone(object):
    def __init__(self, driver):
        self.driver = driver

    def signle_everyday_fb(self):
        times=0
        while 7 > times:
            clcik_pos_locxy(self.driver, FB_START_POS)
            wait_time(6)
            clcik_pos_locxy(self.driver, OK_POS)
            wait_time(2)
            times = times + 1 
        
        times  = 0
        while 7 > times:
            clcik_pos_locxy(self.driver, FB_START_POS)
            wait_time(2)
            times = times + 1
    
    def da_huang_pagoda(self):
        clcik_pos_locxy(self.driver, PAGODA_POS)
        clcik_pos_locxy(self.driver, PAGODA_ZF_CLICK)

    def main_to_everyday_fb(self):
        self.main_to_fb()
        clcik_pos_locxy(self.driver, SINGLE_FB_POS)
        clcik_pos_locxy(self.driver, EVERYDAY_POS)
        self.signle_everyday_fb()

    def main_to_fb(self):
        clcik_pos_locxy(self.driver, MAIN_FB_POS)