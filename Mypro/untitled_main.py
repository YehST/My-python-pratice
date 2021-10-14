from __future__ import absolute_import, division, print_function
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep
import numpy as np
import serial.tools.list_ports

import untitled_ui as ui


from builtins import *  # @UnusedWildImport
from ctypes import cast, POINTER, c_double, c_ushort, c_ulong
from mcculw import ul
from mcculw.enums import ScanOptions, FunctionType, Status
from mcculw.device_info import DaqDeviceInfo

try:
    from console_examples_util import config_first_detected_device
except ImportError:
    from .console_examples_util import config_first_detected_device

# pyuic5 -x untitled.ui -o untitled_ui.py 刷新ui檔


class WorkThread(QThread):
    # 初始化线程
    def __int__(self):
        super(WorkThread, self).__init__()


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('Automatic adjustment')

        # StatusBar
        self.statusBar().showMessage('TEST')

        global C_value
        global D_value
        global E_value
        global F_value

# ________________________初始狀態設定_____________________________
        self.locate_x_value.setReadOnly(True)
        self.locate_y_value.setReadOnly(True)
        self.now_x_value.setReadOnly(True)
        self.now_y_value.setReadOnly(True)
        self.mistake_x_value.setReadOnly(True)
        self.mistake_y_value.setReadOnly(True)
        self.Arduino_port.setReadOnly(True)
        self.DAQ_port.setReadOnly(True)

        self.servo_x_CCW.setEnabled(False)
        self.servo_y_CCW.setEnabled(False)
        self.servo_x_STOP.setEnabled(False)
        self.servo_y_STOP.setEnabled(False)
        self.servo_x_CW.setEnabled(False)
        self.servo_y_CW.setEnabled(False)
        self.catchbutton.setEnabled(False)
        self.locatebutton.setEnabled(False)
        self.servobutton.setEnabled(False)
        self.stoptaskbutton.setEnabled(False)

        layout = QHBoxLayout()
        self.ManualMode.setChecked(True)
        self.ManualMode.toggled.connect(lambda: self.btnstate(self.ManualMode))
        layout.addWidget(self.ManualMode)

        self.AutoMode.toggled.connect(lambda: self.btnstate(self.AutoMode))
        layout.addWidget(self.AutoMode)
        self.setLayout(layout)

        self.getArduino.clicked.connect(self.getArduinoClicked)
        self.getDAQ.clicked.connect(self.getDAQClicked)
        self.catchbutton.clicked.connect(self.select0)
        self.locatebutton.clicked.connect(self.select1)
        self.servobutton.clicked.connect(self.select2)
        self.stoptaskbutton.clicked.connect(self.stopselect)
        self.test.clicked.connect(self.testclicked)

        self.Arduinoexist = '0'

        # ______________________button function_______________________

        self.servo_x_CW.clicked.connect(self.xCW)
        self.servo_x_STOP.clicked.connect(self.xSTOP)
        self.servo_x_CCW.clicked.connect(self.xCCW)
        self.servo_y_CW.clicked.connect(self.YCW)
        self.servo_y_STOP.clicked.connect(self.YSTOP)
        self.servo_y_CCW.clicked.connect(self.YCCW)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update2)
        self.timer3 = QTimer(self)
        self.timer3.timeout.connect(self.update3)
        self.timer4 = QTimer(self)
        self.timer4.timeout.connect(self.AutoX)
        self.timer5 = QTimer(self)
        self.timer5.timeout.connect(self.AutoY)

        self.avgchA = 0.0
        self.avgchB = 0.0
        self.avgchC = 0.0
        self.avgchD = 0.0


