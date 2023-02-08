#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from common import wait_time, Base, clear_kill_go, BLACK_X, click_black
from teams import Teams

HD_POS = (257, 630)  
HD_POS_START = (376, 282)
HD_CLOSE = (468, 199)

#treasure
XF_GOODS_POS =(295, 739)

#protect
PICK_POS = (258, 720)

# boss
BOSS_POS =(324, 720)  
TEAM_POS = (1860, 654) # 469 479
CREATE_TEAM_POS = (1665, 806) 

FIRST_BOSS = (425,555 + BLACK_X) # 419 554
SEC_BOSS = (425, 575 + BLACK_X) 
THIRD_BOSS = (425, 595)

#
TT_MATCH = (338, 648)

# 
DAY_BTN = (457, 528) # 457 404+124
DAY_KILL = (213, 891) # 213 769+124
DAY_BOSS_GET = (260, 783)
DAY_MONSTER_GET =(260, 452)
#

XIAN_NV = (249, 714) # 252 605

# xuanhuo 1-6
XUANHUO_GO = (250, 591 + BLACK_X)
FIND_XUANHUO = (288, 473 + BLACK_X)

# xianmo 
XIANMO = (320, 593 + BLACK_X)

# xianmenzhengba : 6 20:40-21:10 jinying
# xianmenzhengba : 5 20:40-21:10 jifen
XIANMEN_TEAM = (451, 500+BLACK_X)
# xiandaohui : 4 20:40-21:10
# xianyuan : 1 20:40-21:10
# zhandui: 3 20:40-21:10
# shenmo : 2 20:40-21:10
# fengyunleitai : 7 20:40-21:05

def is_between(start_at, end_at):
    now_time = datetime.now()
    if start_at[0] <= now_time.hour <= end_at[0]:
        if start_at[1] <= now_time.minute <=end_at[1]:
            return True
    return False

class DailyActivities(Base):
    def __init__(self, driver):
        super(DailyActivities, self).__init__(driver)
        self.hd_in_progress = False

    def monitor(self):
        while True:
            self.hd_process()
            wait_time()
            if datetime.now().hour == 21:
                break

    def hd_process(self):
        d_now = datetime.now()
        d_wkday = d_now.weekday()
        try:
            self.protect()
            self.god_treasure()
            self.bath()
            self.boss()
            if d_wkday != 6:  # 0:Mon 6:sunday
                self.tianti()
            if d_wkday != 6:
                self.xuanhuo()
            self.xianmo()
            self.jiutian()
            if d_wkday == 1:
                self.shen_mo_battlefield()
        except Exception as e:
            print(f'exception:{e},{d_now}')        
    # down 
    def god_treasure(self):
        if is_between((11,30),(11,37)) or is_between((18,30),(18,37)):
            print("god_treasure start")
            self.start_hd()
            self.click_pos(XF_GOODS_POS)
            wait_time(480)
            print(f"god_treasure end.{datetime.now()}")
            self.close_hd()
            self.use_bags()

    # bath
    def bath(self):
        if is_between((19,1), (19,16)):
            print("bath start")
            self.start_hd()
            wait_time(17*60)
            self.close_hd()
            print("bath end")
            self.use_bags()

    def boss(self):
        if is_between((12,30), (12,42)):
            print("boss start")
            self.start_hd()
            wait_time(3)
            self.click_pos(BOSS_POS)

            wait_time(482 + 25)
            for x in range(1, 4):                
                self.click_pos((FIRST_BOSS[0], FIRST_BOSS[1] + x*20))
                wait_time(25)

            wait_time(4*60)
            self.close_hd()
            self.click_callback()
            print("boss end")
    
    def tianti(self):    
        if is_between((19,30),(19,40)):
            print("tian ti start")
            self.start_hd()
            wait_time(4)
            self.click_pos(TT_MATCH)
            wait_time(10 * 60)
            self.close_hd()
            self.click_callback()
            print("tian ti end")
    
    def protect(self):
        if is_between((16,1),(16,50)):
            self.start_hd(False)
            times = 0
            while times< 3:
                self.click_pos(XIAN_NV)
                self.click_pos(XIAN_NV)
                wait_time(15 * 60)
                self.click_pos(XIAN_NV)
                times = times + 1
            self.click_callback()

    def xuanhuo(self):
        if is_between((19,45), (20,0)):
            print("xuan huo")
            self.start_hd(False)
            wait_time(3)
            self.click_pos(XUANHUO_GO)
            wait_time(3)
            self.click_pos(FIND_XUANHUO)
            wait_time(15 * 60)
            self.click_callback()

    def xianmo(self):
        if is_between((20,0), (20,20)):            
            print('xian mo')
            self.start_hd(False)
            self.click_pos(XIANMO)
            team = Teams(self.driver)
            team.create_team()
            team.auto_match()
            team.auto_go()
            wait_time(15*60)
            self.use_bags()
            clear_kill_go(self.driver)
            self.click_callback()

    def jiutian(self):
        if is_between((20, 20), (20,40)):
            print('jiu tian')
            self.start_hd(False)
            self.click_pos(XUANHUO_GO)
            wait_time(18 * 60)
            self.use_bags()
            click_black(self.driver, )
            self.click_callback()

    def shen_mo_battlefield(self):
        if is_between((20,40), (21,10)):
            print("shen mo battlefiled")
            self.click_pos(XUANHUO_GO)
            wait_time(25*60)
            self.use_bags()
            self.click_callback()

    def start_hd(self, need_start=True): 
        self.driver.save_screenshot("temp/hd_"+ str(datetime.now()).replace(':','_')+'.png')       
        self.click_pos(HD_POS)
        wait_time(2)
        clear_kill_go(self.driver)
        if need_start:
            self.click_pos(HD_POS_START)
        wait_time(3)
    
    def close_hd(self):
        self.click_pos(HD_CLOSE)
        wait_time(1)

    def main_to_daily_boss_gets(self):
        self.click_pos(DAY_BTN)
        self.click_pos(DAY_KILL)
        times = 0
        while times < 11:
            self.click_pos(DAY_BOSS_GET)
            times = times + 1
        times = 0
        while times < 20:
            self.click_pos(DAY_MONSTER_GET)
            times = times + 1

        wait_time(1)
        self.use_bags()
        wait_time(2)
        self.click_callback()    