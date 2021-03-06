# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle


class Ui_PCIeApplicationStressTest(object):
    lnkdwntest_run = False
    pmtest_run = False
    aspmtest_run = False
    lnkrettest_run = False
    linkequtest_run = False

    def setupUi(self, PCIeApplicationStressTest):
        PCIeApplicationStressTest.setObjectName("PCIeApplicationStressTest")
        PCIeApplicationStressTest.resize(509, 361)
        PCIeApplicationStressTest.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                                "background-color: rgb(218, 218, 218);\n"
                                                "background-color: rgb(227, 227, 227);")
        self.progressBar = QtWidgets.QProgressBar(PCIeApplicationStressTest)
        self.progressBar.setGeometry(QtCore.QRect(390, 340, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_funcEP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_funcEP.setGeometry(QtCore.QRect(362, 60, 51, 20))
        self.lineEdit_funcEP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_funcEP.setText("")
        self.lineEdit_funcEP.setObjectName("lineEdit_funcEP")
        self.label_2 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_2.setGeometry(QtCore.QRect(320, 60, 31, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_EPok = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_EPok.setGeometry(QtCore.QRect(430, 60, 56, 17))
        self.pushButton_EPok.setObjectName("pushButton_EPok")

        def bdf_ep_ok():
            self.segep = self.lineEdit_segEP.text()
            self.busep = self.lineEdit_busEP.text()
            self.devep = self.lineEdit_devEP.text()
            self.funcep = self.lineEdit_funcEP.text()
            print(self.segep, self.busep, self.devep, self.funcep)
        self.pushButton_EPok.clicked.connect(bdf_ep_ok)
        self.listView = QtWidgets.QListView(PCIeApplicationStressTest)
        self.listView.setGeometry(QtCore.QRect(20, 121, 421, 191))
        self.listView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listView.setObjectName("listView")
        self.checkBox_LnkDwn = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_LnkDwn.setGeometry(QtCore.QRect(40, 160, 91, 25))
        self.checkBox_LnkDwn.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.checkBox_LnkDwn.setObjectName("checkBox_LnkDwn")
        self.checkBox_LnkRetrain = QtWidgets.QCheckBox(
            PCIeApplicationStressTest)
        self.checkBox_LnkRetrain.setGeometry(QtCore.QRect(40, 190, 81, 20))
        self.checkBox_LnkRetrain.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.checkBox_LnkRetrain.setObjectName("checkBox_LnkRetrain")
        """
        def lnk_ret_test():
            if self.checkBox_LnkRetrain.isChecked() == True and self.lnkrettest_run == False:
                self.lnkrettest = True
                self.lnkrettest_count = self.spinBox_LinkRet.value()
                self.label_LnkRet.setText("Run")
                self.lnkdrettest_run = True
                print("Run Link retrain test count", self.lnkrettest_count)
            else:
                print("Dont Run Link retrain test")
        self.pushButton_LnkRet.clicked.connect(lnk_ret_test)
        """
        self.checkBox_LinkEqua = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_LinkEqua.setGeometry(QtCore.QRect(40, 220, 91, 20))
        self.checkBox_LinkEqua.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.checkBox_LinkEqua.setObjectName("checkBox_LinkEqua")
        self.checkBox_PM = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_PM.setGeometry(QtCore.QRect(40, 250, 101, 20))
        self.checkBox_PM.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.checkBox_PM.setObjectName("checkBox_PM")
        self.checkBox_aspm = QtWidgets.QCheckBox(PCIeApplicationStressTest)
        self.checkBox_aspm.setGeometry(QtCore.QRect(40, 280, 101, 20))
        self.checkBox_aspm.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.checkBox_aspm.setObjectName("checkBox_aspm")
        self.spinBox_LinkDwn = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_LinkDwn.setGeometry(QtCore.QRect(160, 160, 41, 16))
        self.spinBox_LinkDwn.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_LinkDwn.setMinimum(10)
        self.spinBox_LinkDwn.setMaximum(10000)
        self.spinBox_LinkDwn.setObjectName("spinBox_LinkDwn")
        self.spinBox_LnkRet = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_LnkRet.setGeometry(QtCore.QRect(160, 190, 41, 16))
        self.spinBox_LnkRet.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_LnkRet.setMinimum(10)
        self.spinBox_LnkRet.setMaximum(1000)
        self.spinBox_LnkRet.setObjectName("spinBox_LnkRet")
        self.spinBox_LnkEqu = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_LnkEqu.setGeometry(QtCore.QRect(160, 220, 41, 16))
        self.spinBox_LnkEqu.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_LnkEqu.setMinimum(10)
        self.spinBox_LnkEqu.setMaximum(1000)
        self.spinBox_LnkEqu.setObjectName("spinBox_LnkEqu")
        self.spinBox_pm = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_pm.setGeometry(QtCore.QRect(160, 250, 41, 16))
        self.spinBox_pm.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_pm.setMinimum(10)
        self.spinBox_pm.setMaximum(1000)
        self.spinBox_pm.setObjectName("spinBox_pm")
        self.spinBox_aspm = QtWidgets.QSpinBox(PCIeApplicationStressTest)
        self.spinBox_aspm.setGeometry(QtCore.QRect(160, 280, 41, 16))
        self.spinBox_aspm.setStyleSheet(
            "alternate-background-color: rgb(255, 255, 255);")
        self.spinBox_aspm.setMinimum(10)
        self.spinBox_aspm.setMaximum(1000)
        self.spinBox_aspm.setObjectName("spinBox_aspm")
        self.verticalScrollBar = QtWidgets.QScrollBar(
            PCIeApplicationStressTest)
        self.verticalScrollBar.setGeometry(QtCore.QRect(400, 140, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_3 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 81, 16))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_4.setGeometry(QtCore.QRect(150, 130, 51, 16))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.pushButton_LnkDwn = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkDwn.setGeometry(QtCore.QRect(220, 160, 56, 17))
        self.pushButton_LnkDwn.setObjectName("pushButton_LnkDwn")

        def lnk_dwn_test():
            if self.checkBox_LnkDwn.isChecked() == True and self.lnkdwntest_run == False:
                self.lnkdwntest = True
                self.lnkdwntest_count = self.spinBox_LinkDwn.value()
                self.label_LnkDwn.setText("Run")
                self.lnkdwntest_run = True
                print("Run Link down test count", self.lnkdwntest_count)
            else:
                print("Dont Run Link down test")
        self.pushButton_LnkDwn.clicked.connect(lnk_dwn_test)
        self.pushButton_LnkRet = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkRet.setGeometry(QtCore.QRect(220, 190, 56, 17))
        self.pushButton_LnkRet.setObjectName("pushButton_LnkRet")

        def lnk_ret_test():
            if self.checkBox_LnkRetrain.isChecked() == True and self.lnkrettest_run == False:
                self.lnkrettest = True
                self.lnkrettest_count = self.spinBox_LnkRet.value()
                self.label_LnkRet.setText("Run")
                self.lnkrettest_run = True
                print("Run Link retrain test count", self.lnkrettest_count)
            else:
                print("Dont Run Link retrain test")
        self.pushButton_LnkRet.clicked.connect(lnk_ret_test)
        self.pushButton_LnkEq = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkEq.setGeometry(QtCore.QRect(220, 220, 56, 17))
        self.pushButton_LnkEq.setObjectName("pushButton_LnkEq")

        def lnk_equ_test():
            if self.checkBox_LinkEqua.isChecked() == True and self.linkequtest_run == False:
                self.lnkequtest = True
                self.lnkequtest_count = self.spinBox_LnkEqu.value()
                self.label_LnkEqu.setText("Run")
                self.linkequtest_run = True
                print("Run Link Equalization count", self.lnkequtest_count)
            else:
                print("Dont Run Link Equalization test")
        self.pushButton_LnkEq.clicked.connect(lnk_equ_test)
        self.pushButton_PM = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_PM.setGeometry(QtCore.QRect(220, 250, 56, 17))
        self.pushButton_PM.setObjectName("pushButton_PM")

        def pm_test():
            if self.checkBox_PM.isChecked() == True and self.pmtest_run == False:
                self.pmtest = True
                self.pmtest_count = self.spinBox_pm.value()
                self.label_pm.setText("Run")
                self.pmtest_run = True
                print("PM test count", self.pmtest_count)
            else:
                print("Dont Run PM test")
        self.pushButton_PM.clicked.connect(pm_test)

        self.pushButton_aspm = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_aspm.setGeometry(QtCore.QRect(220, 280, 56, 17))
        self.pushButton_aspm.setObjectName("pushButton_aspm")
        self.pushButton_aspmstp = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_aspmstp.setGeometry(QtCore.QRect(280, 280, 56, 17))
        self.pushButton_aspmstp.setObjectName("pushButton_aspmstp")

        def aspm_test_stp():
            if self.checkBox_aspm.isChecked() == True and self.aspmtest_run == True:
                self.label_aspm.setText("Idle")
                self.aspmtest_run = False
                print("stop aspm test count")
            else:
                print("Dont stop aspm test")
        self.pushButton_aspmstp.clicked.connect(aspm_test_stp)
        self.pushButton_LnkStop = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkStop.setGeometry(QtCore.QRect(280, 220, 56, 17))
        self.pushButton_LnkStop.setObjectName("pushButton_LnkStop")

        def lnk_equ_test_stp():
            if self.checkBox_LinkEqua.isChecked() == True and self.linkequtest_run == True:
                self.label_LnkEqu.setText("Idle")
                self.linkequtest_run = False
                print("stop Link Equ test")
            else:
                print("Dont stop Link Equ test")
        self.pushButton_LnkStop.clicked.connect(lnk_equ_test_stp)
        self.pushButton_LnkRetStop = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkRetStop.setGeometry(QtCore.QRect(280, 190, 56, 17))
        self.pushButton_LnkRetStop.setObjectName("pushButton_LnkRetStop")

        def lnkret_test_stp():
            if self.checkBox_LnkRetrain.isChecked() == True and self.lnkrettest_run == True:
                self.label_LnkRet.setText("Idle")
                self.lnkrettest_run = False
                print("stop lnk retrain test count")
            else:
                print("Dont stop lnk retrain test")
        self.pushButton_LnkRetStop.clicked.connect(lnkret_test_stp)
        self.pushButton_LnkDwn_stop2 = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_LnkDwn_stop2.setGeometry(
            QtCore.QRect(280, 160, 56, 17))
        self.pushButton_LnkDwn_stop2.setObjectName("pushButton_LnkDwn_stop2")

        def lnk_dwn_test_stp():
            if self.checkBox_LnkDwn.isChecked() == True and self.lnkdwntest_run == True:
                self.label_LnkDwn.setText("Idle")
                self.lnkdwntest_run = False
                print("Stop Link down")
            else:
                print("Dont stop test")
        self.pushButton_LnkDwn_stop2.clicked.connect(lnk_dwn_test_stp)
        self.pushButton_PMStp = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_PMStp.setGeometry(QtCore.QRect(280, 250, 56, 17))
        self.pushButton_PMStp.setObjectName("pushButton_PMStp")

        def pm_test_stp():
            if self.checkBox_PM.isChecked() == True and self.pmtest_run == True:
                self.label_pm.setText("Idle")
                self.pmtest_run = False
                print("Stop pm test")
            else:
                print("Dont stop test")
        self.pushButton_PMStp.clicked.connect(pm_test_stp)
        #self.pushButton_PMStp = QtWidgets.QPushButton(PCIeApplicationStressTest)
        #self.pushButton_PMStp.setGeometry(QtCore.QRect(280, 250, 56, 17))
        self.pushButton_RunAll = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_RunAll.setGeometry(QtCore.QRect(290, 100, 56, 17))
        self.pushButton_RunAll.setObjectName("pushButton_RunAll")
        self.pushButton_StopAll = QtWidgets.QPushButton(
            PCIeApplicationStressTest)
        self.pushButton_StopAll.setGeometry(QtCore.QRect(360, 100, 56, 17))
        self.pushButton_StopAll.setObjectName("pushButton_StopAll")
        self.label_5 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_5.setGeometry(QtCore.QRect(350, 130, 51, 20))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_LnkDwn = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_LnkDwn.setGeometry(QtCore.QRect(360, 160, 35, 16))
        self.label_LnkDwn.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.label_LnkDwn.setObjectName("label_LnkDwn")
        self.label_LnkRet = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_LnkRet.setGeometry(QtCore.QRect(360, 190, 35, 10))
        self.label_LnkRet.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.label_LnkRet.setObjectName("label_LnkRet")
        self.label_LnkEqu = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_LnkEqu.setGeometry(QtCore.QRect(360, 220, 35, 10))
        self.label_LnkEqu.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.label_LnkEqu.setObjectName("label_LnkEqu")
        self.label_pm = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_pm.setGeometry(QtCore.QRect(360, 250, 35, 10))
        self.label_pm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_pm.setObjectName("label_pm")
        self.label_aspm = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_aspm.setGeometry(QtCore.QRect(360, 280, 35, 10))
        self.label_aspm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_aspm.setObjectName("label_aspm")

        def aspm_test():
            if self.checkBox_aspm.isChecked() == True and self.aspmtest_run == False:
                self.aspmtest = True
                self.aspmtest_count = self.spinBox_aspm.value()
                self.label_aspm.setText("Run")
                self.aspmtest_run = True
                print("Run aspm test count", self.aspmtest_count)
            else:
                print("Dont Run Link down test")
        self.pushButton_aspm.clicked.connect(aspm_test)

        self.lineEdit_devEP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_devEP.setGeometry(QtCore.QRect(262, 60, 51, 20))
        self.lineEdit_devEP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_devEP.setText("")
        self.lineEdit_devEP.setObjectName("lineEdit_devEP")
        self.label_11 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_11.setGeometry(QtCore.QRect(220, 60, 31, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_busEP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_busEP.setGeometry(QtCore.QRect(162, 60, 51, 20))
        self.lineEdit_busEP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_busEP.setText("")
        self.lineEdit_busEP.setObjectName("lineEdit_busEP")
        self.label_12 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_12.setGeometry(QtCore.QRect(120, 60, 31, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_segEP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_segEP.setGeometry(QtCore.QRect(62, 60, 51, 20))
        self.lineEdit_segEP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_segEP.setText("0")
        self.lineEdit_segEP.setObjectName("lineEdit_segEP")
        self.label_13 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_13.setGeometry(QtCore.QRect(20, 60, 31, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_busRP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_busRP.setGeometry(QtCore.QRect(162, 20, 51, 20))
        self.lineEdit_busRP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_busRP.setText("")
        self.lineEdit_busRP.setObjectName("lineEdit_busRP")
        self.pushButton_RPok = QtWidgets.QPushButton(PCIeApplicationStressTest)
        self.pushButton_RPok.setGeometry(QtCore.QRect(430, 20, 56, 17))
        self.pushButton_RPok.setObjectName("pushButton_RPok")

        def bdf_rp_ok():
            self.segrp = self.lineEdit_segRP.text()
            self.busrp = self.lineEdit_busRP.text()
            self.devrp = self.lineEdit_devRP.text()
            self.funcrp = self.lineEdit_funcRP.text()
            print(self.segrp, self.busrp, self.devrp, self.funcrp)
        self.pushButton_RPok.clicked.connect(bdf_rp_ok)
        self.lineEdit_funcRP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_funcRP.setGeometry(QtCore.QRect(362, 20, 51, 20))
        self.lineEdit_funcRP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_funcRP.setText("")
        self.lineEdit_funcRP.setObjectName("lineEdit_funcRP")
        self.label_15 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_15.setGeometry(QtCore.QRect(220, 20, 31, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_segRP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_segRP.setGeometry(QtCore.QRect(62, 20, 51, 20))
        self.lineEdit_segRP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_segRP.setText("0")
        self.lineEdit_segRP.setObjectName("lineEdit_segRP")
        self.label_16 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_16.setGeometry(QtCore.QRect(320, 20, 31, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_devRP = QtWidgets.QLineEdit(PCIeApplicationStressTest)
        self.lineEdit_devRP.setGeometry(QtCore.QRect(262, 20, 51, 20))
        self.lineEdit_devRP.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.lineEdit_devRP.setText("")
        self.lineEdit_devRP.setObjectName("lineEdit_devRP")
        self.label_17 = QtWidgets.QLabel(PCIeApplicationStressTest)
        self.label_17.setGeometry(QtCore.QRect(120, 20, 31, 16))
        self.label_17.setObjectName("label_17")

        self.retranslateUi(PCIeApplicationStressTest)
        QtCore.QMetaObject.connectSlotsByName(PCIeApplicationStressTest)

    def retranslateUi(self, PCIeApplicationStressTest):
        _translate = QtCore.QCoreApplication.translate
        PCIeApplicationStressTest.setWindowTitle(_translate(
            "PCIeApplicationStressTest", "Cadence PCIe Application Stress Test"))
        self.label_2.setText(_translate("PCIeApplicationStressTest", "Func "))
        self.pushButton_EPok.setText(
            _translate("PCIeApplicationStressTest", "OK"))
        self.checkBox_LnkDwn.setText(_translate(
            "PCIeApplicationStressTest", "Link Down Test"))
        self.checkBox_LnkRetrain.setText(_translate(
            "PCIeApplicationStressTest", "Link Retrain Test"))
        self.checkBox_LinkEqua.setText(_translate(
            "PCIeApplicationStressTest", "Link Equalization Test"))
        self.checkBox_PM.setText(_translate(
            "PCIeApplicationStressTest", "PCI Power Down Test"))
        self.checkBox_aspm.setText(_translate(
            "PCIeApplicationStressTest", "ASPM Power Down Test"))
        self.label_3.setText(_translate(
            "PCIeApplicationStressTest", "Test Name"))
        self.label_4.setText(_translate("PCIeApplicationStressTest", "Count"))
        self.pushButton_LnkDwn.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_LnkRet.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_LnkEq.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_PM.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_aspm.setText(_translate(
            "PCIeApplicationStressTest", "Run Test"))
        self.pushButton_aspmstp.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_LnkStop.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_LnkRetStop.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_LnkDwn_stop2.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.pushButton_PMStp.setText(_translate(
            "PCIeApplicationStressTest", "Stop"))
        self.pushButton_RunAll.setText(_translate(
            "PCIeApplicationStressTest", "Run All "))
        self.pushButton_StopAll.setText(
            _translate("PCIeApplicationStressTest", "Stop"))
        self.label_5.setText(_translate("PCIeApplicationStressTest", "Status"))
        self.label_LnkDwn.setText(_translate(
            "PCIeApplicationStressTest", "Idle"))
        self.label_LnkRet.setText(_translate(
            "PCIeApplicationStressTest", "Idle"))
        self.label_LnkEqu.setText(_translate(
            "PCIeApplicationStressTest", "Idle"))
        self.label_pm.setText(_translate("PCIeApplicationStressTest", "Idle"))
        self.label_aspm.setText(_translate(
            "PCIeApplicationStressTest", "Idle"))
        self.label_11.setText(_translate("PCIeApplicationStressTest", "Dev"))
        self.label_12.setText(_translate("PCIeApplicationStressTest", "Bus"))
        self.label_13.setText(_translate("PCIeApplicationStressTest", "Seg"))
        self.label_14.setText(_translate("PCIeApplicationStressTest", "Seg"))
        self.pushButton_RPok.setText(
            _translate("PCIeApplicationStressTest", "OK"))
        self.label_15.setText(_translate("PCIeApplicationStressTest", "Dev"))
        self.label_16.setText(_translate("PCIeApplicationStressTest", "Func "))
        self.label_17.setText(_translate("PCIeApplicationStressTest", "Bus"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PCIeApplicationStressTest = QtWidgets.QDialog()
    ui = Ui_PCIeApplicationStressTest()
    ui.setupUi(PCIeApplicationStressTest)
    PCIeApplicationStressTest.show()
    #print("VALUE:", ui.lnkdwntest)

    test_param = {
        "link_down_test": True,
        "link_down_test_count": 10,
        "link_down_stat": ui.lnkdwntest_run,

        "link_ret_test": True,
        "link_ret_test_count": 10,
        "link_ret_stat": ui.lnkrettest_run,

        "link_equ_test": True,
        "link_equ_test_count": 10,
        "link_equ_stat": ui.linkequtest_run,
        "id": True,
        "aer": False,
        "d1": False,
        "d2": False,
    }
"""
    test_param = {
        "link_down_test": ui.lnkdwntest,
        "link_down_test_count": ui.lnkdwntest_count,
        "link_down_stat": ui.lnkdwntest_run,

        "link_ret_test": ui.lnkrettest,
        "link_ret_test_count": ui.lnkrettest_count,
        "link_ret_stat": ui.lnkrettest_run,

        "link_equ_test": ui.lnkequtest,
        "link_equ_test_count": ui.lnkequtest_count,
        "link_equ_stat": ui.linkequtest_run,
        "id": True,
        "aer": False,
        "d1": False,
        "d2": False,
    }
"""
sys.exit(app.exec_())
