# -*- coding: utf-8 -*-

from common import wait_time, quit_scene, Base
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

class HouseJob(Base):
    def __init__(self, dr):
        super(HouseJob, self).__init__(dr)

    def get_money_reiki(self):
        self.click_pos(MONEY_POS)
        wait_time(4)
        self.click_pos(GET_MONEY_REIKI_POS)
        wait_time(1)
        self.click_pos(REIKI_POS)
        wait_time(4)
        self.click_pos(GET_MONEY_REIKI_POS)

    def house_random_event(self):
        self.click_pos(HOUSE_POS)
        wait_time(4)
        
        self.click_pos(HOUSE_CLICK)
        wait_time(25)
        
        # change
        self.click_pos(HOUSE_SEC)
        self.click_pos(HOUSE_CLICK)
        wait_time(25)
        
        #change
        self.click_pos(HOUSE_THREE)
        self.click_pos(HOUSE_CLICK)
        wait_time(25)
  
    def house_to_pettravel(self):
        self.click_pos(HOUSE_POS)
        wait_time(3)    
        self.get_money_reiki()
        self.click_pos(HOUSE_THREE)
        wait_time(2)    
        self.pet_travel() 

    def pet_travel(self):
        times = 0
        while times < 4:
            if times == 3:
                self.use_bags()        
            self.click_pos((PET1[0]+times*STEP_INTERVAL, PET1[1]))
            self.click_pos(GET_GOODS)
            self.click_pos((PET1[0]+times*STEP_INTERVAL, PET1[1]))
            self.click_pos(START_TRAVEL)
            times = times+1
        self.use_bags()
        quit_scene(self.driver) 
    
    def rechallenge_loop(self):        
        while self.is_exists_image("chat_box.png") == False:
            self.click_pos(CHALLENGE_POS)
            wait_time()
            while self.is_exists_image("guan_ka.png", 0.7) == False:
                wait_time(20)

    def rechallenge_pets(self):
        times=0
        pre_time = datetime(2015, 4, 7, 4, 30, 3, 628556) 
        while times < PET_TRAVEL_TIMES:   
            if get_date_minutes(pre_time, datetime.now()) > 11:     
                pre_time = datetime.now()
                self.house_to_pettravel()
                times = times +1            
            wait_time(3)
            self.click_pos(CHALLENGE_POS)
            wait_time(60)