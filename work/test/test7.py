import os,sys
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as ms
import PIL.Image
import PIL.ImageTk
from PIL import Image, ImageDraw

def callBack_btnSelectFiles():
    print("ボタン1が押されました")
    ms.showinfo('○×プログラム','処理ファイルを選択してください！')
    fTyp=[('画像ファイル','*.gif;*.jpg;*.jpeg;*.png')]
    #複数のタイプを指定することも可能。
    #iDir='c:/'
    iDir=os.getcwd()
    # ここの1行を変更 askopenfilename → askopenfilenames
    file = fd.askopenfilename(filetypes = fTyp,initialdir = iDir)
    # 選択ファイルリスト作成
    list = list(file)
    tk.messagebox.showinfo('画像解析プログラム',list)

root = tk.Tk()
root.geometry("500x200")
lbl = tk.Label(text="ボタン押して画像選択！")
lbl.pack()
btn = tk.Button(root, text="画像ファイル選択", command=callBack_btnSelectFiles)
btn.pack()


tk.mainloop()



