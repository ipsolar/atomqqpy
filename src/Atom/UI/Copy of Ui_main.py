# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hang/workspace/atomqq_py/src/Atom/UI/main.ui'
#
# Created: Thu Apr 26 04:10:09 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(280, 597)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(280, 0))
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setDocumentMode(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.imgUserFace = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgUserFace.sizePolicy().hasHeightForWidth())
        self.imgUserFace.setSizePolicy(sizePolicy)
        self.imgUserFace.setMinimumSize(QtCore.QSize(42, 42))
        self.imgUserFace.setFrameShape(QtGui.QFrame.StyledPanel)
        self.imgUserFace.setFrameShadow(QtGui.QFrame.Sunken)
        self.imgUserFace.setText(_fromUtf8(""))
        self.imgUserFace.setPixmap(QtGui.QPixmap(_fromUtf8("Res/img/header.png")))
        self.imgUserFace.setObjectName(_fromUtf8("imgUserFace"))
        self.gridLayout.addWidget(self.imgUserFace, 1, 1, 2, 1)
        self.lbUserName = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbUserName.sizePolicy().hasHeightForWidth())
        self.lbUserName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbUserName.setFont(font)
        self.lbUserName.setObjectName(_fromUtf8("lbUserName"))
        self.gridLayout.addWidget(self.lbUserName, 1, 2, 1, 1)
        self.lbUserNick = QtGui.QLabel(self.centralWidget)
        self.lbUserNick.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lbUserNick.setObjectName(_fromUtf8("lbUserNick"))
        self.gridLayout.addWidget(self.lbUserNick, 2, 2, 1, 3)
        spacerItem = QtGui.QSpacerItem(1, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.cbxStatus = QtGui.QComboBox(self.centralWidget)
        self.cbxStatus.setObjectName(_fromUtf8("cbxStatus"))
        self.cbxStatus.addItem(_fromUtf8(""))
        self.cbxStatus.setItemText(0, QtGui.QApplication.translate("MainWindow", "Q我吧", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxStatus.addItem(_fromUtf8(""))
        self.cbxStatus.setItemText(1, QtGui.QApplication.translate("MainWindow", "在线", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxStatus.addItem(_fromUtf8(""))
        self.cbxStatus.setItemText(2, QtGui.QApplication.translate("MainWindow", "忙碌", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxStatus.addItem(_fromUtf8(""))
        self.cbxStatus.setItemText(3, QtGui.QApplication.translate("MainWindow", "隐身", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxStatus.addItem(_fromUtf8(""))
        self.cbxStatus.setItemText(4, QtGui.QApplication.translate("MainWindow", "离线", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout.addWidget(self.cbxStatus, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tbMain = QtGui.QTabWidget(self.centralWidget)
        self.tbMain.setElideMode(QtCore.Qt.ElideNone)
        self.tbMain.setObjectName(_fromUtf8("tbMain"))
        self.tbFriends = QtGui.QWidget()
        self.tbFriends.setObjectName(_fromUtf8("tbFriends"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tbFriends)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.twFriends = QtGui.QTreeView(self.tbFriends)
        self.twFriends.setAutoScroll(True)
        self.twFriends.setAutoScrollMargin(1)
        self.twFriends.setAutoExpandDelay(0)
        self.twFriends.setIndentation(12)
        self.twFriends.setAnimated(True)
        self.twFriends.setExpandsOnDoubleClick(True)
        self.twFriends.setObjectName(_fromUtf8("twFriends"))
        self.twFriends.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.twFriends)
        self.tbMain.addTab(self.tbFriends, _fromUtf8(""))
        self.tbQun = QtGui.QWidget()
        self.tbQun.setObjectName(_fromUtf8("tbQun"))
        self.tbMain.addTab(self.tbQun, _fromUtf8(""))
        self.tbLishi = QtGui.QWidget()
        self.tbLishi.setObjectName(_fromUtf8("tbLishi"))
        self.tbMain.addTab(self.tbLishi, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tbMain)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tbMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbFriends), QtGui.QApplication.translate("MainWindow", "好友列表", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbQun), QtGui.QApplication.translate("MainWindow", "群列表", None, QtGui.QApplication.UnicodeUTF8))
        self.tbMain.setTabText(self.tbMain.indexOf(self.tbLishi), QtGui.QApplication.translate("MainWindow", "近期会话", None, QtGui.QApplication.UnicodeUTF8))



