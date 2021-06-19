#删除换行或者空格
from tkinter import *
from tkinter import scrolledtext
import os

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #self.title="Gitcommit tool for BookxNote"
        self.pack()
        self.createWidgets()

    def deln(self,event=None):
        #删除换行
        old_msg=self.msg.get(1.0,END)
        # print(old_msg)
        new_msg=old_msg.replace('\r','').replace("\n",'')
        self.msg.delete(1.0,END)
        self.msg.insert(INSERT,new_msg)
        self.clipboard_clear()
        self.clipboard_append(new_msg)

    def delspace(self,event=None):
        #删除空格
        # print(old_msg)
        old_msg=self.msg.get(1.0,END)
        new_msg=old_msg.replace(' ','')
        self.msg.delete(1.0,END)
        self.msg.insert(INSERT,new_msg)
        self.clipboard_clear()
        self.clipboard_append(new_msg)

    def alldel(self,event=None):
        self.deln()
        self.delspace()

    def myquit(self,event=None):
        #退出
        self.quit()

    def refresh(self,event=None):
        #refresh the clipboard
        self.msg.delete(1.0,END)
        try:
            self.msg.insert(1.0,self.clipboard_get())
        except:
            pass

    def formatting(self,event=None):
        #format the text
        old_msg=self.msg.get(1.0,END)
        pair_dict={
            "。":".",
            "，":",",
            "‘":"\'",
            "’":"\'",
            "“":"\"",
            "”":"\"",
            "：":":",
            "；":";",
            "、":",",
            "（":"(",
            "）":")"
        }
        for key,value in pair_dict.items():
            old_msg=old_msg.replace(key,value)
        new_msg=old_msg
        self.msg.delete(1.0,END)
        self.msg.insert(INSERT,new_msg)
        self.clipboard_clear()
        self.clipboard_append(new_msg)




    def createWidgets(self):
        self.msg=scrolledtext.ScrolledText(self, width=40, height=10)
        self.msg["font"]=('monospace','14','bold')
        try:
            self.msg.insert(1.0,self.clipboard_get())
        except:
            pass
        # self.msg.pack({"side": "left"})
        self.msg.grid(row=0,column=0,columnspan=5)
        self.msg.focus_set()
        self.msg.bind("<Return>",self.deln)
        self.msg.bind("<Escape>",self.myquit)
        self.msg.bind("<Alt_R>",self.refresh)


        self.QUIT = Button(self)
        self.QUIT["text"] = "退出程序"
        self.QUIT["command"] =  self.quit
        # self.QUIT.pack({"side": "bottom"})
        self.QUIT.grid(row=1,column=4,sticky=E+W)

        self.button2=Button(self)
        self.button2['text']='删除空格'
        self.button2['command']=self.delspace
        # self.button2.pack({"side":"bottom"})
        self.button2.grid(row=1,column=0,sticky=E+W)

        self.button1=Button(self)
        self.button1['text']='删除换行'
        self.button1['command']=self.deln
        # self.button1.pack({"side":"bottom"})
        self.button1.grid(row=1,column=1,sticky=E+W)

        self.button3=Button(self)
        self.button3['text']='空换删除'
        self.button3['command']=self.alldel
        # self.button3.pack({"side":"bottom"})
        self.button3.grid(row=1,column=2,sticky=E+W)

        self.button4=Button(self)
        self.button4['text']='半角格式'
        self.button4['command']=self.formatting
        # self.button4.pack(side="bottom")
        self.button4.grid(row=1,column=3,sticky=E+W)




root = Tk()
root.wm_title('Small tool by With')
app = Application(master=root)
app.mainloop()
root.destroy()
