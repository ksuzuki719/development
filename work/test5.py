import sys
import os
#sys.path.append(os.path.join(os.getcwd(), '')
print (os.getcwd())
#sys.path.append(os.path.join(os.getcwd(), '')

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk


root=tk.Tk()
root.withdraw()

fTyp=[('画像ファイル','*.gif;*.jpg;*.jpeg;*.png')]
#複数のタイプを指定することも可能。

#iDir='c:/'
iDir=os.getcwd()

#askopenfilename 一つのファイルを選択する。
filename=fd.askopenfilename(filetypes=fTyp,initialdir=iDir)

tk.Message('FILE NAME is ...',filename)

#askopenfilenames 複数ファイルを選択する。
filenames=tkFileDialog.askopenfilenames(filetypes=fTyp,initialdir=iDir)

for f in filenames:
    tkMessageBox.showinfo('FILE NAME is ...',f)

#askdirectory ディレクトリを選択する。
dirname=tkFileDialog.askdirectory(initialdir=iDir)

tkMessageBox.showinfo('SELECTED DIRECROTY is ...',dirname)

#このコードはutf-8で保存する。
