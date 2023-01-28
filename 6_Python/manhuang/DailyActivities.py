#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from common import wait_time, Base

HD_POS = (257, 630)  
HD_POS_START = (376, 282)
HD_CLOSE = (468, 199)

#treasure
XF_GOODS_POS =(295, 739)

#protect
PICK_POS = (258, 720)

# boss
BOSS_POS =(324, 720)  
TEAM_POS = (1860, 654) 
CREATE_TEAM_POS = (1665, 806) 

#
TT_MATCH = (338, 648)

DAY_BOSS_GET = (260, 783)
DAY_MONSTER_GET =(260, 452)
#

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
            if d_wkday != 6:
                self.tianti()
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

            wait_time(12*60)
            self.close_hd()
            self.click_callback()
            print("boss end")
    
    def tianti(self):    
        if is_between((19,30),(19,43)):
            print("tian ti start")
            self.start_hd()
            wait_time(4)
            self.click_pos(TT_MATCH)
            wait_time(13 * 60)
            self.close_hd()
            self.click_callback()
            print("tian ti end")
    
    def protect(self):
        if is_between((16,1),(16,50)):
            self.click_pos(HD_POS)

    def start_hd(self):
        self.click_pos(HD_POS)
        wait_time(2)
        self.click_pos(HD_POS_START)
        wait_time(3)
    
    def close_hd(self):
        self.click_pos(HD_CLOSE)
        wait_time(1)

    

    