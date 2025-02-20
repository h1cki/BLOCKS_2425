import configparser
import os
import shutil

class ConfigHelper(configparser.ConfigParser):
    
    base_filename = "base.cfg"
    
    def __init__(self, filename: str= base_filename ):
        # self.config = configparser.ConfigParser()
        super().__init__()
        #print(os.getcwd())
        self.filename = filename
        
        dirpath_print_data = os.getcwd() + "\printer_data\config"
        dirpath_blocks_screen = os.getcwd() + "\Blocks_Screen"
        
        # dirpath_print_data = "~/Config/printer_data/config"
        # dirpath_blocks_screen = "~/Config/Blocks_Screen"
        
        filepath_print_data = os.path.join(dirpath_print_data, filename)
        filepath_blocks_screen = os.path.join(dirpath_blocks_screen, filename)
        
        if self.search_file(dirpath_print_data, filename):
            self.read_config(dirpath_print_data, filename)
            
        elif self.search_file(dirpath_blocks_screen, filename):
            # os.symlink(src, dst)
            try:
                shutil.copy(filepath_blocks_screen, filepath_print_data)
                self.read_config(dirpath_blocks_screen, filename)
            except FileExistsError:
                raise(f"Source file not found: {filepath_blocks_screen}")
            
        else:
            raise FileExistsError(f"The {filename} doesn't exist")
        
        
        
    def read_config(self, directory: str, filename: str) -> None:
        if self.has_premission(directory, filename):
            self.read(os.path.join(directory, filename))
    
    def has_premission(self, directory: str, filename: str) -> bool:
        if os.access(os.path.join(directory, filename), os.X_OK):
            return True
        
        return False
    
    def search_file(self, start_directory: str, filename: str,) -> bool:
        if not os.path.isdir(start_directory):
            raise NotADirectoryError(f"Start directory {start_directory} does not exist.")
        
        for root, dirs, files in os.walk(start_directory):
            if filename in files:
                return True
            
        return False
        

    def __getitem__(self, section: tuple): 
        if not self.has_section(section[0]):
            raise ValueError(f"Section '{section[0]}' not found.")
            return
        
        if not self.has_option(section[0],section[1]):
            raise ValueError(f"Key '{section[1]}' not found in section '{section[0]}'.")
            return
        
        return self.get(section[0],section[1])
        
    # def get_value(self, section: str, key: str):
    #     if not self.config.has_section(section):
    #         print(f"Section '{section}' not found.")
    #         return
        
    #     if not self.config.has_option(section, key):
    #         print(f"Key '{key}' not found in section '{section}'.")
    #         return
        
    #     return self.config[section][key]
    
    def modify_value(self, section: str, key: str, new_value: str) -> None:
        if not self.has_section(section):
            raise ValueError(f"Section '{section}' not found.")
            return
        
        if not self.has_option(section, key):
            raise ValueError(f"Key '{key}' not found in section '{section}'.")
            return
        
        self.set(section, key, str(new_value))
        
        with open('base.cfg', 'w') as configfile:
            self.write(configfile)
        
        
if __name__ == "__main__":
    config1 = ConfigHelper()
    print(config1['web_socket', 'port'])
    config1.modify_value('web_socket', 'port', 8000)
    print(config1['web_socket', 'port'])
    config1.modify_value('web_socket', 'port', 7125)
    print(config1['web_socket', 'port'])
    print(config1['web_socket', 'host'])
    # print(config1.get_value('web_socket', 'port'))
    # config1.modify_value('web_socket', 'port', 8000)
    # print(config1.get_value('web_socket', 'port'))
    # config1.get_value('nothing', 'person')
    # config1.get_value('credentials', 'person')
    
    