# -*- coding: utf-8 -*-

from common import wait_time, Base, BLACK_X
from configs import configs
from datetime import datetime, timedelta

MAIN_BOSS_POS =(476, 652)

# CUR server
CUR_SERVER_BOSS = (72, 889)
SINGLE_BOSS =(137, 805)
KILL_SINGLE_BOSS=(398, 261)
ONE_KEY_KILL_SBOSS = (396, 596 + BLACK_X)

OK_POS = (255, 789)

MULTI_POS = (253, 686 + BLACK_X)
YUN_MEN_POS =(373,683 + BLACK_X)
# kua fu 
KUA_FU_BOSS = (150, 892)
THREE_REALM_BOSS = (93, 809)
KILL_THREE_REALM = (257, 719)

#kua qu
KUA_QU_BOSS = (213, 766+BLACK_X)

# huan jing
HUANJING_BOSS = (287,766+BLACK_X)



class Boss(Base):
    def __init__(self, driver):
        super(Boss, self).__init__(driver)
    
    def single_boss(self):
        times=0
        boss_times = configs.reincarnation + 1
        if configs.svip_level > 1:
            self.click_pos(ONE_KEY_KILL_SBOSS)
            times = boss_times+1        
        
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
        wait_time(2)
    
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

    def process_three_realms(self):        
        cur_time =  datetime.now()
        try:
            if cur_time.hour == 23:
                nxt = cur_time + timedelta(days=1)
                next_time = datetime(nxt.year, nxt.month, nxt.day,0,0,10)
            else:
                next_time = datetime(cur_time.year, cur_time.month, cur_time.day, cur_time.hour + 1, 0, 10)
            wait_secs = (next_time - cur_time).seconds  
            if wait_secs<5*60:              
                wait_time(wait_secs)
                self.main_to_three_realms()  
                return 1         
        except Exception as e:
            print(e)
        return 0