from PyQt6.QtCore import pyqtSignal, pyqtSlot, QObject
import lib.user_auth as user_auth
import logging

_logger = logging.getLogger(__name__)


class Authentication(QObject):
    signal_credentials_valid = pyqtSignal()
    signal_credentials_invalid = pyqtSignal()
    signal_admin_credentials_valid = pyqtSignal()
    signal_admin_credentials_invalid = pyqtSignal()

    
    def __init__(self, parent):
        super().__init__(parent)
        user_auth.create_db()
        
    @pyqtSlot(list, name= "Authenticate")    
    def authenticate_credentials(self, credentials: list) -> bool:
        if user_auth.verify_pwd(credentials[0], credentials[1]):
            _logger.debug("User Log in successful")
            self.signal_credentials_valid.emit()
        else:            
            self.signal_credentials_invalid.emit()
      
    @pyqtSlot(list, name= "Authenticate Admin")
    def authenticate_admin_credentials(self, credentials: list) -> bool:
        if user_auth.verify_pwd(credentials[0], credentials[1]) and (user_auth.user_level(credentials[0]) >= 3):
            _logger.debug("Admin Login successful")
            self.signal_admin_credentials_valid.emit()
        else:
            self.signal_admin_credentials_invalid.emit()        
            
    @pyqtSlot(list, name= "Add user")     
    def add_user(self, credentials: list):
        if user_auth.add_user(credentials[0], credentials[1], 0):
            _logger.debug("User Added successful")
        else:
            _logger.debug("User Added unsuccessful")
            
            
    
        
                   
        
        
        
       
    
        
        
        