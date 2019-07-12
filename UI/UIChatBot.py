from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from PyQt5 import uic

app=QApplication([])
loadFile=uic.loadUi("designUI.ui")

def setNameButton(nameBut1,nameBut2,nameBut3,nameBut4): #hàm thiết lập tên cho các button 
  loadFile.pushButton.setText(nameBut1)
  loadFile.pushButton_2.setText(nameBut2)
  loadFile.pushButton_3.setText(nameBut3)
  loadFile.pushButton_4.setText(nameBut4)

def textBelow(textB):                                # ghi nội dung vào khung chữ bên dưới
  loadFile.listWidget2.addItem(textB)

class addText:                                       # class của các button để có thể add text vào khung chữ bên trên khi nhấn nút
  text=0
  def textClickBut(button):
    loadFile.listWidget.addItem(button.text)

def clickButton(but1,but2,but3,but4):                # hàm để khi nhấn nút thì chữ xuất hiện
  loadFile.pushButton.clicked.connect(but1.textClickBut)
  loadFile.pushButton_2.clicked.connect(but2.textClickBut)
  loadFile.pushButton_3.clicked.connect(but3.textClickBut)
  loadFile.pushButton_4.clicked.connect(but4.textClickBut)

def run():          # hàm này để khi gọi nó và ấn chạy chương trình ra giao diện đồ họa
  loadFile.show()
  app.exec()

button1,button2,button3,button4=addText(),addText(),addText(),addText()    #khai báo 4 button với kiểu là class để add chữ

button1.text='hi'            # dòng text sẽ hiện ra khi nhấn nút
button2.text='chao'          # cái này mình tự thiết lập chữ hiện ra ứng với mỗi nút bấm
button3.text='cac'
button4.text='ban'

clickButton(button1,button2,button3,button4)  #gọi hàm này với 4 button đã thiết lập, chữ sẽ hiện ra ở trên khi nhấn nút
setNameButton("nut 1",'nut 2','nut 3','nut 4') # gọi hàm truyền vào tham số là tên các button để thiết lập tên button
textBelow(''' hello ''') # gọi hàm truyền vào tham số là dòng text muốn hiện lên ở khung dứoi
run()# hàm để khi chạy chương trình giao diện đồ họa sẽ hiện ra
