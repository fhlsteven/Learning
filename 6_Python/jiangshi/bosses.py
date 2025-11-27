# -*- coding: utf-8 -*-

from common import wait_time, Base, BLACK_X,click_black
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
SHEN_DIAN_BOSS = (182,679+BLACK_X)
KILL_SHEN_DIAN =(396, 126+BLACK_X)
#kua qu
KUA_QU_BOSS = (213, 766+BLACK_X)

# huan jing
HUANJING_BOSS = (287,766+BLACK_X)



class Boss(Base):
    def __init__(self, driver, waits=1):
        super(Boss, self).__init__(driver, waits=waits)
    
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
        self.use_bags()
        self.click_pos(MAIN_BOSS_POS)
        wait_time(2)
    
    def main_to_three_realms(self):
        if datetime.now().hour == 23:
            click_black(self.driver)
        self.main_to_boss()
        self.click_pos(KUA_FU_BOSS)
        self.click_pos(THREE_REALM_BOSS)
        self.click_pos(KILL_THREE_REALM)

        self.check_is_kill("three_boss.png")

        wait_time(2)
        self.use_bags()
        self.click_callback()
        self.rong_lian()
    
    def main_to_single_boss(self):
        self.main_to_boss()
        self.click_pos(CUR_SERVER_BOSS)
        self.click_pos(SINGLE_BOSS)
        self.single_boss()

    def main_to_shen_dian(self):
        self.main_to_boss()
        self.click_pos(KUA_FU_BOSS)
        self.shen_dian_boss()

    def shen_dian_boss(self):
        self.click_pos(SHEN_DIAN_BOSS)
        self.click_pos(KILL_SHEN_DIAN)
        self.check_is_kill("shen_dian.png")
        self.use_bags()
        self.click_callback()

    def check_is_kill(self, img_tag, duration=20):        
        times = 0
        while self.is_exists_image(img_tag) == False:
            wait_time(60)
            times = times + 60
            if times > 60 * duration:
                break

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