# -*- conding: utf-8 -*-

from common import Base, wait_time,BLACK_X

TEAM_EMAIL_POS = (47, 840)
TEAM_POS = (76, 896)
AUTO_RECEIVE_POS = (341, 751)

CREATE_TEAM = (250,627 + BLACK_X)
AUTO_MATCH = (351,603 + BLACK_X)
AUTO_GO = (351,635 + BLACK_X)

EMAIL_POS = (140, 891) # 140 767+124
EMAIL_GET = (319, 826) # 319 702+124

KICK_OUT = (362, 637) # 362 523
KICK_OUT_OK = (325, 603) # 325 479+124

QUIT = (252,414+BLACK_X)
QUIT_OK = (325, 480+BLACK_X)

QUICK_MATCH = (251, 615 + BLACK_X)

class Teams(Base):
    def __init__(self, driver):
        super(Teams, self).__init__(driver)

    def create_team(self):
        self.click_pos(CREATE_TEAM)

    def auto_match(self):
        self.click_pos(AUTO_MATCH)

    def auto_go(self):
        self.click_pos(AUTO_GO)
    
    def auto_receive(self):
        self.go_to_team()
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

    def go_to_team(self):
        self.click_pos(TEAM_EMAIL_POS)
        self.click_pos(TEAM_POS)

    def kick_out(self):
        self.click_pos(KICK_OUT)
        self.click_pos(KICK_OUT_OK)

    def quit_team_status(self, is_need_cb=True):
        self.click_pos(QUIT)
        self.click_pos(QUIT_OK)
        if is_need_cb:
            self.click_callback()

    def quick_match(self):
        self.click_pos(QUICK_MATCH)

