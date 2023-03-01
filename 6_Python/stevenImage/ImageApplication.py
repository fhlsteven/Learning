# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import askdirectory
import os
import cv2
import numpy as np
from PIL import Image,ImageTk

class Rectangle(object):
    def __init__(self, start_x, start_y):
        self.start_x = start_x 
        self.start_y = start_y
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
    
    def reset(self, x, y):
        self.min_x = min(self.start_x, x)
        self.min_y = min(self.start_y, y)
        self.max_x = max(self.start_x, x)
        self.max_y = max(self.start_y, y)
    
    def width(self):
        return self.max_x- self.min_x
    
    def height(self):
        return self.max_y - self.min_y

    def center(self):
        return int(self.width()/2) + self.min_x, int(self.height()/2)+self.min_y

    def draw(self, img):
        cv2.rectangle(img, (self.min_x, self.min_y), (self.max_x,self.max_y), (0, 255, 0), 1)

    def __str__(self):
        if self.min_x==0 and self.min_y ==0 and self.max_x==0 and self.max_y==0:
            return f'pos({self.start_x},{self.start_y})'
        return f'({self.min_x},{self.min_y},{self.max_x},{self.max_y});w:h({self.width()},{self.height()});center:{self.center()}'

    __repr__ = __str__

class ImageApplication(object):
    def __init__(self, win):
        self.main_win = win
        self.cur_path = StringVar()
        self.cur_path.set(os.path.abspath("."))
        self.image_names = []
        self.clicked = False
        self.g_rectrangles = []
        self.g_start_point = [] 
        self.cur_rectangle = None
        self.cur_img_path=''
        self.cur_img = None
    
    def window_boxes(self):
        self.main_win.title("Images")
        self.main_win.geometry("780x590+550+150")

        Label(self.main_win, text="目标路径:").grid(row=0,column=0)
        Entry(self.main_win, textvariable= self.cur_path, state="readonly").grid(row=0,column=1,ipadx=100)
        Button(self.main_win, text="选择路径", command=self.select_folder_path).grid(row=0,column=2)
        Button(self.main_win, text="全部保存", command=self.save_all_rect_img).grid(row=0,column=3)

        self.lb_image_names = Listbox(self.main_win, height=30, width=50)
        self.lb_image_names.bind("<<ListboxSelect>>",self.show_msg)
        self.lb_image_names.grid(row=1,column=0,columnspan=2)
        
        self.txt_result = Text(self.main_win, height=38, width=53)
        self.txt_result.grid(row=1, column=2,columnspan=2)

        Label(self.main_win, text='按 ESC 退出图像画框模式').grid(row=2,column=0,columnspan=2)

        self.read_all_images_name()

    def read_img(self, path):
        cur_img = cv2.imread(path)
        if cur_img is None:
            cur_img = cv2.imdecode(np.fromfile(path, dtype=np.uint8),-1)
        return cur_img   

    def process_img_file(self, index=0):
        if len(self.image_names)<=0:
            return
               
        img_path = os.path.join(self.cur_path.get(), self.image_names[index])
        if self.cur_img_path != img_path:
            self.cur_img = None
            self.g_rectrangles.clear()
            self.txt_result.delete('1.0','end') 
            
        self.cur_img = self.read_img(img_path)     
        if self.cur_img is not None:
            self.cur_img_path = img_path
            cv2.namedWindow(img_path, 0)
            cv2.resizeWindow(img_path, self.cur_img.shape[1], self.cur_img.shape[0])  # 设置长和宽
            cv2.setMouseCallback(img_path, self.on_mouse)
            self.show_img(img_path)

    def show_img(self, path):
        while cv2.waitKey(30) != 27:  
            img_4_show = self.cur_img.copy()          
            if len(self.g_rectrangles)>0:
                for rect in self.g_rectrangles:
                    rect.draw(img_4_show)
            if self.cur_rectangle is not None:
                self.cur_rectangle.draw(img_4_show)
            cv2.imshow(path, img_4_show)
        
        cv2.destroyWindow(path) 
        self.show_result()       

    def select_folder_path(self):
        get_path = askdirectory() #使用askdirectory()方法返回文件夹的路径        
        if get_path == "":            
            pass#self.cur_path.get() # #当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
        else:
            get_path = get_path.replace("/","\\") # 实际在代码中执行的路径为“\“ 所以替换一下            
            self.cur_path.set(get_path)
        self.read_all_images_name()

    def read_all_images_name(self):
        self.image_names.clear()
        self.lb_image_names.delete(0,END)
        for file_name in os.listdir(self.cur_path.get()):
            file_exten = os.path.splitext(file_name)[-1]
            if  file_exten != '' and file_exten in ".png,.jpg,.gif":
                self.image_names.append(file_name)
        if len(self.image_names)>0:
            for i,item in enumerate(self.image_names):                
                self.lb_image_names.insert(i, item)
                if not i%2:
                    self.lb_image_names.itemconfig(i,bg="#f0f0ff")

    def on_mouse(self, event, x, y,flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            if self.clicked:
                self.cur_rectangle.reset(x, y)

        if event == cv2.EVENT_LBUTTONDOWN:
            self.clicked = True
            self.cur_rectangle = Rectangle(x, y)
        
        if event == cv2.EVENT_LBUTTONUP:
            self.clicked = False
            self.g_rectrangles.append(self.cur_rectangle)
            self.cur_rectangle = None

    def show_result(self):
        if len(self.g_rectrangles)<=0:
            return
        for rect in self.g_rectrangles:
            self.txt_result.insert(END, str(rect)+'\n')
        '''
        # 测试显示截图图片
        rect = self.g_rectrangles[0]

        cur_image = Image.open(self.cur_img_path)
        crop = cur_image.crop((rect.min_x,rect.min_y, rect.max_x, rect.max_y))

        first_img = ImageTk.PhotoImage(crop)
        curimg_lb=Label(self.main_win, image=first_img)
        curimg_lb.image = first_img
        curimg_lb.grid(row=3,column=0,columnspan=3)
        '''
    def save_all_rect_img(self):
        if len(self.g_rectrangles)<=0:
            return        
        cur_image = Image.open(self.cur_img_path)
        for i,rect in enumerate(self.g_rectrangles):
            crop = cur_image.crop((rect.min_x,rect.min_y, rect.max_x, rect.max_y))
            crop.save(str(i)+".png")
    
    def show_msg(self, *args):
        indexs = self.lb_image_names.curselection()
        if len(indexs) > 0:
            index = int(indexs[0])
            self.process_img_file(index)
        
def image_exe():
    # 调用Tk()创建主窗口
    window = Tk()
    app = ImageApplication(window)
    app.window_boxes()
    #开启主循环，让窗口处于显示状态
    window.mainloop()

if __name__ == "__main__":
    image_exe()