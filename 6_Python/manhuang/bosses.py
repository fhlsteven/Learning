# -*- coding: utf-8 -*-

from common import wait_time, Base
from configs import configs

MAIN_BOSS_POS =(476, 652)

CUR_SERVER_BOSS = (72, 889)
SINGLE_BOSS =(137, 805)
KILL_SINGLE_BOSS=(398, 261)

OK_POS = (255, 789)

KUA_FU_BOSS = (150, 892)
THREE_REALM_BOSS = (93, 809)
KILL_THREE_REALM = (257, 719)

class Boss(Base):
    def __init__(self, driver):
        super(Boss, self).__init__(driver)
    
    def single_boss(self):
        times=0
        boss_times = configs.reincarnation + 1
        while boss_times > times:
            self.click_pos(KILL_SINGLE_BOSS)
            wait_time(3)
            self.click_pos(OK_POS)
            wait_time(2)
            times = times + 1
        wait_time(2)
        self.use_bags()
        self.click_callback()

    def main_to_boss(self):
        self.rong_lian()
        self.click_pos(MAIN_BOSS_POS)
        wait_time(3)
    
    def main_to_three_realms(self):
        self.main_to_boss()
        self.click_pos(KUA_FU_BOSS)
        self.click_pos(THREE_REALM_BOSS)
        self.click_pos(KILL_THREE_REALM)

        times = 0
        while self.is_exists_image("three_boss.png") == False:
            wait_time(60)
            times = times + 60
            if times > 60 * 20:
                break
        
        wait_time(2)
        self.use_bags()
        self.click_callback()
        self.rong_lian()
    
    def main_to_single_boss(self):
        self.main_to_boss()
        self.click_pos(CUR_SERVER_BOSS)
        self.click_pos(SINGLE_BOSS)
        self.single_boss()