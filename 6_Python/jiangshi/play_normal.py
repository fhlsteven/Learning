from common import wait_time, Base, BLACK_X
from configs import configs
from datetime import datetime


class PlayNormal(Base):
    def __init__(self, driver, waits=1):
         super(PlayNormal, self).__init__(driver, waits=waits)

    def playNormal(self):
        print('playNormal start')
        selectPos = (255, 835)
        #startplay = self.get_pos_byimg("start.png", (0,0), 0.7)
        #print(startplay)
        #if startplay and startplay[0] > 0:
        #    self.click_by_js(startplay[0], [1])
        #    wait_time(2)
        #else:
        #    print('palynormal not found start img')
        
        while True:
            if self.is_exists_image("select.png", confidence=0.7):
                self.click_pos(selectPos)
                print('select click')
            elif self.is_exists_image("replay.png",confidence=0.7):
                print('replay click')
                self.click_pos((250, 1040))
            elif self.is_exists_image("boss_kill.png", confidence=0.7):
                print('boss_kill click')
                self.click_pos(selectPos)
            wait_time(3)

    def test_click_pos(self, x,y):
        self.click_pos((x,y))
