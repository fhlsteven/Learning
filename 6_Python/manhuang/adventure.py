# -*- coding: utf-8 -*-

from common import Base, wait_time, BLACK_X


ADVENTRUE_POS = (472, 446+BLACK_X)
SCISSORS = (249, 536+BLACK_X)
CLOSE_GAMBLE = (440, 260+BLACK_X)
EX_OK_POS = (247,667 +BLACK_X)

class Adventure(Base):
    def __init__(self, driver):
        super(Adventure, self).__init__(driver)

    def main_to_adventure(self):
        self.click_pos(ADVENTRUE_POS)

    def process_adventure_events(self):
        self.main_to_adventure()
        if self.is_exists_image("adv_black.png") == False:
            self.process_kill_go()
            self.process_small_gamble(False)
            self.process_open(False)
            self.process_explore(False)
            self.process_fariy(False)
            self.use_bags()
        self.click_callback()
    
    def process_kill_go(self):
        while True:
            pos = self.get_pos_byimg("adv_kill.png",confidence=0.7)
            if pos[0]> 0:
                self.go_kill(pos)
            else:
                break

    def process_open(self, is_save_all):
        while True:
            pos = self.get_pos_byimg("adv_open.png", confidence=0.7, screen_shot=is_save_all)
            if pos[0]>0:
                self.click_pos(pos)
                wait_time(2*60+3)
                self.click_pos(pos)
                is_save_all = True
            else:
                break

    def process_small_gamble(self, is_save_all):
        while True:
            pos = self.get_pos_byimg("adv_gamble.png", screen_shot=is_save_all)
            if pos[0]>0:
                self.small_gamble(pos)
                is_save_all =True
            else:
                break

    def process_fariy(self, is_save_all):
        while True:
            pos = self.get_pos_byimg("adv_recv.png", screen_shot=is_save_all)
            if pos[0]>0:
                self.receive_fariy(pos)
                is_save_all=True
            else:
                break

    def process_explore(self, is_save_all):
        while True:
            pos = self.get_pos_byimg("adv_explore.png", confidence=0.7, screen_shot=is_save_all)
            if pos[0]>0:
                self.click_pos(pos)
                wait_time(35)
                self.click_pos(EX_OK_POS)
                is_save_all = True
            else:
                break
    
    def receive_fariy(self, pos):
        self.click_pos(pos) # todo:

    def small_gamble(self, pos):
        self.click_pos(pos)
        wait_time(1)
        self.click_pos(SCISSORS)
        wait_time(4)
        self.click_pos(CLOSE_GAMBLE)

    def go_kill(self, pos):
        self.click_pos(pos)
        wait_time(5)
        self.click_pos(EX_OK_POS)
        while self.is_adventure() == False:
            wait_time(5)
    
    def is_adventure(self):
        return self.is_exists_image("adv_event.png")

        