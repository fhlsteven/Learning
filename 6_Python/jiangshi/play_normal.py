from common import wait_time, Base, click_black, BLACK_X
from configs import configs
from roles import Roles
from datetime import datetime


class PlayNormal(Base):
    def __init__(self, driver, waits=1):
         super(PlayNormal, self).__init__(driver, waits=waits)

    def playNormal(self):
        print('playNormal start')
        startplay = self.get_pos_byimg("start.png", (0,0), 0.7)
        print(startplay)
        if startplay and startplay[0] > 0:
            startplay[1] = startplay[1] + BLACK_X
            self.click_pos(startplay)
            wait_time(2)
        else:
            print('palynormal not found start img')
        
        while True:
            if self.is_exists_image("select.png", confidence=0.7):
                self.click_pos((255, 835))
                wait_time(5)
                print('playNormal')
            elif self.is_exists_image("replay.png",confidence=0.7):
                replay = self.get_pos_byimg("replay.png", (0, 0), 0.7)
                if replay and replay[0] > 0:
                    replay[1] = replay[1] + BLACK_X
                    self.click_pos(replay)
                    wait_time(10)
                else:
                    print('playNormal not found replay img')
                    wait_time(2)
                    return
            wait_time(5)
