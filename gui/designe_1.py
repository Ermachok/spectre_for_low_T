# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designe_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 1043)
        MainWindow.setMaximumSize(QtCore.QSize(1260, 16777215))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 244, 248);\n"
"background-color: rgb(255, 243, 240);")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1271, 1051))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAutoFillBackground(False)
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 341))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.OpticTranslabel = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.OpticTranslabel.setFrame(False)
        self.OpticTranslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OpticTranslabel.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.OpticTranslabel.setSpecialValueText("")
        self.OpticTranslabel.setDecimals(3)
        self.OpticTranslabel.setMaximum(10.0)
        self.OpticTranslabel.setSingleStep(0.001)
        self.OpticTranslabel.setProperty("value", 0.21)
        self.OpticTranslabel.setObjectName("OpticTranslabel")
        self.gridLayout.addWidget(self.OpticTranslabel, 16, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 11, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.LEnSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.LEnSpinBox.setFrame(False)
        self.LEnSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.LEnSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.LEnSpinBox.setSpecialValueText("")
        self.LEnSpinBox.setDecimals(1)
        self.LEnSpinBox.setMaximum(10.0)
        self.LEnSpinBox.setSingleStep(0.2)
        self.LEnSpinBox.setProperty("value", 1.0)
        self.LEnSpinBox.setObjectName("LEnSpinBox")
        self.gridLayout.addWidget(self.LEnSpinBox, 14, 1, 1, 1)
        self.LWSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.LWSpinBox.setFrame(False)
        self.LWSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.LWSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.LWSpinBox.setSpecialValueText("")
        self.LWSpinBox.setDecimals(1)
        self.LWSpinBox.setMaximum(2000.0)
        self.LWSpinBox.setProperty("value", 1064.4)
        self.LWSpinBox.setObjectName("LWSpinBox")
        self.gridLayout.addWidget(self.LWSpinBox, 10, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 14, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.TionSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.TionSpinBox.setFrame(False)
        self.TionSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.TionSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TionSpinBox.setSpecialValueText("")
        self.TionSpinBox.setDecimals(2)
        self.TionSpinBox.setMaximum(5000.0)
        self.TionSpinBox.setProperty("value", 100.0)
        self.TionSpinBox.setObjectName("TionSpinBox")
        self.gridLayout.addWidget(self.TionSpinBox, 3, 1, 1, 1)
        self.ZeffSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.ZeffSpinBox.setFrame(False)
        self.ZeffSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ZeffSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ZeffSpinBox.setSpecialValueText("")
        self.ZeffSpinBox.setDecimals(1)
        self.ZeffSpinBox.setMaximum(10.0)
        self.ZeffSpinBox.setProperty("value", 2.0)
        self.ZeffSpinBox.setObjectName("ZeffSpinBox")
        self.gridLayout.addWidget(self.ZeffSpinBox, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.ConcSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConcSpinBox.sizePolicy().hasHeightForWidth())
        self.ConcSpinBox.setSizePolicy(sizePolicy)
        self.ConcSpinBox.setMouseTracking(True)
        self.ConcSpinBox.setWrapping(False)
        self.ConcSpinBox.setFrame(False)
        self.ConcSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ConcSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ConcSpinBox.setSpecialValueText("")
        self.ConcSpinBox.setDecimals(1)
        self.ConcSpinBox.setMaximum(300.0)
        self.ConcSpinBox.setProperty("value", 5.0)
        self.ConcSpinBox.setObjectName("ConcSpinBox")
        self.gridLayout.addWidget(self.ConcSpinBox, 1, 1, 1, 1)
        self.TeSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.TeSpinBox.setFrame(False)
        self.TeSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.TeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TeSpinBox.setSpecialValueText("")
        self.TeSpinBox.setDecimals(3)
        self.TeSpinBox.setMaximum(5000.0)
        self.TeSpinBox.setSingleStep(0.1)
        self.TeSpinBox.setProperty("value", 100.0)
        self.TeSpinBox.setObjectName("TeSpinBox")
        self.gridLayout.addWidget(self.TeSpinBox, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setIndent(0)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 16, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 13, 0, 1, 1)
        self.OmegaSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.OmegaSpinBox.setFrame(False)
        self.OmegaSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.OmegaSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.OmegaSpinBox.setDecimals(5)
        self.OmegaSpinBox.setMaximum(12.0)
        self.OmegaSpinBox.setSingleStep(0.001)
        self.OmegaSpinBox.setProperty("value", 0.0025)
        self.OmegaSpinBox.setObjectName("OmegaSpinBox")
        self.gridLayout.addWidget(self.OmegaSpinBox, 13, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 20, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.formLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 20, 0, 1, 1)
        self.SolpiterSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.SolpiterSpinBox.setFrame(False)
        self.SolpiterSpinBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.SolpiterSpinBox.setReadOnly(True)
        self.SolpiterSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.SolpiterSpinBox.setSpecialValueText("")
        self.SolpiterSpinBox.setDecimals(3)
        self.SolpiterSpinBox.setMaximum(50.0)
        self.SolpiterSpinBox.setObjectName("SolpiterSpinBox")
        self.gridLayout.addWidget(self.SolpiterSpinBox, 19, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 19, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 17, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 17, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 18, 0, 1, 1)
        self.DebaySpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.DebaySpinBox.setEnabled(True)
        self.DebaySpinBox.setFrame(False)
        self.DebaySpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.DebaySpinBox.setReadOnly(True)
        self.DebaySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.DebaySpinBox.setSpecialValueText("")
        self.DebaySpinBox.setPrefix("")
        self.DebaySpinBox.setSuffix(" mm")
        self.DebaySpinBox.setDecimals(6)
        self.DebaySpinBox.setMaximum(100.0)
        self.DebaySpinBox.setObjectName("DebaySpinBox")
        self.gridLayout.addWidget(self.DebaySpinBox, 18, 1, 1, 1)
        self.ScatLenSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.ScatLenSpinBox.setFrame(False)
        self.ScatLenSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ScatLenSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ScatLenSpinBox.setSpecialValueText("")
        self.ScatLenSpinBox.setDecimals(5)
        self.ScatLenSpinBox.setMaximum(10.0)
        self.ScatLenSpinBox.setSingleStep(0.001)
        self.ScatLenSpinBox.setProperty("value", 0.015)
        self.ScatLenSpinBox.setObjectName("ScatLenSpinBox")
        self.gridLayout.addWidget(self.ScatLenSpinBox, 15, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 8, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 15, 0, 1, 1)
        self.ThetaSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.ThetaSpinBox.setFrame(False)
        self.ThetaSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ThetaSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ThetaSpinBox.setDecimals(1)
        self.ThetaSpinBox.setMaximum(400.0)
        self.ThetaSpinBox.setProperty("value", 110.0)
        self.ThetaSpinBox.setObjectName("ThetaSpinBox")
        self.gridLayout.addWidget(self.ThetaSpinBox, 11, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(300, 10, 20, 341))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(320, 10, 681, 341))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.DetectorLoadButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.DetectorLoadButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.DetectorLoadButton.setObjectName("DetectorLoadButton")
        self.gridLayout_5.addWidget(self.DetectorLoadButton, 20, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setStyleSheet("background-color: rgb(255, 217, 249)")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 18, 0, 1, 1)
        self.FilterLoadpushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.FilterLoadpushButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.FilterLoadpushButton.setObjectName("FilterLoadpushButton")
        self.gridLayout_5.addWidget(self.FilterLoadpushButton, 11, 0, 1, 1)
        self.ShowOrigFiltersButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ShowOrigFiltersButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.ShowOrigFiltersButton.setObjectName("ShowOrigFiltersButton")
        self.gridLayout_5.addWidget(self.ShowOrigFiltersButton, 12, 0, 1, 1)
        self.DetectorShowButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.DetectorShowButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.DetectorShowButton.setObjectName("DetectorShowButton")
        self.gridLayout_5.addWidget(self.DetectorShowButton, 21, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 22, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 16, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 9, 0, 1, 1)
        self.filter_status_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.filter_status_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.filter_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filter_status_label.setObjectName("filter_status_label")
        self.gridLayout_5.addWidget(self.filter_status_label, 11, 2, 1, 1)
        self.Filter_Origdata_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Filter_Origdata_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.Filter_Origdata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Filter_Origdata_label.setObjectName("Filter_Origdata_label")
        self.gridLayout_5.addWidget(self.Filter_Origdata_label, 12, 2, 1, 1)
        self.SpecChdata_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.SpecChdata_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.SpecChdata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SpecChdata_label.setObjectName("SpecChdata_label")
        self.gridLayout_5.addWidget(self.SpecChdata_label, 15, 2, 1, 1)
        self.PolyData_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.PolyData_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.PolyData_label.setAlignment(QtCore.Qt.AlignCenter)
        self.PolyData_label.setObjectName("PolyData_label")
        self.gridLayout_5.addWidget(self.PolyData_label, 23, 2, 1, 1)
        self.DetectorShowData_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.DetectorShowData_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.DetectorShowData_label.setAlignment(QtCore.Qt.AlignCenter)
        self.DetectorShowData_label.setObjectName("DetectorShowData_label")
        self.gridLayout_5.addWidget(self.DetectorShowData_label, 21, 2, 1, 1)
        self.Detectordata_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Detectordata_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.Detectordata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Detectordata_label.setObjectName("Detectordata_label")
        self.gridLayout_5.addWidget(self.Detectordata_label, 20, 2, 1, 1)
        self.DetectorPathlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.DetectorPathlineEdit.setObjectName("DetectorPathlineEdit")
        self.gridLayout_5.addWidget(self.DetectorPathlineEdit, 18, 2, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_5.addWidget(self.line_9, 25, 2, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_5.addWidget(self.line_8, 25, 0, 1, 1)
        self.BuildSpecChpushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.BuildSpecChpushButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.BuildSpecChpushButton.setObjectName("BuildSpecChpushButton")
        self.gridLayout_5.addWidget(self.BuildSpecChpushButton, 15, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setStyleSheet("background-color: rgb(255, 217, 249)")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 10, 0, 1, 1)
        self.FilterlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.FilterlineEdit.setObjectName("FilterlineEdit")
        self.gridLayout_5.addWidget(self.FilterlineEdit, 10, 2, 1, 1)
        self.PolyBuildpushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.PolyBuildpushButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.PolyBuildpushButton.setObjectName("PolyBuildpushButton")
        self.gridLayout_5.addWidget(self.PolyBuildpushButton, 23, 0, 1, 1)
        self.widget_for_plot = QtWidgets.QWidget(self.tab)
        self.widget_for_plot.setGeometry(QtCore.QRect(10, 500, 991, 511))
        self.widget_for_plot.setObjectName("widget_for_plot")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 360, 291, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TempStepsSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.TempStepsSpinBox.setFrame(False)
        self.TempStepsSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.TempStepsSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TempStepsSpinBox.setDecimals(0)
        self.TempStepsSpinBox.setMaximum(20000.0)
        self.TempStepsSpinBox.setSingleStep(10.0)
        self.TempStepsSpinBox.setProperty("value", 100.0)
        self.TempStepsSpinBox.setObjectName("TempStepsSpinBox")
        self.gridLayout_2.addWidget(self.TempStepsSpinBox, 3, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setScaledContents(False)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setIndent(0)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 2, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 3, 0, 1, 1)
        self.TempStartSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.TempStartSpinBox.setFrame(False)
        self.TempStartSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.TempStartSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TempStartSpinBox.setPrefix("")
        self.TempStartSpinBox.setDecimals(2)
        self.TempStartSpinBox.setMaximum(20000.0)
        self.TempStartSpinBox.setSingleStep(0.01)
        self.TempStartSpinBox.setProperty("value", 0.2)
        self.TempStartSpinBox.setObjectName("TempStartSpinBox")
        self.gridLayout_2.addWidget(self.TempStartSpinBox, 1, 1, 1, 1)
        self.TempEndSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.TempEndSpinBox.setFrame(False)
        self.TempEndSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.TempEndSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TempEndSpinBox.setDecimals(3)
        self.TempEndSpinBox.setMaximum(20000.0)
        self.TempEndSpinBox.setSingleStep(0.5)
        self.TempEndSpinBox.setProperty("value", 20.0)
        self.TempEndSpinBox.setObjectName("TempEndSpinBox")
        self.gridLayout_2.addWidget(self.TempEndSpinBox, 2, 1, 1, 1)
        self.PhElcalcpushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PhElcalcpushButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.PhElcalcpushButton.setObjectName("PhElcalcpushButton")
        self.gridLayout_2.addWidget(self.PhElcalcpushButton, 4, 0, 1, 1)
        self.PhEldata_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.PhEldata_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.PhEldata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.PhEldata_label.setObjectName("PhEldata_label")
        self.gridLayout_2.addWidget(self.PhEldata_label, 4, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 360, 281, 121))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setIndent(0)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)
        self.CalcSecButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.CalcSecButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.CalcSecButton.setObjectName("CalcSecButton")
        self.gridLayout_3.addWidget(self.CalcSecButton, 4, 0, 1, 1)
        self.WlStepsSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.WlStepsSpinBox.setFrame(False)
        self.WlStepsSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.WlStepsSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.WlStepsSpinBox.setDecimals(0)
        self.WlStepsSpinBox.setMaximum(20000.0)
        self.WlStepsSpinBox.setSingleStep(10.0)
        self.WlStepsSpinBox.setProperty("value", 600.0)
        self.WlStepsSpinBox.setObjectName("WlStepsSpinBox")
        self.gridLayout_3.addWidget(self.WlStepsSpinBox, 3, 1, 1, 1)
        self.PhEldata_label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.PhEldata_label_2.setStyleSheet("background-color: rgb(255, 133, 182);")
        self.PhEldata_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.PhEldata_label_2.setObjectName("PhEldata_label_2")
        self.gridLayout_3.addWidget(self.PhEldata_label_2, 4, 1, 1, 1)
        self.wlEndSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.wlEndSpinBox.setFrame(False)
        self.wlEndSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.wlEndSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.wlEndSpinBox.setDecimals(1)
        self.wlEndSpinBox.setMaximum(2000.0)
        self.wlEndSpinBox.setProperty("value", 1070.0)
        self.wlEndSpinBox.setObjectName("wlEndSpinBox")
        self.gridLayout_3.addWidget(self.wlEndSpinBox, 2, 1, 1, 1)
        self.wlStartSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.wlStartSpinBox.setFrame(False)
        self.wlStartSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.wlStartSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.wlStartSpinBox.setSpecialValueText("")
        self.wlStartSpinBox.setPrefix("")
        self.wlStartSpinBox.setDecimals(1)
        self.wlStartSpinBox.setMaximum(2000.0)
        self.wlStartSpinBox.setProperty("value", 1030.0)
        self.wlStartSpinBox.setObjectName("wlStartSpinBox")
        self.gridLayout_3.addWidget(self.wlStartSpinBox, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpticTranslabel.setSuffix(_translate("MainWindow", " "))
        self.label_2.setText(_translate("MainWindow", "Theta scattering"))
        self.label_8.setText(_translate("MainWindow", "Diagnostic parameters "))
        self.label_4.setText(_translate("MainWindow", "Laser wavelength"))
        self.LEnSpinBox.setSuffix(_translate("MainWindow", " J"))
        self.LWSpinBox.setSuffix(_translate("MainWindow", " nm"))
        self.label_17.setText(_translate("MainWindow", "Laser energy"))
        self.label.setText(_translate("MainWindow", "Z effective"))
        self.label_3.setText(_translate("MainWindow", "Concentration"))
        self.label_9.setText(_translate("MainWindow", "Ion temperature"))
        self.TionSpinBox.setSuffix(_translate("MainWindow", " eV"))
        self.label_10.setText(_translate("MainWindow", "Electron temperature"))
        self.ConcSpinBox.setSuffix(_translate("MainWindow", "*E20, m^-3"))
        self.TeSpinBox.setSuffix(_translate("MainWindow", " eV"))
        self.label_7.setText(_translate("MainWindow", "Plasma parameters "))
        self.label_22.setText(_translate("MainWindow", "Optic transmission"))
        self.label_16.setText(_translate("MainWindow", "Solid angle, Omega"))
        self.OmegaSpinBox.setSuffix(_translate("MainWindow", " st"))
        self.label_6.setText(_translate("MainWindow", "Solpiter  parameter "))
        self.label_5.setText(_translate("MainWindow", "Debay radius"))
        self.ScatLenSpinBox.setSuffix(_translate("MainWindow", " m"))
        self.label_19.setText(_translate("MainWindow", "Scattering length"))
        self.ThetaSpinBox.setSuffix(_translate("MainWindow", " deg "))
        self.DetectorLoadButton.setText(_translate("MainWindow", "Load detector data"))
        self.label_13.setText(_translate("MainWindow", "Path to detector data file: "))
        self.FilterLoadpushButton.setText(_translate("MainWindow", "Load filter data"))
        self.ShowOrigFiltersButton.setText(_translate("MainWindow", "Show original data"))
        self.DetectorShowButton.setText(_translate("MainWindow", "Show detector data"))
        self.label_11.setText(_translate("MainWindow", "Filters data"))
        self.filter_status_label.setText(_translate("MainWindow", "no data "))
        self.Filter_Origdata_label.setText(_translate("MainWindow", "no data "))
        self.SpecChdata_label.setText(_translate("MainWindow", "no data "))
        self.PolyData_label.setText(_translate("MainWindow", "no data "))
        self.DetectorShowData_label.setText(_translate("MainWindow", "no data "))
        self.Detectordata_label.setText(_translate("MainWindow", "no data "))
        self.DetectorPathlineEdit.setText(_translate("MainWindow", "D:\\Ioffe\\divertor_thomson\\different_calcuations\\spectre_for_low_T\\expected\\S15995_qe.csv"))
        self.BuildSpecChpushButton.setText(_translate("MainWindow", "Buid and show spectral channels"))
        self.label_12.setText(_translate("MainWindow", "Path to filter data file: "))
        self.FilterlineEdit.setText(_translate("MainWindow", "D:\\Ioffe\\divertor_thomson\\different_calcuations\\spectre_for_low_T\\expected\\\\filters16_19_doc.csv"))
        self.PolyBuildpushButton.setText(_translate("MainWindow", "Build and show polychomator"))
        self.label_26.setText(_translate("MainWindow", "Temperature grid parameters "))
        self.label_24.setText(_translate("MainWindow", "end temperature"))
        self.label_23.setText(_translate("MainWindow", "start temperature"))
        self.label_25.setText(_translate("MainWindow", "steps number"))
        self.TempStartSpinBox.setSuffix(_translate("MainWindow", "  eV"))
        self.TempEndSpinBox.setSuffix(_translate("MainWindow", " eV"))
        self.PhElcalcpushButton.setText(_translate("MainWindow", "Calculate and show photoelectrons"))
        self.PhEldata_label.setText(_translate("MainWindow", "doesn\'t ready"))
        self.label_15.setText(_translate("MainWindow", "Wavelength grid parameters "))
        self.label_20.setText(_translate("MainWindow", "end wavelength"))
        self.label_21.setText(_translate("MainWindow", "steps number"))
        self.label_18.setText(_translate("MainWindow", "start wavelength "))
        self.CalcSecButton.setText(_translate("MainWindow", "Calculate and show section"))
        self.PhEldata_label_2.setText(_translate("MainWindow", "waiting"))
        self.wlEndSpinBox.setSuffix(_translate("MainWindow", " nm "))
        self.wlStartSpinBox.setSuffix(_translate("MainWindow", " nm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Section calculation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
