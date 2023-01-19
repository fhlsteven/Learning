# -*- coding: utf-8 -*-

from common import wait_time, clcik_pos_locxy

MAIN_BOSS_POS =(476, 652)

CUR_SERVER_BOSS = (72, 889)
SINGLE_BOSS =(137, 805)
KILL_SINGLE_BOSS=(398, 261)

OK_POS = (255, 789)
SINGLE_BOOS_TIMES = 5 

class Boss(object):
    def __init__(self, driver):
        self.driver = driver
    
    def single_boss(self):
        times=0
        while SINGLE_BOOS_TIMES > times:
            clcik_pos_locxy(self.driver, KILL_SINGLE_BOSS)
            wait_time(3)
            clcik_pos_locxy(self.driver, OK_POS)
            wait_time(2)
            times = times + 1

    def main_to_boss(self):
        clcik_pos_locxy(self.driver, MAIN_BOSS_POS)
        wait_time(3)
    
    def main_to_single_boss(self):
        self.main_to_boss()
        clcik_pos_locxy(self.driver, CUR_SERVER_BOSS)
        clcik_pos_locxy(self.driver, SINGLE_BOSS)
        self.single_boss()