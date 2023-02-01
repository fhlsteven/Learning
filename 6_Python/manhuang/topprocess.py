# -*- coding: utf-8 -*-

from common import wait_time, Base, click_black

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

class TopProcess(Base):
    def __init__(self, driver):
        super(TopProcess, self).__init__(driver)
    
    def process_top(self):        
        self.get_welfare()
        self.get_rank()
        self.find_treasure()
        self.xd_rank()
        self.get_yb()

    def get_welfare(self):
        welfare_pos = self.get_pos_byimg(WELFARE_IMG, WELFARE_POS, 0.8)
        self.click_pos(welfare_pos)
        wait_time(2)
        self.click_pos(LOGIN_GIGT)
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
            self.click_pos((ZB_POS[0] + times * X_STEP, ZB_POS[1]))
            self.click_pos(FREE_FIND_POS)
            times = times + 1
            wait_time(1)
        
        times = 0
        while times < 3:
            self.click_pos((ZB_POS[0] + times * X_STEP, ZB_POS[1] +Y_STEP))
            self.click_pos(FREE_FIND_POS)
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

