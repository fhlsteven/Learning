# -*- coding: utf-8 -*-

from common import Base, wait_time, BLACK_X


ADVENTRUE_POS = (472,446+BLACK_X)

class Adventure(Base):
    def __init__(self, driver):
        super(Adventure, self).__init__(driver)

    def main_to_adventure(self):
        self.click_pos(ADVENTRUE_POS)

        