import os
from pathlib import Path

from archive import ArchiveMixin


class TestingArchiveMixin(ArchiveMixin):
    def __init__(self, *path_elements):
        self.path = os.path.join(os.getcwd(), *path_elements)
