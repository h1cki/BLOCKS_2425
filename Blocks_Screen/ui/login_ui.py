# Form implementation generated from reading ui file 'c:\Users\Asus\Documents\Universidade\Estágio\BLOCKS\App\Blocks_Screen\ui\login.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StackedWidget.sizePolicy().hasHeightForWidth())
        StackedWidget.setSizePolicy(sizePolicy)
        StackedWidget.setBaseSize(QtCore.QSize(800, 480))
        font = QtGui.QFont()
        font.setFamily("Arial")
        StackedWidget.setFont(font)
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.login_label = QtWidgets.QLabel(parent=self.login_page)
        self.login_label.setGeometry(QtCore.QRect(120, 80, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.wifi_button = QtWidgets.QPushButton(parent=self.login_page)
        self.wifi_button.setGeometry(QtCore.QRect(730, 20, 50, 50))
        self.wifi_button.setObjectName("wifi_button")
        self.userlist_login = QtWidgets.QComboBox(parent=self.login_page)
        self.userlist_login.setGeometry(QtCore.QRect(120, 200, 541, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.userlist_login.setFont(font)
        self.userlist_login.setObjectName("userlist_login")
        self.cancel_login_button = QtWidgets.QPushButton(parent=self.login_page)
        self.cancel_login_button.setGeometry(QtCore.QRect(120, 320, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_login_button.setFont(font)
        self.cancel_login_button.setObjectName("cancel_login_button")
        self.login_admin_button = QtWidgets.QPushButton(parent=self.login_page)
        self.login_admin_button.setGeometry(QtCore.QRect(590, 350, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_admin_button.setFont(font)
        self.login_admin_button.setObjectName("login_admin_button")
        StackedWidget.addWidget(self.login_page)
        self.password_page = QtWidgets.QWidget()
        self.password_page.setObjectName("password_page")
        self.password_label = QtWidgets.QLabel(parent=self.password_page)
        self.password_label.setGeometry(QtCore.QRect(120, 80, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.password_input = QtWidgets.QLineEdit(parent=self.password_page)
        self.password_input.setGeometry(QtCore.QRect(120, 200, 531, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.wifi_button_2 = QtWidgets.QPushButton(parent=self.password_page)
        self.wifi_button_2.setGeometry(QtCore.QRect(730, 20, 50, 50))
        self.wifi_button_2.setObjectName("wifi_button_2")
        self.cancel_password_button = QtWidgets.QPushButton(parent=self.password_page)
        self.cancel_password_button.setGeometry(QtCore.QRect(120, 330, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_password_button.setFont(font)
        self.cancel_password_button.setObjectName("cancel_password_button")
        self.user_login_button = QtWidgets.QPushButton(parent=self.password_page)
        self.user_login_button.setGeometry(QtCore.QRect(630, 360, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_login_button.setFont(font)
        self.user_login_button.setObjectName("user_login_button")
        self.login_invalid_label = QtWidgets.QLabel(parent=self.password_page)
        self.login_invalid_label.setGeometry(QtCore.QRect(380, 290, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_invalid_label.setFont(font)
        self.login_invalid_label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.login_invalid_label.setText("")
        self.login_invalid_label.setObjectName("login_invalid_label")
        StackedWidget.addWidget(self.password_page)
        self.admin_login_page = QtWidgets.QWidget()
        self.admin_login_page.setObjectName("admin_login_page")
        self.cancel_admin_login_button = QtWidgets.QPushButton(parent=self.admin_login_page)
        self.cancel_admin_login_button.setGeometry(QtCore.QRect(120, 330, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_admin_login_button.setFont(font)
        self.cancel_admin_login_button.setObjectName("cancel_admin_login_button")
        self.login_admin_label = QtWidgets.QLabel(parent=self.admin_login_page)
        self.login_admin_label.setGeometry(QtCore.QRect(120, 90, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.login_admin_label.setFont(font)
        self.login_admin_label.setObjectName("login_admin_label")
        self.wifi_button_3 = QtWidgets.QPushButton(parent=self.admin_login_page)
        self.wifi_button_3.setGeometry(QtCore.QRect(720, 30, 50, 50))
        self.wifi_button_3.setObjectName("wifi_button_3")
        self.admin_user_list = QtWidgets.QComboBox(parent=self.admin_login_page)
        self.admin_user_list.setGeometry(QtCore.QRect(120, 210, 541, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.admin_user_list.setFont(font)
        self.admin_user_list.setObjectName("admin_user_list")
        StackedWidget.addWidget(self.admin_login_page)
        self.admin_password_page = QtWidgets.QWidget()
        self.admin_password_page.setObjectName("admin_password_page")
        self.admin_password_input = QtWidgets.QLineEdit(parent=self.admin_password_page)
        self.admin_password_input.setGeometry(QtCore.QRect(110, 210, 521, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.admin_password_input.setFont(font)
        self.admin_password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.admin_password_input.setObjectName("admin_password_input")
        self.wifi_button_4 = QtWidgets.QPushButton(parent=self.admin_password_page)
        self.wifi_button_4.setGeometry(QtCore.QRect(720, 30, 50, 50))
        self.wifi_button_4.setObjectName("wifi_button_4")
        self.password_admin_label = QtWidgets.QLabel(parent=self.admin_password_page)
        self.password_admin_label.setGeometry(QtCore.QRect(110, 90, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.password_admin_label.setFont(font)
        self.password_admin_label.setObjectName("password_admin_label")
        self.cancel_admin_password_button = QtWidgets.QPushButton(parent=self.admin_password_page)
        self.cancel_admin_password_button.setGeometry(QtCore.QRect(110, 330, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_admin_password_button.setFont(font)
        self.cancel_admin_password_button.setObjectName("cancel_admin_password_button")
        self.admin_login_done_button = QtWidgets.QPushButton(parent=self.admin_password_page)
        self.admin_login_done_button.setGeometry(QtCore.QRect(630, 370, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.admin_login_done_button.setFont(font)
        self.admin_login_done_button.setObjectName("admin_login_done_button")
        self.login_admin_invalid_label = QtWidgets.QLabel(parent=self.admin_password_page)
        self.login_admin_invalid_label.setGeometry(QtCore.QRect(340, 310, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_admin_invalid_label.setFont(font)
        self.login_admin_invalid_label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.login_admin_invalid_label.setText("")
        self.login_admin_invalid_label.setObjectName("login_admin_invalid_label")
        StackedWidget.addWidget(self.admin_password_page)
        self.admin_page = QtWidgets.QWidget()
        self.admin_page.setObjectName("admin_page")
        self.admin_page_label = QtWidgets.QLabel(parent=self.admin_page)
        self.admin_page_label.setGeometry(QtCore.QRect(70, 50, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.admin_page_label.setFont(font)
        self.admin_page_label.setObjectName("admin_page_label")
        self.wifi_button_5 = QtWidgets.QPushButton(parent=self.admin_page)
        self.wifi_button_5.setGeometry(QtCore.QRect(720, 30, 50, 50))
        self.wifi_button_5.setObjectName("wifi_button_5")
        self.admin_page_back_button = QtWidgets.QPushButton(parent=self.admin_page)
        self.admin_page_back_button.setGeometry(QtCore.QRect(60, 410, 111, 41))
        self.admin_page_back_button.setObjectName("admin_page_back_button")
        self.add_user_button = QtWidgets.QPushButton(parent=self.admin_page)
        self.add_user_button.setGeometry(QtCore.QRect(410, 420, 101, 41))
        self.add_user_button.setObjectName("add_user_button")
        self.remove_user_button = QtWidgets.QPushButton(parent=self.admin_page)
        self.remove_user_button.setGeometry(QtCore.QRect(660, 420, 101, 41))
        self.remove_user_button.setObjectName("remove_user_button")
        self.reset_password_button = QtWidgets.QPushButton(parent=self.admin_page)
        self.reset_password_button.setGeometry(QtCore.QRect(530, 420, 111, 41))
        self.reset_password_button.setObjectName("reset_password_button")
        self.admin_table = QtWidgets.QTableWidget(parent=self.admin_page)
        self.admin_table.setGeometry(QtCore.QRect(70, 130, 641, 251))
        self.admin_table.setShowGrid(False)
        self.admin_table.setColumnCount(0)
        self.admin_table.setObjectName("admin_table")
        self.admin_table.setRowCount(0)
        self.admin_table.verticalHeader().setVisible(False)
        self.admin_info_label = QtWidgets.QLabel(parent=self.admin_page)
        self.admin_info_label.setGeometry(QtCore.QRect(380, 390, 331, 20))
        self.admin_info_label.setText("")
        self.admin_info_label.setObjectName("admin_info_label")
        StackedWidget.addWidget(self.admin_page)
        self.new_username_page = QtWidgets.QWidget()
        self.new_username_page.setObjectName("new_username_page")
        self.cancel_add_user_button = QtWidgets.QPushButton(parent=self.new_username_page)
        self.cancel_add_user_button.setGeometry(QtCore.QRect(100, 340, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_add_user_button.setFont(font)
        self.cancel_add_user_button.setObjectName("cancel_add_user_button")
        self.new_user_done_button_1 = QtWidgets.QPushButton(parent=self.new_username_page)
        self.new_user_done_button_1.setGeometry(QtCore.QRect(580, 380, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_user_done_button_1.setFont(font)
        self.new_user_done_button_1.setObjectName("new_user_done_button_1")
        self.add_user_label = QtWidgets.QLabel(parent=self.new_username_page)
        self.add_user_label.setGeometry(QtCore.QRect(110, 90, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.add_user_label.setFont(font)
        self.add_user_label.setObjectName("add_user_label")
        self.wifi_button_6 = QtWidgets.QPushButton(parent=self.new_username_page)
        self.wifi_button_6.setGeometry(QtCore.QRect(720, 30, 50, 50))
        self.wifi_button_6.setObjectName("wifi_button_6")
        self.add_user_username_input = QtWidgets.QLineEdit(parent=self.new_username_page)
        self.add_user_username_input.setGeometry(QtCore.QRect(100, 190, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_user_username_input.setFont(font)
        self.add_user_username_input.setObjectName("add_user_username_input")
        self.add_username_invalid_label = QtWidgets.QLabel(parent=self.new_username_page)
        self.add_username_invalid_label.setGeometry(QtCore.QRect(250, 300, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_username_invalid_label.setFont(font)
        self.add_username_invalid_label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.add_username_invalid_label.setText("")
        self.add_username_invalid_label.setObjectName("add_username_invalid_label")
        StackedWidget.addWidget(self.new_username_page)
        self.new_user_password_page = QtWidgets.QWidget()
        self.new_user_password_page.setObjectName("new_user_password_page")
        self.wifi_button_7 = QtWidgets.QPushButton(parent=self.new_user_password_page)
        self.wifi_button_7.setGeometry(QtCore.QRect(720, 30, 50, 50))
        self.wifi_button_7.setObjectName("wifi_button_7")
        self.add_user_label_2 = QtWidgets.QLabel(parent=self.new_user_password_page)
        self.add_user_label_2.setGeometry(QtCore.QRect(110, 90, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.add_user_label_2.setFont(font)
        self.add_user_label_2.setObjectName("add_user_label_2")
        self.cancel_add_password_button = QtWidgets.QPushButton(parent=self.new_user_password_page)
        self.cancel_add_password_button.setGeometry(QtCore.QRect(100, 340, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_add_password_button.setFont(font)
        self.cancel_add_password_button.setObjectName("cancel_add_password_button")
        self.add_user_password_input = QtWidgets.QLineEdit(parent=self.new_user_password_page)
        self.add_user_password_input.setGeometry(QtCore.QRect(100, 190, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add_user_password_input.setFont(font)
        self.add_user_password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.add_user_password_input.setObjectName("add_user_password_input")
        self.new_user_done_button_2 = QtWidgets.QPushButton(parent=self.new_user_password_page)
        self.new_user_done_button_2.setGeometry(QtCore.QRect(590, 370, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_user_done_button_2.setFont(font)
        self.new_user_done_button_2.setObjectName("new_user_done_button_2")
        self.add_pwd_invalid_label = QtWidgets.QLabel(parent=self.new_user_password_page)
        self.add_pwd_invalid_label.setGeometry(QtCore.QRect(270, 290, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_pwd_invalid_label.setFont(font)
        self.add_pwd_invalid_label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.add_pwd_invalid_label.setText("")
        self.add_pwd_invalid_label.setObjectName("add_pwd_invalid_label")
        StackedWidget.addWidget(self.new_user_password_page)
        self.reset_password = QtWidgets.QWidget()
        self.reset_password.setObjectName("reset_password")
        self.wifi_button_8 = QtWidgets.QPushButton(parent=self.reset_password)
        self.wifi_button_8.setGeometry(QtCore.QRect(710, 30, 50, 50))
        self.wifi_button_8.setObjectName("wifi_button_8")
        self.reset_password_done_button = QtWidgets.QPushButton(parent=self.reset_password)
        self.reset_password_done_button.setGeometry(QtCore.QRect(580, 370, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_password_done_button.setFont(font)
        self.reset_password_done_button.setObjectName("reset_password_done_button")
        self.cancel_reset_password_button = QtWidgets.QPushButton(parent=self.reset_password)
        self.cancel_reset_password_button.setGeometry(QtCore.QRect(90, 340, 93, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_reset_password_button.setFont(font)
        self.cancel_reset_password_button.setObjectName("cancel_reset_password_button")
        self.add_user_label_3 = QtWidgets.QLabel(parent=self.reset_password)
        self.add_user_label_3.setGeometry(QtCore.QRect(100, 90, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.add_user_label_3.setFont(font)
        self.add_user_label_3.setObjectName("add_user_label_3")
        self.reset_password_input = QtWidgets.QLineEdit(parent=self.reset_password)
        self.reset_password_input.setGeometry(QtCore.QRect(90, 190, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.reset_password_input.setFont(font)
        self.reset_password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.reset_password_input.setObjectName("reset_password_input")
        self.reset_pwd_invalid_label = QtWidgets.QLabel(parent=self.reset_password)
        self.reset_pwd_invalid_label.setGeometry(QtCore.QRect(230, 290, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_pwd_invalid_label.setFont(font)
        self.reset_pwd_invalid_label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.reset_pwd_invalid_label.setText("")
        self.reset_pwd_invalid_label.setObjectName("reset_pwd_invalid_label")
        StackedWidget.addWidget(self.reset_password)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.login_label.setText(_translate("StackedWidget", "Login"))
        self.wifi_button.setText(_translate("StackedWidget", "Wifi"))
        self.cancel_login_button.setText(_translate("StackedWidget", "Cancel"))
        self.login_admin_button.setText(_translate("StackedWidget", "Login as Admin"))
        self.password_label.setText(_translate("StackedWidget", "Password"))
        self.wifi_button_2.setText(_translate("StackedWidget", "Wifi"))
        self.cancel_password_button.setText(_translate("StackedWidget", "Cancel"))
        self.user_login_button.setText(_translate("StackedWidget", "Log In"))
        self.cancel_admin_login_button.setText(_translate("StackedWidget", "Cancel"))
        self.login_admin_label.setText(_translate("StackedWidget", "Login Admin"))
        self.wifi_button_3.setText(_translate("StackedWidget", "Wifi"))
        self.wifi_button_4.setText(_translate("StackedWidget", "Wifi"))
        self.password_admin_label.setText(_translate("StackedWidget", "Password Admin"))
        self.cancel_admin_password_button.setText(_translate("StackedWidget", "Cancel"))
        self.admin_login_done_button.setText(_translate("StackedWidget", "Done"))
        self.admin_page_label.setText(_translate("StackedWidget", "Admin Page"))
        self.wifi_button_5.setText(_translate("StackedWidget", "Wifi"))
        self.admin_page_back_button.setText(_translate("StackedWidget", "Back"))
        self.add_user_button.setText(_translate("StackedWidget", "Add user"))
        self.remove_user_button.setText(_translate("StackedWidget", "Remove User"))
        self.reset_password_button.setText(_translate("StackedWidget", "Reset Password"))
        self.cancel_add_user_button.setText(_translate("StackedWidget", "Cancel"))
        self.new_user_done_button_1.setText(_translate("StackedWidget", "Done"))
        self.add_user_label.setText(_translate("StackedWidget", "Username"))
        self.wifi_button_6.setText(_translate("StackedWidget", "Wifi"))
        self.wifi_button_7.setText(_translate("StackedWidget", "Wifi"))
        self.add_user_label_2.setText(_translate("StackedWidget", "Password"))
        self.cancel_add_password_button.setText(_translate("StackedWidget", "Cancel"))
        self.new_user_done_button_2.setText(_translate("StackedWidget", "Done"))
        self.wifi_button_8.setText(_translate("StackedWidget", "Wifi"))
        self.reset_password_done_button.setText(_translate("StackedWidget", "Done"))
        self.cancel_reset_password_button.setText(_translate("StackedWidget", "Cancel"))
        self.add_user_label_3.setText(_translate("StackedWidget", "Reset Password"))
