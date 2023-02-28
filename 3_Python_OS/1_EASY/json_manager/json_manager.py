import json
import sys
from pathlib import Path

sys.path.append("C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY")

from path_methods import MixinPathMethods


class JsonManager(MixinPathMethods):
    def __init__(self, path_string, file_name="", depth=0):
        self.path = Path(path_string)
        self.file_name_path = self.path.joinpath(file_name)
        self.abs_path = (
            self.file_name_path
            if self.file_name_path.is_absolute()
            else Path.cwd().joinpath(self.file_name_path)
        )
        self.depth = depth

    def read_file(self):
        """Reading json file."""
        with open(self.abs_path, "r") as file:
            return json.load(file)

    def set_data(self, data: dict):
        """Setting data to json file."""
        with open(self.abs_path, "w") as file:
            json.dump(data, file, indent=2)

    def update_file(self, data):
        """Updating json file by modifying value indicated by given key."""
        with open(self.abs_path, "w") as file:
            file.seek(0)
            json.dump(data, file, indent=2)

    def append_data(self, data):
        """Updating json file by appending data at the end of the file."""
        with open(self.abs_path, "r+") as file:
            file_data = json.load(file)
            file_data.update(data)
            file.seek(0)
            json.dump(file_data, file, indent=2)


# 'C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\json_manager',
#  'C:\\Program Files\\Python310\\python310.zip',
#  'C:\\Program Files\\Python310\\DLLs',
#  'C:\\Program Files\\Python310\\lib',
#  'C:\\Program Files\\Python310',
#  'C:\\Users\\aleks\\AppData\\Roaming\\Python\\Python310\\site-packages',
#  'C:\\Users\\aleks\\AppData\\Roaming\\Python\\Python310\\site-packages\\win32',
#  'C:\\Users\\aleks\\AppData\\Roaming\\Python\\Python310\\site-packages\\win32\\lib',
#  'C:\\Users\\aleks\\AppData\\Roaming\\Python\\Python310\\site-packages\\Pythonwin',
#  'C:\\Program Files\\Python310\\lib\\site-packages']

jm = JsonManager(
    "C:\\Ola\\LocalHost\\python-fundamentals-master\\3_Python_OS\\1_EASY\\json_manager",
    file_name="test_json_file.json",
)

update_dict = {"first": "content", "second": "content"}
# jm.update_file(["testname1", "testname2"], "2ndfolder")
jm.update_file(update_dict)