# ____________________________按鈕控制_____________________________

    def getArduinoClicked(self):
        ports = ('COM3', 'COM8')
        port, ok = QInputDialog.getItem(
            self, "select", "請選擇Arduino所在的連接埠", ports, 0, False)
        if ok and port:
            self.Arduino_port.setText(port)

        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) == 0:
            QMessageBox.warning(self, "警告", "找不到裝置",
                                QMessageBox.Retry, QMessageBox.Retry)
            self.Arduinoexist = '0'
        else:
            for i in range(0, len(port_list)):
                # print(port_list[i])
                if port in port_list[i]:
                    self.Arduinoexist = True
                else:
                    self.Arduinoexist = False
        # print(Arduinoexist)              #Arduino是否存在
        # print(port)
        if self.Arduinoexist == True:
            QMessageBox.information(
                self, "訊息", "請等待連接", QMessageBox.Ok, QMessageBox.Ok)
            self.Arduinoconnect()
            sleep(5)
            QMessageBox.information(
                self, "訊息", "已連接Arduino裝置", QMessageBox.Ok, QMessageBox.Ok)
            self.getArduino.setEnabled(False)

        elif self.Arduinoexist == False:
            QMessageBox.warning(
                self, "警告", "找不到Arduino裝置", QMessageBox.Ok, QMessageBox.Ok)

        else:
            pass

    def Arduinoconnect(self):  # 連接Arduino serial
        BAUD_RATES = 9600
        port = str(self.Arduino_port.text())
        self.ser = serial.Serial(port, BAUD_RATES)

        '''
        port = str(self.Arduino_port.text())     #Firmata方式
        global board
        board = Arduino(port)
        global pin
        pin = 9
        global pin2
        pin2 = 10
        board.digital[pin].mode = OUTPUT
        board.digital[pin].write(0)
        board.digital[pin2].mode = OUTPUT
        board.digital[pin2].write(0)
        '''

    def getDAQClicked(self):
        QMessageBox.information(
            self, "訊息", "請等待連接", QMessageBox.Ok, QMessageBox.Ok)
        # By default, the example detects and displays all available devices and
        # selects the first device listed. Use the dev_id_list variable to filter
        # detected devices by device ID (see UL documentation for device IDs).
        # If use_device_detection is set to False, the board_num variable needs to
        # match the desired board number configured with Instacal.
        self.use_device_detection = True
        self.dev_id_list = []
        self.board_num = 0

        if self.use_device_detection:
            config_first_detected_device(self.board_num, self.dev_id_list)

        daq_dev_info = DaqDeviceInfo(self.board_num)
        if not daq_dev_info.supports_analog_input:
            raise Exception('Error: The DAQ device does not support '
                            'analog input')

        # print('\nActive DAQ device: ', daq_dev_info.product_name, ' (',
        #      daq_dev_info.unique_id, ')\n', sep='')
        self.cha_num = []
        self.ai_info = daq_dev_info.get_ai_info()
        self.ai_range = self.ai_info.supported_ranges[0]
        self.DAQ_port.setText(daq_dev_info.product_name)
        QMessageBox.information(
            self, "訊息", "已連接裝置", QMessageBox.Ok, QMessageBox.Ok)

    def catchbuttonClicked(self):
        layout2 = QFormLayout()
        layout2.addRow(self.locate_x_value)
        layout2.addRow(self.locate_y_value)
        self.setLayout(layout2)
        self.Mytimer()
        self.Mytimer3()

    def locatebuttonClicked(self):
        C_value = self.A_value
        D_value = self.B_value
        self.locate_x_value.setText(str('%f' % C_value))
        self.locate_y_value.setText(str('%f' % D_value))
        layout2 = QFormLayout()
        layout2.addRow(self.locate_x_value)
        layout2.addRow(self.locate_y_value)
        self.setLayout(layout2)
        self.Mytimer2()
