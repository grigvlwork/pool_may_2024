# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.hint1_le = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.hint1_le.setFont(font)
        self.hint1_le.setObjectName("hint1_le")
        self.horizontalLayout.addWidget(self.hint1_le)
        self.clear_hint1_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.clear_hint1_btn.setFont(font)
        self.clear_hint1_btn.setObjectName("clear_hint1_btn")
        self.horizontalLayout.addWidget(self.clear_hint1_btn)
        self.copy_hint1_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.copy_hint1_btn.setFont(font)
        self.copy_hint1_btn.setObjectName("copy_hint1_btn")
        self.horizontalLayout.addWidget(self.copy_hint1_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.hint2_le = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.hint2_le.setFont(font)
        self.hint2_le.setObjectName("hint2_le")
        self.horizontalLayout_2.addWidget(self.hint2_le)
        self.clear_hint2_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.clear_hint2_btn.setFont(font)
        self.clear_hint2_btn.setObjectName("clear_hint2_btn")
        self.horizontalLayout_2.addWidget(self.clear_hint2_btn)
        self.copy_hint2_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.copy_hint2_btn.setFont(font)
        self.copy_hint2_btn.setObjectName("copy_hint2_btn")
        self.horizontalLayout_2.addWidget(self.copy_hint2_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.hint3_le = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.hint3_le.setFont(font)
        self.hint3_le.setObjectName("hint3_le")
        self.horizontalLayout_3.addWidget(self.hint3_le)
        self.clear_hint3_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.clear_hint3_btn.setFont(font)
        self.clear_hint3_btn.setObjectName("clear_hint3_btn")
        self.horizontalLayout_3.addWidget(self.clear_hint3_btn)
        self.copy_hint3_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.copy_hint3_btn.setFont(font)
        self.copy_hint3_btn.setObjectName("copy_hint3_btn")
        self.horizontalLayout_3.addWidget(self.copy_hint3_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.answer_pte = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.answer_pte.setFont(font)
        self.answer_pte.setObjectName("answer_pte")
        self.verticalLayout.addWidget(self.answer_pte)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.clear_hints_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.clear_hints_btn.setFont(font)
        self.clear_hints_btn.setObjectName("clear_hints_btn")
        self.horizontalLayout_4.addWidget(self.clear_hints_btn)
        self.sql_env_rb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.sql_env_rb.setFont(font)
        self.sql_env_rb.setObjectName("sql_env_rb")
        self.horizontalLayout_4.addWidget(self.sql_env_rb)
        self.python_env_rb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.python_env_rb.setFont(font)
        self.python_env_rb.setObjectName("python_env_rb")
        self.horizontalLayout_4.addWidget(self.python_env_rb)
        self.js_env_rb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.js_env_rb.setFont(font)
        self.js_env_rb.setObjectName("js_env_rb")
        self.horizontalLayout_4.addWidget(self.js_env_rb)
        self.html_env_rb = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.html_env_rb.setFont(font)
        self.html_env_rb.setObjectName("html_env_rb")
        self.horizontalLayout_4.addWidget(self.html_env_rb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.hints_tv = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.hints_tv.setFont(font)
        self.hints_tv.setObjectName("hints_tv")
        self.verticalLayout_2.addWidget(self.hints_tv)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.copy_answer_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.copy_answer_btn.setFont(font)
        self.copy_answer_btn.setObjectName("copy_answer_btn")
        self.verticalLayout_3.addWidget(self.copy_answer_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Пул май 2024"))
        self.label.setText(_translate("MainWindow", "Подсказка 1"))
        self.clear_hint1_btn.setText(_translate("MainWindow", "X"))
        self.copy_hint1_btn.setText(_translate("MainWindow", "<"))
        self.label_2.setText(_translate("MainWindow", "Подсказка 2"))
        self.clear_hint2_btn.setText(_translate("MainWindow", "X"))
        self.copy_hint2_btn.setText(_translate("MainWindow", "<"))
        self.label_3.setText(_translate("MainWindow", "Подсказка 3"))
        self.clear_hint3_btn.setText(_translate("MainWindow", "X"))
        self.copy_hint3_btn.setText(_translate("MainWindow", "<"))
        self.clear_hints_btn.setText(_translate("MainWindow", "Очистить"))
        self.sql_env_rb.setText(_translate("MainWindow", "SQL"))
        self.python_env_rb.setText(_translate("MainWindow", "Python"))
        self.js_env_rb.setText(_translate("MainWindow", "Javascript"))
        self.html_env_rb.setText(_translate("MainWindow", "HTML"))
        self.copy_answer_btn.setText(_translate("MainWindow", "Копировать ответ"))
