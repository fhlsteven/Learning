# -*- coding: utf-8 -*-
from common import Base, wait_time, IMG_PREFIX,BLACK_X
from socket import socket
from DailyActivities import DailyActivities, is_between
from housejobs import HouseJob
from bosses import Boss
from instancezones import InstanceZone
from adventure import Adventure
from roles import Roles
from esports import ESports
from topprocess import TopProcess
from datetime import datetime, timedelta
from teams import Teams

YUAN_SHEN = [b'\xe7\x83\x81\xe9\x87\x91', b'\xe7\x8e\x84\xe8\x8b\x8d', b'\xe5\xb9\xbb\xe6\xb5\xb7', b'\xe7\x82\xbd\xe5\xa4\xa9', b'\xe6\x98\x86\xe5\xa2\x9f']
BA_GUA = [b'\xe7\x8e\x84\xe9\xbe\x9f', b'\xe6\x83\x8a\xe9\x9b\xb7', b'\xe7\x99\xbd\xe6\xb3\xbd', b'\xe7\x82\x8e\xe5\x87\xb0', b'\xe8\x8b\x8d\xe9\xbe\x99']
YI_BAO = [b'\xe4\xbb\x99\xe5\x99\xa8', b'\xe7\x81\xb5\xe5\xae\xa0', b'\xe7\xa5\x9e\xe5\x88\x83', b'\xe4\xbb\x99\xe7\xbe\xbd', b'\xe8\xa3\x85\xe8\xa2\x8d', b'\xe7\x8f\xa0\xe7\xba\xb9']

OTHER_FB = [b'\xe5\xb9\xbd\xe5\x86\xa5', b'\xe6\x88\x98\xe9\xad\x82', b'\xe8\x99\x9a\xe6\x97\xa0']

ONE_ALL = b'\xe7\x83\x81\xe9\x87\x91\xe7\x8e\x84\xe8\x8b\x8d\xe5\xb9\xbb\xe6\xb5\xb7\xe7\x82\xbd\xe5\xa4\xa9\xe6\x98\x86\xe5\xa2\x9f\xe7\x8e\x84\xe9\xbe\x9f\xe6\x83\x8a\xe9\x9b\xb7\xe7\x99\xbd\xe6\xb3\xbd\xe7\x82\x8e\xe5\x87\xb0\xe8\x8b\x8d\xe9\xbe\x99\xe4\xbb\x99\xe5\x99\xa8\xe7\x81\xb5\xe5\xae\xa0\xe7\xa5\x9e\xe5\x88\x83\xe4\xbb\x99\xe7\xbe\xbd\xe8\xa3\x85\xe8\xa2\x8d\xe7\x8f\xa0\xe7\xba\xb9\xe5\xb9\xbd\xe5\x86\xa5\xe8\x99\x9a\xe6\x97\xa0\xe6\x88\x98\xe9\xad\x82'

CQ_POS = (324, 287+BLACK_X)
PT_POS= (176,286+BLACK_X)
CQ_REFRESH = (250,652+BLACK_X)
CQ_KILL = (385,233+BLACK_X)

