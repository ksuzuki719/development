import os,sys
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as ms
import PIL.Image
import PIL.ImageTk
from PIL import Image, ImageDraw
from io import BytesIO 
import numpy as np

def callBack_btnSelectFiles():
    print("ボタン1が押されました")
    ms.showinfo('○×プログラム','処理ファイルを選択してください！')
    fTyp=[('画像ファイル','*.gif;*.jpg;*.jpeg;*.png')]
    #複数のタイプを指定することも可能。
    #iDir='c:/'
    iDir=os.getcwd()
    # ここの1行を変更 askopenfilename → askopenfilenames
    filename = fd.askopenfilename(filetypes = fTyp,initialdir = iDir)
    tk.messagebox.showinfo('画像解析プログラム',filename)


    # 画像ファイルパスから読み込み
    img = Image.open(filename)
    #オリジナル画像の幅と高さを取得
    width, height = img.size
    # オリジナル画像と同じサイズのImageオブジェクトを作成する
    img2 = Image.new('RGB', (width, height))

    img_pixels = []
    for y in range(height):
      for x in range(width):
        # getpixel((x,y))で左からx番目,上からy番目のピクセルの色を取得し、img_pixelsに追加する
        img_pixels.append(img.getpixel((x,y)))
    # あとで計算しやすいようにnumpyのarrayに変換しておく
    img_pixels = np.array(img_pixels)

    # バイナリから読み込み(python3なのでbinaryモードで読み込み)
    with open(filename, 'rb') as f:
        binary = f.read()
    img = Image.open(BytesIO(binary))

    # numpy配列の取得
    img_array = np.asarray(img)

    # 色の変換も簡単ですが、できる色が制限されます。
    print(img.mode) # RGBA
    rgb = img.convert('RGB')
    img.show()

root = tk.Tk()
root.geometry("500x200")
lbl = tk.Label(text="ボタン押して画像選択！")
lbl.pack()
btn = tk.Button(root, text="画像ファイル選択", command=callBack_btnSelectFiles)
btn.pack()


tk.mainloop()




