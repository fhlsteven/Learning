# -*- coding: utf-8 -*-
from common import Base
from socket import socket

YUAN_SHEN = ['烁金','玄苍','幻海','炽天','昆墟']
BA_GUA = ['玄龟','惊雷','白泽','炎凰','苍龙']
YI_BAO = ['仙器','灵宠','神刃','仙羽','装袍','珠纹']

class Monitors(Base):
    def __init__(self, driver):
        super(Monitors, self).__init__(driver)
        self.pre_msg = ""
        self.socket = None
    
    def get_socket(self):
        if self.socket == None:
            self.socket = socket()
            self.socket.connect(('192.168.200.205',13148))

    def monitor_msg(self):
        self.driver


    def monitor_yuan_shen(self, special= -1):          
        pass

    def monitor_ba_gua(self):
        pass

    def monitor_yi_bao(self):
        pass