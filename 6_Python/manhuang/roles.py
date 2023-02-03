# -*- coding: utf-8 -*-

from common import Base, BLACK_X, wait_time

ROLE_POS = (126, 769 + BLACK_X) # 126 769 + 124

CUR_ROLE = (66, 769 + BLACK_X)
ELIXIR_POS = (250 , 597 + BLACK_X)
EAT_ELIXIR = (251, 682 + BLACK_X)

FIRST_ELIXIR = (112, 143 + BLACK_X)
ELIXIR_X = 90
ELIXIR_Y = 75

# first down: 112 215
# last: 379 213

BLACK_POS = (250, 59+BLACK_X)

class Roles(Base):
    def __init__(self, driver):
        super(Roles, self).__init__(driver)

    def main_to_role(self):
        self.click_pos(ROLE_POS)

    def main_to_eat_Elixir(self):
        self.main_to_role()
        self.click_pos(CUR_ROLE)
        self.click_pos(ELIXIR_POS)
        self.eat_Elixir()
        self.click_callback()
    
    def eat_Elixir(self):
        times = 0
        while times < 8:
            x = FIRST_ELIXIR[0] + (times%4) * ELIXIR_X
            y = FIRST_ELIXIR[1] + int(times/4) * ELIXIR_Y
            self.click_pos((x, y))
            self.click_pos(EAT_ELIXIR)
            self.click_pos(BLACK_POS)
            times = times + 1
        wait_time(2)       
    
    