class Monitors(Base):
    def __init__(self, driver):
        super(Monitors, self).__init__(driver)
        self.driver = driver
        self.pre_msg = ""
        self.socket = None
    
    def get_socket(self):
        if self.socket == None:
            self.socket = socket()
            self.socket.connect(('192.168.200.205',13148))
    
    def send_msg(self, msg):
        self.get_socket()
        self.socket.send(msg.encode('utf-8'))

    def close_socket(self):
        if self.socket is not None:
            self.socket.close()
        self.socket = None

    def monitor_msg(self, check_s=''):
        if check_s == '':
            check_s = ONE_ALL
                
        check_s = check_s.decode('utf-8')        
        pre_msg = ''
        while self.is_exists_image('chat_box.png'):
            wait_time(4)            
            region = (155,567,263,112)
            self.driver.save_screenshot(IMG_PREFIX+'chat.png')
            wait_time(1)
            chat_im = self.crop_by_region(IMG_PREFIX+'chat.png', region)
            rec_result = self.recognize(chat_im)
            if pre_msg != rec_result:
                pre_msg = rec_result
                for s in rec_result:
                    if s in check_s:
                        self.send_msg(rec_result)                
            wait_time(15)
        self.close_socket()          

    def monitor_yuan_shen(self):       
        self.monitor_msg(b''.join(YUAN_SHEN))

    def monitor_ba_gua(self):
        self.monitor_msg(b''.join(BA_GUA))

    def monitor_yi_bao(self):
        self.monitor_msg(b''.join(YI_BAO))
    
    def monitor_fb(self):
        self.monitor_msg(b''.join(OTHER_FB))

    def monitor_hd(self):
        hd_monitor = DailyActivities(self.driver)
        while self.is_exit(False):
            wait_time()
            hd_monitor.hd_process()            
            if datetime.now().hour == 22 or self.is_exit(True):
                break
    
    def is_exit(self, status):
        return self.is_exists_image('chat_box.png') == status

    def quick_mode(self):
        boss = Boss(self.driver)
    
        print(f"main_to_single_boss:{datetime.now()}")
        boss.main_to_single_boss()
       
        print("house_to_pettravel")
        HouseJob(self.driver).house_to_pettravel(True)
 
        print("main_to_everyday_fb")
        InstanceZone(self.driver).main_to_everyday_fb()
     
        print("main_to_shenbeast_island")
        InstanceZone(self.driver).main_to_shenbeast_island()

        print("main_to_single_boss")
        boss.main_to_single_boss()

        print("adventure")
        Adventure(self.driver).process_adventure_events()

        print("shen dian boss")
        boss.main_to_shen_dian()

        print("eat elixir")
        Roles(self.driver).main_to_eat_Elixir()

        print("xian yuan")
        Roles(self.driver).main_to_xianyuan_fb()

        print("adventure")
        Adventure(self.driver).process_adventure_events()

        print("xy esports")
        ESports(self.driver).main_to_xy()        

        print("adventrue")
        Adventure(self.driver).process_adventure_events()

        print("get email")
        Teams(self.driver).get_email()

        print("top process")
        TopProcess(self.driver).process_top()

    def quick_daylies_more_times(self, is_adventure=False):
        Roles(self.driver).check_login()
        self.to_main()
        if is_adventure:
            Adventure(self.driver).process_adventure_events()
        ESports(self.driver).main_to_xy()
        InstanceZone(self.driver).main_to_shenbeast_island()

        # three boos
    def monitor_three_boss(self):
        c_times = 0
        while self.is_exit(False) and c_times < 5:            
            c_times = c_times + Boss(self.driver).process_three_realms()

    def monitor_yiyu_boss(self, is_chuan_qi=True):
        pt_times = 0
        while self.is_exit(False):          
            if pt_times >= 9:
                break  

            while self.is_exists_image("yi_yu_boss.png") == False:
                wait_time(15)

            if is_chuan_qi:
                self.click_pos(CQ_POS)
            else:
                self.click_pos(PT_POS)
                pt_times = pt_times + 1            
                        
            c_times = 0 
            while self.is_exists_image("boss_zh.png") == False:
                self.click_pos(CQ_REFRESH)
                wait_time(5)
                c_times = c_times+1
                if self.is_exists_image("chat_box.png", is_save_img=False) or c_times==12:
                    break
            if c_times== 12:
                break

            self.click_pos(CQ_KILL)
            
            c_times = 0 
            while self.is_exists_image("quit_left.png"):
                wait_time(30)
                c_times= c_times +1
                if c_times>5 or self.is_exists_image("chat_box.png", is_save_img=False):
                    break
            pos = self.get_pos_byimg("ok.png", screen_shot=False)
            if pos[0]>0:
                self.click_pos(pos)
    
    def monitor_end(self):
        while self.is_exit(False):            
            wait_time(30)
            if self.is_exists_image("team.png"):
                break
            
            


           
