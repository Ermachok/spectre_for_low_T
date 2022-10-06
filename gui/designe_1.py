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
        MainWindow.resize(1123, 697)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 244, 248);\n"
"background-color: rgb(255, 243, 240);")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 40, 300, 103))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
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
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
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
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(40, 150, 301, 78))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.formLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.ThetaSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget_2)
        self.ThetaSpinBox.setFrame(False)
        self.ThetaSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ThetaSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ThetaSpinBox.setDecimals(1)
        self.ThetaSpinBox.setMaximum(400.0)
        self.ThetaSpinBox.setProperty("value", 110.0)
        self.ThetaSpinBox.setObjectName("ThetaSpinBox")
        self.gridLayout_2.addWidget(self.ThetaSpinBox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.LEnSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget_2)
        self.LEnSpinBox.setFrame(False)
        self.LEnSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.LEnSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.LEnSpinBox.setSpecialValueText("")
        self.LEnSpinBox.setDecimals(1)
        self.LEnSpinBox.setMaximum(10.0)
        self.LEnSpinBox.setSingleStep(0.2)
        self.LEnSpinBox.setProperty("value", 1.0)
        self.LEnSpinBox.setObjectName("LEnSpinBox")
        self.gridLayout_2.addWidget(self.LEnSpinBox, 3, 1, 1, 1)
        self.LWSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget_2)
        self.LWSpinBox.setFrame(False)
        self.LWSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.LWSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.LWSpinBox.setSpecialValueText("")
        self.LWSpinBox.setDecimals(1)
        self.LWSpinBox.setMaximum(2000.0)
        self.LWSpinBox.setProperty("value", 1064.4)
        self.LWSpinBox.setObjectName("LWSpinBox")
        self.gridLayout_2.addWidget(self.LWSpinBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 400, 262, 82))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.DebaySpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.DebaySpinBox.setFrame(False)
        self.DebaySpinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DebaySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.DebaySpinBox.setSpecialValueText("")
        self.DebaySpinBox.setPrefix("")
        self.DebaySpinBox.setSuffix(" mm")
        self.DebaySpinBox.setDecimals(4)
        self.DebaySpinBox.setMaximum(100.0)
        self.DebaySpinBox.setObjectName("DebaySpinBox")
        self.gridLayout_3.addWidget(self.DebaySpinBox, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.SolpiterSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.SolpiterSpinBox.setFrame(False)
        self.SolpiterSpinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SolpiterSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.SolpiterSpinBox.setSpecialValueText("")
        self.SolpiterSpinBox.setDecimals(3)
        self.SolpiterSpinBox.setMaximum(50.0)
        self.SolpiterSpinBox.setObjectName("SolpiterSpinBox")
        self.gridLayout_3.addWidget(self.SolpiterSpinBox, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 230, 341, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(350, 40, 20, 351))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 250, 272, 87))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 1, 0, 1, 1)
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
        self.gridLayout_4.addWidget(self.wlStartSpinBox, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 2, 0, 1, 1)
        self.WlStepsSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.WlStepsSpinBox.setFrame(False)
        self.WlStepsSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.WlStepsSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.WlStepsSpinBox.setDecimals(0)
        self.WlStepsSpinBox.setMaximum(1000.0)
        self.WlStepsSpinBox.setProperty("value", 200.0)
        self.WlStepsSpinBox.setObjectName("WlStepsSpinBox")
        self.gridLayout_4.addWidget(self.WlStepsSpinBox, 3, 1, 1, 1)
        self.wlEndSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.wlEndSpinBox.setFrame(False)
        self.wlEndSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.wlEndSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.wlEndSpinBox.setDecimals(1)
        self.wlEndSpinBox.setMaximum(2000.0)
        self.wlEndSpinBox.setProperty("value", 1070.0)
        self.wlEndSpinBox.setObjectName("wlEndSpinBox")
        self.gridLayout_4.addWidget(self.wlEndSpinBox, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setIndent(0)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)
        self.CalcSecButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalcSecButton.setGeometry(QtCore.QRect(250, 350, 89, 23))
        self.CalcSecButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.CalcSecButton.setObjectName("CalcSecButton")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(380, 40, 671, 321))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.FilterLoadpushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.FilterLoadpushButton_6.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.FilterLoadpushButton_6.setObjectName("FilterLoadpushButton_6")
        self.gridLayout_5.addWidget(self.FilterLoadpushButton_6, 11, 0, 1, 1)
        self.Detectordata_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Detectordata_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.Detectordata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Detectordata_label.setObjectName("Detectordata_label")
        self.gridLayout_5.addWidget(self.Detectordata_label, 8, 1, 1, 1)
        self.DetectorLoadButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.DetectorLoadButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.DetectorLoadButton.setObjectName("DetectorLoadButton")
        self.gridLayout_5.addWidget(self.DetectorLoadButton, 8, 0, 1, 1)
        self.SpecChdata_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.SpecChdata_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.SpecChdata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SpecChdata_label.setObjectName("SpecChdata_label")
        self.gridLayout_5.addWidget(self.SpecChdata_label, 4, 1, 1, 1)
        self.BuildSpecChpushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.BuildSpecChpushButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.BuildSpecChpushButton.setObjectName("BuildSpecChpushButton")
        self.gridLayout_5.addWidget(self.BuildSpecChpushButton, 4, 0, 1, 1)
        self.ShowOrigFiltersButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.ShowOrigFiltersButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.ShowOrigFiltersButton.setObjectName("ShowOrigFiltersButton")
        self.gridLayout_5.addWidget(self.ShowOrigFiltersButton, 3, 0, 1, 1)
        self.FilterLoadpushButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.FilterLoadpushButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.FilterLoadpushButton.setObjectName("FilterLoadpushButton")
        self.gridLayout_5.addWidget(self.FilterLoadpushButton, 2, 0, 1, 1)
        self.FilterlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.FilterlineEdit.setObjectName("FilterlineEdit")
        self.gridLayout_5.addWidget(self.FilterlineEdit, 1, 1, 1, 1)
        self.FilterLoadpushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.FilterLoadpushButton_7.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.FilterLoadpushButton_7.setObjectName("FilterLoadpushButton_7")
        self.gridLayout_5.addWidget(self.FilterLoadpushButton_7, 12, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)
        self.FilterPolydata_label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.FilterPolydata_label_5.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.FilterPolydata_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.FilterPolydata_label_5.setObjectName("FilterPolydata_label_5")
        self.gridLayout_5.addWidget(self.FilterPolydata_label_5, 12, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.FilterPolydata_label_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.FilterPolydata_label_4.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.FilterPolydata_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.FilterPolydata_label_4.setObjectName("FilterPolydata_label_4")
        self.gridLayout_5.addWidget(self.FilterPolydata_label_4, 11, 1, 1, 1)
        self.DetectorShowData_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.DetectorShowData_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.DetectorShowData_label.setAlignment(QtCore.Qt.AlignCenter)
        self.DetectorShowData_label.setObjectName("DetectorShowData_label")
        self.gridLayout_5.addWidget(self.DetectorShowData_label, 9, 1, 1, 1)
        self.DetectorShowButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.DetectorShowButton.setStyleSheet("background-color: rgb(189, 255, 250);")
        self.DetectorShowButton.setObjectName("DetectorShowButton")
        self.gridLayout_5.addWidget(self.DetectorShowButton, 9, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 10, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 10, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 5, 0, 1, 1)
        self.filter_status_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.filter_status_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.filter_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filter_status_label.setObjectName("filter_status_label")
        self.gridLayout_5.addWidget(self.filter_status_label, 2, 1, 1, 1)
        self.Filter_Origdata_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Filter_Origdata_label.setStyleSheet("background-color: rgb(255, 94, 105);")
        self.Filter_Origdata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Filter_Origdata_label.setObjectName("Filter_Origdata_label")
        self.gridLayout_5.addWidget(self.Filter_Origdata_label, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 6, 0, 1, 1)
        self.DetectorPathlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.DetectorPathlineEdit.setObjectName("DetectorPathlineEdit")
        self.gridLayout_5.addWidget(self.DetectorPathlineEdit, 6, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(20, 380, 331, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ConcSpinBox.setSuffix(_translate("MainWindow", "*1E19, m^-3"))
        self.label_7.setText(_translate("MainWindow", "Plasma parameters "))
        self.TeSpinBox.setSuffix(_translate("MainWindow", " eV"))
        self.TionSpinBox.setSuffix(_translate("MainWindow", " eV"))
        self.label_9.setText(_translate("MainWindow", "Ion temperature"))
        self.label_3.setText(_translate("MainWindow", "Concentration"))
        self.label_10.setText(_translate("MainWindow", "Electron temperature"))
        self.label.setText(_translate("MainWindow", "Z effective"))
        self.label_8.setText(_translate("MainWindow", "Diagnostic parameters "))
        self.ThetaSpinBox.setSuffix(_translate("MainWindow", " deg "))
        self.label_4.setText(_translate("MainWindow", "Laser wavelength"))
        self.LEnSpinBox.setSuffix(_translate("MainWindow", " J"))
        self.LWSpinBox.setSuffix(_translate("MainWindow", " nm"))
        self.label_2.setText(_translate("MainWindow", "Theta scattering"))
        self.label_17.setText(_translate("MainWindow", "Laser energy"))
        self.label_6.setText(_translate("MainWindow", "Solpiter  (  1 / ( k *  D )  on laser wavelength )"))
        self.label_5.setText(_translate("MainWindow", "Debay radius, D = (T/(4*pi * n * e**2))^(1/2)"))
        self.label_18.setText(_translate("MainWindow", "start wavelength "))
        self.wlStartSpinBox.setSuffix(_translate("MainWindow", " nm"))
        self.label_20.setText(_translate("MainWindow", "end wavelength"))
        self.wlEndSpinBox.setSuffix(_translate("MainWindow", " nm "))
        self.label_21.setText(_translate("MainWindow", "steps number"))
        self.label_15.setText(_translate("MainWindow", "Section calculation parameters "))
        self.CalcSecButton.setText(_translate("MainWindow", "Calculate section"))
        self.FilterLoadpushButton_6.setText(_translate("MainWindow", "Build polychomator"))
        self.Detectordata_label.setText(_translate("MainWindow", "no data "))
        self.DetectorLoadButton.setText(_translate("MainWindow", "Load detector data"))
        self.SpecChdata_label.setText(_translate("MainWindow", "no data "))
        self.BuildSpecChpushButton.setText(_translate("MainWindow", "Buid and show spectral channels"))
        self.ShowOrigFiltersButton.setText(_translate("MainWindow", "Show original data"))
        self.FilterLoadpushButton.setText(_translate("MainWindow", "Load filter data"))
        self.FilterlineEdit.setText(_translate("MainWindow", "D:\\Ioffe\\divertor_thomson\\different_calcuations\\spectre_for_low_T\\expected\\\\filters16_19_doc.csv"))
        self.FilterLoadpushButton_7.setText(_translate("MainWindow", "Show poly data"))
        self.label_12.setText(_translate("MainWindow", "Path to filter data file: "))
        self.FilterPolydata_label_5.setText(_translate("MainWindow", "no data "))
        self.label_11.setText(_translate("MainWindow", "Filters data"))
        self.FilterPolydata_label_4.setText(_translate("MainWindow", "no data "))
        self.DetectorShowData_label.setText(_translate("MainWindow", "no data "))
        self.DetectorShowButton.setText(_translate("MainWindow", "Show detector data"))
        self.filter_status_label.setText(_translate("MainWindow", "no data "))
        self.Filter_Origdata_label.setText(_translate("MainWindow", "no data "))
        self.label_13.setText(_translate("MainWindow", "Path to detector data file: "))
        self.DetectorPathlineEdit.setText(_translate("MainWindow", "D:\\Ioffe\\divertor_thomson\\different_calcuations\\spectre_for_low_T\\expected\\S15995_qe.csv"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
