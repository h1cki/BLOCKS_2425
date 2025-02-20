from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QTableWidgetItem, QComboBox, QHeaderView
import sys
import logging
#from lib import moonrakerComm
from lib.config import config
from functools import partial 

from ui.login_ui import Ui_StackedWidget
from lib.qt_auth import Authentication
import lib.user_auth as user_auth

logging.basicConfig(
    filename="logs/app.log",
    format="[%(levelname)s] | %(asctime)s | %(name)s | %(relativeCreated)6d | %(threadName)s : %(message)s",
    level=logging.DEBUG,
    force=True
)

_logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    signal_extruder_sub = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()
        
        self.config = config.ConfigHelper()
        # self.ws = moonrakerComm.MoonWebSocket(self.config["web_socket", "host"], self.config["web_socket", "port"], self)
        # self.ws.start()
        # self.ws.try_connection()
        # self.signal_extruder_sub.connect(self.ws.api.object_subscription)
        # self.signal_extruder_sub.emit({"gcode_move": None, "toolhead": ["position", "status"]})

        self.setWindowTitle("My App")
        self.resize(800, 480)
        
        self.stacked_widget = StackedWidget(self)
        
        self.stacked_widget.show()
        self.show()
        

class StackedWidget(QStackedWidget):
    signal_credentials = pyqtSignal(list)
    signal_admin_credentials = pyqtSignal(list)
    signal_add_user = pyqtSignal(list)  
    signal_reset_login_page = pyqtSignal() 
    signal_reset_admin_login_page = pyqtSignal()
    signal_reset_admin_page = pyqtSignal()
    signal_update_lvl = pyqtSignal(int, str, int, list)
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self)
        self.auth = Authentication(self)
        
        
        self.signal_credentials.connect(self.auth.authenticate_credentials)
        self.signal_admin_credentials.connect(self.auth.authenticate_admin_credentials)
        
        # User Login Page
        self.ui.userlist_login.activated.connect(self.handle_userlist_login)
        self.ui.cancel_login_button.clicked.connect(self.handle_cancel_login)
        self.ui.login_admin_button.clicked.connect(self.handle_login_admin_button)
        self.ui.userlist_login.addItems(user_auth.get_users())
        
        self.signal_reset_login_page.connect(self.reset_login_page)
        
        # Password Page
        self.ui.password_input.returnPressed.connect(self.handle_password_inserted)
        self.ui.user_login_button.clicked.connect(self.handle_password_inserted)
        self.ui.cancel_password_button.clicked.connect(self.handle_cancel_passsword)
        
        self.auth.signal_credentials_invalid.connect(self.handle_login_invalid_label)
        self.auth.signal_credentials_valid.connect(self.handle_valid_user_login)
        self.signal_reset_admin_login_page.connect(self.reset_admin_login_page)
        
        # Admin Login Page
        self.ui.admin_user_list.activated.connect(self.handle_admin_user_list)
        self.ui.cancel_admin_login_button.clicked.connect(self.handle_cancel_admin_login_passsword)
        
        # Admin Passowrd Page
        self.ui.admin_password_input.returnPressed.connect(self.handle_admin_login)
        self.ui.admin_login_done_button.clicked.connect(self.handle_admin_login)
        self.ui.cancel_admin_password_button.clicked.connect(self.handle_cancel_admin_passsword)
        
        self.auth.signal_admin_credentials_invalid.connect(self.handle_login_admin_invalid_label)
        self.auth.signal_admin_credentials_valid.connect(self.admin_page)
        
        # Admin page
        self.ui.add_user_button.clicked.connect(self.handle_add_user)
        self.ui.remove_user_button.clicked.connect(self.handle_remove_user_button)
        self.ui.reset_password_button.clicked.connect(self.handle_reset_user_button)
        self.ui.admin_page_back_button.clicked.connect(self.handle_admin_page_back)
        self.signal_reset_admin_page.connect(self.admin_page)
        self.signal_update_lvl.connect(self.handle_update_lvl)
        
        # Reset Password
        self.ui.reset_password_input.returnPressed.connect(self.handle_reset_password)
        self.ui.reset_password_done_button.clicked.connect(self.handle_reset_password)
        self.ui.cancel_reset_password_button.clicked.connect(self.handle_cancel_reset_pwd)
        
        # Add new user username
        self.ui.cancel_add_user_button.clicked.connect(self.handle_cancel_add_user_button)
        self.ui.new_user_done_button_1.clicked.connect(self.handle_add_username_done)
        self.ui.add_user_username_input.returnPressed.connect(self.handle_add_username_done)
        
        # Add new user password
        self.ui.cancel_add_password_button.clicked.connect(self.handle_cancel_add_password_button)
        self.ui.new_user_done_button_2.clicked.connect(self.handle_add_password_done)
        self.ui.add_user_password_input.returnPressed.connect(self.handle_add_password_done)
        
        self.show()

    def stackedWidget(self):
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self)
                
    
    
    # Login page
    @pyqtSlot(name= "Users List")
    def handle_userlist_login(self):
        _logger.debug("Username inserted")
        self.setCurrentIndex(1)
    
    @pyqtSlot(name= "Cancel Login")
    def handle_cancel_login(self):
        ...
        # Go Back to Main Menu
        
    @pyqtSlot(name= "Login as Admin")   
    def handle_login_admin_button(self):
        _logger.debug("Admin login")
        self.signal_reset_admin_login_page.emit()
        
    @pyqtSlot(name= "Reset Login")
    def reset_login_page(self):
        self.setCurrentIndex(0)
        self.ui.userlist_login.clear()
        self.ui.userlist_login.addItems(user_auth.get_users())
    
    # Password page     
    @pyqtSlot(name= "Password")
    def handle_password_inserted(self):
        _logger.debug("Password inserted")
        self.signal_credentials.emit([self.ui.userlist_login.currentText(), self.ui.password_input.text()])
        
    @pyqtSlot(name= "Cancel Password")
    def handle_cancel_passsword(self):
        self.signal_reset_login_page.emit()
        self.ui.password_input.clear()
        self.ui.password_input.setStyleSheet("")
        self.ui.login_invalid_label.clear()
        
    @pyqtSlot(name= "Login Invalid 1")
    def handle_login_invalid_label(self):
        self.ui.login_invalid_label.setText("Login Unsuccessful")
        self.ui.password_input.setStyleSheet("border: 2px solid red;")
        self.ui.password_input.clear()
        _logger.debug("User Log in unsuccessful")
    
    @pyqtSlot(name= "Valid User Login")
    def handle_valid_user_login(self):
        ...
        # Back To Main Menu ?????
    
    
    # Admin Login page
    @pyqtSlot(name= "Admin Users List")
    def handle_admin_user_list(self):
        _logger.debug("Admin username inserted")
        self.setCurrentIndex(3)
        
    @pyqtSlot(name= "Cancel Admin Log in")
    def handle_cancel_admin_login_passsword(self):
        self.signal_reset_login_page.emit()
        self.ui.password_input.clear()
        self.ui.login_admin_invalid_label.clear()
    
    @pyqtSlot(name= "Reset Admin Login Page")    
    def reset_admin_login_page(self):
        self.setCurrentIndex(2)
        self.ui.admin_user_list.clear()
        self.ui.admin_user_list.addItems(user_auth.get_users())
        
    
    # Admin Password Page
    @pyqtSlot(name = "Admin Password")
    def handle_admin_login(self):
        _logger.debug("Admin Password inserted")
        self.signal_admin_credentials.emit([self.ui.admin_user_list.currentText(), self.ui.admin_password_input.text()])     
        self.ui.admin_password_input.clear()      
    
    @pyqtSlot(name= "Cancel Admin Password")
    def handle_cancel_admin_passsword(self):
        self.signal_reset_admin_login_page.emit()
        self.ui.admin_password_input.clear()
        self.ui.login_admin_invalid_label.clear()
        self.ui.admin_password_input.setStyleSheet("")
            
    @pyqtSlot(name= "Login Invalid 2")
    def handle_login_admin_invalid_label(self):
        self.ui.login_admin_invalid_label.setText("Login Unsuccessful")
        self.ui.admin_password_input.setStyleSheet("border: 2px solid red;")
        _logger.debug("Admin Log in unsuccessful")
        
        

    # Admin Page
    @pyqtSlot(name= "Load Admin Page")
    def admin_page(self):
        self.ui.admin_password_input.setStyleSheet("")
        self.ui.login_admin_invalid_label.clear()
         
        self.ui.admin_table.clear()
        self.ui.admin_info_label.clear()
        self.setCurrentIndex(4)
        
        self.level_mapping = {
            4: "Super Admin",
            3: "Admin",
            2: "Senior Moderator",
            1: "Moderator",
            0: "Regular User"
        }
        
        self.ui.admin_table.setRowCount(len(user_auth.get_users()))
        self.ui.admin_table.setColumnCount(3)
        
        self.ui.admin_table.setHorizontalHeaderLabels(("Usernames", "User Level", "Premissions"))
        
        user_list = user_auth.get_users()
        user_data = []
        
        for username in user_list:
            level = user_auth.user_level(username)
            user_data.append((username, level))
            
        
        for index, (username, level) in enumerate(user_data):
            combo = QComboBox()
            combo.addItems(self.level_mapping.values())

            lvl_item = QTableWidgetItem(str(level))
            
            level_text = self.level_mapping.get(level)
            combo.setCurrentText(level_text)
            
            new_lvl = int([key for key, value in self.level_mapping.items() if value == combo.currentText()][0])
            
            combo.currentIndexChanged.connect(partial(self.handle_update_lvl, username, combo))

            self.ui.admin_table.setItem(index, 0, QTableWidgetItem(username))
            self.ui.admin_table.setItem(index, 1, lvl_item)
            self.ui.admin_table.setCellWidget(index, 2, combo)
            
        
        self.ui.admin_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ui.admin_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.admin_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
    
            
    def handle_update_lvl(self, username: str, combo):
        new_level = int([key for key, value in self.level_mapping.items() if value == combo.currentText()][0])
        user_auth.update_lvl(username, new_level)
        self.signal_reset_admin_page.emit()
                
    @pyqtSlot(name= "Add User")
    def handle_add_user(self):
        self.setCurrentIndex(5)
    
    @pyqtSlot(name= "Back Admin Page")    
    def handle_admin_page_back(self):
        self.signal_reset_login_page.emit()
    
       
    # Remove User
    @pyqtSlot(name= "Remove User")
    def handle_remove_user_button(self):
        selected_item = self.ui.admin_table.selectedIndexes()
        if selected_item:
            row = selected_item[0].row()
            item = self.ui.admin_table.item(row, 0) 
            if item:
                username = item.text()
                if username:
                    user_auth.rm_user(username)
                    self.signal_reset_admin_page.emit()
        else:
            self.ui.admin_info_label.setText("No user selected")


    # Reset Password
    @pyqtSlot(name= "Reset User")
    def handle_reset_user_button(self):
        selected_item = self.ui.admin_table.selectedIndexes()
        if selected_item:
            self.setCurrentIndex(7)
        else:
            self.ui.admin_info_label.setText("No user selected")
    
    @pyqtSlot(name= "Reset Password")
    def handle_reset_password(self):
        selected_item = self.ui.admin_table.selectedIndexes()
        row = selected_item[0].row()
        item = self.ui.admin_table.item(row, 0) 
        if item:
            username = item.text()
            if username:
                valid, message = user_auth.valid_pwd(self.ui.reset_password_input.text())
                if valid:
                    user_auth.reset_password(username, self.ui.reset_password_input.text())
                    self.signal_reset_admin_page.emit()
                    self.ui.reset_pwd_invalid_label.clear() 
                    self.ui.reset_password_input.text()                 
                else:
                    self.ui.reset_pwd_invalid_label.setText(f"{message}")
        else:
            self.signal_reset_admin_page.emit()
            
    @pyqtSlot(name= "Cancel Reset Password")
    def handle_cancel_reset_pwd(self):
        self.ui.reset_password_input.clear()
        self.ui.reset_pwd_invalid_label.clear()
        self.signal_reset_admin_page.emit()
                
      
    # Add User Username
    @pyqtSlot(name= "Cancel Add User")
    def handle_cancel_add_user_button(self):
        self.ui.add_username_invalid_label.clear()
        self.ui.add_user_username_input.clear()
        self.signal_reset_admin_page.emit()
        
    
    @pyqtSlot(name= "Add Username Done")
    def handle_add_username_done(self):
        valid, message = user_auth.valid_username(self.ui.add_user_username_input.text())
        if valid:
            self.ui.add_username_invalid_label.clear()
            self.setCurrentIndex(6)
        else:
            self.ui.add_username_invalid_label.setText(f"{message}")
        
   
   
    # Add User Password
    @pyqtSlot(name= "Cancel Add Password")
    def handle_cancel_add_password_button(self):
        self.setCurrentIndex(5)
        self.ui.add_user_username_input.clear()
        self.ui.add_user_password_input.clear()
        self.ui.add_pwd_invalid_label.clear()
    
    @pyqtSlot(name= "Add Password Done")   
    def handle_add_password_done(self):
        valid, message = user_auth.valid_pwd(self.ui.add_user_password_input.text())
        if valid:
            self.auth.add_user([self.ui.add_user_username_input.text(), self.ui.add_user_password_input.text()])
            self.ui.add_user_username_input.clear()
            self.ui.add_user_password_input.clear()
            self.ui.add_pwd_invalid_label.clear()
            self.signal_reset_admin_page.emit()
        else:
            self.ui.add_pwd_invalid_label.setText(f"{message}")    
    
        
            

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()