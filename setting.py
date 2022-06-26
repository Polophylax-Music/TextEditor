#coding: utf-8
import os, tkinter, tkinter.filedialog, tkinter.messagebox
from PIL import Image
import numpy as np


tki = tkinter.Tk()
tki.geometry('250x150')
tki.title('背景画面の選択')

rdo_txt = ['デフォルト', 'png画像を選択する']
rdo_var = tkinter.IntVar()


for i in range(len(rdo_txt)):
	rdo = tkinter.Radiobutton(tki, value=i, variable=rdo_var, text=rdo_txt[i]) 
	rdo.place(x=50, y=30 + (i * 24))

def btn_click():
	num = rdo_var.get()
	if(num == 1):
		fTyp = [("PNG","png")]
		iDir = os.path.abspath(os.path.dirname(__file__))
		tkinter.messagebox.showinfo('png画像の選択','ファイルを選択してください。')
		file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
		img2 = Image.open(file)
		img2.save('image.png', quality = 95)
		tkinter.messagebox.showinfo('画像の変更', '背景画像を変更しました。')
	else:
		with open("image.png","w"):pass
		tkinter.messagebox.showinfo('画像の変更', 'デフォルトに変更しました。')

btn = tkinter.Button(tki, text='OK', command=btn_click)
btn.place(x=100, y=100)

rdo.mainloop()