# -*- coding: utf-8 -*-

from tkinter import *
import time
from testSel import get_driver, login
import socket

from housejobs import HouseJob
from bosses import Boss
from instancezones import InstanceZone
from topprocess import TopProcess
from teams import Teams
from DailyActivities import DailyActivities
from common import clear_kill_go

LOG_LINE_NUM = 0

def send_msg(msg='gamewin'):
    s = socket.socket()
    s.connect(('192.168.200.205',13148))
    s.send(msg.encode('ascii'))
    time.sleep(3)
    s.close()

class MHApplication(object):
    def __init__(self, window, driver):
        self.main_win = window
        self.driver = driver
        self.msg_sock = None
    
    def window_box(self):
        column_num = 6
        row_start = 0 
        # 标题 和 标签
        self.main_win.title("man")
        self.main_win.geometry("605x590+550+150")

        cur_column = 0
        self.lb_common_tools = Label(self.main_win, text="common tools", fg='green', font=('宋体',16))
        self.lb_common_tools.grid(row=row_start,column=cur_column) 
        cur_column =cur_column + 1
        self.lb_one_long = Label(self.main_win, text="one long time(hour)", fg='red')
        self.lb_one_long.grid(row=row_start,column=cur_column)
        cur_column =cur_column + 1
        self.txt_one_long = Text(self.main_win, width=10, height=1)
        self.txt_one_long.grid(row=row_start,column=cur_column) 

        row_start = row_start + 1
        cur_column = 0
        self.btn_rechallenge_pets = Button(self.main_win, text='rechange pets', command=self.rechallenge_pets, width=20)
        self.btn_rechallenge_pets.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_hd_monitor = Button(self.main_win, text='one long server', command=self.one_long_service, width=20)
        self.btn_hd_monitor.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_screen_img = Button(self.main_win, text='screen img', command=self.screen_img, width=20)
        self.btn_screen_img.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_smelt_bag = Button(self.main_win, text='smelt bag', command=self.smelt_bag, width=20)
        self.btn_smelt_bag.grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        cur_column = 0        
        self.lb_tools = Label(self.main_win, text="tools", fg='green', font=('宋体',16))
        self.lb_tools.grid(row=row_start, column=cur_column) 

        row_start = row_start + 1
        cur_column = 0
        self.btn_login = Button(self.main_win, text='login', command=self.login, width=20)
        self.btn_login.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_rechallenge = Button(self.main_win, text='rechange loop', command=self.rechallenge, width=20)
        self.btn_rechallenge.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_single_boss = Button(self.main_win, text='single boss', command=self.single_boss, width=20)
        self.btn_single_boss.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_instance_zone = Button(self.main_win, text='instance zone(fb)', command=self.instance_zone_fb, width=20)
        self.btn_instance_zone.grid(row=row_start, column=cur_column)
        
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

        row_start = row_start + 1
        cur_column = 0 
        self.btn_day_boss_kill = Button(self.main_win, text='daily boss kill', command=self.day_boss_kills, width=20)
        self.btn_day_boss_kill.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_clear_kill_go = Button(self.main_win, text='clear kill go', command=self.clear_kill_go_click, width=20)
        self.btn_clear_kill_go.grid(row=row_start, column=cur_column)
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

        row_start = row_start + 1
        cur_column =0
        self.txt_log = Text(self.main_win, height=10)
        self.txt_log.grid(row=row_start, column=cur_column, columnspan=column_num)

    def island_kill_click(self):
        InstanceZone(self.driver).main_to_shenbeast_island()

    def hd_process_click(self):
        DailyActivities(self.driver).hd_process()

    def kick_out_team(self):
        Teams(self.driver).kick_out()

    def one_long_service(self):
        duration = int(self.txt_one_long.get("1.0","end"))
        self.log_show(duration)
    
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
        TopProcess(driver).process_top()
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
            HouseJob(self.driver).house_to_pettravel()
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
        HouseJob(self.driver).house_to_pettravel()        

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
        login(self.driver)

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
    window =  Tk()
    driver = get_driver("https://h5game.gowan8.com/?yisdk_param=mZpuX9Lm2M_S&ext_param=ZJ1raKOp")   
    app = MHApplication(window, driver)
    app.window_box()
    window.mainloop()

if __name__ == '__main__':
    mh_gui()