# x方向自動校正

    def servobuttonAutoX(self):
        reply = QMessageBox.question(
            self, "提問", "即將開始校正？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # print(reply)
        if reply == 16384:  # 16384為提問視窗按下Yes後回傳值
            self.Mytimer4()
        else:
            pass

    def testclicked(self):
        pass

    # _________________________Select_____________________________
    def select0(self):
        if self.DAQ_port.text() != "":
            self.catchbuttonClicked()
        else:
            self.msg0()

    def select1(self):
        if self.now_x_value.text() != "":
            self.locatebuttonClicked()
        else:
            self.msg1()

    def select2(self):
        if self.locate_x_value.text() != "":
            self.servobuttonAutoX()
        else:
            self.msg2()

    def stopselect(self):
        if self.now_x_value.text() != "":
            self.stoptask()
        else:
            self.stopfailmsg()

    # _________________________彈跳視窗_____________________________
    def msg0(self):
        QMessageBox.warning(
            self, "警告", "未連接擷取卡", QMessageBox.Ok, QMessageBox.Ok)
        # print(reply)

    def msg1(self):
        QMessageBox.warning(
            self, "警告", "無擷取資料無法定位", QMessageBox.Ok, QMessageBox.Ok)
        # print(reply)

    def msg2(self):
        QMessageBox.warning(
            self, "警告", "無定位資料無法開始校正", QMessageBox.Ok, QMessageBox.Ok)
        # print(reply)

    def stopfailmsg(self):
        QMessageBox.warning(
            self, "警告", "沒有資料可以清除", QMessageBox.Ok, QMessageBox.Ok)
        # print(reply)

    # _________________________計時器_____________________________

    def update(self):  # 當時間到時觸發函式    #擷取程式

        # Get a value from the device
        for i in range(0, 4):
            # if self.ai_info.resolution <= 16:
            # Use the v_in method for devices with a resolution <= 16
            # (optional parameter omitted)
            value = ul.v_in(self.board_num, i, self.ai_range)
            #    print(i, "\n")
            # else:
            # Use the v_in_32 method for devices with a resolution > 16
            # (optional parameter omitted)
            #value = ul.v_in_32(self.board_num, i, self.ai_range)
            #print(i, "+32\n")
            self.cha_num.append(value)

        # Display the value
        self.avgchA = self.avgchA+self.cha_num[0] + 1.455078
        self.avgchB = self.avgchB+self.cha_num[1] + 1.455078
        self.avgchC = self.avgchC+self.cha_num[2] + 1.445312
        self.avgchD = self.avgchD+self.cha_num[3] + 1.455078
        self.cha_num.clear()

    def update2(self):
        G_value = self.locate_x_value.text()
        H_value = self.locate_y_value.text()
        self.E_value = float(self.A_value) - float(G_value)
        self.F_value = float(self.B_value) - float(H_value)
        self.mistake_x_value.setText(str('%f' % self.E_value))
        self.mistake_y_value.setText(str('%f' % self.F_value))

    def update3(self):
        self.avgchA = np.round(self.avgchA/1, 6)  # A-B
        self.avgchB = np.round(self.avgchB/1, 6)  # A+B
        self.avgchC = np.round(self.avgchC/1, 6)  # C-D
        self.avgchD = np.round(self.avgchD/1, 6)  # C+D
        print('Value:{:6},{:6},{:6},{:6}'.format(
            self.avgchA, self.avgchB, self.avgchC, self.avgchD))
        self.A_value = (self.avgchA/self.avgchB)*-9.9937+0.0103
        self.B_value = (self.avgchC/self.avgchD)*-12.8752-0.0953
        self.now_x_value.setText(str('%f' % self.A_value))
        self.now_y_value.setText(str('%f' % self.B_value))
        self.avgchA = 0.0
        self.avgchB = 0.0
        self.avgchC = 0.0
        self.avgchD = 0.0

    def AutoX(self):
        if self.E_value > 5 or self.E_value < -5:
            self.timer4.stop()
            QMessageBox.warning(
                self, "異常", "X方向擷取資料超出範圍", QMessageBox.Ok, QMessageBox.Ok)

        elif -0.01 < self.E_value < 0.01:
            # self.xSTOP
            self.timer4.stop()
            QMessageBox.information(
                self, "訊息", "X方向校正完畢", QMessageBox.Ok, QMessageBox.Ok)
            self.Mytimer5()

        else:
            if self.E_value > 0:
                self.ser.write(b'XCC\n')
                sleep(0.1)
                self.ser.write(b'XS\n')
            else:
                self.ser.write(b'XC\n')
                sleep(0.1)
                self.ser.write(b'XS\n')

    def AutoY(self):
        if self.F_value > 5 or self.F_value < -5:
            self.timer5.stop()
            QMessageBox.warning(
                self, "異常", "Y方向擷取資料超出範圍", QMessageBox.Ok, QMessageBox.Ok)

        elif -0.01 < self.F_value < 0.01:
            # self.YSTOP
            self.timer5.stop()
            QMessageBox.information(
                self, "訊息", "Y方向校正完畢", QMessageBox.Ok, QMessageBox.Ok)
            QMessageBox.information(
                self, "訊息", "調校系統以校正完畢", QMessageBox.Ok, QMessageBox.Ok)

        else:
            if self.F_value > 0:
                self.ser.write(b'YC\n')
                sleep(0.1)
                self.ser.write(b'YS\n')

            else:
                self.ser.write(b'YCC\n')
                sleep(0.1)
                self.ser.write(b'YS\n')

    # 擷取資料

    def Mytimer(self):  # 開啟計時器 每100MS觸發一次上面函式

        self.timer.start(500)

    # 顯示誤差資料
    def Mytimer2(self):

        self.timer2.start(100)

    # 顯示擷取資料
    def Mytimer3(self):

        self.timer3.start(500)

    # X方向校正
    def Mytimer4(self):

        self.timer4.start(1000)

    # Y方向校正
    def Mytimer5(self):

        self.timer5.start(1000)

    # _________________________清除本次任務_____________________________

    def stoptask(self):
        reply = QMessageBox.question(
            self, "提問", "確定要清除本次資料嗎？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # print(reply)
        if reply == 16384:  # 16384為提問視窗按下Yes後回傳值
            self.timer.stop()
            self.timer2.stop()
            self.timer3.stop()
            self.timer4.stop()
            self.timer5.stop()
            self.now_x_value.clear()
            self.now_y_value.clear()
            self.locate_x_value.clear()
            self.locate_y_value.clear()
            self.mistake_x_value.clear()
            self.mistake_y_value.clear()
            self.DAQselect = False
            self.ser.write(b'XS\n')
            self.ser.write(b'YS\n')
            ul.stop_background(self.board_num, FunctionType.AIFUNCTION)
            print('Scan completed successfully')

        else:
            pass


# _______________________模式更換時按鈕隱藏___________________________

    def btnstate(self, btn):
        if btn.text() == "ManualMode":
            if btn.isChecked() == False:
                self.servo_x_CCW.setEnabled(False)
                self.servo_y_CCW.setEnabled(False)
                self.servo_x_STOP.setEnabled(False)
                self.servo_y_STOP.setEnabled(False)
                self.servo_x_CW.setEnabled(False)
                self.servo_y_CW.setEnabled(False)
                self.catchbutton.setEnabled(True)
                self.locatebutton.setEnabled(True)
                self.servobutton.setEnabled(True)
                self.stoptaskbutton.setEnabled(True)
                if self.Arduinoexist == True:
                    self.ser.write(b'XS\n')
                    self.ser.write(b'YS\n')
        if btn.text() == "AutoMode":
            if btn.isChecked() == False:
                self.servo_x_CCW.setEnabled(True)
                self.servo_x_CCW.setAutoRepeat(True)
                self.servo_y_CCW.setEnabled(True)
                self.servo_x_STOP.setEnabled(True)
                self.servo_y_STOP.setEnabled(True)
                self.servo_x_CW.setEnabled(True)
                self.servo_x_CW.setAutoRepeat(True)
                self.servo_y_CW.setEnabled(True)
                self.catchbutton.setEnabled(False)
                self.locatebutton.setEnabled(False)
                self.servobutton.setEnabled(False)
                self.stoptaskbutton.setEnabled(False)
                if self.Arduinoexist == True:
                    self.ser.write(b'XS\n')
                    self.ser.write(b'YS\n')


# 馬達函式


    def xCW(self):  # B servo X--
        # board.digital[pin].mode = SERVO
        # board.digital[pin].write(94)
        self.ser.write(b'XC\n')  # 訊息必須是位元組類型
        sleep(0.5)

    def xSTOP(self):
        # board.digital[pin].mode = OUTPUT
        # board.digital[pin].write(0)
        self.ser.write(b'XS\n')  # 訊息必須是位元組類型
        sleep(0.5)

    def xCCW(self):  # X++
        # board.digital[pin].mode = SERVO
        # board.digital[pin].write(100)
        self.ser.write(b'XCC\n')  # 訊息必須是位元組類型
        sleep(0.5)

    def YCW(self):  # A servo Y++
        # board.digital[pin2].mode = SERVO
        # board.digital[pin2].write(86)
        self.ser.write(b'YC\n')  # 訊息必須是位元組類型
        sleep(0.5)

    def YSTOP(self):
        # board.digital[pin2].mode = OUTPUT
        # board.digital[pin2].write(0)
        self.ser.write(b'YS\n')  # 訊息必須是位元組類型
        sleep(0.5)

    def YCCW(self):  # Y--
        # board.digital[pin2].mode = SERVO
        # board.digital[pin2].write(92)
        self.ser.write(b'YCC\n')  # 訊息必須是位元組類型
        sleep(0.5)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    workThread = WorkThread()
    workThread.start()

    sys.exit(app.exec_())
