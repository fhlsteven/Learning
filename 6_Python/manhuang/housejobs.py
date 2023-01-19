# -*- coding: utf-8 -*-

from common import clcik_pos_locxy,wait_time,get_goods,quit_scene
from datetime import datetime

CHALLENGE_POS = (59, 796)

HOUSE_POS = (448, 900)
HOUSE_CLICK =(253, 639)
HOUSE_SEC = (76, 625)
HOUSE_THREE = (74, 665)

PET1 = (120, 750)
STEP_INTERVAL= 90
START_TRAVEL =(255, 760)
GET_GOODS = (257, 673)

PET_TRAVEL_TIMES = 12

MONEY_POS = (193, 752)
REIKI_POS = (322, 752)
GET_MONEY_REIKI_POS = (257, 637)

def get_date_minutes(start, end):
    return int((end-start).seconds /60) 

class HouseJob(object):
    def __init__(self, dr):
        self.driver = dr

    def get_money_reiki(self):
        clcik_pos_locxy(self.driver, MONEY_POS)
        wait_time(4)
        clcik_pos_locxy(self.driver, GET_MONEY_REIKI_POS)
        wait_time(1)
        clcik_pos_locxy(self.driver, REIKI_POS)
        wait_time(4)
        clcik_pos_locxy(self.driver, GET_MONEY_REIKI_POS)

    def house_random_event(self):
        clcik_pos_locxy(self.driver, HOUSE_POS)
        wait_time(5)
        
        clcik_pos_locxy(self.driver, HOUSE_CLICK)
        wait_time(25)
        
        # change
        clcik_pos_locxy(self.driver, HOUSE_SEC)
        clcik_pos_locxy(self.driver, HOUSE_CLICK)
        wait_time(25)
        
        #change
        clcik_pos_locxy(self.driver, HOUSE_THREE)
        clcik_pos_locxy(self.driver, HOUSE_CLICK)
        wait_time(25)
  
    def house_to_pettravel(self):
        clcik_pos_locxy(self.driver, HOUSE_POS)
        wait_time(5)    
        self.get_money_reiki()
        clcik_pos_locxy(self.driver, HOUSE_THREE)
        wait_time(5)    
        self.pet_travel() 

    def pet_travel(self):
        times = 0
        while times < 4:
            if times == 3:
                get_goods(self.driver)        
            clcik_pos_locxy(self.driver, (PET1[0]+times*STEP_INTERVAL, PET1[1]))
            wait_time(1)
            clcik_pos_locxy(self.driver, GET_GOODS)
            wait_time(1)
            clcik_pos_locxy(self.driver, (PET1[0]+times*STEP_INTERVAL, PET1[1]))
            wait_time(1)
            clcik_pos_locxy(self.driver, START_TRAVEL)
            wait_time(1)
            times = times+1
        quit_scene(self.driver) 

    def rechallenge_pets(self):
        times=0
        pre_time = datetime(2015, 4, 7, 4, 30, 3, 628556) 
        while True:   
            if times < PET_TRAVEL_TIMES and get_date_minutes(pre_time, datetime.now()) > 11:            
                wait_time(60)
                pre_time = datetime.now()
                self.house_to_pettravel()
                times = times +1
            clcik_pos_locxy(self.driver, CHALLENGE_POS)
            wait_time()