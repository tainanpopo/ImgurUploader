# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgur.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 389)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgur.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: rgb(68, 69, 73);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.modeComboBox = QtWidgets.QComboBox(self.widget)
        self.modeComboBox.setMinimumSize(QtCore.QSize(270, 0))
        self.modeComboBox.setStyleSheet("border: 2px solid grey;\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"background:#565454;\n"
"color:#fff;")
        self.modeComboBox.setObjectName("modeComboBox")
        self.gridLayout.addWidget(self.modeComboBox, 2, 1, 1, 1)
        self.modelLabel = QtWidgets.QLabel(self.widget)
        self.modelLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.modelLabel.setStyleSheet("border:none;\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color:white;")
        self.modelLabel.setObjectName("modelLabel")
        self.gridLayout.addWidget(self.modelLabel, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.titleLabel = QtWidgets.QLabel(self.widget)
        self.titleLabel.setStyleSheet("border:none;\n"
"image: url(:/imgur.ico);\n"
"image-position: left;\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color:white;")
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 1, 0, 1, 1)
        self.statusLabel = QtWidgets.QLabel(self.widget)
        self.statusLabel.setStyleSheet("border:none;\n"
"color: rgb(170, 85, 127);\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";")
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout.addWidget(self.statusLabel, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.copyButton = QtWidgets.QPushButton(self.widget)
        self.copyButton.setMinimumSize(QtCore.QSize(150, 25))
        self.copyButton.setMaximumSize(QtCore.QSize(93, 25))
        self.copyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copyButton.setStyleSheet("color: rgb(255, 85, 127);\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";")
        self.copyButton.setObjectName("copyButton")
        self.gridLayout_2.addWidget(self.copyButton, 2, 3, 1, 1)
        self.urlLineEdit = QtWidgets.QLineEdit(self.widget)
        self.urlLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.urlLineEdit.setStyleSheet("border: 2px solid grey;\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"background:#565454;\n"
"color:#fff;")
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.gridLayout_2.addWidget(self.urlLineEdit, 0, 1, 1, 1)
        self.urlResponseLineEdit = QtWidgets.QLineEdit(self.widget)
        self.urlResponseLineEdit.setStyleSheet("border: 2px solid grey;\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"background:#565454;\n"
"color:#fff;")
        self.urlResponseLineEdit.setObjectName("urlResponseLineEdit")
        self.gridLayout_2.addWidget(self.urlResponseLineEdit, 2, 1, 1, 1)
        self.uploadButton = QtWidgets.QPushButton(self.widget)
        self.uploadButton.setMinimumSize(QtCore.QSize(150, 25))
        self.uploadButton.setMaximumSize(QtCore.QSize(93, 25))
        self.uploadButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uploadButton.setStyleSheet("color: rgb(85, 170, 255);\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";")
        self.uploadButton.setObjectName("uploadButton")
        self.gridLayout_2.addWidget(self.uploadButton, 4, 3, 1, 1)
        self.selectToolButton = QtWidgets.QToolButton(self.widget)
        self.selectToolButton.setMinimumSize(QtCore.QSize(150, 25))
        self.selectToolButton.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.selectToolButton.setStyleSheet("color: rgb(85, 170, 127);\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";")
        self.selectToolButton.setObjectName("selectToolButton")
        self.gridLayout_2.addWidget(self.selectToolButton, 0, 3, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.widget)
        self.clearButton.setMinimumSize(QtCore.QSize(93, 25))
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setStyleSheet("color: rgb(255, 170, 127);\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";")
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_2.addWidget(self.clearButton, 4, 1, 1, 1)
        self.ImageLabel = QtWidgets.QLabel(self.widget)
        self.ImageLabel.setMinimumSize(QtCore.QSize(30, 0))
        self.ImageLabel.setText("")
        self.ImageLabel.setObjectName("ImageLabel")
        self.gridLayout_2.addWidget(self.ImageLabel, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.dropLineEdit = QtWidgets.QLineEdit(self.widget)
        self.dropLineEdit.setMinimumSize(QtCore.QSize(385, 200))
        self.dropLineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dropLineEdit.setStyleSheet("font-size:20px;\n"
"font-weight:700;\n"
"font: 63 12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color:white;")
        self.dropLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dropLineEdit.setDragEnabled(True)
        self.dropLineEdit.setReadOnly(True)
        self.dropLineEdit.setObjectName("dropLineEdit")
        self.gridLayout_2.addWidget(self.dropLineEdit, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImgurUploader"))
        self.modelLabel.setText(_translate("MainWindow", "PLEASE SELECT THE UPLOAD MODE"))
        self.titleLabel.setText(_translate("MainWindow", "        ImgurUploader"))
        self.copyButton.setText(_translate("MainWindow", "COPY URL"))
        self.uploadButton.setText(_translate("MainWindow", "UPLOAD"))
        self.selectToolButton.setText(_translate("MainWindow", "SELECT FILE"))
        self.clearButton.setText(_translate("MainWindow", "CLEAR"))
        self.dropLineEdit.setText(_translate("MainWindow", "DROP YOUR IMAGE HERE"))