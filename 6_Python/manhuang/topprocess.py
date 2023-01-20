# -*- coding: utf-8 -*-

from common import wait_time, Base

WELFARE_POS=(65, 261)
WELFARE_IMG = "welfare.png"

SIGN_IN = (265, 723)
DAY_SIGN_IN =(74, 891)

ONLINE_BAGS = (146, 895)
ONLINE_GET = (377, 241)

class TopProcess(Base):
    def __init__(self, driver):
        super(TopProcess, self).__init__(driver)
    
    def process_top(self):        
        self.get_welfare()

    def get_welfare(self):
        welfare_pos = self.get_pos_byimg(WELFARE_IMG, WELFARE_POS, 0.8)
        print(welfare_pos)
        self.clcik_pos(welfare_pos)
        wait_time(2)
        self.clcik_pos(DAY_SIGN_IN)
        wait_time(1)
        self.clcik_pos(SIGN_IN)
        wait_time(2)
        self.clcik_pos(ONLINE_BAGS)
        self.clcik_pos(ONLINE_GET)
        self.use_bags()
    
    def get_rank(self):
        rank_pos = slef.get_pos_byimg()
        print(rank_pos)

        
