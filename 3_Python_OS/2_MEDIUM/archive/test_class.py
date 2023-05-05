import os
from pathlib import Path

from archive import ArchiveMixin


class TestingArchiveMixin(ArchiveMixin):
    def __init__(self, *path_elements):
        self.path = Path(os.path.join(*path_elements)).absolute()
