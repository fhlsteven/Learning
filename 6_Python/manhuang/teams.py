# -*- conding: utf-8 -*-

from common import Base, wait_time

TEAM_EMAIL_POS = (47, 840)
TEAM_POS = (76, 896)
AUTO_RECEIVE_POS = (341, 751)

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