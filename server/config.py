import os

__server_config_file_path__ = os.path.realpath(__file__)
__server_folder_path__ = os.path.dirname(__server_config_file_path__)
DATA_FILE_PATH = os.path.join(__server_folder_path__, r'data\data.txt')
