# -*- coding: utf-8 -*-

from tkinter import *
import time
from testSel import get_driver, login

from housejobs import HouseJob

LOG_LINE_NUM = 0

class MHApplication(object):
    def __init__(self, window, driver):
        self.main_win = window
        self.driver = driver
    
    def window_box(self):
        column_num = 6
        row_start = 0 
        # 标题 和 标签
        self.main_win.title("man")
        self.main_win.geometry("605x590+550+150")

        cur_column = 0
        self.lb_common_tools = Label(self.main_win, text="common tools", fg='green', font=('宋体',16))
        self.lb_common_tools.grid(row=row_start,column=cur_column) 

        row_start = row_start + 1
        cur_column = 0
        self.btn_rechallenge_pets = Button(self.main_win, text='rechange pets', command=self.rechallenge_pets, width=20)
        self.btn_rechallenge_pets.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_hd_monitor = Button(self.main_win, text='daily activites monitor', command=self.hd_monitor, width=20)
        self.btn_hd_monitor.grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        cur_column = 0        
        self.lb_tools = Label(self.main_win, text="tools", fg='green', font=('宋体',16))
        self.lb_tools.grid(row=row_start, column=cur_column) 

        row_start = row_start + 1
        cur_column = 0
        self.btn_login = Button(self.main_win, text='login', command=self.login, width=20)
        self.btn_login.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_rechallenge = Button(self.main_win, text='rechange', command=self.rechallenge, width=20)
        self.btn_rechallenge.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.btn_single_boss = Button(self.main_win, text='single boss', command=self.single_boss, width=20)
        self.btn_single_boss.grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        cur_column =0
        self.txt_log = Text(self.main_win, height=10)
        self.txt_log.grid(row=row_start, column=cur_column, columnspan=column_num)
    
    def rechallenge_pets(self):
        self.log_show('rechallenge_pets')
        HouseJob(self.driver).house_to_pettravel()        

    def single_boss(self):
        self.log_show('single bosss')

    def login(self):
        self.log_show('login')
        login(self.driver)

    def hd_monitor(self):
        self.log_show('hd monitor')

    def rechallenge(self):
        self.log_show('rechallenge')

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
    login(driver)
    app = MHApplication(window, driver)
    app.window_box()
    window.mainloop()

if __name__ == '__main__':
    mh_gui()