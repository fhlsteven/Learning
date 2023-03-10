import cv2
import numpy as np
import colorlist_config
import time
 
filename='F:\\Python\\code\\0.png'
 
#处理图片
def get_color(frame):
    print('go in get_color')
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    color_dict = colorlist_config.getColorList()
    mask = cv2.inRange(hsv, color_dict['red'][0], color_dict['red'][1])
    #cv2.imshow('Mask', mask)

    cv2.imwrite('red.png', mask)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    #cv2.imshow('Result', res)   
    
    #cv2.waitKey(0)
 
 
if __name__ == '__main__':
    frame = cv2.imread(filename)
    #cv2.imshow('test', frame)
    get_color(frame)