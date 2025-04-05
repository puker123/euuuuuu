from sys import * 
from pygame import *
mixer.init()
import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt #нужна константа Qt.KeepAspectRatio для изменения размеров с сохранением пропорций
from PyQt5.QtGui import QPixmap #оптимизированная для показа на экране картинка


from PIL import Image
from PIL.ImageQt import ImageQt #для перевода графики из Pillow в Qt 
from PIL import ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   GaussianBlur, UnsharpMask
)


app = QApplication([])
win = QWidget()       
win.resize(700, 500) 
win.setWindowTitle('синтезатор')

btn_dir = QPushButton("1")



btn_left = QPushButton("2")
btn_right = QPushButton("3")
btn_flip = QPushButton("4")
btn_sharp = QPushButton("5")
btn_bw = QPushButton("6")


row = QHBoxLayout()          # Основная строка
        # делится на два столбца
col2 = QVBoxLayout()
    # в первом - кнопка выбора директории
    # и список файлов
 # вo втором - картинка
row_tools = QHBoxLayout()    # и строка кнопок
row_tools.addWidget(btn_dir)
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)



row.addLayout(col2, 80)
win.setLayout(row)

q = mixer.Sound('brue.ogg')
w = mixer.Sound('legko-strannyiy-smeshnoy-fon-42347.ogg')
e = mixer.Sound('multfilm-treniya-tvist-smeshnaya-animatsiya-42004.ogg')
r = mixer.Sound('angry-birds-smeshnyie-kovarnyie-zvukovyie-effektyi-42869.ogg')
t = mixer.Sound('nya.ogg')
y = mixer.Sound('tuturu.ogg')

def a():
   q.play()

def s():
   w.play()

def d():
   e.play()

def f():
   r.play()

def g():
   t.play()

def h():
   y.play()


win.show()

btn_dir.clicked.connect(a)

btn_left.clicked.connect(s)

btn_right.clicked.connect(d)

btn_flip.clicked.connect(f)

btn_sharp.clicked.connect(g)

btn_bw.clicked.connect(h)






app.exec_()