# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import askdirectory
import os

class ImageApplication(object):
    def __init__(self, win):
        self.main_win = win
        self.cur_path = StringVar()
        self.cur_path.set(os.path.abspath("."))
        self.image_names = []
    
    def window_boxes(self):
        self.main_win.title("Images")
        self.main_win.geometry("605x590+550+150")

        Label(self.main_win, text="目标路径:").grid(row=0,column=0)
        Entry(self.main_win, textvariable= self.cur_path, state="readonly").grid(row=0,column=1,ipadx=100)
        Button(self.main_win, text="选择路径", command=self.select_folder_path).grid(row=0,column=2)

        self.lb_image_names = Listbox(self.main_win,height=30, width=50)
        self.lb_image_names.bind("<<ListboxSelect>>",self.show_msg)
        self.lb_image_names.grid(row=1,column=0,columnspan=2)

        self.read_all_images_name()

    def select_folder_path(self):
        get_path = askdirectory() #使用askdirectory()方法返回文件夹的路径
        
        if get_path == "":
            pass#self.cur_path.get() # #当打开文件路径选择框后点击"取消" 输入框会清空路径，所以使用get()方法再获取一次路径
        else:
            get_path = get_path.replace("/","\\") # 实际在代码中执行的路径为“\“ 所以替换一下            
            self.cur_path.set(get_path)
            self.read_all_images_name()

    def read_all_images_name(self):
        for i, j, k in os.walk(self.cur_path.get()):
            for file_name in k:
                if os.path.splitext(file_name)[-1] in ".png,.jpg,.gif":
                    self.image_names.append(file_name)
        if len(self.image_names)>0:
            for i,item in enumerate(self.image_names):                
                self.lb_image_names.insert(i, item)
                if not i%2:
                    self.lb_image_names.itemconfig(i,bg="#f0f0ff")


    def show_msg(self, *args):
        indexs = self.lb_image_names.curselection()
        index = int(indexs[0])
        print(self.image_names[index])
        #self.lb_image_names.see(index)
        #self.lb_image_names.select_set(index)
    
def image_exe():
    # 调用Tk()创建主窗口
    window = Tk()
    app = ImageApplication(window)
    app.window_boxes()
    #开启主循环，让窗口处于显示状态
    window.mainloop()

if __name__ == "__main__":
    image_exe()