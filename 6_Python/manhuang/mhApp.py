# -*- coding: utf-8 -*-

from tkinter import *
import time
from testSel import get_driver, login
import socket
import traceback

from housejobs import HouseJob, get_date_minutes
from bosses import Boss
from instancezones import InstanceZone
from topprocess import TopProcess
from teams import Teams
from DailyActivities import DailyActivities,is_between
from common import clear_kill_go,is_exists_image, wait_time,callback_click
from roles import Roles
from adventure import Adventure
from monitor import Monitors
from configs import configs
from datetime import datetime
from esports import ESports

LOG_LINE_NUM = 0

def send_msg(msg='gamewin'):
    try:
        s = socket.socket()
        s.connect(('192.168.200.205',13148))
        s.send(msg.encode('ascii'))
        time.sleep(3)
        s.close()
    except Exception as e:
        print(e)

class MHApplication(object):
    def __init__(self, window, driver):
        self.main_win = window
        self.driver = driver
        self.msg_sock = None
        self.is_done_quick_mode = False
    
    def window_box(self):
        column_num = 6
        row_start = 0 
        # 标题 和 标签
        self.main_win.title("man:"+configs.login.cur_index)
        self.main_win.geometry("605x590+550+150")

        cur_column = 0
        Label(self.main_win, text="common tools", fg='green', font=('宋体',16)).grid(row=row_start,column=cur_column) 
        cur_column =cur_column + 1
        Label(self.main_win, text="one long time(hour)", fg='red').grid(row=row_start,column=cur_column)
        cur_column =cur_column + 1
        self.txt_one_long = Text(self.main_win, width=10, height=1)
        self.txt_one_long.insert('0.0', '1')
        self.txt_one_long.grid(row=row_start,column=cur_column) 

        row_start = row_start + 1
        cur_column = 0
        Button(self.main_win, text='rechange pets', command=self.rechallenge_pets, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text='one long server', command=self.one_long_service, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text='screen img', command=self.screen_img, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text='smelt bag', command=self.smelt_bag, width=20).grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        cur_column = 0        
        Label(self.main_win, text="tools", fg='green', font=('宋体',16)).grid(row=row_start, column=cur_column) 

        row_start = row_start + 1
        cur_column = 0
        Button(self.main_win, text='login', command=self.login, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text='rechange loop', command=self.rechallenge, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text='single boss', command=self.single_boss, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text='instance zone(fb)', command=self.instance_zone_fb, width=20).grid(row=row_start, column=cur_column)
        
        row_start = row_start + 1
        cur_column = 0 
        self.btn_boss_fb = Button(self.main_win, text='boss & fb', command=self.boss_and_fb, width=20)
        self.btn_boss_fb.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_boss_three_realm = Button(self.main_win, text='boss three realm', command=self.boss_three_realm, width=20)
        self.btn_boss_three_realm.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_use_bags = Button(self.main_win, text='use bags', command=self.use_bags, width=20)
        self.btn_use_bags.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_get_email = Button(self.main_win, text='get email', command=self.get_email, width=20)
        self.btn_get_email.grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        cur_column = 0 
        self.btn_kick_out = Button(self.main_win, text='kick out', command=self.kick_out_team, width=20)
        self.btn_kick_out.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_hd_process = Button(self.main_win, text='hd  process', command=self.hd_process_click, width=20)
        self.btn_hd_process.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_island = Button(self.main_win, text='island kill', command=self.island_kill_click, width=20)
        self.btn_island.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_go_youm = Button(self.main_win, text='go youming', command=self.go_youm_click, width=20)
        self.btn_go_youm.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1

        row_start = row_start + 1
        cur_column = 0 
        Button(self.main_win, text='daily boss kill', command=self.day_boss_kills, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text='clear kill go', command=self.clear_kill_go_click, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text="adventrure", command=self.process_adventure_click, width=20).grid(row=row_start, column=cur_column)
        cur_column = cur_column+1
        Button(self.main_win, text="esports kill", command=self.esports_kill_click,width=20).grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        cur_column = 0 
        Button(self.main_win, text="shen dian boss", command=self.shen_dian_boss_click,width=20).grid(row=row_start, column=cur_column)
        cur_column = cur_column+1
        Button(self.main_win, text="xian yuan fb", command=self.xina_yuan_fb_click,width=20).grid(row=row_start, column=cur_column)
        cur_column = cur_column+1
        Button(self.main_win, text="hd mid", command=self.m_id_hd_click,width=20).grid(row=row_start, column=cur_column)
        cur_column = cur_column+1
        Button(self.main_win, text="xian yuan esport", command=self.xy_esports_click,width=20).grid(row=row_start, column=cur_column)

        row_start =row_start+1
        cur_column = 0
        Button(self.main_win, text="protect", command=self.xv_protect_click).grid(row=row_start, column=cur_column)
        
        row_start = row_start + 1
        cur_column = 0        
        self.lb_house_tools = Label(self.main_win, text="house tools", fg='green', font=('宋体',16))
        self.lb_house_tools.grid(row=row_start, column=cur_column) 
        row_start = row_start + 1
        cur_column = 0         
        self.btn_pets_travel = Button(self.main_win, text='pets travel', command=self.pets_travel, width=20)
        self.btn_pets_travel.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_house_event = Button(self.main_win, text='house event', command=self.house_event_p, width=20)
        self.btn_house_event.grid(row=row_start, column=cur_column) 
        cur_column =cur_column + 1
        self.btn_pets_travels_all = Button(self.main_win, text='pets travels all', command=self.pets_travels_all_click, width=20)
        self.btn_pets_travels_all.grid(row=row_start, column=cur_column) 

        row_start = row_start + 1
        cur_column = 0        
        self.lb_top_tools = Label(self.main_win, text="top tools", fg='green', font=('宋体',16))
        self.lb_top_tools.grid(row=row_start, column=cur_column) 

        row_start = row_start + 1
        cur_column = 0
        self.btn_top_all = Button(self.main_win, text='top all', command=self.top_all, width=20)
        self.btn_top_all.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_welfare = Button(self.main_win, text='welfare', command=self.welfare_click, width=20)
        self.btn_welfare.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_rank = Button(self.main_win, text='rank', command=self.rank_clcik, width=20)
        self.btn_rank.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_find_god = Button(self.main_win, text='find god', command=self.find_god, width=20)
        self.btn_find_god.grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        cur_column = 0
        self.btn_xd_rank = Button(self.main_win, text='xd rank', command=self.xd_rank, width=20)
        self.btn_xd_rank.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_get_yb = Button(self.main_win, text='get yuanbao', command=self.get_yuanbao, width=20)
        self.btn_get_yb.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text="xf shop", command=self.xf_shop_click).grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        self.lb_role = Label(self.main_win, text="role", fg='green', font=('宋体',16))
        self.lb_role.grid(row=row_start, column=0) 

        row_start = row_start + 1
        cur_column = 0
        self.btn_eat_elixir = Button(self.main_win, text='eat Elixir', command=self.eat_elixir_click, width=20)
        self.btn_eat_elixir.grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        Label(self.main_win, text="monitor", fg='green', font=('宋体',16)).grid(row=row_start, column=0)
        
        self.txt_three_times = Text(self.main_win, width=10, height=1)
        self.txt_three_times.insert('0.0', '5')
        self.txt_three_times.grid(row=row_start,column=1) 

        self.txt_pets_times = Text(self.main_win, width=10, height=1)
        self.txt_pets_times.insert('0.0', '13')
        self.txt_pets_times.grid(row=row_start,column=2) 

        row_start = row_start + 1
        cur_column = 0
        self.btn_monitor_msg = Button(self.main_win, text='monitor msg', command=self.monitor_msg_click, width=20)
        self.btn_monitor_msg.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_monitor_fb = Button(self.main_win, text='monitor fb', command=self.monitor_fb_click, width=20)
        self.btn_monitor_fb.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_monitor_huod = Button(self.main_win, text='monitor huod', command=self.monitor_huod_click, width=20)
        self.btn_monitor_huod.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_monitor_three_real = Button(self.main_win, text='monitor three real', command=self.btn_monitor_three_real, width=20)
        self.btn_monitor_three_real.grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        cur_column = 0
        self.btn_monitor_three_and_pets = Button(self.main_win, text='monitor three and pets', command=self.monitor_three_and_pets_click, width=20)
        self.btn_monitor_three_and_pets.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text="monitor end", command=self.monitor_end_click).grid(row=row_start,column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text="monitor cqzh boss", command=self.monitor_cqzh_boss_click).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text="monitor ptzh boss", command=self.monitor_ptzh_boss_click).grid(row=row_start, column=cur_column)
        row_start = row_start + 1
        cur_column =0
        self.txt_log = Text(self.main_win, height=10)
        self.txt_log.grid(row=row_start, column=cur_column, columnspan=column_num)

    def xf_shop_click(self):
        TopProcess(self.driver).main_to_xf_shop()
        send_msg()

    def monitor_ptzh_boss_click(self):
        Monitors(self.driver).monitor_yiyu_boss(False)
        send_msg()
    
    def monitor_cqzh_boss_click(self):
        Monitors(self.driver).monitor_yiyu_boss()

    def monitor_end_click(self):
        Monitors(self.driver).monitor_end()
        send_msg()

    def xv_protect_click(self):
        DailyActivities(self.driver).protect(True)
        send_msg()

    def xy_esports_click(self):
        ESports(self.driver).main_to_xy()
        send_msg()

    def m_id_hd_click(self):
        DailyActivities(self.driver).monitor_mid()
        send_msg()

    def shen_dian_boss_click(self):
        Boss(self.driver).main_to_shen_dian()
        send_msg()

    def xina_yuan_fb_click(self):
        Roles(self.driver).main_to_xianyuan_fb()
        send_msg()

    def esports_kill_click(self):
        ESports(self.driver).kill_single()

    def process_adventure_click(self):
        Adventure(self.driver).process_adventure_events()
        send_msg()

    def pets_travels_all_click(self):
        self.log_show("pets_travels_all_click")
        HouseJob(self.driver).process_pets_travels()
        send_msg()

    def monitor_three_and_pets_click(self):
        pets_times = int(self.txt_pets_times .get("1.0","end"))
        three_times = int(self.txt_three_times .get("1.0","end"))
        times = 0
        c_times = 0
        pre_time = datetime(2015, 4, 7, 4, 30, 3, 628556) 
        r_pre_time = pre_time 
        while is_exists_image(self.driver, "chat_box.png") == False:  
            try: 
                if get_date_minutes(pre_time, datetime.now()) > 5 and times < pets_times: 
                    HouseJob(self.driver).house_to_pettravel(times%5==0)
                    pre_time = datetime.now()
                    times = times +1  
                
                if get_date_minutes(r_pre_time, datetime.now()) > 20:
                    Boss(self.driver).rong_lian()
                    r_pre_time = datetime.now()
                
                if c_times < three_times:
                    c_times = c_times + Boss(self.driver).process_three_realms()

                _now = datetime.now()
                if _now.day in(5,6) and _now.hour == 11:
                    DailyActivities(self.driver).monitor_mid()
                elif _now.hour == 16:
                    DailyActivities(self.driver).protect()
                
                _now = datetime.now()
                if _now.hour>=18 and _now.hour<22:
                    Roles(self.driver).check_login()
                    print(f'monitor_hd:{_now}')
                    if get_date_minutes(r_pre_time, datetime.now()) > 20:
                        Boss(self.driver).rong_lian()
                    Monitors(self.driver).monitor_hd()
                
                if _now.hour == 2 and self.is_done_quick_mode:
                    self.is_done_quick_mode = False
                    Roles(self.dirver).check_login()
                    Monitors(self.driver).quick_daylies_more_times(False)                   
                    Boss(self.driver).rong_lian()
                    Teams(self.driver).get_email()

                if is_between((5,1), (9,1)) and self.is_done_quick_mode == False:
                    times = 13
                    c_times = 5
                    Roles(self.driver).check_login()
                    wait_time(configs.wait_min_morning * 60)                   
                    Monitors(self.driver).quick_mode()
                    if _now.day in(5,6):                        
                        Teams(self.driver).auto_receive()
                    self.is_done_quick_mode = True

            except Exception as ex:
                print(datetime.now(),ex)
                traceback.print_exc()
                wait_time()
            wait_time(3)

    def go_youm_click(self):
        InstanceZone(self.driver).go_you_ming()
        send_msg()
    
    def btn_monitor_three_real(self):
        Monitors(self.driver).monitor_three_boss()
        # Monitors(self.driver).quick_mode()

    def monitor_huod_click(self):
        Monitors(self.driver).monitor_hd()

    def eat_elixir_click(self):
        Roles(self.driver).main_to_eat_Elixir()
    
    def monitor_fb_click(self):
        Monitors(self.driver).monitor_fb()

    def monitor_msg_click(self):
        Monitors(self.driver).monitor_msg()

    def island_kill_click(self):
        InstanceZone(self.driver).main_to_shenbeast_island()

    def hd_process_click(self):
        DailyActivities(self.driver).hd_process()

    def kick_out_team(self):
        Teams(self.driver).kick_out()

    def one_long_service(self):
        Monitors(self.driver).quick_mode()
        send_msg()
    
    def clear_kill_go_click(self):
        clear_kill_go(self.driver)

    def day_boss_kills(self):
        DailyActivities(self.driver).main_to_daily_boss_gets()
        send_msg()

    def get_email(self):
        Teams(self.driver).get_email()

    def get_yuanbao(self):
        TopProcess(self.driver).get_yb()

    def xd_rank(self):
        TopProcess(self.driver).xd_rank()

    def house_event_p(self):
        HouseJob(self.driver).house_random_event()
        send_msg()

    def boss_three_realm(self):
        Boss(self.driver).main_to_three_realms()
        send_msg()

    def top_all(self):
        TopProcess(self.driver).process_top()
        send_msg()

    def find_god(self):
        TopProcess(self.driver).find_treasure()

    def use_bags(self):
        Boss(self.driver).use_bags()

    def boss_and_fb(self):
        Boss(self.driver).main_to_single_boss()
        InstanceZone(self.driver).main_to_everyday_fb()
        send_msg()

    def rank_clcik(self):
        TopProcess(self.driver).get_rank()

    def welfare_click(self):
        TopProcess(self.driver).get_welfare()

    def pets_travel(self):
        self.log_show('pets_travel ...')
        try:
            HouseJob(self.driver).house_to_pettravel(True)
        except Exception as e:
            self.log_show(e)
        send_msg()

    def screen_img(self):
        f_name = 'temp/'+str(self.get_time()).replace(':', '-')+'.png'
        self.driver.save_screenshot(f_name)

    def smelt_bag(self):
        Boss(self.driver).rong_lian()
        Boss(self.driver).use_bags()

    def rechallenge_pets(self):
        self.log_show('rechallenge_pets')
        HouseJob(self.driver).rechallenge_pets()       

    def single_boss(self):
        self.log_show('single_boss ...')
        Boss(self.driver).main_to_single_boss()
        send_msg()        

    def instance_zone_fb(self):
        self.log_show('instance_zone_fb ...')
        InstanceZone(self.driver).main_to_everyday_fb()
        send_msg()

    def login(self):
        self.log_show('login')
        login(self.driver, False)

    def rechallenge(self):
        self.log_show('rechallenge loop')
        HouseJob(self.driver).rechallenge_loop()

    def get_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time
    
    def log_show(self, log_msg):
        global LOG_LINE_NUM
        current_time = self.get_time()
        logmessage_in = str(current_time) +" " + str(log_msg) + "\n"      #换行
        if LOG_LINE_NUM <= 10:
            self.txt_log.insert(END, logmessage_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.txt_log.delete(1.0, 2.0)
            self.txt_log.insert(END, logmessage_in)

def mh_gui():
    # 调用Tk()创建主窗口
    window =  Tk()
    driver = get_driver(configs.login.url)   
    app = MHApplication(window, driver)
    app.window_box()
    window.mainloop()

if __name__ == '__main__':
    mh_gui()