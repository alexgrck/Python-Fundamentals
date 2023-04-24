import os
from pathlib import Path

from archive import ArchiveMixin


class TestingArchive_mixin(ArchiveMixin):
    def __init__(self, *path_elements):
        self.path = Path(os.path.join(*path_elements)).absolute()
