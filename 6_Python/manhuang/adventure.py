# -*- coding: utf-8 -*-

from common import Base, wait_time, BLACK_X


ADVENTRUE_POS = (472,446+BLACK_X)

class Adventure(Base):
    def __init__(self, driver):
        super(Adventure, self).__init__(driver)

    def main_to_adventure(self):
        self.click_pos(ADVENTRUE_POS)

    def process_adventure_events(self):
        self.main_to_adventure()
        self.process_kill_go()

    def process_open(self):
        while True:
            pos = self.get_pos_byimg("adv_open.png")
            if pos[0]>0:
                self.click_pos(pos)
                wait_time(2*60+3)
                self.click_pos(pos)
            else:
                break

    def process_kill_go(self):
        while True:
            pos = self.get_pos_byimg("adv_kill.png")
            if pos[0]> 0:
                self.go_kill(pos)
            else:
                break

    def go_kill(self, pos):
        self.click_pos(pos)
        wait_time(5)
        while self.is_adventure()== False:
            wait_time(5)
    
    def is_adventure(self):
        return self.is_exists_image("adv_event.png")

        