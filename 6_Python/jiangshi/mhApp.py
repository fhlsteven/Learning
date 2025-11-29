# -*- coding: utf-8 -*-

from tkinter import *
import time
from testSel import get_driver
import socket
import traceback

from common import is_exists_image, wait_time

from configs import configs
from datetime import datetime
from play_normal import PlayNormal

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
        Button(self.main_win, text='paly normal', command=self.palynormal, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.point_x_entry = Text(self.main_win, width=10, height=1)
        self.point_x_entry.insert('0.0', '1')
        self.point_x_entry.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        self.point_y_entry = Text(self.main_win, width=10, height=1)
        self.point_y_entry.insert('0.0', '1')
        self.point_y_entry.grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text='click point', command=self.click_point, width=20).grid(row=row_start, column=cur_column)

        row_start = row_start + 1
        cur_column = 0        
        Label(self.main_win, text="tools", fg='green', font=('宋体',16)).grid(row=row_start, column=cur_column) 

        row_start = row_start + 1
        cur_column = 0
        Button(self.main_win, text='reset point', command=self.reset_point, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        Button(self.main_win, text='screen img', command=self.screen_img, width=20).grid(row=row_start, column=cur_column)
        cur_column =cur_column + 1
        
        row_start = row_start + 1
        cur_column =0
        self.txt_log = Text(self.main_win, height=10)
        self.txt_log.grid(row=row_start, column=cur_column, columnspan=column_num)

    def palynormal(self):
        while True:
            PlayNormal(self.driver).playNormal()
            wait_time(2)
    
    def click_point(self):
        try:
            x = int(self.point_x_entry.get("1.0","end"))
            y = int(self.point_y_entry.get("1.0","end"))
            print(f'click point:{x},{y}')
            PlayNormal(self.driver).test_click_pos(x,y)
        except Exception as e:
            print(e)
    
    def reset_point(self):
        PlayNormal(self.driver).test_click_pos(0,0)

    def screen_img(self):
        f_name = 'temp/'+str(self.get_time()).replace(':', '-')+'.png'
        self.driver.save_screenshot(f_name)
   
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
    print(configs.login.url)
    window =  Tk()
    driver = get_driver(configs.login.url)   
    app = MHApplication(window, driver)
    app.window_box()
    window.mainloop()

if __name__ == '__main__':
    mh_gui()