# -*- conding: utf-8 -*-

from common import Base, wait_time

TEAM_EMAIL_POS = (47, 840)
TEAM_POS = (76, 896)
AUTO_RECEIVE_POS = (341, 751)

EMAIL_POS = (140, 891) # 140 767+124
EMAIL_GET = (319, 826) # 319 702+124

KICK_OUT = (362, 637) # 362 523
KICK_OUT_OK = (325, 603) # 325 479+124

class Teams(Base):
    def __init__(self, driver):
        super(Teams, self).__init__(driver)
    
    def auto_receive(self):
        self.click_pos(TEAM_EMAIL_POS)
        wait_time(2)
        self.click_pos(TEAM_POS)
        wait_time(2)
        self.click_pos(AUTO_RECEIVE_POS)
        wait_time(2)
        self.click_callback()
    
    def get_email(self):
        self.click_pos(TEAM_EMAIL_POS)
        wait_time(1)
        self.click_pos(EMAIL_POS)
        self.click_pos(EMAIL_GET)
        wait_time(1)
        self.use_bags()        
        wait_time(1)
        self.click_pos(EMAIL_GET) # some need to click blank 
        self.click_callback()

    def kick_out(self):
        self.click_pos(KICK_OUT)
        self.click_pos(KICK_OUT_OK)
