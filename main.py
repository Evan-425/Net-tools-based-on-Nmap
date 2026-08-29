import os
import sys
import subprocess
import threading
import time

from PySide6.QtWidgets import QMainWindow, QApplication,QDialog
import sys
# import pygame
import time
from mainwindow import Ui_MainWindow
from result import Ui_Dialog2
from loginwindow import Ui_Dialog1
from warning import Ui_Dialog
from warning2 import Ui_Dialog3
with open(r'path.txt') as f:
    nmap_path = f.read()
    f.close()
flag=0
out1 = []
out2 = []
analyze_data=[]

is_init=0
check_pass=0
username=''
password1=''
password2=''
class loginwindow(QDialog,Ui_Dialog1):
    def __init__(self,*args, **kwargs):
        QDialog.__init__(self,*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check)
    def check(self):
        global username,password2,password1
        username=self.lineEdit.text()
        password1=self.lineEdit_2.text()
        password2=self.lineEdit_3.text()
        self.close()
        return True
class result(QDialog,Ui_Dialog2):
    def __init__(self,*args, **kwargs):
        QDialog.__init__(self,*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ok)
        self.listWidget.addItem('found'+str(len(ips))+'ipadress:')
        for i in ips:
            self.listWidget.addItem(i)

    def ok(self):
        self.close()

class Warning_init(QDialog, Ui_Dialog):
    def __init__(self,*args, **kwargs):
        QDialog.__init__(self,*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ok)
    def ok(self):
        self.close()
class Warning_text(QDialog, Ui_Dialog3):
    def __init__(self,*args, **kwargs):
        QDialog.__init__(self,*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ok)
    def ok(self):
        self.close()
class main_window(
    QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.pushButton_3.clicked.connect(self.on_button_clicked)
        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.reload)
        self.pushButton_4.clicked.connect(self.on_button_clicked2)
        self.pushButton_5.clicked.connect(self.on_button_clicked3)
        self.pushButton_6.clicked.connect(self.on_button_clicked4)
        self.pushButton_7.clicked.connect(self.on_button_clicked5)
        self.pushButton_8.clicked.connect(self.on_button_clicked6)
        try:
            with open(r'main.txt','r') as f:
                self.textEdit.setText(f.read())
                f.close()
        except:
            with open(r'main.txt','w') as f:
                f.write('')
                f.close()
    def warning_init(self):
        dialog = Warning_init()
        dialog.exec()
    def warning_text(self):
        dialog = Warning_text()
        dialog.exec()
    def init_check(self):
        global is_init
        if is_init==0:
            return True
        else:
            return False
    def scan(self,ip):
        self.listWidget.clear()

        def read_output(process):
            """在后台线程中持续读取输出"""
            for line in iter(process.stdout.readline, ''):
                if line:
                    self.listWidget_1.addItem(line.strip())
                out2.append(line.strip())
            process.stdout.close()
        nmap_order = {'Intense scan': [nmap_path, '-T4', '-A', '-v', str(ip)],
                      'Quick scan': [nmap_path, '-T4', '-F', str(ip)],
                      'Intense scan, all TCP ports': [nmap_path, '-p 1-65535', '-T4', '-A', '-v', str(ip)],
                      'Intense scan, no ping': [nmap_path, '-T4', '-A', '-v', '-Pn', str(ip)]
                      }
        # 启动进程
        process = subprocess.Popen(
            args=nmap_order[str(self.comboBox.currentText())],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        # 启动后台线程读取输出
        thread = threading.Thread(target=read_output, args=(process,), daemon=True)
        thread.start()
    def check(self):
        global nmap_path,username,password1,password2,check_pass
        if check_pass != 1:
            login=loginwindow()
            login.exec()
        if username=='admin' and password1=='qwedcxzas' and password2=='7355608':
            self.label_8.setText('身份验证通过')
            check_pass = 1
            try:
                process = subprocess.Popen(
                    args=[nmap_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                self.label.setText('Init Success!')

            except:
                self.label.setText('---Warning! Nmap not find---')
        else:
            login.close()
    def reload(self):
        global is_init
        if check_pass==1:
            is_init=1
            self.listWidget_3.clear()
            self.listWidget.clear()
            self.lineEdit.clear()
            nmap=['Quick scan','Intense scan','Intense scan plus UDP','Intense scan, all TCP ports','Intense scan, no ping']
            for i in range(101):
                self.progressBar.setValue(i)
                time.sleep(0.02)
            for i in nmap:
                self.comboBox.addItem(i)
                self.comboBox_2.addItem(i)
            self.label_2.setText('初始化完成')

            self.listWidget_2.clear()
            self.lineEdit_2.clear()
        else:
            self.check()
    def nmap1(self,ip):
        if not self.init_check():
            if ip != '':
                global out2
                self.scan(ip)
            else:
                self.warning_text()
        else:
            self.warning_init()
    def nmap2(self,ip):
        if not self.init_check():
            if ip != '':
                global out2
                self.scan(ip)
            else:
                self.warning_text()
        else:
            self.warning_init()

    def analyze(self, ip):
        if not self.init_check():
            if ip != '':
                self.listWidget_3.clear()
                global nmap_path
                global analyze_data, flag, thread

                def read_output(process):
                    """在后台线程中持续读取输出"""
                    for line in iter(process.stdout.readline, ''):
                        self.listWidget_3.addItem(line.strip())
                        temp = str(line.strip())
                        if 'Completed SYN Stealth Scan against' in temp:
                            analyze_data.append(line.strip())

                    process.stdout.close()

                # 启动进程
                process = subprocess.Popen(
                    args=[nmap_path, '-T4', '-A', '-v', str(ip)],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )

                # 🔥 启动后台线程读取输出
                thread = threading.Thread(target=read_output, args=(process,), daemon=True)
                thread.start()
            else:
                self.warning_text()
        else:
            self.warning_init()
    def command(self):
        os.startfile('cmd.exe')
    def on_button_clicked(self):
        global out1
        self.nmap1(self.lineEdit.text())
    def on_button_clicked2(self):
        self.command()
        global out1
        print(out1)
    def on_button_clicked3(self):
        self.nmap2(self.lineEdit_2.text())
    def on_button_clicked4(self):
        os.startfile(r'E:\Nmap\Zenmap')
    def on_button_clicked5(self):
        self.analyze(self.lineEdit_3.text())
    def on_button_clicked6(self):
        global analyze_data,ips
        ips = []
        if thread.is_alive():
            pass
        else:
            print(analyze_data)
            for i in analyze_data:
                ips.append(i[35:47])
            print(ips)
            results=result()
            results.exec()
app = QApplication(sys.argv)
window = main_window()
window.show()
sys.exit(app.exec())
