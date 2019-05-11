#!/usr/bin/env python
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from config import client_id, client_secret, album_id, access_token, refresh_token
from imgur import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox, QProgressBar, QPushButton, QMainWindow, QFileDialog, QLineEdit
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QFont, QCursor, QIcon, QPixmap
import os
import sys
import re
import resource_rc
from PIL import ImageGrab
im = ImageGrab.grabclipboard()

class QTitleButton(QPushButton):  # 新建標題欄按鈕類別

    def __init__(self, *args):
        super(QTitleButton, self).__init__(*args)
        self.setFont(QFont("Webdings"))  # 特殊字型以不借助圖片實現最小化最大化和關閉按鈕
        self.setFixedWidth(40)

class Upload(QThread):  # 開始跑下載，利用Qt的thread，用原生的打包會出錯。

    def __init__(self, client, LineEdit, LineEditText, selectToolButton, uploadButton, copyButton, clearButton, statusLabel, urlResponseLineEdit, checker):
        QThread.__init__(self)
        self.client = client
        self.LineEdit = LineEdit
        self.LineEditText = LineEditText
        self.selectToolButton = selectToolButton
        self.uploadButton = uploadButton
        self.copyButton = copyButton
        self.clearButton = clearButton
        self.checker = checker
        self.statusLabel = statusLabel
        self.urlResponseLineEdit = urlResponseLineEdit

    def run(self):
        if self.checker == False:
            uploadImage = self.client.upload_from_path(self.LineEditText, anon=False)
        else :
            uploadImage = self.client.upload_from_url(self.LineEditText, anon=False)
        if uploadImage:
            self.statusLabel.setText('Upload Done')
        images = self.client.get_account_images('me', page=0)
        if images:
            for image in images:
                link = image.link.replace("http://", "https://")
                print(link)
                self.urlResponseLineEdit.setText(link)
                break
        self.selectToolButton.setEnabled(True)
        self.uploadButton.setEnabled(True)
        self.copyButton.setEnabled(True)
        self.clearButton.setEnabled(True)

        # get album
        # for album in self.client.get_account_albums('me'):
        #     album_title = album.title if album.title else 'Untitled'
        #     print('Album: {0} ({1})'.format(album_title, album.id))

class MyForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        self.uploadButton.clicked.connect(self.upload)
        self.selectToolButton.clicked.connect(self.openFileDialog)
        self.copyButton.clicked.connect(self.copyText)
        self.clearButton.clicked.connect(self.clear)
        self.uploadButton.setToolTip("開始上傳")
        self.selectToolButton.setToolTip("選擇檔案")
        self.copyButton.setToolTip("複製網址")
        self.clearButton.setToolTip("清除網址")
        self.items = ["PASTE YOUR IMAGE URL", "SELECT IMAGE FROM PC"]
        self.modeComboBox.addItems(self.items)
        self.modeComboBox.currentIndexChanged.connect(self.index_changed)
        self.client = ImgurClient(client_id, client_secret, access_token, refresh_token)
        self.setMinimumWidth(530)  # 設定主視窗最小寬度
        # self.setWindowOpacity(0.9)  # 設定視窗透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 設定視窗透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隱藏邊框
        self.m_flag = None
        self.checker = True
        self.drop = False
        self.paste = False
        self.titleLabel.setFixedHeight(20)  # 設定標題欄高度
        self.setBackGroundStyle()
        self.dropLineEdit.setAcceptDrops(True)
        self.dropLineEdit.installEventFilter(self)
        QApplication.clipboard().dataChanged.connect(self.clipboardChanged)

    # Get the system clipboard contents
    def clipboardChanged(self):
        text = QApplication.clipboard().text()
        text = text.replace("file:", "")
        text = text.replace("///", "")
        print(text)

        pixmap = QPixmap(text)
        if pixmap.isNull() == False:
            smaller_pixmap = pixmap.scaled(354, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.urlLineEdit.setText(text)
            self.ImageLabel.setPixmap(smaller_pixmap)
            self.paste = True
        else:
            pass

    def eventFilter(self, object, event): # DropLineEdit
        if (object is self.dropLineEdit):
            if (event.type() == QtCore.QEvent.DragEnter):
                if event.mimeData().hasUrls():
                    event.accept()   # must accept the dragEnterEvent or else the dropEvent can't occur !!!
                    print("accept")
                    self.drop = True
                else:
                    event.ignore()
                    print("ignore")
            if (event.type() == QtCore.QEvent.Drop):
                if event.mimeData().hasUrls():   # if file or link is dropped
                    st = str(event.mimeData().urls())
                    st = st.replace("[PyQt5.QtCore.QUrl('file:", "")
                    st = st.replace("///", "")
                    st = st.replace("')]","") 
                    print(st)
                    self.urlLineEdit.setText(st)
                    pixmap = QPixmap(st)
                    smaller_pixmap = pixmap.scaled(354, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
                    self.ImageLabel.setPixmap(smaller_pixmap)
                    print("Drop end")
            return False # lets the event continue to the edit
        return False

    def setBackGroundStyle(self):
        # 設定關閉跟縮小按鈕的顏色跟 hover
        # 設定主視窗背景顏色
        # QWidget #widget{
        #     background-color: #D3D3D3;
        #     border:1px solid #D3D3D3;
        # }
        # border:1px solid #DDDDDD;
        # border-radius: 5px;
        self.setStyleSheet("""
            QWidget #closeButton {
                color:white;
                }
            QWidget #minButton {
                color:white;
                margin-right:2px;
                }
            QWidget #closeButton:hover{
                background-color: #D32424;
                }
            QWidget #minButton:hover{
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #636363, stop:1 #575757);
                }
            QLineEdit{
                background: rgb(50, 50, 52);
                font-size:20px;
                font-weight:700;
                font: 63 12pt "Bahnschrift SemiBold SemiConden";
                color:white;
            }
            QLineEdit QMenu {
                background-color:#686464;
            }
            QLineEdit QMenu::item {   
                padding: 2px 12px 2px 12px;
            }
            QLineEdit QMenu::item:selected {
                color: #F0F0F0;
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #424141, stop:1 #292929); 
            }
            QLineEdit QMenu::separator {
                height: 1px;
                background: #a39e9e;
            }
            QMessageBox{
                background: rgb(50, 50, 50);
                font: 63 12pt "Bahnschrift SemiBold SemiConden";
            }
            QMessageBox QLabel{
                color:white;
            }
            QMessageBox QPushButton{
                width:75px;
                color:white;
                font: 63 12pt "Bahnschrift SemiBold SemiConden";
            }
            QPushButton{
                border-style: none;
                border: 0px;
                padding: 5px;   
                height: 20px;
                border-radius:5px;
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #424141, stop:1 #292929); 
            }
            QPushButton:hover{ 
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #636363, stop:1 #575757);
            }
            
            QPushButton:pressed{ 
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #424141, stop:1 #292929);
            }
            QToolButton{
                border-style: none;
                border: 0px;
                color: #F0F0F0;
                padding: 5px;   
                height: 20px;
                border-radius:5px;
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #424141, stop:1 #292929); 
            }
            QToolButton:hover{ 
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #636363, stop:1 #575757);
            }
            
            QToolButton:pressed{ 
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #424141, stop:1 #292929);
            }
            QMenu {
                background-color:#F0F0F0;
            }
            QMenu::item {   
                padding: 2px 12px 2px 12px;
            }
            QMenu::item:selected {
                color: #F0F0F0;
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #424141, stop:1 #292929); 
            }
            QMenu::separator {
                height: 1px;
                background: #636363;
            }
            QWidget #widget {
                background: #4D4D4D;
            }
        """)

    def copyText(self): 
        clipboard = QApplication.clipboard()
        if self.urlResponseLineEdit.text() != '':
            clipboard.setText(self.urlResponseLineEdit.text())
            self.statusLabel.setText('Copied')
            self.urlResponseLineEdit.setFocus(True)
    
    def clear(self):
        self.urlLineEdit.setText('')
        self.urlResponseLineEdit.setText('')
        self.statusLabel.setText('')
        self.ImageLabel.clear()

    def upload(self):
        pattern = re.compile('http[s]?://')
        if pattern.match(self.urlLineEdit.text()) and self.checker == False:
            print(pattern.match(self.urlLineEdit.text()).group())
            buttonReply = QMessageBox.question(
                self, 'Warning', 'Please check your mode!', QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                self.urlLineEdit.setText('')
                self.urlResponseLineEdit.setText('')
                return
        elif self.drop == True and self.checker == True:
            buttonReply = QMessageBox.question(
                self, 'Warning', 'Please check your mode!', QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                self.urlResponseLineEdit.setText('')
                return
        elif self.paste == True and self.checker == True:
            buttonReply = QMessageBox.question(
                self, 'Warning', 'Please check your mode!', QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                self.urlResponseLineEdit.setText('')
                return

        if self.urlLineEdit.text() == '' and self.checker == True:
            buttonReply = QMessageBox.question(
                self, 'Warning', 'Please enter your url!', QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                return
        elif self.urlLineEdit.text() == '' and self.checker == False:
            buttonReply = QMessageBox.question(
                self, 'Warning', 'Please select your file!', QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                return
        else:
            self.uploadButton.setEnabled(False)
            self.selectToolButton.setEnabled(False)
            self.copyButton.setEnabled(False)
            self.clearButton.setEnabled(False)
            if self.urlLineEdit.text() != '':
                self.statusLabel.setText('Start Upload')
                try:
                    self.upToImgur = Upload(
                        self.client, self.urlLineEdit, self.urlLineEdit.text(), self.selectToolButton, self.uploadButton, self.copyButton, self.clearButton, self.statusLabel, self.urlResponseLineEdit, self.checker)
                    self.upToImgur.start()
                except Exception as e:
                    print(e)


    def openFileDialog(self):
        if self.checker == True:
            return

        fileName, filetype = QFileDialog.getOpenFileName(self,'Open file','C:\\','Image files (*.jpg *.gif *.png *.jpeg)')
        print(fileName)

        if fileName:
            self.urlLineEdit.setText(str(fileName))
        else:
            self.urlLineEdit.setText('')
            buttonReply = QMessageBox.question(
                self, 'Warning', 'Please select your file!', QMessageBox.Ok)
            if buttonReply == QMessageBox.Ok:
                return
    
    def index_changed(self, i):  # 找出 comboBox 當前選擇哪個
        if self.modeComboBox.currentText() == "PASTE YOUR IMAGE URL":
            print(i)
            self.checker = True
            self.selectToolButton.setCursor(QCursor(Qt.ForbiddenCursor))
            self.urlLineEdit.setText('')
            self.urlResponseLineEdit.setText('')
            self.ImageLabel.clear()
        elif self.modeComboBox.currentText() == "SELECT IMAGE FROM PC":
            print(i)
            self.checker = False
            self.selectToolButton.setCursor(QCursor(Qt.PointingHandCursor))
            self.urlLineEdit.setText('')
            self.urlResponseLineEdit.setText('')
            self.ImageLabel.clear()

    def setCloseButton(self, bool):
        # 給widget定義一個setCloseButton函式，為True時設定一個關閉按鈕
        if bool == True:
            self.closeButton = QTitleButton(
                b'\xef\x81\xb2'.decode("utf-8"), self)
            # 設定按鈕的ObjectName以在qss樣式表內定義不同的按鈕樣式
            self.closeButton.setObjectName("closeButton")
            self.closeButton.setToolTip("關閉視窗")
            self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
            self.closeButton.setFixedHeight(
                self.titleLabel.height())  # 設定按鈕高度為標題欄高度
            self.closeButton.clicked.connect(
                self.close)  # 按鈕訊號連線到關閉視窗的槽函式(self.close)

    def setMinButton(self, bool):
        # 給widget定義一個setMinButton函式，為True時設定一組最小化按鈕
        if bool == False:
            self.minButton = QTitleButton(
                b'\xef\x80\xb0'.decode("utf-8"), self)
            self.minButton.setObjectName("minButton")
            self.minButton.setToolTip("最小化")
            self.minButton.setCursor(QCursor(Qt.PointingHandCursor))
            self.minButton.setFixedHeight(
                self.titleLabel.height())  # 設定按鈕高度為標題欄高度
            self.minButton.clicked.connect(
                self.showMinimized)  # 按鈕訊號連線到最小化視窗的槽函式

    def resizeEvent(self, QResizeEvent):
        # 自定義視窗調整大小事件
        self.titleLabel.setFixedWidth(self.width())  # 將標題標籤始終設為視窗寬度
        # 分別移動二個按鈕到正確的位置
        try:
            # print(self.width())
            # print(self.closeButton.width())
            self.closeButton.move(
                self.width() - self.closeButton.width() - 10, 10)
        except:
            pass
        try:
            self.minButton.move(
                self.width() - (self.closeButton.width()) * 2 - 10, 10)
        except:
            pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()  # 獲取鼠標相對視窗位置
            # print(event.globalPos())  # 全域座標
            # print(self.pos())  # 主視窗左上角座標
            # print(self.m_Position)  # 滑鼠相對座標
            event.accept()
            self.setCursor(Qt.OpenHandCursor)  # 更改鼠標圖示

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            # 移動後拿全域座標減掉滑鼠座標就是新的主視窗座標
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改視窗位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(Qt.ArrowCursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.setWindowIcon(QIcon(":/imgur.ico"))
    myapp.setCloseButton(True)
    myapp.setMinButton(False)
    myapp.show()
    sys.exit(app.exec_())
    # client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    # try:
    #     fields = {
    #         'album': album_id,
    #         'name': 'test-name!',
    #         'title': 'test-title',
    #         'description': 'test-description',
    #         'privacy': 'hidden'
    #     }
    #     test = client.create_album(fields)
    #     images = client.get_album_images(album_id)
    # except ImgurClientError as e:
    #     print('ERROR: {}'.format(e.error_message))
    #     print('Status code {}'.format(e.status_code))

    # print("Downloading album {} ({!s} images)".format(album_id, len(images)))

    # config = {
    #     'album': album_id,
    #     'name': 'test-name!',
    #     'title': 'test-title',
    #     'description': 'test-description'
    # }
    # data = [
    #     'https://pbs.twimg.com/media/DX19qeEVwAAuv12.jpg:large',
    #     'https://pbs.twimg.com/media/DX19qeAUMAAtUfl.jpg:large',
    #     'https://pbs.twimg.com/media/DX19qeOV4AAIh6v.jpg:large',
    #     'https://pbs.twimg.com/media/DX19qeIU8AYB47S.jpg:large',
    #     'https://pbs.twimg.com/media/D4ookC5VUAADGBR.jpg:large',
    #     'https://pbs.twimg.com/media/D4mk5XYUwAAB-UT.jpg:large',
    #     'https://pbs.twimg.com/media/D4mk5XFUcAUl0By.jpg:large',
    #     'https://pbs.twimg.com/media/D4mk5YBUIAUdCtM.jpg:large',
    #     'https://pbs.twimg.com/media/D4kAuXUUwAE1IEt.jpg:large',
    #     'https://pbs.twimg.com/media/D4j84-YVUAEXYGE.jpg:large',
    #     'https://pbs.twimg.com/media/D4Gxn-JU0AANPDN.jpg:large'
    # ]
    # print("Uploading image... ")
    # for url in data:
    #     image = client.upload_from_url(url, config=config, anon=False)
    #     print(url)
#     image = client.upload_from_path('beauty.png', anon=False)
# print("Done")
