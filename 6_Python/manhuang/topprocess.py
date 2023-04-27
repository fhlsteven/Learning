# -*- coding: utf-8 -*-

from common import wait_time, Base, click_black, BLACK_X
from configs import configs

WELFARE_POS=(65, 261)
WELFARE_IMG = "welfare.png"
RANK_IMG="rank.png"

LOGIN_GIGT = (70, 884) # 70 760
LOGIN_GIGT_GET = (402, 374) #402 250

SIGN_IN = (265, 723) # 
DAY_SIGN_IN =(143, 894) # 143 770

ONLINE_BAGS = (212, 895) # 212 772
ONLINE_GET = (377, 241) 

RANK_POS = (118, 259) # 115 134
CUR_AREA_RANK = (148, 890)
ONE_POS = (275, 417)
TWO_POS = (137, 469)
THREE_POS = (413, 483)

FIND_POS = (168, 260)
FIND_GOD_IMG = 'find_god.png'
FIND_GOD_POS = (70, 763)
FREE_FIND_POS = (120, 755)
ZB_POS = (85, 800)
X_STEP = 82
Y_STEP = 36

XD_RANK_IMG = 'xd_rank.png'
WORSHIP_POS = (250, 509)
XD_SEC_POS = (378 ,807)
XD_QUIT = (443, 227)

YB_IMG = 'yb.png'
YB_GET_POS = (372, 480)
YB_QUIT = (446, 413) #289 +124

#SVIP
SVIP_POS = (235, 56+BLACK_X)
SVIP_GIFT=(414, 205+BLACK_X)
SVIP_GET =(250,482+BLACK_X)

#shop free
SHOP_POS =(459,716+BLACK_X)
SHOP_FREE = (174,152+BLACK_X)
SEC_SHOP = (145,772+BLACK_X)
XF_SHOP = (83,712+BLACK_X)
BUY_OK = (250, 480 +BLACK_X)

class TopProcess(Base):
    def __init__(self, driver, waits=1):
        super(TopProcess, self).__init__(driver, waits=waits)
    
    def process_top(self):  
        self.to_main()      
        self.get_welfare()
        self.get_rank()
        self.find_treasure()
        self.xd_rank()
        self.get_yb()
        self.free_shop()
        if configs.svip_level > 0:
            self.get_svip()

    def get_welfare(self):
        welfare_pos = self.get_pos_byimg(WELFARE_IMG, WELFARE_POS, 0.8)
        self.click_pos(welfare_pos)
        wait_time(2)
        self.click_pos(LOGIN_GIGT)
        self.click_pos(LOGIN_GIGT_GET)
        if configs.svip_level>0:
            self.click_pos(LOGIN_GIGT_GET)            
        wait_time(2)
        self.click_pos(DAY_SIGN_IN)
        wait_time(1)
        self.click_pos(SIGN_IN)        
        self.click_pos(ONLINE_BAGS)
        wait_time(2)
        self.click_pos(ONLINE_GET)
        self.use_bags()
        wait_time(2)
        click_black(self.driver)
        self.click_callback()
    
    def get_rank(self):
        rank_pos = self.get_pos_byimg(RANK_IMG, RANK_POS, 0.8)
        print(rank_pos)
        self.click_pos(rank_pos)
        self.click_pos(CUR_AREA_RANK)
        self.click_pos(ONE_POS)
        self.click_pos(TWO_POS)
        self.click_pos(THREE_POS)
        self.click_callback()
    
    def find_treasure(self):
        find_god_pos = self.get_pos_byimg(FIND_GOD_IMG, FIND_GOD_POS, 0.5)
        self.click_pos(find_god_pos)
        wait_time(2)
        times = 0
        while times < 5:
            if times>=3:
                self.use_bags()
            self.click_pos((ZB_POS[0] + times * X_STEP, ZB_POS[1]))            
            self.click_pos(FREE_FIND_POS)
            click_black(self.driver)
            times = times + 1
            wait_time(1)
        
        times = 0
        while times < 3:
            self.click_pos((ZB_POS[0] + times * X_STEP, ZB_POS[1] +Y_STEP))
            self.click_pos(FREE_FIND_POS)
            click_black(self.driver)
            times = times + 1
            wait_time(1)

        self.click_callback()
    
    def xd_rank(self):
        xd_rank_pos = self.get_pos_byimg(XD_RANK_IMG, confidence=0.5)
        if xd_rank_pos[0]>0:
            self.click_pos(xd_rank_pos)
            wait_time(2)
            self.click_pos(WORSHIP_POS)
            wait_time(1)
            self.click_pos(XD_SEC_POS)
            wait_time(1)
            self.use_bags()
            wait_time(2)
            self.click_pos(XD_QUIT)

    def get_yb(self):
        yb_pos = self.get_pos_byimg(YB_IMG, confidence=0.5)
        if yb_pos[0] > 0:
            self.click_pos(yb_pos)
            wait_time(2)
            self.click_pos(YB_GET_POS)
            wait_time(1)
            self.click_pos(YB_QUIT)

    def get_svip(self):
        self.click_pos(SVIP_POS)
        self.click_pos(SVIP_GIFT)
        self.click_pos(SVIP_GET)
        click_black(self.driver,times=1)
        self.click_callback()

    def free_shop(self):
        self.click_pos(SHOP_POS)
        self.click_pos(SHOP_FREE)
        self.use_bags()
        self.click_callback()

    def main_to_xf_shop(self):
        self.click_pos(SHOP_POS)
        wait_time(5)
        self.click_pos(SEC_SHOP)
        self.click_pos(XF_SHOP)
        wait_time(3)
        self.xf_shop()
        self.click_callback()

    def xf_shop(self):
        c_times = 0
        while True:
            pos = self.get_pos_byimg("xf_shop.png")
            if pos[0]>0:
                buy_pos = (pos[0]+23, pos[1]+33)                
                self.click_pos(buy_pos)
                self.click_pos(BUY_OK)
                wait_time(3)  
            c_times = c_times+1
            if c_times >6:
                break
        c_times = 0
        while True:
            pos = self.get_pos_byimg("xf_yb.png", confidence=0.98)
            if pos[0]>0:
                buy_pos = (pos[0], pos[1]+11)
                self.click_pos(buy_pos)
                self.click_pos(BUY_OK)
                wait_time(3)            
            c_times = c_times+1
            if c_times >3:
                break



