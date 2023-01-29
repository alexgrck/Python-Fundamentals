import os


class FileHandler:
    def __init__(self, *file_path, last_index=0):
        self.file_path = os.path.join(*file_path)
        self.abs_path = (
            self.file_path
            if os.path.isabs(self.file_path)
            else os.path.join(os.getcwd(), self.file_path)
        )
        self.last_index = last_index

    def __enter__(self):
        self.file_object = open(self.abs_path, mode="r")
        self.read = self.file_object.readlines()
        return self

    def read_lines(self, lines_left=0):
        self.readlines = self.read[self.last_index : (self.last_index + lines_left)]
        self.last_index += lines_left
        return self.readlines

    def __exit__(self, exc_type=None, exc_value=None, exc_tb=None):
        self.file_object.close()
