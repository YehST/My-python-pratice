import sys
import sqlite3
import re
import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from POS_Design_by_Qt import Ui_Form
#from Enter_stock import Ui_Form2
from Enter_New_Item import Ui_Form3

#global value
item_price = 0
item_num = 0
total_price = 0
item_name = ''
item_dict = {}
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.stockButton.clicked.connect(self.stock_btn)
        self.ui.searchButton.clicked.connect(self.search_btn)
        self.ui.numButton.clicked.connect(self.num_btn)
        #self.ui.check_stockButton.clicked.connect(self.check_stock_btn)
        self.ui.settleButton.clicked.connect(self.settle_btn)
        self.ui.clearButton.clicked.connect(self.clear_btn)
        self.ui.cancelButton.clicked.connect(self.cancel_btn)
        self.ui.sells_stateButton.clicked.connect(self.sells_state_btn)
        self.ui.cancelorderButton.clicked.connect(self.cancel_order_btn)
        self.ui.revenueButton.clicked.connect(self.revenue_btn)
        #self.ui.eachitemButton.clicked.connect(self.each_item_btn)
        self.ui.num0.clicked.connect(self.num0)
        self.ui.num1.clicked.connect(self.num1)
        self.ui.num2.clicked.connect(self.num2)
        self.ui.num3.clicked.connect(self.num3)
        self.ui.num4.clicked.connect(self.num4)
        self.ui.num5.clicked.connect(self.num5)
        self.ui.num6.clicked.connect(self.num6)
        self.ui.num7.clicked.connect(self.num7)
        self.ui.num8.clicked.connect(self.num8)
        self.ui.num9.clicked.connect(self.num9)
        self.show()

    #商品清單
    def stock_btn(self):
        #建立SQLite連線
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('pos.db')
        self.db.open()
        #建立SQLite Model
        self.sqlt = QSqlTableModel()
        self.sqlt.setTable('product')
        self.sqlt.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.sqlt.select()
        #放入ui的tableView物件
        self.ui.tableView.setShowGrid(True)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.verticalHeader().setVisible(False)
        self.ui.tableView.setModel(self.sqlt)
        self.db.close()

    #商品查詢
    def search_btn(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('pos.db')
        self.db.open()

        str1 = self.ui.plainTextEdit.toPlainText()
        self.sqlt = QSqlQueryModel()
        execed = 'select * from product where name like '+ '\''+str1 + '\''
        self.sqlt.setQuery(execed)

        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.setModel(self.sqlt)
        
        self.db.close()

        self.ui.plainTextEdit.clear()
 
    #數量
    def num_btn(self):
        #數量
        num = self.ui.plainTextEdit.toPlainText()
        if num == '':#避免忘記選擇數量
            self.ui.Errorlabel.setText('商品數量錯誤')
        elif num != '':
            self.ui.Errorlabel.setText('')
            global item_num
            item_num = int(num)

            #品項&價格
            item = self.ui.tableView.currentIndex().data()
            if item == None:#避免忘記選擇商品
                self.ui.Errorlabel.setText('尚未選擇商品')
            elif item != None:
                self.ui.Errorlabel.setText('')
                execed = 'select price from product where name = ' + '\'' + item + '\''
                conn = sqlite3.connect("pos.db")
                cu = conn.cursor()
                cu.execute(execed)
                price = cu.fetchone()

                global item_price
                item_price = int(price[0])
                global item_name 
                item_name = item
                cu.close()

                #小計
                global total_price, item_dict
                total_price += item_num * item_price

                item_dict[item_name] = 'x' + str(item_num)

                #item_dict轉為字串且正規化存入check_list
                check = str(item_dict)
                check_list = re.sub(r'[\'{}:]', '', check)
                check_list = check_list.replace(' ', '')
                check_res = re.sub(',', '\n',check_list)

                self.ui.textBrowser.clear()
                self.ui.textBrowser.append(check_res + '\n\n金額累計:' + str(total_price))
                self.ui.plainTextEdit.clear()

                self.ui.tableView.setShowGrid(True)
                self.ui.tableView.horizontalHeader().setVisible(False)

    ''' 
    #庫存查詢
    def check_stock_btn(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('pos.db')
        self.db.open()
        #建立SQLite Model
        self.sqlt = QSqlTableModel()
        self.sqlt.setTable('stock')
        self.sqlt.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.sqlt.select()
        #放入ui的tableView物件
        self.ui.tableView.setShowGrid(True)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.setModel(self.sqlt)
        self.db.close()
    '''

    #結帳
    def settle_btn(self):
        global item_dict, total_price
        check = str(item_dict)
        check_list = re.sub(r'[\'{}:]','',check)
        check_list = check_list.replace(' ', '')
        check_msgbox = re.sub(',', '\n',check_list)
        print(type(check_list))
        print(check_list)
        check_msg = QMessageBox()
        check_msg.setStyleSheet('QMessageBox{font-size:25px;}\nQPushButton{font-size:20px;}')
        money = self.ui.plainTextEdit.toPlainText()
        if money == '':#避免忘記輸入付款金額
            self.ui.Errorlabel.setText('付款金額尚未輸入')
        elif money != '':
            self.ui.Errorlabel.setText('')
            money_int = int(money)
            cash = money_int - total_price
            check_msg.setWindowTitle('結帳')
            check_msg.setText('總金額:' + str(total_price) + '\n' + 
                            '找零:' + str(cash) + '\n\n' + '品項:' + '\n' + check_msgbox)
            check_msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            reValue = check_msg.exec()
            if reValue == QMessageBox.Ok:
                sell_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                execed = 'insert into sells values(' + '\'' + sell_time + '\'' + ',\'' + check_list + '\',' + str(total_price) + ')'
                conn = sqlite3.connect("pos.db")
                cu = conn.cursor()
                cu.execute(execed)
                conn.commit()
                cu.close()
                self.ui.textBrowser.clear()
                self.ui.plainTextEdit.clear()
                total_price = 0
                item_dict = {}
            elif reValue == QMessageBox.Cancel:
                self.ui.plainTextEdit.clear()
                print('cancel')
            check_msg.show()

    #數字鍵
    def num0(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('0')
        elif str_chk != None:
            str_new = str_chk + '0'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num1(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('1')
        elif str_chk != None:
            str_new = str_chk + '1'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num2(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('2')
        elif str_chk != None:
            str_new = str_chk + '2'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num3(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('3')
        elif str_chk != None:
            str_new = str_chk + '3'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num4(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('4')
        elif str_chk != None:
            str_new = str_chk + '4'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num5(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('5')
        elif str_chk != None:
            str_new = str_chk + '5'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num6(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('6')
        elif str_chk != None:
            str_new = str_chk + '6'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num7(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('7')
        elif str_chk != None:
            str_new = str_chk + '7'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num8(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('8')
        elif str_chk != None:
            str_new = str_chk + '8'
            self.ui.plainTextEdit.setPlainText(str_new)
    def num9(self):
        str_chk = self.ui.plainTextEdit.toPlainText()
        if str_chk == None:
            self.ui.plainTextEdit.setPlainText('9')
        elif str_chk != None:
            str_new = str_chk + '9'
            self.ui.plainTextEdit.setPlainText(str_new)
    
    #清除
    def clear_btn(self):
        self.ui.plainTextEdit.clear()
    
    #取消
    def cancel_btn(self):
        self.ui.textBrowser.clear()
        global total_price, item_dict
        total_price = 0
        item_dict = {}
    
    #銷售狀況
    def sells_state_btn(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('pos.db')
        self.db.open()

        self.sqlt = QSqlTableModel()
        self.sqlt.setTable('sells')
        self.sqlt.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.sqlt.select()

        self.ui.tableView.setShowGrid(True)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setVisible(False)
        self.ui.tableView.verticalHeader().setVisible(False)
        self.ui.tableView.setModel(self.sqlt)
        self.db.close()
    
    #刪除訂單
    def cancel_order_btn(self):
        #刪除
        target = self.ui.tableView.currentIndex().data()
        #print(len(target)) = 19
        if target == None:
            self.ui.Errorlabel.setText('選擇日期欄位進行刪除')
        elif len(target) != 19:
            self.ui.Errorlabel.setText('選擇日期欄位進行刪除')
        elif len(target) == 19:
            self.ui.Errorlabel.clear()
            execed = 'delete from sells where date = ' + '\'' + target + '\''
            conn = sqlite3.connect("pos.db")
            cu = conn.cursor()
            cu.execute(execed)
            conn.commit()
            cu.close()
            #顯示刪除後結果
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName('pos.db')
            self.db.open()

            self.sqlt = QSqlTableModel()
            self.sqlt.setTable('sells')
            self.sqlt.setEditStrategy(QSqlTableModel.OnManualSubmit)
            self.sqlt.select()

            self.ui.tableView.setShowGrid(True)
            self.ui.tableView.horizontalHeader().setStretchLastSection(True)
            self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.tableView.horizontalHeader().setVisible(False)
            self.ui.tableView.verticalHeader().setVisible(False)
            self.ui.tableView.setModel(self.sqlt)
            self.db.close()

    #銷售額
    def revenue_btn(self):
        execed = 'select price from sells'
        conn = sqlite3.connect("pos.db")
        cu = conn.cursor()
        cu.execute(execed)
        revenue = cu.fetchall()
        total = 0
        for i in range (0, len(revenue)):
            res = revenue[i]
            res_format = re.sub(r'[,()]','',str(res))
            c = int(res_format)
            total += c
        revenue_msg = QMessageBox()
        revenue_msg.setStyleSheet('QMessageBox{font-size:25px;}\nQPushButton{font-size:20px;}')
        revenue_msg.setWindowTitle('總銷售額')
        revenue_msg.setText('總銷售額:' + str(total) + '元')
        revenue_msg.setStandardButtons(QMessageBox.Ok)
        reValue = revenue_msg.exec()
        if reValue == QMessageBox.Ok:
            self.ui.Errorlabel.setText('總銷售額:' + str(total) + '元')
        revenue_msg.show()

    #單項銷售
    #def each_item_btn(self):

'''
#登入庫存視窗
class Enter_stock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_Form2()
        self.ui2.setupUi(self)
        self.ui2.pushButton.clicked.connect(self.ok_btn)
        #顯示庫存
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('pos.db')
        self.db.open()

        self.sqlt = QSqlTableModel()
        self.sqlt.setTable('stock')
        self.sqlt.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.sqlt.select()

        self.ui2.tableView.setShowGrid(True)
        self.ui2.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui2.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui2.tableView.horizontalHeader().setVisible(False)
        self.ui2.tableView.setModel(self.sqlt)

        self.db.close()

        self.ui2.label_3.setText(' ')
    #確認
    def ok_btn(self):
        item = self.ui2.tableView.currentIndex().data()
        self.ui2.label_3.setText(str(item))

        number = self.ui2.plainTextEdit.toPlainText()

        execed = 'update stock set stock = ' + number + ' where name = ' + '\'' + item + '\''
        conn = sqlite3.connect("pos.db")
        cu = conn.cursor()
        cu.execute(execed)
        conn.commit()
        cu.close()

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('pos.db')
        self.db.open()

        self.sqlt = QSqlTableModel()
        self.sqlt.setTable('stock')
        self.sqlt.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.sqlt.select()

        self.ui2.tableView.setShowGrid(True)
        self.ui2.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui2.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui2.tableView.horizontalHeader().setVisible(False)
        self.ui2.tableView.setModel(self.sqlt)

        self.db.close()
'''
#登入新品項
class Enter_New_Item(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui3 = Ui_Form3()
        self.ui3.setupUi(self)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('pos.db')
        self.db.open()

        self.sqlt = QSqlTableModel()
        self.sqlt.setTable('product')
        self.sqlt.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.sqlt.select()

        self.ui3.tableView.setShowGrid(True)
        self.ui3.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui3.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui3.tableView.horizontalHeader().setVisible(False)
        self.ui3.tableView.verticalHeader().setVisible(False)
        self.ui3.tableView.setModel(self.sqlt)

        self.db.close()

        self.ui3.okButton.clicked.connect(self.ok_btn)

    def ok_btn(self):
        sql_name = self.ui3.name_textEdit_2.toPlainText()
        sql_price = self.ui3.price_textEdit_3.toPlainText()

        execed = 'insert into product values(' + '\'' + sql_name + '\',' + sql_price + ')'
        print(execed)
        
        conn = sqlite3.connect('pos.db')
        cu = conn.cursor()
        cu.execute(execed)
        conn.commit()
        cu.close()
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('pos.db')
        self.db.open()

        self.sqlt = QSqlTableModel()
        self.sqlt.setTable('product')
        self.sqlt.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.sqlt.select()

        self.ui3.tableView.setShowGrid(True)
        self.ui3.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui3.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui3.tableView.horizontalHeader().setVisible(False)
        self.ui3.tableView.verticalHeader().setVisible(False)
        self.ui3.tableView.setModel(self.sqlt)

        self.db.close()


app = QApplication(sys.argv)
form = MainWindow()
#form2 = Enter_stock()
form3 = Enter_New_Item()
#form.ui.enter_stockButton.clicked.connect(form2.show)
form.ui.enter_itemButton.clicked.connect(form3.show)
form.show()
sys.exit(app.exec_())